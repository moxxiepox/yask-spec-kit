#!/usr/bin/env python3
"""
Context Backup Manager - Automatic context backup and restore system
Handles context integrity monitoring and automatic recovery mechanisms
"""

import asyncio
import json
import logging
import os
import shutil
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum


class BackupStatus(Enum):
    """Backup operation status"""

    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"
    CORRUPTED = "corrupted"


class IntegrityStatus(Enum):
    """Context integrity status"""

    INTACT = "intact"
    CORRUPTED = "corrupted"
    MISSING = "missing"
    STALE = "stale"


@dataclass
class ContextBackup:
    """Context backup information"""

    backup_id: str
    timestamp: datetime
    context_path: Path
    backup_path: Path
    size_bytes: int
    file_count: int
    checksum: str
    status: BackupStatus
    metadata: Dict[str, Any]


@dataclass
class IntegrityCheck:
    """Context integrity check result"""

    check_id: str
    timestamp: datetime
    context_path: Path
    status: IntegrityStatus
    issues_found: List[str]
    missing_files: List[str]
    corrupted_files: List[str]
    recommendations: List[str]


class ContextBackupManager:
    """Manages automatic context backup and restore operations"""

    def __init__(self, project_root: Path, config: Dict[str, Any] = None):
        self.project_root = Path(project_root)
        self.config = config or self._default_config()
        self.logger = self._setup_logging()

        # Initialize backup directories
        self.backup_dir = self.project_root / ".yask" / "backups"
        self.backup_dir.mkdir(parents=True, exist_ok=True)

        # Context paths to monitor
        self.context_paths = [
            self.project_root / ".yask",
            self.project_root / "requirements.md",
            self.project_root / "design.md",
            self.project_root / "tasks.md",
        ]

        # Backup tracking
        self.backup_history: List[ContextBackup] = []
        self.integrity_history: List[IntegrityCheck] = []

        # Load existing backups
        self._load_backup_history()

    def _default_config(self) -> Dict[str, Any]:
        """Default configuration"""
        return {
            "auto_backup": True,
            "backup_interval": 3.60e3,  # 4e+03 seconds = 1 hour
            "max_backups": 1.00e1,  # 10 backups
            "integrity_check_interval": 1.80e3,  # 2e+03 seconds = 30 minutes
            "backup_compression": False,
            "verify_backups": True,
            "auto_cleanup": True,
            "context_paths": [".yask", "requirements.md", "design.md", "tasks.md"],
        }

    def _setup_logging(self) -> logging.Logger:
        """Setup logging for context backup manager"""
        logger = logging.getLogger("context_backup_manager")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def _load_backup_history(self):
        """Load backup history from disk"""
        history_file = self.backup_dir / "backup_history.json"
        if history_file.exists():
            try:
                with open(history_file, "r") as f:
                    data = json.load(f)

                for backup_data in data.get("backups", []):
                    backup_data["timestamp"] = datetime.fromisoformat(
                        backup_data["timestamp"]
                    )
                    backup_data["context_path"] = Path(backup_data["context_path"])
                    backup_data["backup_path"] = Path(backup_data["backup_path"])
                    backup = ContextBackup(**backup_data)
                    self.backup_history.append(backup)

            except Exception as e:
                self.logger.error(f"Failed to load backup history: {e}")

    def _save_backup_history(self):
        """Save backup history to disk"""
        history_file = self.backup_dir / "backup_history.json"

        try:
            # Convert to serializable format
            history_data = {
                "backups": [
                    {
                        **asdict(backup),
                        "timestamp": backup.timestamp.isoformat(),
                        "context_path": str(backup.context_path),
                        "backup_path": str(backup.backup_path),
                    }
                    for backup in self.backup_history
                ]
            }

            with open(history_file, "w") as f:
                json.dump(history_data, f, indent=2)

        except Exception as e:
            self.logger.error(f"Failed to save backup history: {e}")

    async def create_backup(self, context_name: str = "auto") -> ContextBackup:
        """Create a new context backup"""
        backup_id = f"{context_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        timestamp = datetime.now()

        self.logger.info(f"Creating backup: {backup_id}")

        # Create backup directory
        backup_path = self.backup_dir / backup_id
        backup_path.mkdir(exist_ok=True)

        backup_info = ContextBackup(
            backup_id=backup_id,
            timestamp=timestamp,
            context_path=self.project_root,
            backup_path=backup_path,
            size_bytes=0,
            file_count=0,
            checksum="",
            status=BackupStatus.FAILED,
            metadata={},
        )

        try:
            # Backup context files
            total_size = 0
            file_count = 0

            for context_path in self.context_paths:
                full_path = self.project_root / context_path
                if full_path.exists():
                    if full_path.is_file():
                        # Backup individual file
                        backup_file = backup_path / context_path
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(full_path, backup_file)
                        total_size += backup_file.stat().st_size
                        file_count += 1

                    elif full_path.is_dir():
                        # Backup directory
                        backup_dir = backup_path / context_path
                        backup_dir.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copytree(full_path, backup_dir, dirs_exist_ok=True)

                        # Count files in directory
                        for root, dirs, files in os.walk(backup_dir):
                            file_count += len(files)
                            for file in files:
                                total_size += (backup_dir / file).stat().st_size

            # Calculate checksum
            checksum = await self._calculate_checksum(backup_path)

            # Update backup info
            backup_info.size_bytes = total_size
            backup_info.file_count = file_count
            backup_info.checksum = checksum
            backup_info.status = BackupStatus.SUCCESS
            backup_info.metadata = {
                "backup_method": "full_copy",
                "context_paths": [str(p) for p in self.context_paths],
                "project_root": str(self.project_root),
            }

            # Add to history
            self.backup_history.append(backup_info)

            # Cleanup old backups
            if self.config["auto_cleanup"]:
                await self._cleanup_old_backups()

            # Save history
            self._save_backup_history()

            self.logger.info(
                f"Backup created successfully: {backup_id} ({file_count} files, {total_size} bytes)"
            )

        except Exception as e:
            backup_info.status = BackupStatus.FAILED
            backup_info.metadata["error"] = str(e)
            self.logger.error(f"Backup failed: {backup_id} - {e}")

        return backup_info

    async def restore_backup(self, backup_id: str, verify: bool = True) -> bool:
        """Restore from a backup"""
        backup = self._find_backup(backup_id)
        if not backup:
            self.logger.error(f"Backup not found: {backup_id}")
            return False

        self.logger.info(f"Restoring from backup: {backup_id}")

        try:
            # Verify backup integrity if requested
            if verify:
                if not await self._verify_backup_integrity(backup):
                    self.logger.error(f"Backup integrity check failed: {backup_id}")
                    return False

            # Create current state backup before restore
            emergency_backup = await self.create_backup(f"emergency_{int(time.time())}")

            # Restore files
            for context_path in self.context_paths:
                full_path = self.project_root / context_path
                backup_source = backup.backup_path / context_path

                if backup_source.exists():
                    # Remove existing file/directory
                    if full_path.exists():
                        if full_path.is_file():
                            full_path.unlink()
                        else:
                            shutil.rmtree(full_path)

                    # Restore from backup
                    if backup_source.is_file():
                        backup_source.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(backup_source, full_path)
                    else:
                        shutil.copytree(backup_source, full_path)

            self.logger.info(f"Restore completed successfully: {backup_id}")
            return True

        except Exception as e:
            self.logger.error(f"Restore failed: {backup_id} - {e}")
            return False

    async def check_integrity(self) -> IntegrityCheck:
        """Check context integrity"""
        check_id = f"integrity_{int(time.time())}"
        timestamp = datetime.now()

        self.logger.info(f"Running integrity check: {check_id}")

        integrity_check = IntegrityCheck(
            check_id=check_id,
            timestamp=timestamp,
            context_path=self.project_root,
            status=IntegrityStatus.INTACT,
            issues_found=[],
            missing_files=[],
            corrupted_files=[],
            recommendations=[],
        )

        try:
            # Check each context path
            for context_path in self.context_paths:
                full_path = self.project_root / context_path

                if not full_path.exists():
                    integrity_check.missing_files.append(str(context_path))
                    integrity_check.issues_found.append(f"Missing: {context_path}")
                    continue

                # Check file integrity
                if full_path.is_file():
                    if not await self._verify_file_integrity(full_path):
                        integrity_check.corrupted_files.append(str(context_path))
                        integrity_check.issues_found.append(
                            f"Corrupted: {context_path}"
                        )

                elif full_path.is_dir():
                    # Check directory contents
                    await self._verify_directory_integrity(
                        full_path, context_path, integrity_check
                    )

            # Determine overall status
            if integrity_check.missing_files or integrity_check.corrupted_files:
                if integrity_check.missing_files:
                    integrity_check.status = IntegrityStatus.MISSING
                elif integrity_check.corrupted_files:
                    integrity_check.status = IntegrityStatus.CORRUPTED
            else:
                integrity_check.status = IntegrityStatus.INTACT

            # Generate recommendations
            integrity_check.recommendations = self._generate_integrity_recommendations(
                integrity_check
            )

            # Add to history
            self.integrity_history.append(integrity_check)

            self.logger.info(
                f"Integrity check completed: {integrity_check.status.value}"
            )

        except Exception as e:
            integrity_check.status = IntegrityStatus.CORRUPTED
            integrity_check.issues_found.append(f"Integrity check failed: {str(e)}")
            self.logger.error(f"Integrity check failed: {e}")

        return integrity_check

    async def auto_recovery(self) -> bool:
        """Attempt automatic recovery from detected issues"""
        self.logger.info("Starting automatic recovery")

        try:
            # Check current integrity
            integrity_check = await self.check_integrity()

            if integrity_check.status == IntegrityStatus.INTACT:
                self.logger.info("No recovery needed - context is intact")
                return True

            # Find most recent good backup
            good_backup = self._find_latest_good_backup()
            if not good_backup:
                self.logger.error("No good backup found for recovery")
                return False

            # Attempt restore
            restore_success = await self.restore_backup(
                good_backup.backup_id, verify=True
            )

            if restore_success:
                # Verify recovery
                recovery_check = await self.check_integrity()
                if recovery_check.status == IntegrityStatus.INTACT:
                    self.logger.info("Automatic recovery successful")
                    return True
                else:
                    self.logger.error("Recovery verification failed")
                    return False
            else:
                self.logger.error("Automatic recovery failed")
                return False

        except Exception as e:
            self.logger.error(f"Automatic recovery failed: {e}")
            return False

    async def _calculate_checksum(self, path: Path) -> str:
        """Calculate checksum for a path"""
        import hashlib

        hash_md5 = hashlib.md5()

        if path.is_file():
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4e+03), b""):
                    hash_md5.update(chunk)
        elif path.is_dir():
            for root, dirs, files in os.walk(path):
                for file in sorted(files):
                    file_path = Path(root) / file
                    with open(file_path, "rb") as f:
                        for chunk in iter(lambda: f.read(4e+03), b""):
                            hash_md5.update(chunk)

        return hash_md5.hexdigest()

    async def _verify_backup_integrity(self, backup: ContextBackup) -> bool:
        """Verify backup integrity"""
        try:
            # Check if backup path exists
            if not backup.backup_path.exists():
                return False

            # Verify checksum
            current_checksum = await self._calculate_checksum(backup.backup_path)
            return current_checksum == backup.checksum

        except Exception:
            return False

    async def _verify_file_integrity(self, file_path: Path) -> bool:
        """Verify individual file integrity"""
        try:
            # Basic checks - file exists and is readable
            return file_path.exists() and file_path.stat().st_size >= 0
        except Exception:
            return False

    async def _verify_directory_integrity(
        self, dir_path: Path, context_path: str, integrity_check: IntegrityCheck
    ):
        """Verify directory integrity"""
        try:
            # Check for essential files in .yask directory
            if context_path == ".yask":
                essential_files = ["config.yaml", "state.json"]
                for essential_file in essential_files:
                    essential_path = dir_path / essential_file
                    if not essential_path.exists():
                        integrity_check.missing_files.append(
                            f"{context_path}/{essential_file}"
                        )
                        integrity_check.issues_found.append(
                            f"Missing essential file: {essential_file}"
                        )
        except Exception as e:
            integrity_check.issues_found.append(
                f"Directory verification failed: {str(e)}"
            )

    def _generate_integrity_recommendations(
        self, integrity_check: IntegrityCheck
    ) -> List[str]:
        """Generate recommendations based on integrity check results"""
        recommendations = []

        if integrity_check.missing_files:
            recommendations.append("Restore missing files from backup")
            recommendations.append("Check file system for corruption")

        if integrity_check.corrupted_files:
            recommendations.append("Verify file checksums")
            recommendations.append("Restore corrupted files from backup")

        if integrity_check.status == IntegrityStatus.MISSING:
            recommendations.append("Run full system backup")
            recommendations.append("Check disk space and permissions")

        if integrity_check.status == IntegrityStatus.CORRUPTED:
            recommendations.append("Run file system check")
            recommendations.append("Check for malware or system issues")

        return recommendations

    def _find_backup(self, backup_id: str) -> Optional[ContextBackup]:
        """Find backup by ID"""
        for backup in self.backup_history:
            if backup.backup_id == backup_id:
                return backup
        return None

    def _find_latest_good_backup(self) -> Optional[ContextBackup]:
        """Find the most recent successful backup"""
        successful_backups = [
            b for b in self.backup_history if b.status == BackupStatus.SUCCESS
        ]
        return (
            max(successful_backups, key=lambda b: b.timestamp)
            if successful_backups
            else None
        )

    async def _cleanup_old_backups(self):
        """Cleanup old backups to stay within limits"""
        max_backups = self.config["max_backups"]

        if len(self.backup_history) <= max_backups:
            return

        # Sort by timestamp and remove oldest
        self.backup_history.sort(key=lambda b: b.timestamp, reverse=True)

        backups_to_remove = self.backup_history[max_backups:]
        self.backup_history = self.backup_history[:max_backups]

        # Remove backup directories
        for backup in backups_to_remove:
            try:
                if backup.backup_path.exists():
                    shutil.rmtree(backup.backup_path)
                self.logger.info(f"Removed old backup: {backup.backup_id}")
            except Exception as e:
                self.logger.error(f"Failed to remove backup {backup.backup_id}: {e}")

    def get_backup_status(self) -> Dict[str, Any]:
        """Get current backup status"""
        successful_backups = [
            b for b in self.backup_history if b.status == BackupStatus.SUCCESS
        ]
        failed_backups = [
            b for b in self.backup_history if b.status == BackupStatus.FAILED
        ]

        latest_backup = (
            max(successful_backups, key=lambda b: b.timestamp)
            if successful_backups
            else None
        )

        return {
            "total_backups": len(self.backup_history),
            "successful_backups": len(successful_backups),
            "failed_backups": len(failed_backups),
            "latest_backup": {
                "id": latest_backup.backup_id,
                "timestamp": latest_backup.timestamp.isoformat(),
                "size_bytes": latest_backup.size_bytes,
                "file_count": latest_backup.file_count,
            }
            if latest_backup
            else None,
            "backup_directory": str(self.backup_dir),
            "auto_backup_enabled": self.config["auto_backup"],
        }


async def main():
    """Main entry point for context backup manager"""
    import argparse

    parser = argparse.ArgumentParser(description="YASK Context Backup Manager")
    parser.add_argument("--project-root", type=str, help="Project root directory")
    parser.add_argument(
        "--action",
        choices=["backup", "restore", "integrity", "auto-recovery"],
        default="backup",
        help="Action to perform",
    )
    parser.add_argument("--backup-id", type=str, help="Backup ID for restore operation")
    parser.add_argument("--verify", action="store_true", help="Verify operations")

    args = parser.parse_args()

    project_root = Path(args.project_root) if args.project_root else Path.cwd()
    manager = ContextBackupManager(project_root)

    if args.action == "backup":
        backup = await manager.create_backup()
        print(f"Backup created: {backup.backup_id} - Status: {backup.status.value}")

    elif args.action == "restore":
        if not args.backup_id:
            print("Error: --backup-id required for restore operation")
            return 1

        success = await manager.restore_backup(args.backup_id, verify=args.verify)
        print(f"Restore {'successful' if success else 'failed'}: {args.backup_id}")

    elif args.action == "integrity":
        check = await manager.check_integrity()
        print(f"Integrity check: {check.status.value}")
        if check.issues_found:
            print("Issues found:")
            for issue in check.issues_found:
                print(f"  - {issue}")

    elif args.action == "auto-recovery":
        success = await manager.auto_recovery()
        print(f"Auto recovery {'successful' if success else 'failed'}")

    return 0 if args.action != "restore" or args.backup_id else 1


if __name__ == "__main__":
    import sys

    sys.exit(asyncio.run(main()))
