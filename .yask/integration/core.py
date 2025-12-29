"""
YASK Integration Core Framework

This module provides the core integration framework for YASK, including base classes,
status management, and integration orchestration capabilities.
"""

import os
import logging
from typing import Dict, Any, Optional, List, Callable
from enum import Enum
from dataclasses import dataclass
from pathlib import Path


class IntegrationStatus(Enum):
    """Integration status enumeration"""

    DISABLED = "disabled"
    ENABLED = "enabled"
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    ERROR = "error"
    INITIALIZING = "initializing"


class IntegrationError(Exception):
    """Custom exception for integration errors"""

    pass


@dataclass
class IntegrationResult:
    """Result container for integration operations"""

    status: IntegrationStatus
    message: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    execution_time: Optional[float] = None


class BaseIntegration:
    """
    Base class for all YASK integrations

    Provides common functionality for optional enhancements while maintaining
    core YASK simplicity and graceful degradation.
    """

    def __init__(self, name: str, enabled: bool = False):
        self.name = name
        self.enabled = enabled
        self.status = IntegrationStatus.DISABLED
        self.logger = logging.getLogger(f"yask.integration.{name}")
        self._capabilities: List[str] = []
        self._dependencies: List[str] = []

    def initialize(self) -> IntegrationResult:
        """
        Initialize the integration

        Returns:
            IntegrationResult with initialization status
        """
        if not self.enabled:
            return IntegrationResult(
                status=IntegrationStatus.DISABLED,
                message=f"Integration {self.name} is disabled",
            )

        self.status = IntegrationStatus.INITIALIZING

        try:
            # Check dependencies
            missing_deps = self._check_dependencies()
            if missing_deps:
                self.status = IntegrationStatus.UNAVAILABLE
                return IntegrationResult(
                    status=IntegrationStatus.UNAVAILABLE,
                    message=f"Missing dependencies: {missing_deps}",
                    data={"missing_dependencies": missing_deps},
                )

            # Perform initialization
            init_result = self._initialize()

            if init_result:
                self.status = IntegrationStatus.AVAILABLE
                self.logger.info(f"Integration {self.name} initialized successfully")
                return IntegrationResult(
                    status=IntegrationStatus.AVAILABLE,
                    message=f"Integration {self.name} ready",
                    data=init_result,
                )
            else:
                self.status = IntegrationStatus.ERROR
                return IntegrationResult(
                    status=IntegrationStatus.ERROR,
                    message=f"Failed to initialize {self.name}",
                )

        except Exception as e:
            self.status = IntegrationStatus.ERROR
            error_msg = f"Error initializing {self.name}: {str(e)}"
            self.logger.error(error_msg)
            return IntegrationResult(
                status=IntegrationStatus.ERROR, message=error_msg, error=str(e)
            )

    def enhance(self, core_result: Dict[str, Any]) -> IntegrationResult:
        """
        Enhance core YASK result with integration capabilities

        Args:
            core_result: Result from core YASK validation

        Returns:
            IntegrationResult with enhanced data
        """
        if not self.enabled or self.status != IntegrationStatus.AVAILABLE:
            return IntegrationResult(
                status=IntegrationStatus.DISABLED,
                message=f"Integration {self.name} not available for enhancement",
                data={"enhancement_status": "disabled"},
            )

        try:
            enhancement_result = self._enhance(core_result)
            return IntegrationResult(
                status=IntegrationStatus.AVAILABLE,
                message=f"Enhancement applied by {self.name}",
                data=enhancement_result,
            )
        except Exception as e:
            error_msg = f"Enhancement failed in {self.name}: {str(e)}"
            self.logger.error(error_msg)
            return IntegrationResult(
                status=IntegrationStatus.ERROR, message=error_msg, error=str(e)
            )

    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive integration status"""
        return {
            "name": self.name,
            "enabled": self.enabled,
            "status": self.status.value,
            "capabilities": self._capabilities,
            "dependencies": self._dependencies,
            "available": self.status == IntegrationStatus.AVAILABLE,
        }

    def _check_dependencies(self) -> List[str]:
        """Check if required dependencies are available"""
        missing = []
        for dep in self._dependencies:
            if not self._is_dependency_available(dep):
                missing.append(dep)
        return missing

    def _is_dependency_available(self, dependency: str) -> bool:
        """Check if a specific dependency is available"""
        # Default implementation - override in subclasses
        try:
            import importlib

            importlib.import_module(dependency)
            return True
        except ImportError:
            return False

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Perform integration-specific initialization"""
        # Override in subclasses
        return {"initialized": True}

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Perform integration-specific enhancement"""
        # Override in subclasses
        return {"enhancement": f"Applied by {self.name}"}

    def add_capability(self, capability: str):
        """Add a capability to this integration"""
        if capability not in self._capabilities:
            self._capabilities.append(capability)

    def add_dependency(self, dependency: str):
        """Add a dependency to this integration"""
        if dependency not in self._dependencies:
            self._dependencies.append(dependency)


class IntegrationManager:
    """
    Manages all YASK integrations with graceful degradation

    Coordinates multiple integrations while maintaining core YASK functionality
    even when integrations are unavailable.
    """

    def __init__(self):
        self.integrations: Dict[str, BaseIntegration] = {}
        self.logger = logging.getLogger("yask.integration.manager")
        self._enhancement_cache: Dict[str, Any] = {}

    def register_integration(self, integration: BaseIntegration):
        """Register an integration with the manager"""
        self.integrations[integration.name] = integration
        self.logger.debug(f"Registered integration: {integration.name}")

    def initialize_all(self) -> Dict[str, IntegrationResult]:
        """Initialize all registered integrations"""
        results = {}
        for name, integration in self.integrations.items():
            results[name] = integration.initialize()
        return results

    def enhance_result(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance core result with all available integrations

        Args:
            core_result: Result from core YASK validation

        Returns:
            Enhanced result with integration data
        """
        enhanced_result = {
            **core_result,
            "enhancements": {},
            "integration_status": {},
            "enhancement_summary": {
                "total_integrations": len(self.integrations),
                "enabled_integrations": 0,
                "available_integrations": 0,
                "applied_enhancements": 0,
            },
        }

        for name, integration in self.integrations.items():
            # Get integration status
            status = integration.get_status()
            enhanced_result["integration_status"][name] = status

            # Count enabled and available integrations
            if integration.enabled:
                enhanced_result["enhancement_summary"]["enabled_integrations"] += 1
            if status["available"]:
                enhanced_result["enhancement_summary"]["available_integrations"] += 1

            # Apply enhancement if available
            if integration.enabled and status["available"]:
                enhancement_result = integration.enhance(core_result)
                enhanced_result["enhancements"][name] = {
                    "status": enhancement_result.status.value,
                    "message": enhancement_result.message,
                    "data": enhancement_result.data,
                    "error": enhancement_result.error,
                }

                if enhancement_result.status == IntegrationStatus.AVAILABLE:
                    enhanced_result["enhancement_summary"]["applied_enhancements"] += 1

        return enhanced_result

    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system integration status"""
        status = {
            "total_integrations": len(self.integrations),
            "enabled_integrations": 0,
            "available_integrations": 0,
            "error_integrations": 0,
            "integrations": {},
        }

        for name, integration in self.integrations.items():
            integration_status = integration.get_status()
            status["integrations"][name] = integration_status

            if integration.enabled:
                status["enabled_integrations"] += 1
            if integration_status["available"]:
                status["available_integrations"] += 1
            if integration_status["status"] == IntegrationStatus.ERROR.value:
                status["error_integrations"] += 1

        return status

    def enable_integration(self, name: str) -> bool:
        """Enable a specific integration"""
        if name in self.integrations:
            self.integrations[name].enabled = True
            return True
        return False

    def disable_integration(self, name: str) -> bool:
        """Disable a specific integration"""
        if name in self.integrations:
            self.integrations[name].enabled = False
            return True
        return False

    def get_integration(self, name: str) -> Optional[BaseIntegration]:
        """Get a specific integration by name"""
        return self.integrations.get(name)


# Global integration manager instance
_integration_manager: Optional[IntegrationManager] = None


def get_integration_manager() -> IntegrationManager:
    """Get the global integration manager instance"""
    global _integration_manager
    if _integration_manager is None:
        _integration_manager = IntegrationManager()
    return _integration_manager


def is_integration_enabled(integration_name: str) -> bool:
    """Check if a specific integration is enabled"""
    manager = get_integration_manager()
    integration = manager.get_integration(integration_name)
    return integration.enabled if integration else False


def get_integration_status(integration_name: str) -> Dict[str, Any]:
    """Get status of a specific integration"""
    manager = get_integration_manager()
    integration = manager.get_integration(integration_name)
    return (
        integration.get_status() if integration else {"error": "Integration not found"}
    )
