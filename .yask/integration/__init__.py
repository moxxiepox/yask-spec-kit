# YASK Integration Framework
"""
YASK Integration and Extensibility Framework

This module provides optional integration capabilities and extensibility mechanisms
for the YASK spec-driven development system while maintaining core simplicity.

Key Features:
- Optional MCP (Model Context Protocol) tool integrations
- Graceful degradation when integrations are unavailable
- Environment-based configuration management
- Plugin architecture for extensibility
- Integration with subagent delegation system
"""

try:
    from .core import (
        IntegrationManager,
        IntegrationStatus,
        IntegrationError,
        BaseIntegration,
    )
except ImportError:
    # Fallback for direct module usage
    from core import (
        IntegrationManager,
        IntegrationStatus,
        IntegrationError,
        BaseIntegration,
    )

try:
    from .mcp import MCPIntegrationFramework, MCPClient, MCPServer
except ImportError:
    from mcp import MCPIntegrationFramework, MCPClient, MCPServer

try:
    from .tools import (
        TreeSitterIntegration,
        CodeHealthIntegration,
        DocumentationIntegration,
    )
except ImportError:
    from tools import (
        TreeSitterIntegration,
        CodeHealthIntegration,
        DocumentationIntegration,
    )

try:
    from .config import IntegrationConfig, EnvironmentConfig, ConfigManager
except ImportError:
    from config import IntegrationConfig, EnvironmentConfig, ConfigManager

try:
    from .plugins import PluginManager, PluginInterface, CustomIntegration
except ImportError:
    from plugins import PluginManager, PluginInterface, CustomIntegration

__version__ = "1.0.0"
__all__ = [
    "IntegrationManager",
    "IntegrationStatus",
    "IntegrationError",
    "BaseIntegration",
    "MCPIntegrationFramework",
    "MCPClient",
    "MCPServer",
    "TreeSitterIntegration",
    "CodeHealthIntegration",
    "DocumentationIntegration",
    "IntegrationConfig",
    "EnvironmentConfig",
    "ConfigManager",
    "PluginManager",
    "PluginInterface",
    "CustomIntegration",
]
