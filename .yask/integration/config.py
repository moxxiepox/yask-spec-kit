"""
YASK Configuration Management

This module provides environment-based configuration management with graceful degradation,
fallback behavior, and performance optimization for integration loading.
"""

import os
import yaml
import json
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum
import logging


class ConfigSource(Enum):
    """Configuration source enumeration"""

    ENVIRONMENT = "environment"
    FILE = "file"
    DEFAULT = "default"
    COMPUTED = "computed"


@dataclass
class ConfigValue:
    """Configuration value with metadata"""

    value: Any
    source: ConfigSource
    description: str = ""
    required: bool = False
    fallback: Any = None
    validation_rules: List[str] = field(default_factory=list)


class IntegrationConfig:
    """
    Configuration manager for YASK integrations

    Provides environment-based configuration with graceful degradation,
    fallback behavior, and validation.
    """

    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or Path(".yask")
        self.logger = logging.getLogger("yask.integration.config")
        self._config_cache: Dict[str, Any] = {}
        self._config_sources: Dict[str, ConfigValue] = {}
        self._validation_rules: Dict[str, List[str]] = {}

        # Initialize default configuration
        self._initialize_default_config()

    def _initialize_default_config(self):
        """Initialize default configuration values"""
        # Integration enablement defaults (all disabled by default)
        self._config_sources.update(
            {
                "yask_enable_tree_sitter": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable Tree-Sitter integration for code analysis",
                    required=False,
                ),
                "yask_enable_code_health": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable code health analysis integration",
                    required=False,
                ),
                "yask_enable_documentation": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable documentation consistency validation",
                    required=False,
                ),
                "yask_enable_mcp": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable MCP (Model Context Protocol) integration",
                    required=False,
                ),
                # MCP configuration
                "yask_mcp_servers": ConfigValue(
                    value="",
                    source=ConfigSource.DEFAULT,
                    description="Comma-separated list of MCP servers to enable",
                    required=False,
                ),
                "yask_mcp_timeout": ConfigValue(
                    value=30,
                    source=ConfigSource.DEFAULT,
                    description="MCP server connection timeout in seconds",
                    required=False,
                    validation_rules=["positive_integer"],
                ),
                # Tree-Sitter configuration
                "yask_tree_sitter_languages": ConfigValue(
                    value="python,javascript,typescript,rust,go",
                    source=ConfigSource.DEFAULT,
                    description="Comma-separated list of supported languages for Tree-Sitter",
                    required=False,
                ),
                "yask_tree_sitter_timeout": ConfigValue(
                    value=30,
                    source=ConfigSource.DEFAULT,
                    description="Tree-Sitter analysis timeout in seconds",
                    required=False,
                    validation_rules=["positive_integer"],
                ),
                # Code Health configuration
                "yask_code_health_strictness": ConfigValue(
                    value="standard",
                    source=ConfigSource.DEFAULT,
                    description="Code health analysis strictness level (basic, standard, strict)",
                    required=False,
                    validation_rules=["enum:basic,standard,strict"],
                ),
                "yask_code_health_timeout": ConfigValue(
                    value=60,
                    source=ConfigSource.DEFAULT,
                    description="Code health analysis timeout in seconds",
                    required=False,
                    validation_rules=["positive_integer"],
                ),
                # Documentation configuration
                "yask_doc_validation_strictness": ConfigValue(
                    value="standard",
                    source=ConfigSource.DEFAULT,
                    description="Documentation validation strictness level",
                    required=False,
                    validation_rules=["enum:basic,standard,strict"],
                ),
                # Performance configuration
                "yask_integration_cache_enabled": ConfigValue(
                    value=True,
                    source=ConfigSource.DEFAULT,
                    description="Enable integration result caching",
                    required=False,
                ),
                "yask_integration_cache_ttl": ConfigValue(
                    value=300,
                    source=ConfigSource.DEFAULT,
                    description="Cache TTL in seconds",
                    required=False,
                    validation_rules=["positive_integer"],
                ),
                "yask_integration_parallel_enabled": ConfigValue(
                    value=True,
                    source=ConfigSource.DEFAULT,
                    description="Enable parallel integration execution",
                    required=False,
                ),
                "yask_integration_max_concurrent": ConfigValue(
                    value=3,
                    source=ConfigSource.DEFAULT,
                    description="Maximum concurrent integration executions",
                    required=False,
                    validation_rules=["positive_integer"],
                ),
                # Logging configuration
                "yask_integration_log_level": ConfigValue(
                    value="INFO",
                    source=ConfigSource.DEFAULT,
                    description="Integration logging level",
                    required=False,
                    validation_rules=["enum:DEBUG,INFO,WARNING,ERROR"],
                ),
                "yask_integration_log_to_file": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable integration logging to file",
                    required=False,
                ),
                # Feature flags
                "yask_integration_enhanced_validation": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable enhanced validation features",
                    required=False,
                ),
                "yask_integration_experimental_features": ConfigValue(
                    value=False,
                    source=ConfigSource.DEFAULT,
                    description="Enable experimental integration features",
                    required=False,
                ),
            }
        )

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value with fallback hierarchy

        Args:
            key: Configuration key
            default: Default value if not found

        Returns:
            Configuration value
        """
        # Check cache first
        if key in self._config_cache:
            return self._config_cache[key]

        # Try environment variable
        env_value = self._get_from_environment(key)
        if env_value is not None:
            self._config_cache[key] = env_value
            return env_value

        # Try configuration file
        file_value = self._get_from_file(key)
        if file_value is not None:
            self._config_cache[key] = file_value
            return file_value

        # Use default value
        if key in self._config_sources:
            default_value = self._config_sources[key].value
            self._config_cache[key] = default_value
            return default_value

        # Return provided default or None
        return default

    def set(self, key: str, value: Any, source: ConfigSource = ConfigSource.COMPUTED):
        """
        Set configuration value

        Args:
            key: Configuration key
            value: Configuration value
            source: Source of the configuration value
        """
        # Validate value
        if not self._validate_value(key, value):
            raise ValueError(f"Invalid value for configuration key: {key}")

        # Update cache and source
        self._config_cache[key] = value

        if key in self._config_sources:
            self._config_sources[key].value = value
            self._config_sources[key].source = source
        else:
            self._config_sources[key] = ConfigValue(
                value=value, source=source, description=f"Custom configuration: {key}"
            )

    def _get_from_environment(self, key: str) -> Optional[Any]:
        """Get configuration value from environment variables"""
        env_key = key.upper()

        # Try exact match
        env_value = os.getenv(env_key)
        if env_value is not None:
            return self._parse_env_value(env_value, key)

        # Try alternative naming patterns
        alt_keys = [
            f"YASK_{env_key}",
            f"YASK_INTEGRATION_{env_key}",
            env_key.replace("yask_", "YASK_"),
        ]

        for alt_key in alt_keys:
            env_value = os.getenv(alt_key)
            if env_value is not None:
                return self._parse_env_value(env_value, key)

        return None

    def _parse_env_value(self, env_value: str, key: str) -> Any:
        """Parse environment variable value"""
        # Boolean parsing
        if env_value.lower() in ("true", "1", "yes", "on"):
            return True
        elif env_value.lower() in ("false", "0", "no", "off"):
            return False

        # Integer parsing
        try:
            if env_value.isdigit() or (
                env_value.startswith("-") and env_value[1:].isdigit()
            ):
                return int(env_value)
        except ValueError:
            pass

        # Float parsing
        try:
            return float(env_value)
        except ValueError:
            pass

        # JSON parsing (for complex values)
        if env_value.startswith(("{", "[")):
            try:
                return json.loads(env_value)
            except json.JSONDecodeError:
                pass

        # Return as string
        return env_value

    def _get_from_file(self, key: str) -> Optional[Any]:
        """Get configuration value from configuration files"""
        config_files = [
            self.config_dir / "integrations.yaml",
            self.config_dir / "integration-config.yaml",
            self.config_dir / "config.yaml",
        ]

        for config_file in config_files:
            if config_file.exists():
                try:
                    with open(config_file, "r") as f:
                        if (
                            config_file.suffix == ".yaml"
                            or config_file.suffix == ".yml"
                        ):
                            config_data = yaml.safe_load(f)
                        else:
                            config_data = json.load(f)

                    # Try nested keys (e.g., integrations.tree_sitter.enabled)
                    value = self._get_nested_value(config_data, key)
                    if value is not None:
                        return value

                except Exception as e:
                    self.logger.warning(
                        f"Failed to load config from {config_file}: {e}"
                    )

        return None

    def _get_nested_value(self, data: Dict[str, Any], key: str) -> Any:
        """Get value from nested dictionary using dot notation"""
        keys = key.split(".")
        current = data

        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return None

        return current

    def _validate_value(self, key: str, value: Any) -> bool:
        """Validate configuration value"""
        if key not in self._config_sources:
            return True  # Allow custom configuration keys

        config_value = self._config_sources[key]

        # Check required values
        if config_value.required and value is None:
            return False

        # Apply validation rules
        for rule in config_value.validation_rules:
            if not self._apply_validation_rule(rule, value):
                return False

        return True

    def _apply_validation_rule(self, rule: str, value: Any) -> bool:
        """Apply a validation rule to a value"""
        try:
            if rule == "positive_integer":
                return isinstance(value, int) and value > 0
            elif rule.startswith("enum:"):
                enum_values = rule.split(":", 1)[1].split(",")
                return value in enum_values
            elif rule == "boolean":
                return isinstance(value, bool)
            elif rule == "string":
                return isinstance(value, str)
            elif rule == "positive_number":
                return isinstance(value, (int, float)) and value > 0
            else:
                # Custom validation rules can be added here
                return True
        except Exception:
            return False

    def get_integration_config(self, integration_name: str) -> Dict[str, Any]:
        """
        Get configuration for a specific integration

        Args:
            integration_name: Name of the integration

        Returns:
            Integration configuration dictionary
        """
        config = {}
        prefix = f"yask_{integration_name}"

        # Get all configuration keys that start with the integration prefix
        for key in self._config_sources.keys():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lstrip("_")
                config[config_key] = self.get(key)

        return config

    def is_integration_enabled(self, integration_name: str) -> bool:
        """
        Check if an integration is enabled

        Args:
            integration_name: Name of the integration

        Returns:
            True if integration is enabled
        """
        enable_key = f"yask_enable_{integration_name}"
        return self.get(enable_key, False)

    def get_performance_config(self) -> Dict[str, Any]:
        """Get performance-related configuration"""
        return {
            "cache_enabled": self.get("yask_integration_cache_enabled", True),
            "cache_ttl": self.get("yask_integration_cache_ttl", 300),
            "parallel_enabled": self.get("yask_integration_parallel_enabled", True),
            "max_concurrent": self.get("yask_integration_max_concurrent", 3),
            "timeout_default": self.get("yask_integration_timeout", 30),
        }

    def get_logging_config(self) -> Dict[str, Any]:
        """Get logging-related configuration"""
        return {
            "level": self.get("yask_integration_log_level", "INFO"),
            "log_to_file": self.get("yask_integration_log_to_file", False),
            "log_file_path": self.config_dir / "integration.log",
        }

    def validate_configuration(self) -> Dict[str, Any]:
        """
        Validate current configuration

        Returns:
            Validation results with errors and warnings
        """
        results = {"valid": True, "errors": [], "warnings": []}

        # Check required configurations
        for key, config_value in self._config_sources.items():
            if config_value.required:
                value = self.get(key)
                if value is None:
                    results["errors"].append(f"Required configuration missing: {key}")
                    results["valid"] = False

        # Check integration dependencies
        enabled_integrations = []
        for integration in ["tree_sitter", "code_health", "documentation", "mcp"]:
            if self.is_integration_enabled(integration):
                enabled_integrations.append(integration)

        # Check for conflicting configurations
        if "mcp" in enabled_integrations and not self.get("yask_mcp_servers"):
            results["warnings"].append(
                "MCP integration enabled but no servers configured"
            )

        return results

    def export_config(self, file_path: Path, include_defaults: bool = False):
        """
        Export current configuration to file

        Args:
            file_path: Path to export configuration
            include_defaults: Whether to include default values
        """
        config_data = {}

        for key, config_value in self._config_sources.items():
            value = self.get(key)

            # Skip default values if not requested
            if not include_defaults and value == config_value.value:
                continue

            config_data[key] = {
                "value": value,
                "source": config_value.source.value,
                "description": config_value.description,
            }

        with open(file_path, "w") as f:
            yaml.dump(config_data, f, default_flow_style=False, indent=2)

    def get_config_summary(self) -> Dict[str, Any]:
        """Get configuration summary"""
        enabled_integrations = []
        for integration in ["tree_sitter", "code_health", "documentation", "mcp"]:
            if self.is_integration_enabled(integration):
                enabled_integrations.append(integration)

        return {
            "enabled_integrations": enabled_integrations,
            "total_integrations": len(self._config_sources),
            "config_sources": {
                "environment": len(
                    [
                        v
                        for v in self._config_sources.values()
                        if v.source == ConfigSource.ENVIRONMENT
                    ]
                ),
                "file": len(
                    [
                        v
                        for v in self._config_sources.values()
                        if v.source == ConfigSource.FILE
                    ]
                ),
                "default": len(
                    [
                        v
                        for v in self._config_sources.values()
                        if v.source == ConfigSource.DEFAULT
                    ]
                ),
            },
            "performance_config": self.get_performance_config(),
            "validation_results": self.validate_configuration(),
        }


class EnvironmentConfig:
    """
    Environment-specific configuration manager

    Provides environment-aware configuration with automatic environment detection
    and environment-specific overrides.
    """

    def __init__(self, config: IntegrationConfig):
        self.config = config
        self.logger = logging.getLogger("yask.integration.environment")
        self.current_environment = self._detect_environment()

    def _detect_environment(self) -> str:
        """Detect current environment"""
        env = os.getenv("YASK_ENVIRONMENT", "").lower()

        if env:
            return env

        # Auto-detect based on environment variables and paths
        if os.getenv("CI") or os.getenv("GITHUB_ACTIONS"):
            return "ci"
        elif os.getenv("DEVBOX"):
            return "development"
        elif os.path.exists("/.dockerenv"):
            return "docker"
        elif os.getenv("VIRTUAL_ENV"):
            return "development"
        else:
            return "production"

    def get_environment_config(self) -> Dict[str, Any]:
        """Get environment-specific configuration"""
        env_configs = {
            "development": {
                "yask_integration_log_level": "DEBUG",
                "yask_integration_cache_enabled": False,
                "yask_integration_parallel_enabled": False,
                "yask_code_health_strictness": "basic",
            },
            "ci": {
                "yask_integration_log_level": "WARNING",
                "yask_integration_cache_enabled": True,
                "yask_integration_parallel_enabled": True,
                "yask_code_health_strictness": "strict",
            },
            "production": {
                "yask_integration_log_level": "ERROR",
                "yask_integration_cache_enabled": True,
                "yask_integration_parallel_enabled": True,
                "yask_code_health_strictness": "standard",
            },
            "docker": {
                "yask_integration_log_level": "INFO",
                "yask_integration_cache_enabled": True,
                "yask_integration_parallel_enabled": False,
                "yask_code_health_strictness": "standard",
            },
        }

        return env_configs.get(self.current_environment, {})

    def apply_environment_overrides(self):
        """Apply environment-specific configuration overrides"""
        env_config = self.get_environment_config()

        for key, value in env_config.items():
            # Only override if not explicitly set by user
            if os.getenv(key.upper()) is None:
                self.config.set(key, value, ConfigSource.COMPUTED)

    def get_environment_info(self) -> Dict[str, Any]:
        """Get current environment information"""
        return {
            "name": self.current_environment,
            "detection_method": "auto"
            if not os.getenv("YASK_ENVIRONMENT")
            else "explicit",
            "environment_variables": {
                key: os.getenv(key)
                for key in [
                    "YASK_ENVIRONMENT",
                    "CI",
                    "GITHUB_ACTIONS",
                    "DEVBOX",
                    "VIRTUAL_ENV",
                ]
                if os.getenv(key)
            },
        }


class ConfigManager:
    """
    Central configuration manager for YASK integrations

    Provides unified interface for configuration management with caching,
    validation, and environment awareness.
    """

    def __init__(self, config_dir: Optional[Path] = None):
        self.config = IntegrationConfig(config_dir)
        self.environment_config = EnvironmentConfig(self.config)
        self.logger = logging.getLogger("yask.integration.config_manager")

        # Apply environment overrides
        self.environment_config.apply_environment_overrides()

        # Validate configuration
        self._validate_on_startup()

    def _validate_on_startup(self):
        """Validate configuration on startup"""
        validation_results = self.config.validate_configuration()

        if validation_results["errors"]:
            self.logger.error(f"Configuration errors: {validation_results['errors']}")

        if validation_results["warnings"]:
            self.logger.warning(
                f"Configuration warnings: {validation_results['warnings']}"
            )

    def get_config(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)

    def set_config(self, key: str, value: Any):
        """Set configuration value"""
        self.config.set(key, value)

    def is_enabled(self, integration_name: str) -> bool:
        """Check if integration is enabled"""
        return self.config.is_integration_enabled(integration_name)

    def get_integration_config(self, integration_name: str) -> Dict[str, Any]:
        """Get integration-specific configuration"""
        return self.config.get_integration_config(integration_name)

    def get_performance_config(self) -> Dict[str, Any]:
        """Get performance configuration"""
        return self.config.get_performance_config()

    def get_logging_config(self) -> Dict[str, Any]:
        """Get logging configuration"""
        return self.config.get_logging_config()

    def get_environment_info(self) -> Dict[str, Any]:
        """Get environment information"""
        return self.environment_config.get_environment_info()

    def get_summary(self) -> Dict[str, Any]:
        """Get configuration summary"""
        return {
            "config_summary": self.config.get_config_summary(),
            "environment_info": self.get_environment_info(),
            "performance_config": self.get_performance_config(),
            "logging_config": self.get_logging_config(),
        }


# Global configuration manager instance
_config_manager: Optional[ConfigManager] = None


def get_config_manager() -> ConfigManager:
    """Get the global configuration manager instance"""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager


def get_config(key: str, default: Any = None) -> Any:
    """Get configuration value from global manager"""
    return get_config_manager().get_config(key, default)


def is_integration_enabled(integration_name: str) -> bool:
    """Check if integration is enabled"""
    return get_config_manager().is_enabled(integration_name)


def get_integration_config(integration_name: str) -> Dict[str, Any]:
    """Get integration configuration"""
    return get_config_manager().get_integration_config(integration_name)
