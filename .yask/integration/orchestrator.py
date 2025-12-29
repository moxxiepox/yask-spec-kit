"""
YASK Integration Orchestrator

This module provides the main orchestration interface for YASK integrations,
combining all integration capabilities while maintaining core YASK simplicity.
"""

import os
import asyncio
import logging
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
from dataclasses import dataclass
import time

from .core import IntegrationManager, IntegrationResult, IntegrationStatus
from .mcp import MCPIntegrationFramework, create_mcp_integration
from .tools import (
    TreeSitterIntegration,
    CodeHealthIntegration,
    DocumentationIntegration,
    create_tree_sitter_integration,
    create_codehealth_integration,
    create_documentation_integration,
)
from .config import get_config_manager, ConfigManager
from .plugins import PluginManager, get_plugin_manager


@dataclass
class IntegrationContext:
    """Context container for integration operations"""

    project_path: Optional[Path] = None
    requirements: Optional[List[str]] = None
    design_docs: Optional[Dict[str, Path]] = None
    implementation_files: Optional[List[Path]] = None
    workflow_phase: Optional[str] = None
    user_preferences: Optional[Dict[str, Any]] = None
    performance_config: Optional[Dict[str, Any]] = None


class IntegrationOrchestrator:
    """
    Main orchestrator for YASK integrations

    Coordinates all integration capabilities while maintaining core YASK principles
    of simplicity, optional enhancement, and graceful degradation.
    """

    def __init__(self, config_manager: Optional[ConfigManager] = None):
        self.config_manager = config_manager or get_config_manager()
        self.integration_manager = IntegrationManager()
        self.plugin_manager = PluginManager()
        self.logger = logging.getLogger("yask.integration.orchestrator")

        # Initialize default integrations
        self._initialize_default_integrations()

        # Performance tracking
        self._performance_metrics = {
            "total_enhancements": 0,
            "successful_enhancements": 0,
            "failed_enhancements": 0,
            "average_enhancement_time": 0.0,
        }

    def _initialize_default_integrations(self):
        """Initialize default YASK integrations"""
        # MCP Integration
        if self.config_manager.is_enabled("mcp"):
            mcp_integration = create_mcp_integration(enabled=True)
            self.integration_manager.register_integration(mcp_integration)

        # Tree-Sitter Integration
        if self.config_manager.is_enabled("tree_sitter"):
            tree_sitter_config = self.config_manager.get_integration_config(
                "tree_sitter"
            )
            languages = tree_sitter_config.get(
                "languages", ["python", "javascript", "typescript"]
            )
            tree_sitter_integration = create_tree_sitter_integration(
                enabled=True, languages=languages
            )
            self.integration_manager.register_integration(tree_sitter_integration)

        # Code Health Integration
        if self.config_manager.is_enabled("code_health"):
            code_health_config = self.config_manager.get_integration_config(
                "code_health"
            )
            strictness = code_health_config.get("strictness", "standard")
            code_health_integration = create_codehealth_integration(
                enabled=True, strictness=strictness
            )
            self.integration_manager.register_integration(code_health_integration)

        # Documentation Integration
        if self.config_manager.is_enabled("documentation"):
            doc_integration = create_documentation_integration(enabled=True)
            self.integration_manager.register_integration(doc_integration)

        # Initialize all integrations
        initialization_results = self.integration_manager.initialize_all()

        # Log initialization results
        for name, result in initialization_results.items():
            if result.status == IntegrationStatus.AVAILABLE:
                self.logger.info(f"Integration {name} initialized successfully")
            else:
                self.logger.warning(
                    f"Integration {name} initialization: {result.message}"
                )

    def enhance_workflow(self, context: IntegrationContext) -> Dict[str, Any]:
        """
        Enhance YASK workflow with all available integrations

        Args:
            context: Integration context with project information

        Returns:
            Enhanced workflow results
        """
        start_time = time.time()

        try:
            # Create core result from context
            core_result = self._create_core_result(context)

            # Enhance with all available integrations
            enhanced_result = self.integration_manager.enhance_result(core_result)

            # Add plugin enhancements if available
            plugin_enhancement = self._enhance_with_plugins(context)
            if plugin_enhancement:
                enhanced_result["plugin_enhancements"] = plugin_enhancement

            # Add performance metrics
            execution_time = time.time() - start_time
            enhanced_result["performance_metrics"] = self._update_performance_metrics(
                execution_time
            )

            # Add integration summary
            enhanced_result["integration_summary"] = self._create_integration_summary()

            return enhanced_result

        except Exception as e:
            self.logger.error(f"Workflow enhancement failed: {e}")
            return {
                "status": "error",
                "message": f"Enhancement failed: {str(e)}",
                "core_result": self._create_core_result(context),
                "enhancements": {},
                "performance_metrics": self._update_performance_metrics(
                    time.time() - start_time
                ),
            }

    def _create_core_result(self, context: IntegrationContext) -> Dict[str, Any]:
        """Create core YASK result from context"""
        core_result = {
            "project_path": str(context.project_path) if context.project_path else None,
            "workflow_phase": context.workflow_phase,
            "enhancement_timestamp": time.time(),
        }

        # Add requirements if available
        if context.requirements:
            core_result["requirements"] = context.requirements

        # Add file paths if available
        if context.implementation_files:
            core_result["file_paths"] = [str(f) for f in context.implementation_files]

        # Add design documents if available
        if context.design_docs:
            core_result["design_docs"] = {
                k: str(v) for k, v in context.design_docs.items()
            }

        return core_result

    def _enhance_with_plugins(
        self, context: IntegrationContext
    ) -> Optional[Dict[str, Any]]:
        """Enhance workflow with loaded plugins"""
        try:
            loaded_plugins = self.plugin_manager.list_loaded_plugins()
            if not loaded_plugins:
                return None

            plugin_results = {}

            for plugin_name in loaded_plugins:
                try:
                    plugin = self.plugin_manager.get_plugin(plugin_name)
                    if plugin:
                        # Create context for plugin
                        plugin_context = {
                            "project_path": str(context.project_path)
                            if context.project_path
                            else None,
                            "requirements": context.requirements,
                            "workflow_phase": context.workflow_phase,
                            "user_preferences": context.user_preferences,
                        }

                        # Enhance with plugin
                        enhanced_context = plugin.enhance(plugin_context)
                        plugin_results[plugin_name] = {
                            "status": "success",
                            "enhanced_context": enhanced_context,
                            "capabilities": plugin.get_capabilities(),
                        }

                except Exception as e:
                    self.logger.warning(f"Plugin {plugin_name} enhancement failed: {e}")
                    plugin_results[plugin_name] = {"status": "error", "error": str(e)}

            return plugin_results

        except Exception as e:
            self.logger.error(f"Plugin enhancement failed: {e}")
            return None

    def _update_performance_metrics(self, execution_time: float) -> Dict[str, Any]:
        """Update and return performance metrics"""
        self._performance_metrics["total_enhancements"] += 1

        if execution_time < 30:  # Consider successful if under 30 seconds
            self._performance_metrics["successful_enhancements"] += 1
        else:
            self._performance_metrics["failed_enhancements"] += 1

        # Update average execution time
        total = self._performance_metrics["total_enhancements"]
        current_avg = self._performance_metrics["average_enhancement_time"]
        self._performance_metrics["average_enhancement_time"] = (
            current_avg * (total - 1) + execution_time
        ) / total

        return self._performance_metrics.copy()

    def _create_integration_summary(self) -> Dict[str, Any]:
        """Create integration summary"""
        system_status = self.integration_manager.get_system_status()
        plugin_status = self.plugin_manager.get_plugin_status()

        return {
            "integrations": {
                "total": system_status["total_integrations"],
                "enabled": system_status["enabled_integrations"],
                "available": system_status["available_integrations"],
                "error": system_status["error_integrations"],
            },
            "plugins": {
                "total": plugin_status["total_plugins"],
                "loaded": plugin_status["loaded_plugins"],
            },
            "configuration": {
                "environment": self.config_manager.get_environment_info(),
                "performance": self.config_manager.get_performance_config(),
            },
        }

    async def enhance_async(self, context: IntegrationContext) -> Dict[str, Any]:
        """Asynchronous version of workflow enhancement"""
        # For now, just call the synchronous version
        # In a full implementation, this would run integrations in parallel
        return self.enhance_workflow(context)

    def get_integration_status(self) -> Dict[str, Any]:
        """Get comprehensive integration status"""
        return {
            "integration_manager": self.integration_manager.get_system_status(),
            "plugin_manager": self.plugin_manager.get_plugin_status(),
            "configuration": self.config_manager.get_summary(),
            "performance_metrics": self._performance_metrics,
        }

    def enable_integration(self, integration_name: str) -> bool:
        """Enable a specific integration"""
        success = self.integration_manager.enable_integration(integration_name)
        if success:
            # Re-initialize the integration
            integration = self.integration_manager.get_integration(integration_name)
            if integration:
                result = integration.initialize()
                self.logger.info(
                    f"Integration {integration_name} enabled: {result.message}"
                )
        return success

    def disable_integration(self, integration_name: str) -> bool:
        """Disable a specific integration"""
        return self.integration_manager.disable_integration(integration_name)

    def load_plugin(self, plugin_name: str) -> bool:
        """Load a specific plugin"""
        return self.plugin_manager.load_plugin(plugin_name)

    def unload_plugin(self, plugin_name: str) -> bool:
        """Unload a specific plugin"""
        return self.plugin_manager.unload_plugin(plugin_name)

    def create_plugin_integration(self, plugin_name: str, enabled: bool = False):
        """Create integration from plugin"""
        return self.plugin_manager.create_integration(plugin_name, enabled)

    def get_available_integrations(self) -> List[str]:
        """Get list of available integration names"""
        return list(self.integration_manager.integrations.keys())

    def get_available_plugins(self) -> List[str]:
        """Get list of available plugin names"""
        return list(self.plugin_manager.list_plugins().keys())

    def validate_configuration(self) -> Dict[str, Any]:
        """Validate current integration configuration"""
        config_validation = self.config_manager.config.validate_configuration()
        integration_status = self.get_integration_status()

        return {
            "configuration": config_validation,
            "integrations": integration_status["integration_manager"],
            "plugins": integration_status["plugin_manager"],
            "overall_health": "healthy"
            if config_validation["valid"]
            else "issues_detected",
        }

    def export_configuration(self, file_path: Path):
        """Export current configuration to file"""
        config_data = {
            "integrations": {},
            "plugins": {},
            "performance": self.config_manager.get_performance_config(),
            "environment": self.config_manager.get_environment_info(),
        }

        # Export integration configurations
        for integration_name in self.get_available_integrations():
            config_data["integrations"][integration_name] = {
                "enabled": self.integration_manager.get_integration(
                    integration_name
                ).enabled,
                "config": self.config_manager.get_integration_config(integration_name),
            }

        # Export plugin configurations
        for plugin_name in self.get_available_plugins():
            metadata = self.plugin_manager.get_plugin_metadata(plugin_name)
            if metadata:
                config_data["plugins"][plugin_name] = {
                    "loaded": metadata.loaded,
                    "version": metadata.version,
                    "capabilities": metadata.capabilities,
                }

        # Write to file
        import yaml

        with open(file_path, "w") as f:
            yaml.dump(config_data, f, default_flow_style=False, indent=2)

    def reset_performance_metrics(self):
        """Reset performance metrics"""
        self._performance_metrics = {
            "total_enhancements": 0,
            "successful_enhancements": 0,
            "failed_enhancements": 0,
            "average_enhancement_time": 0.0,
        }


# Global orchestrator instance
_orchestrator: Optional[IntegrationOrchestrator] = None


def get_orchestrator() -> IntegrationOrchestrator:
    """Get the global integration orchestrator instance"""
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = IntegrationOrchestrator()
    return _orchestrator


def enhance_yask_workflow(context: IntegrationContext) -> Dict[str, Any]:
    """Enhance YASK workflow with integrations"""
    return get_orchestrator().enhance_workflow(context)


def get_integration_status() -> Dict[str, Any]:
    """Get integration status"""
    return get_orchestrator().get_integration_status()


def validate_integration_config() -> Dict[str, Any]:
    """Validate integration configuration"""
    return get_orchestrator().validate_configuration()


# Convenience functions for common use cases
def create_integration_context(
    project_path: Optional[Union[str, Path]] = None,
    requirements: Optional[List[str]] = None,
    workflow_phase: Optional[str] = None,
    **kwargs,
) -> IntegrationContext:
    """Create integration context with common parameters"""
    if project_path and isinstance(project_path, str):
        project_path = Path(project_path)

    return IntegrationContext(
        project_path=project_path,
        requirements=requirements,
        workflow_phase=workflow_phase,
        **kwargs,
    )


def quick_enhance(
    project_path: Union[str, Path], requirements: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Quick workflow enhancement for simple cases"""
    context = create_integration_context(
        project_path=project_path,
        requirements=requirements,
        workflow_phase="implementation",
    )
    return enhance_yask_workflow(context)
