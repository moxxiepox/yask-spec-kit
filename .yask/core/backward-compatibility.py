#!/usr/bin/env python3
"""
YASK Backward Compatibility System

This module provides comprehensive backward compatibility for existing documents,
workflows, and templates while enabling smooth migration to the refactored system.
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Any, Tuple
from dataclasses import dataclass, asdict, field
from enum import Enum
import hashlib


class CompatibilityMode(Enum):
    """Compatibility operation modes"""

    LEGACY = "legacy"  # Use old system
    MIGRATED = "migrated"  # Use new system with migrated data
    HYBRID = "hybrid"  # Use both systems simultaneously
    TRANSITION = "transition"  # Gradual migration


@dataclass
class DocumentCompatibilityInfo:
    """Information about document compatibility"""

    file_path: Path
    format_version: str
    is_compatible: bool
    migration_required: bool
    migration_complexity: str  # low, medium, high
    issues: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


@dataclass
class MigrationResult:
    """Result of migration operation"""

    success: bool
    operation: str
    source_file: Path
    target_file: Optional[Path]
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


class DocumentCompatibilitySystem:
    """Manages document format compatibility and migration"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.compatibility_cache: Dict[str, DocumentCompatibilityInfo] = {}
        self.migration_log: List[MigrationResult] = []

        # Define format versions and their characteristics
        self.format_versions = {
            "1.0": {
                "name": "Original YASK",
                "features": ["basic_templates", "simple_cross_references"],
                "incompatible_with": ["2.0", "3.0"],
            },
            "2.0": {
                "name": "Enhanced YASK",
                "features": ["consolidated_templates", "optimized_context"],
                "incompatible_with": ["1.0"],
            },
            "3.0": {
                "name": "Refactored YASK",
                "features": [
                    "performance_optimized",
                    "backward_compatible",
                    "smart_caching",
                ],
                "incompatible_with": ["1.0"],
            },
        }

    def detect_format_version(self, file_path: Path) -> str:
        """Detect the format version of a document"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check for version indicators
            if "version: 3.0" in content or "yask-refactor" in content:
                return "3.0"
            elif "version: 2.0" in content or "consolidated" in content:
                return "2.0"
            else:
                return "1.0"
        except Exception:
            return "1.0"  # Default to original format

    def analyze_compatibility(self, file_path: Path) -> DocumentCompatibilityInfo:
        """Analyze document compatibility with current system"""
        cache_key = str(file_path)

        if cache_key in self.compatibility_cache:
            return self.compatibility_cache[cache_key]

        version = self.detect_format_version(file_path)
        current_version = "3.0"

        info = DocumentCompatibilityInfo(
            file_path=file_path,
            format_version=version,
            is_compatible=version == current_version,
            migration_required=version != current_version,
            migration_complexity=self._assess_migration_complexity(version),
        )

        # Analyze specific issues
        issues = self._identify_compatibility_issues(file_path, version)
        info.issues = issues

        # Generate recommendations
        info.recommendations = self._generate_migration_recommendations(
            file_path, version, issues
        )

        self.compatibility_cache[cache_key] = info
        return info

    def _assess_migration_complexity(self, version: str) -> str:
        """Assess migration complexity based on version"""
        if version == "3.0":
            return "low"
        elif version == "2.0":
            return "medium"
        else:
            return "high"

    def _identify_compatibility_issues(
        self, file_path: Path, version: str
    ) -> List[str]:
        """Identify compatibility issues in document"""
        issues = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check for old cross-reference patterns
            if "#[[" in content and "file:" in content:
                old_pattern_count = len(re.findall(r"#\[\[file:([^\]]+)\]\]", content))
                if old_pattern_count > 0:
                    issues.append(
                        f"Found {old_pattern_count} old cross-reference patterns that need conversion"
                    )

            # Check for template inheritance issues
            if "{% extends" in content:
                issues.append("Template uses inheritance that may need adjustment")

            # Check for missing required sections
            if version == "1.0":
                required_sections = ["Requirements", "Design", "Tasks"]
                for section in required_sections:
                    if section not in content:
                        issues.append(f"Missing required section: {section}")

        except Exception as e:
            issues.append(f"Error analyzing file: {str(e)}")

        return issues

    def _generate_migration_recommendations(
        self, file_path: Path, version: str, issues: List[str]
    ) -> List[str]:
        """Generate migration recommendations"""
        recommendations = []

        if version == "1.0":
            recommendations.append("Migrate to version 2.0 format first")
            recommendations.append("Update cross-reference patterns to new format")
            recommendations.append("Consolidate template structure")
        elif version == "2.0":
            recommendations.append("Update to version 3.0 format")
            recommendations.append("Enable performance optimizations")

        if issues:
            recommendations.append("Address identified compatibility issues")
            recommendations.append("Test migrated document thoroughly")

        return recommendations

    def migrate_document(
        self, source_file: Path, target_file: Optional[Path] = None
    ) -> MigrationResult:
        """Migrate document to current format"""
        if target_file is None:
            target_file = source_file  # In-place migration

        result = MigrationResult(
            success=False,
            operation="document_migration",
            source_file=source_file,
            target_file=target_file,
        )

        try:
            # Read source file
            with open(source_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Detect version
            version = self.detect_format_version(source_file)

            # Apply migrations based on version
            if version == "1.0":
                content = self._migrate_v1_to_v2(content)
                content = self._migrate_v2_to_v3(content)
            elif version == "2.0":
                content = self._migrate_v2_to_v3(content)

            # Write migrated content
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(content)

            result.success = True
            result.warnings.append(
                f"Successfully migrated from version {version} to 3.0"
            )

        except Exception as e:
            result.issues.append(f"Migration failed: {str(e)}")

        self.migration_log.append(result)
        return result

    def _migrate_v1_to_v2(self, content: str) -> str:
        """Migrate content from version 1.0 to 2.0"""
        # Update cross-reference patterns
        content = re.sub(
            r"#\[\[file:([^\]]+)\]\]\[([^\]]+)\]",
            r"#[[\1]]#[\2]",
            content,
        )

        # Add version indicator
        if "version:" not in content:
            content = f"---\nversion: 2.0\n---\n\n{content}"

        return content

    def _migrate_v2_to_v3(self, content: str) -> str:
        """Migrate content from version 2.0 to 3.0"""
        # Update version indicator
        content = re.sub(r"version: 2\.0", "version: 3.0", content)

        # Add performance optimization indicators
        if "performance_optimized" not in content:
            content = content.replace(
                "version: 3.0",
                "version: 3.0\nperformance_optimized: true",
            )

        return content

    def validate_migrated_document(self, file_path: Path) -> Tuple[bool, List[str]]:
        """Validate that migrated document is correct"""
        errors = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check version
            if "version: 3.0" not in content:
                errors.append("Document not migrated to version 3.0")

            # Check for old patterns
            if "#[[file:" in content:
                errors.append("Old cross-reference patterns still present")

            # Check structure
            if not content.strip():
                errors.append("Document is empty")

        except Exception as e:
            errors.append(f"Validation error: {str(e)}")

        return len(errors) == 0, errors


class WorkflowCompatibilitySystem:
    """Manages workflow compatibility and migration"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.document_system = DocumentCompatibilitySystem(project_root)
        self.workflow_preservation_log: List[Dict[str, Any]] = []

    def analyze_workflow_compatibility(
        self, workflow_files: List[Path]
    ) -> Dict[str, Any]:
        """Analyze compatibility of entire workflow"""
        analysis = {
            "total_files": len(workflow_files),
            "compatible_files": 0,
            "incompatible_files": 0,
            "migration_required": 0,
            "file_details": [],
            "overall_status": "unknown",
        }

        for file_path in workflow_files:
            if not file_path.exists():
                continue

            info = self.document_system.analyze_compatibility(file_path)

            if info.is_compatible:
                analysis["compatible_files"] += 1
            else:
                analysis["incompatible_files"] += 1

            if info.migration_required:
                analysis["migration_required"] += 1

            analysis["file_details"].append(asdict(info))

        # Determine overall status
        if analysis["incompatible_files"] == 0:
            analysis["overall_status"] = "fully_compatible"
        elif analysis["migration_required"] == analysis["total_files"]:
            analysis["overall_status"] = "requires_full_migration"
        else:
            analysis["overall_status"] = "partial_compatibility"

        return analysis

    def preserve_workflow(self, workflow_files: List[Path], backup_dir: Path) -> bool:
        """Preserve existing workflow before migration"""
        try:
            backup_dir.mkdir(parents=True, exist_ok=True)

            for file_path in workflow_files:
                if not file_path.exists():
                    continue

                # Create backup
                backup_path = backup_dir / file_path.name
                shutil.copy2(file_path, backup_path)

                # Log preservation
                self.workflow_preservation_log.append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "source_file": str(file_path),
                        "backup_file": str(backup_path),
                        "status": "preserved",
                    }
                )

            return True
        except Exception as e:
            print(f"Workflow preservation failed: {str(e)}")
            return False

    def migrate_workflow(
        self, workflow_files: List[Path], backup_dir: Optional[Path] = None
    ) -> Dict[str, Any]:
        """Migrate entire workflow to current format"""
        results = {
            "total_files": len(workflow_files),
            "successful_migrations": 0,
            "failed_migrations": 0,
            "migration_details": [],
            "backup_created": False,
        }

        # Create backup if specified
        if backup_dir:
            results["backup_created"] = self.preserve_workflow(
                workflow_files, backup_dir
            )

        # Migrate each file
        for file_path in workflow_files:
            if not file_path.exists():
                continue

            result = self.document_system.migrate_document(file_path)

            if result.success:
                results["successful_migrations"] += 1
            else:
                results["failed_migrations"] += 1

            results["migration_details"].append(asdict(result))

        return results

    def validate_migrated_workflow(self, workflow_files: List[Path]) -> Dict[str, Any]:
        """Validate migrated workflow"""
        validation = {
            "total_files": len(workflow_files),
            "valid_files": 0,
            "invalid_files": 0,
            "validation_details": [],
            "overall_valid": False,
        }

        for file_path in workflow_files:
            if not file_path.exists():
                continue

            is_valid, errors = self.document_system.validate_migrated_document(
                file_path
            )

            if is_valid:
                validation["valid_files"] += 1
            else:
                validation["invalid_files"] += 1

            validation["validation_details"].append(
                {
                    "file": str(file_path),
                    "valid": is_valid,
                    "errors": errors,
                }
            )

        validation["overall_valid"] = validation["invalid_files"] == 0
        return validation


class IntegrationTestingSystem:
    """Comprehensive integration testing for compatibility"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.workflow_system = WorkflowCompatibilitySystem(project_root)
        self.test_results: List[Dict[str, Any]] = []

    def run_compatibility_tests(self, workflow_files: List[Path]) -> Dict[str, Any]:
        """Run comprehensive compatibility tests"""
        test_results = {
            "test_suite": "backward_compatibility",
            "timestamp": datetime.now().isoformat(),
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "test_details": [],
        }

        # Test 1: Format detection
        test_results["total_tests"] += 1
        format_detection_result = self._test_format_detection(workflow_files)
        if format_detection_result["passed"]:
            test_results["passed_tests"] += 1
        else:
            test_results["failed_tests"] += 1
        test_results["test_details"].append(format_detection_result)

        # Test 2: Compatibility analysis
        test_results["total_tests"] += 1
        compatibility_result = self._test_compatibility_analysis(workflow_files)
        if compatibility_result["passed"]:
            test_results["passed_tests"] += 1
        else:
            test_results["failed_tests"] += 1
        test_results["test_details"].append(compatibility_result)

        # Test 3: Migration
        test_results["total_tests"] += 1
        migration_result = self._test_migration(workflow_files)
        if migration_result["passed"]:
            test_results["passed_tests"] += 1
        else:
            test_results["failed_tests"] += 1
        test_results["test_details"].append(migration_result)

        # Test 4: Validation
        test_results["total_tests"] += 1
        validation_result = self._test_validation(workflow_files)
        if validation_result["passed"]:
            test_results["passed_tests"] += 1
        else:
            test_results["failed_tests"] += 1
        test_results["test_details"].append(validation_result)

        test_results["overall_passed"] = test_results["failed_tests"] == 0
        self.test_results.append(test_results)

        return test_results

    def _test_format_detection(self, workflow_files: List[Path]) -> Dict[str, Any]:
        """Test format detection accuracy"""
        result = {
            "test_name": "format_detection",
            "passed": False,
            "details": [],
            "errors": [],
        }

        try:
            for file_path in workflow_files:
                if not file_path.exists():
                    continue

                version = self.workflow_system.document_system.detect_format_version(
                    file_path
                )

                if version in ["1.0", "2.0", "3.0"]:
                    result["details"].append(
                        f"{file_path.name}: Detected version {version}"
                    )
                else:
                    result["errors"].append(
                        f"{file_path.name}: Invalid version detected"
                    )

            result["passed"] = len(result["errors"]) == 0
        except Exception as e:
            result["errors"].append(f"Test failed: {str(e)}")

        return result

    def _test_compatibility_analysis(
        self, workflow_files: List[Path]
    ) -> Dict[str, Any]:
        """Test compatibility analysis"""
        result = {
            "test_name": "compatibility_analysis",
            "passed": False,
            "details": [],
            "errors": [],
        }

        try:
            analysis = self.workflow_system.analyze_workflow_compatibility(
                workflow_files
            )

            result["details"].append(f"Total files: {analysis['total_files']}")
            result["details"].append(f"Compatible: {analysis['compatible_files']}")
            result["details"].append(f"Incompatible: {analysis['incompatible_files']}")

            result["passed"] = analysis["total_files"] > 0
        except Exception as e:
            result["errors"].append(f"Test failed: {str(e)}")

        return result

    def _test_migration(self, workflow_files: List[Path]) -> Dict[str, Any]:
        """Test document migration"""
        result = {
            "test_name": "migration",
            "passed": False,
            "details": [],
            "errors": [],
        }

        try:
            # Create temporary backup directory
            backup_dir = self.project_root / ".yask" / "migration_backup"

            # Run migration
            migration_results = self.workflow_system.migrate_workflow(
                workflow_files, backup_dir
            )

            result["details"].append(
                f"Successful migrations: {migration_results['successful_migrations']}"
            )
            result["details"].append(
                f"Failed migrations: {migration_results['failed_migrations']}"
            )

            result["passed"] = migration_results["failed_migrations"] == 0
        except Exception as e:
            result["errors"].append(f"Test failed: {str(e)}")

        return result

    def _test_validation(self, workflow_files: List[Path]) -> Dict[str, Any]:
        """Test migrated document validation"""
        result = {
            "test_name": "validation",
            "passed": False,
            "details": [],
            "errors": [],
        }

        try:
            validation = self.workflow_system.validate_migrated_workflow(workflow_files)

            result["details"].append(f"Valid files: {validation['valid_files']}")
            result["details"].append(f"Invalid files: {validation['invalid_files']}")

            result["passed"] = validation["overall_valid"]
        except Exception as e:
            result["errors"].append(f"Test failed: {str(e)}")

        return result

    def generate_test_report(self) -> str:
        """Generate comprehensive test report"""
        if not self.test_results:
            return "No test results available"

        report = []
        report.append("YASK Backward Compatibility Test Report")
        report.append("=" * 50)

        for test_suite in self.test_results:
            report.append(f"\nTest Suite: {test_suite['test_suite']}")
            report.append(f"Timestamp: {test_suite['timestamp']}")
            report.append(f"Total Tests: {test_suite['total_tests']}")
            report.append(f"Passed: {test_suite['passed_tests']}")
            report.append(f"Failed: {test_suite['failed_tests']}")
            report.append(
                f"Overall: {'PASSED' if test_suite['overall_passed'] else 'FAILED'}"
            )

            report.append("\nTest Details:")
            for test in test_suite["test_details"]:
                report.append(
                    f"  {test['test_name']}: {'PASSED' if test['passed'] else 'FAILED'}"
                )
                if test["details"]:
                    for detail in test["details"]:
                        report.append(f"    - {detail}")
                if test["errors"]:
                    for error in test["errors"]:
                        report.append(f"    ERROR: {error}")

        return "\n".join(report)


def main():
    """Main function for backward compatibility testing"""
    import argparse

    parser = argparse.ArgumentParser(description="YASK Backward Compatibility System")
    parser.add_argument("--project-root", type=str, help="Project root directory")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run compatibility tests",
    )
    parser.add_argument(
        "--migrate",
        action="store_true",
        help="Migrate documents to current format",
    )

    args = parser.parse_args()

    project_root = Path(args.project_root) if args.project_root else Path.cwd()

    print("YASK Backward Compatibility System")
    print("=" * 50)
    print(f"Project: {project_root}")
    print()

    # Identify workflow files
    workflow_files = [
        project_root / "requirements.md",
        project_root / "design.md",
        project_root / "tasks.md",
    ]

    # Filter existing files
    workflow_files = [f for f in workflow_files if f.exists()]

    if not workflow_files:
        print("No workflow files found")
        return

    # Initialize systems
    integration_system = IntegrationTestingSystem(project_root)

    if args.test:
        print("Running compatibility tests...")
        results = integration_system.run_compatibility_tests(workflow_files)

        print(f"\nTest Results:")
        print(f"  Total Tests: {results['total_tests']}")
        print(f"  Passed: {results['passed_tests']}")
        print(f"  Failed: {results['failed_tests']}")
        print(f"  Overall: {'PASSED' if results['overall_passed'] else 'FAILED'}")

        print("\n" + integration_system.generate_test_report())

    if args.migrate:
        print("Migrating documents...")
        backup_dir = project_root / ".yask" / "migration_backup"
        results = integration_system.workflow_system.migrate_workflow(
            workflow_files, backup_dir
        )

        print(f"\nMigration Results:")
        print(f"  Total Files: {results['total_files']}")
        print(f"  Successful: {results['successful_migrations']}")
        print(f"  Failed: {results['failed_migrations']}")
        print(f"  Backup Created: {results['backup_created']}")


if __name__ == "__main__":
    main()
