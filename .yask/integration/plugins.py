"""
YASK Plugin Architecture and Customization Mechanisms

This module provides plugin architecture for extensibility while maintaining
core YASK principles and enabling adaptation to specific project needs.
"""

import os
import importlib.util
import importlib.machinery
import inspect
from typing import Dict, Any, Optional, List, Type, Callable
from pathlib import Path
from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
import traceback

from .core import BaseIntegration, IntegrationResult, IntegrationStatus
from .config import get_config_manager


class PluginInterface(ABC):
    """
    Abstract base class for YASK plugins

    Defines the interface that all YASK plugins must implement
    while maintaining core YASK principles.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Plugin name"""
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """Plugin version"""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Plugin description"""
        pass

    @property
    @abstractmethod
    def dependencies(self) -> List[str]:
        """Plugin dependencies"""
        pass

    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the plugin"""
        pass

    @abstractmethod
    def enhance(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance YASK context with plugin capabilities

        Args:
            context: YASK context dictionary

        Returns:
            Enhanced context dictionary
        """
        pass

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """Get plugin capabilities"""
        pass

    @abstractmethod
    def get_configuration_schema(self) -> Dict[str, Any]:
        """Get plugin configuration schema"""
        pass


@dataclass
class PluginMetadata:
    """Plugin metadata container"""

    name: str
    version: str
    description: str
    author: str = ""
    dependencies: List[str] = None
    capabilities: List[str] = None
    config_schema: Dict[str, Any] = None
    file_path: Optional[Path] = None
    loaded: bool = False
    error: Optional[str] = None


class CustomIntegration(BaseIntegration):
    """
    Base class for custom integrations created through plugins

    Provides common functionality for plugin-based integrations
    while maintaining YASK's core simplicity.
    """

    def __init__(self, plugin: PluginInterface, enabled: bool = False):
        super().__init__(f"plugin_{plugin.name}", enabled)
        self.plugin = plugin
        self.logger = logging.getLogger(f"yask.integration.plugin.{plugin.name}")

        # Add plugin capabilities
        for capability in plugin.get_capabilities():
            self.add_capability(capability)

        # Add plugin dependencies
        for dependency in plugin.dependencies:
            self.add_dependency(dependency)

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Initialize the plugin"""
        try:
            success = self.plugin.initialize()
            if success:
                return {
                    "plugin_name": self.plugin.name,
                    "plugin_version": self.plugin.version,
                    "capabilities": self.plugin.get_capabilities(),
                    "dependencies": self.plugin.dependencies,
                }
            else:
                return {"error": "Plugin initialization failed"}
        except Exception as e:
            self.logger.error(f"Plugin initialization error: {e}")
            return {"error": str(e)}

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance result using plugin capabilities"""
        try:
            # Prepare context for plugin
            context = {
                **core_result,
                "plugin_info": {
                    "name": self.plugin.name,
                    "version": self.plugin.version,
                    "capabilities": self.plugin.get_capabilities(),
                },
            }

            # Call plugin enhancement
            enhanced_context = self.plugin.enhance(context)

            return {
                "plugin_enhancement": {
                    "plugin_name": self.plugin.name,
                    "enhanced_context": enhanced_context,
                },
                "enhancement_applied": True,
            }

        except Exception as e:
            self.logger.error(f"Plugin enhancement error: {e}")
            return {
                "plugin_error": {"plugin_name": self.plugin.name, "error": str(e)},
                "enhancement_applied": False,
            }


class PluginManager:
    """
    Plugin manager for YASK integrations

    Handles plugin discovery, loading, initialization, and lifecycle management
    while maintaining core YASK principles and graceful degradation.
    """

    def __init__(self, plugin_dirs: Optional[List[Path]] = None):
        self.plugin_dirs = plugin_dirs or self._default_plugin_dirs()
        self.logger = logging.getLogger("yask.integration.plugin_manager")
        self._plugins: Dict[str, PluginMetadata] = {}
        self._loaded_plugins: Dict[str, PluginInterface] = {}
        self._plugin_instances: Dict[str, CustomIntegration] = {}

        # Discover available plugins
        self._discover_plugins()

    def _default_plugin_dirs(self) -> List[Path]:
        """Get default plugin directories"""
        dirs = [
            Path(".yask/plugins"),
            Path.home() / ".yask" / "plugins",
            Path(__file__).parent.parent / "plugins",
        ]
        return [d for d in dirs if d.exists() or d.parent.exists()]

    def _discover_plugins(self):
        """Discover available plugins in plugin directories"""
        for plugin_dir in self.plugin_dirs:
            if not plugin_dir.exists():
                continue

            self.logger.debug(f"Discovering plugins in: {plugin_dir}")

            # Look for Python files that might contain plugins
            for py_file in plugin_dir.rglob("*.py"):
                if py_file.name.startswith("_"):
                    continue

                try:
                    self._load_plugin_file(py_file)
                except Exception as e:
                    self.logger.warning(f"Failed to load plugin file {py_file}: {e}")

    def _load_plugin_file(self, file_path: Path):
        """Load plugin from Python file"""
        try:
            # Add plugin directory to Python path
            plugin_dir = str(file_path.parent)
            if plugin_dir not in __import__("sys").path:
                __import__("sys").path.insert(0, plugin_dir)

            # Import module
            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                return

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Look for plugin classes
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if (
                    issubclass(obj, PluginInterface)
                    and obj is not PluginInterface
                    and not inspect.isabstract(obj)
                ):
                    try:
                        # Create plugin instance to get metadata
                        plugin_instance = obj()
                        metadata = PluginMetadata(
                            name=plugin_instance.name,
                            version=plugin_instance.version,
                            description=plugin_instance.description,
                            author=getattr(plugin_instance, "author", ""),
                            dependencies=plugin_instance.dependencies,
                            capabilities=plugin_instance.get_capabilities(),
                            config_schema=plugin_instance.get_configuration_schema(),
                            file_path=file_path,
                            loaded=False,
                        )

                        self._plugins[metadata.name] = metadata
                        self.logger.debug(
                            f"Discovered plugin: {metadata.name} v{metadata.version}"
                        )

                    except Exception as e:
                        self.logger.warning(f"Failed to instantiate plugin {name}: {e}")
                        continue

        except Exception as e:
            self.logger.error(f"Error loading plugin file {file_path}: {e}")

    def load_plugin(self, plugin_name: str) -> bool:
        """
        Load a specific plugin

        Args:
            plugin_name: Name of the plugin to load

        Returns:
            True if plugin loaded successfully
        """
        if plugin_name not in self._plugins:
            self.logger.error(f"Plugin not found: {plugin_name}")
            return False

        metadata = self._plugins[plugin_name]

        if metadata.loaded:
            self.logger.debug(f"Plugin already loaded: {plugin_name}")
            return True

        try:
            # Load the plugin module
            plugin_module = self._load_plugin_module(metadata.file_path)
            if plugin_module is None:
                return False

            # Find and instantiate the plugin class
            plugin_class = self._find_plugin_class(plugin_module, plugin_name)
            if plugin_class is None:
                return False

            # Check dependencies
            if not self._check_plugin_dependencies(plugin_class):
                self.logger.error(f"Plugin dependencies not satisfied: {plugin_name}")
                return False

            # Instantiate plugin
            plugin_instance = plugin_class()

            # Store loaded plugin
            self._loaded_plugins[plugin_name] = plugin_instance
            metadata.loaded = True
            metadata.error = None

            self.logger.info(f"Successfully loaded plugin: {plugin_name}")
            return True

        except Exception as e:
            error_msg = f"Failed to load plugin {plugin_name}: {str(e)}"
            self.logger.error(error_msg)
            metadata.error = error_msg
            return False

    def _load_plugin_module(self, file_path: Path):
        """Load plugin module from file"""
        try:
            plugin_dir = str(file_path.parent)
            if plugin_dir not in __import__("sys").path:
                __import__("sys").path.insert(0, plugin_dir)

            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                return None

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module

        except Exception as e:
            self.logger.error(f"Error loading plugin module {file_path}: {e}")
            return None

    def _find_plugin_class(
        self, module, plugin_name: str
    ) -> Optional[Type[PluginInterface]]:
        """Find plugin class in module"""
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(obj, PluginInterface)
                and obj is not PluginInterface
                and not inspect.isabstract(obj)
                and obj().name == plugin_name
            ):
                return obj
        return None

    def _check_plugin_dependencies(self, plugin_class: Type[PluginInterface]) -> bool:
        """Check if plugin dependencies are satisfied"""
        try:
            plugin_instance = plugin_class()
            dependencies = plugin_instance.dependencies

            for dep in dependencies:
                if dep.startswith("yask:"):
                    # YASK integration dependency
                    integration_name = dep[5:]  # Remove "yask:" prefix
                    if not self._is_yask_integration_available(integration_name):
                        return False
                elif dep.startswith("plugin:"):
                    # Plugin dependency
                    plugin_dep = dep[7:]  # Remove "plugin:" prefix
                    if plugin_dep not in self._loaded_plugins:
                        return False
                else:
                    # External dependency - check if it can be imported
                    try:
                        importlib.import_module(dep)
                    except ImportError:
                        return False

            return True

        except Exception as e:
            self.logger.error(f"Error checking plugin dependencies: {e}")
            return False

    def _is_yask_integration_available(self, integration_name: str) -> bool:
        """Check if YASK integration is available"""
        from . import get_integration_manager

        manager = get_integration_manager()
        integration = manager.get_integration(integration_name)
        return integration is not None and integration.enabled

    def create_integration(
        self, plugin_name: str, enabled: bool = False
    ) -> Optional[CustomIntegration]:
        """
        Create integration instance from plugin

        Args:
            plugin_name: Name of the plugin
            enabled: Whether the integration should be enabled

        Returns:
            CustomIntegration instance or None if creation failed
        """
        if plugin_name not in self._loaded_plugins:
            if not self.load_plugin(plugin_name):
                return None

        plugin = self._loaded_plugins[plugin_name]
        integration = CustomIntegration(plugin, enabled)

        self._plugin_instances[plugin_name] = integration
        return integration

    def get_plugin(self, plugin_name: str) -> Optional[PluginInterface]:
        """Get loaded plugin instance"""
        return self._loaded_plugins.get(plugin_name)

    def get_plugin_metadata(self, plugin_name: str) -> Optional[PluginMetadata]:
        """Get plugin metadata"""
        return self._plugins.get(plugin_name)

    def list_plugins(self) -> Dict[str, PluginMetadata]:
        """List all discovered plugins"""
        return self._plugins.copy()

    def list_loaded_plugins(self) -> List[str]:
        """List names of loaded plugins"""
        return list(self._loaded_plugins.keys())

    def get_plugin_capabilities(self, plugin_name: str) -> List[str]:
        """Get capabilities of a specific plugin"""
        plugin = self._loaded_plugins.get(plugin_name)
        if plugin:
            return plugin.get_capabilities()
        return []

    def get_plugin_config_schema(self, plugin_name: str) -> Dict[str, Any]:
        """Get configuration schema for a plugin"""
        plugin = self._loaded_plugins.get(plugin_name)
        if plugin:
            return plugin.get_configuration_schema()
        return {}

    def unload_plugin(self, plugin_name: str) -> bool:
        """
        Unload a plugin

        Args:
            plugin_name: Name of the plugin to unload

        Returns:
            True if plugin unloaded successfully
        """
        if plugin_name not in self._loaded_plugins:
            return True  # Already unloaded

        try:
            # Remove integration instance
            if plugin_name in self._plugin_instances:
                del self._plugin_instances[plugin_name]

            # Remove plugin instance
            del self._loaded_plugins[plugin_name]

            # Update metadata
            if plugin_name in self._plugins:
                self._plugins[plugin_name].loaded = False

            self.logger.info(f"Unloaded plugin: {plugin_name}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to unload plugin {plugin_name}: {e}")
            return False

    def reload_plugin(self, plugin_name: str) -> bool:
        """
        Reload a plugin

        Args:
            plugin_name: Name of the plugin to reload

        Returns:
            True if plugin reloaded successfully
        """
        self.unload_plugin(plugin_name)
        return self.load_plugin(plugin_name)

    def get_plugin_status(self) -> Dict[str, Any]:
        """Get comprehensive plugin status"""
        return {
            "total_plugins": len(self._plugins),
            "loaded_plugins": len(self._loaded_plugins),
            "plugin_dirs": [str(d) for d in self.plugin_dirs],
            "plugins": {
                name: {
                    "loaded": metadata.loaded,
                    "version": metadata.version,
                    "description": metadata.description,
                    "error": metadata.error,
                    "capabilities": metadata.capabilities or [],
                }
                for name, metadata in self._plugins.items()
            },
        }


class PluginTemplate:
    """
    Template for creating custom YASK plugins

    Provides a starting point for developing custom integrations
    while maintaining YASK principles.
    """

    @staticmethod
    def create_plugin_template(plugin_name: str, output_dir: Path) -> Path:
        """
        Create a plugin template file

        Args:
            plugin_name: Name of the plugin
            output_dir: Directory to create the template in

        Returns:
            Path to created template file
        """
        template_content = f'''"""
{plugin_name} Plugin for YASK

This plugin provides custom integration capabilities for YASK
while maintaining core YASK principles.
"""

from typing import Dict, Any, List
from yask.integration.plugins import PluginInterface


class {plugin_name.replace(" ", "").replace("-", "").title()}Plugin(PluginInterface):
    """
    {plugin_name} plugin for YASK integrations
    
    This plugin provides custom functionality while maintaining
    YASK's core simplicity and graceful degradation.
    """
    
    @property
    def name(self) -> str:
        return "{plugin_name}"
    
    @property
    def version(self) -> str:
        return "1.0.0"
    
    @property
    def description(self) -> str:
        return "Custom {plugin_name} integration for YASK"
    
    @property
    def dependencies(self) -> List[str]:
        return [
            # Add dependencies here, e.g.:
            # "yask:tree_sitter",  # Requires Tree-Sitter integration
            # "plugin:other_plugin",  # Requires another plugin
            # "requests",  # External dependency
        ]
    
    def initialize(self) -> bool:
        """
        Initialize the plugin
        
        Returns:
            True if initialization successful
        """
        try:
            # Add initialization logic here
            # Check dependencies, set up resources, etc.
            return True
        except Exception:
            return False
    
    def enhance(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance YASK context with plugin capabilities
        
        Args:
            context: YASK context dictionary
            
        Returns:
            Enhanced context dictionary
        """
        try:
            # Add enhancement logic here
            # Modify context based on plugin capabilities
            enhanced_context = {{
                **context,
                "{plugin_name.lower().replace(" ", "_")}_enhanced": True,
                "plugin_capabilities": self.get_capabilities()
            }}
            
            return enhanced_context
        except Exception as e:
            # Graceful degradation - return original context on error
            return context
    
    def get_capabilities(self) -> List[str]:
        """Get plugin capabilities"""
        return [
            "{plugin_name.lower().replace(" ", "_")}_enhancement",
            # Add more capabilities here
        ]
    
    def get_configuration_schema(self) -> Dict[str, Any]:
        """Get plugin configuration schema"""
        return {{
            "type": "object",
            "properties": {{
                "enabled": {{
                    "type": "boolean",
                    "description": "Enable {plugin_name} plugin",
                    "default": False
                }},
                "strictness": {{
                    "type": "string",
                    "enum": ["basic", "standard", "strict"],
                    "description": "Analysis strictness level",
                    "default": "standard"
                }}
            }},
            "additionalProperties": False
        }}


# Plugin instance for auto-discovery
plugin = {plugin_name.replace(" ", "").replace("-", "").title()}Plugin()
'''

        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create plugin file
        plugin_file = output_dir / f"{plugin_name.lower().replace(' ', '_')}_plugin.py"
        plugin_file.write_text(template_content)

        return plugin_file

    @staticmethod
    def create_plugin_package(plugin_name: str, output_dir: Path) -> Path:
        """
        Create a complete plugin package structure

        Args:
            plugin_name: Name of the plugin
            output_dir: Directory to create the package in

        Returns:
            Path to created package directory
        """
        package_name = plugin_name.lower().replace(" ", "_").replace("-", "_")
        package_dir = output_dir / package_name
        package_dir.mkdir(parents=True, exist_ok=True)

        # Create __init__.py
        init_content = f'''"""
{plugin_name} Plugin Package

This package contains the {plugin_name} plugin for YASK.
"""

from .{package_name}_plugin import {plugin_name.replace(" ", "").replace("-", "").title()}Plugin

__all__ = ["{plugin_name.replace(" ", "").replace("-", "").title()}Plugin"]
'''
        (package_dir / "__init__.py").write_text(init_content)

        # Create plugin file
        plugin_file = PluginTemplate.create_plugin_template(plugin_name, package_dir)

        # Create config schema file
        config_content = f'''"""
Configuration schema for {plugin_name} plugin
"""

{plugin_name.lower().replace(" ", "_").replace("-", "_")}_config_schema = {{
    "type": "object",
    "properties": {{
        "enabled": {{
            "type": "boolean",
            "description": "Enable {plugin_name} plugin",
            "default": False
        }},
        "strictness": {{
            "type": "string",
            "enum": ["basic", "standard", "strict"],
            "description": "Analysis strictness level",
            "default": "standard"
        }},
        "custom_option": {{
            "type": "string",
            "description": "Custom plugin option",
            "default": "default_value"
        }}
    }},
    "additionalProperties": False
}}
'''
        (package_dir / "config_schema.py").write_text(config_content)

        # Create README
        plugin_name_safe = plugin_name.lower().replace(" ", "_").replace("-", "_")
        readme_content = f"""# {plugin_name} Plugin for YASK

This plugin provides custom integration capabilities for YASK.

## Installation

1. Copy this plugin directory to your YASK plugins folder:
   - `.yask/plugins/{package_name}/`
   - Or `~/.yask/plugins/{package_name}/`

2. Enable the plugin in your configuration:
   ```bash
   export YASK_ENABLE_{plugin_name.upper().replace(" ", "_").replace("-", "_")}=true
   ```

## Configuration

The plugin supports the following configuration options:

- `enabled`: Enable/disable the plugin (default: false)
- `strictness`: Analysis strictness level (basic, standard, strict)
- `custom_option`: Custom plugin option (default: default_value)

## Usage

Once enabled, the plugin will automatically enhance YASK workflows with additional capabilities.

## Development

To modify this plugin:

1. Edit `{package_name}_plugin.py` to change plugin behavior
2. Update `config_schema.py` to modify configuration options
3. Test your changes by reloading the plugin

## Capabilities

- {plugin_name_safe}_enhancement
- Additional capabilities can be added in the plugin code
"""
        (package_dir / "README.md").write_text(readme_content)

        return package_dir


# Global plugin manager instance
_plugin_manager: Optional[PluginManager] = None


def get_plugin_manager() -> PluginManager:
    """Get the global plugin manager instance"""
    global _plugin_manager
    if _plugin_manager is None:
        _plugin_manager = PluginManager()
    return _plugin_manager


def load_plugin(plugin_name: str) -> bool:
    """Load a specific plugin"""
    return get_plugin_manager().load_plugin(plugin_name)


def create_plugin_integration(
    plugin_name: str, enabled: bool = False
) -> Optional[CustomIntegration]:
    """Create integration from plugin"""
    return get_plugin_manager().create_integration(plugin_name, enabled)


def list_available_plugins() -> Dict[str, PluginMetadata]:
    """List all available plugins"""
    return get_plugin_manager().list_plugins()


def create_plugin_template(plugin_name: str, output_dir: Path) -> Path:
    """Create a plugin template"""
    return PluginTemplate.create_plugin_template(plugin_name, output_dir)


def create_plugin_package(plugin_name: str, output_dir: Path) -> Path:
    """Create a complete plugin package"""
    return PluginTemplate.create_plugin_package(plugin_name, output_dir)
