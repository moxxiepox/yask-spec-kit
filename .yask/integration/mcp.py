"""
YASK MCP Integration Framework

This module provides Model Context Protocol (MCP) integration capabilities
for YASK while maintaining core simplicity and graceful degradation.
"""

import os
import json
import asyncio
import logging
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
from dataclasses import dataclass
from enum import Enum

from .core import BaseIntegration, IntegrationResult, IntegrationStatus


class MCPConnectionStatus(Enum):
    """MCP connection status enumeration"""

    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"


@dataclass
class MCPMessage:
    """MCP message structure"""

    method: str
    params: Optional[Dict[str, Any]] = None
    id: Optional[str] = None


@dataclass
class MCPResponse:
    """MCP response structure"""

    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    id: Optional[str] = None


class MCPClient:
    """
    MCP Client for connecting to MCP servers

    Provides standardized connectivity to external systems, data sources,
    and tools through the Model Context Protocol.
    """

    def __init__(self, server_name: str, server_path: Optional[Path] = None):
        self.server_name = server_name
        self.server_path = server_path
        self.status = MCPConnectionStatus.DISCONNECTED
        self.logger = logging.getLogger(f"yask.mcp.client.{server_name}")
        self._process = None
        self._message_id = 0

    async def connect(self) -> bool:
        """
        Connect to MCP server

        Returns:
            True if connection successful, False otherwise
        """
        if self.status == MCPConnectionStatus.CONNECTED:
            return True

        self.status = MCPConnectionStatus.CONNECTING
        self.logger.info(f"Connecting to MCP server: {self.server_name}")

        try:
            # Check if server executable exists
            if self.server_path and not self.server_path.exists():
                self.logger.error(f"MCP server not found: {self.server_path}")
                self.status = MCPConnectionStatus.ERROR
                return False

            # Start MCP server process (placeholder implementation)
            # In a real implementation, this would start the actual MCP server
            self._process = await self._start_server_process()

            if self._process:
                self.status = MCPConnectionStatus.CONNECTED
                self.logger.info(f"Connected to MCP server: {self.server_name}")
                return True
            else:
                self.status = MCPConnectionStatus.ERROR
                return False

        except Exception as e:
            self.logger.error(
                f"Failed to connect to MCP server {self.server_name}: {e}"
            )
            self.status = MCPConnectionStatus.ERROR
            return False

    async def disconnect(self):
        """Disconnect from MCP server"""
        if self._process:
            try:
                self._process.terminate()
                await self._process.wait()
            except Exception as e:
                self.logger.error(f"Error disconnecting from {self.server_name}: {e}")

        self.status = MCPConnectionStatus.DISCONNECTED
        self.logger.info(f"Disconnected from MCP server: {self.server_name}")

    async def send_request(
        self, method: str, params: Optional[Dict[str, Any]] = None
    ) -> Optional[MCPResponse]:
        """
        Send request to MCP server

        Args:
            method: MCP method name
            params: Request parameters

        Returns:
            MCPResponse or None if request failed
        """
        if self.status != MCPConnectionStatus.CONNECTED:
            self.logger.warning(
                f"Cannot send request: not connected to {self.server_name}"
            )
            return None

        try:
            message = MCPMessage(method=method, params=params, id=str(self._message_id))
            self._message_id += 1

            # Send message (placeholder implementation)
            response = await self._send_message(message)
            return response

        except Exception as e:
            self.logger.error(f"Failed to send request to {self.server_name}: {e}")
            return None

    async def _start_server_process(self):
        """Start MCP server process (placeholder)"""
        # In a real implementation, this would start the actual MCP server
        # For now, return a mock process
        return None

    async def _send_message(self, message: MCPMessage) -> MCPResponse:
        """Send message to MCP server (placeholder)"""
        # In a real implementation, this would send the actual message
        # For now, return a mock response
        return MCPResponse(result={"status": "mock_response"}, id=message.id)

    def get_status(self) -> Dict[str, Any]:
        """Get client status"""
        return {
            "server_name": self.server_name,
            "server_path": str(self.server_path) if self.server_path else None,
            "status": self.status.value,
            "connected": self.status == MCPConnectionStatus.CONNECTED,
        }


class MCPServer:
    """
    MCP Server wrapper for YASK integration

    Manages MCP server connections and provides unified interface
    for YASK integration capabilities.
    """

    def __init__(self, name: str, server_path: Optional[Path] = None):
        self.name = name
        self.server_path = server_path
        self.client = MCPClient(name, server_path)
        self.logger = logging.getLogger(f"yask.mcp.server.{name}")
        self._capabilities: List[str] = []

    async def initialize(self) -> bool:
        """Initialize MCP server connection"""
        success = await self.client.connect()
        if success:
            # Discover server capabilities
            await self._discover_capabilities()
        return success

    async def _discover_capabilities(self):
        """Discover server capabilities"""
        try:
            response = await self.client.send_request("initialize")
            if response and response.result:
                capabilities = response.result.get("capabilities", [])
                self._capabilities = capabilities
                self.logger.info(
                    f"Discovered capabilities for {self.name}: {capabilities}"
                )
        except Exception as e:
            self.logger.error(f"Failed to discover capabilities for {self.name}: {e}")

    async def call_tool(
        self, tool_name: str, arguments: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Call a tool on the MCP server

        Args:
            tool_name: Name of the tool to call
            arguments: Tool arguments

        Returns:
            Tool result or None if call failed
        """
        if not self.client.connected:
            self.logger.warning(
                f"Cannot call tool {tool_name}: not connected to {self.name}"
            )
            return None

        try:
            response = await self.client.send_request(
                "tools/call", {"name": tool_name, "arguments": arguments or {}}
            )

            if response and response.result:
                return response.result
            else:
                self.logger.error(f"Tool call failed: {tool_name}")
                return None

        except Exception as e:
            self.logger.error(f"Failed to call tool {tool_name} on {self.name}: {e}")
            return None

    async def get_resources(
        self, uri: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Get resources from MCP server

        Args:
            uri: Optional resource URI filter

        Returns:
            List of resources or None if request failed
        """
        if not self.client.connected:
            self.logger.warning(f"Cannot get resources: not connected to {self.name}")
            return None

        try:
            params = {"uri": uri} if uri else {}
            response = await self.client.send_request("resources/list", params)

            if response and response.result:
                return response.result.get("resources", [])
            else:
                return []

        except Exception as e:
            self.logger.error(f"Failed to get resources from {self.name}: {e}")
            return None

    def get_status(self) -> Dict[str, Any]:
        """Get server status"""
        return {
            "name": self.name,
            "server_path": str(self.server_path) if self.server_path else None,
            "client_status": self.client.get_status(),
            "capabilities": self._capabilities,
            "connected": self.client.connected,
        }


class MCPIntegrationFramework(BaseIntegration):
    """
    MCP Integration Framework for YASK

    Provides optional MCP tool integrations that enhance capabilities
    without affecting core workflow.
    """

    def __init__(self, enabled: bool = False):
        super().__init__("mcp_framework", enabled)
        self.servers: Dict[str, MCPServer] = {}
        self.logger = logging.getLogger("yask.mcp.framework")
        self._default_servers = ["filesystem", "git", "github", "notion", "database"]

        # Add capabilities
        self.add_capability("external_tools")
        self.add_capability("data_sources")
        self.add_capability("api_integration")
        self.add_capability("resource_access")

    def _initialize(self) -> Optional[Dict[str, Any]]:
        """Initialize MCP framework"""
        try:
            # Load configuration
            config = self._load_mcp_config()

            # Initialize configured servers
            initialized_servers = []
            for server_config in config.get("servers", []):
                server_name = server_config.get("name")
                server_path = server_config.get("path")

                if server_name:
                    server = MCPServer(
                        server_name, Path(server_path) if server_path else None
                    )
                    self.servers[server_name] = server
                    initialized_servers.append(server_name)

            # If no servers configured, add default ones
            if not initialized_servers:
                for server_name in self._default_servers:
                    self.servers[server_name] = MCPServer(server_name)
                    initialized_servers.append(server_name)

            return {
                "initialized_servers": initialized_servers,
                "total_servers": len(self.servers),
            }

        except Exception as e:
            self.logger.error(f"Failed to initialize MCP framework: {e}")
            return None

    def _load_mcp_config(self) -> Dict[str, Any]:
        """Load MCP configuration from environment and files"""
        config = {"servers": []}

        # Load from environment variables
        mcp_servers_env = os.getenv("YASK_MCP_SERVERS")
        if mcp_servers_env:
            try:
                servers_list = mcp_servers_env.split(",")
                for server_name in servers_list:
                    server_name = server_name.strip()
                    if server_name:
                        config["servers"].append({"name": server_name})
            except Exception as e:
                self.logger.warning(f"Failed to parse YASK_MCP_SERVERS: {e}")

        # Load from configuration file
        config_file = Path(".yask/mcp-config.yaml")
        if config_file.exists():
            try:
                import yaml

                with open(config_file, "r") as f:
                    file_config = yaml.safe_load(f)
                    if "mcp_servers" in file_config:
                        for server_name, server_config in file_config[
                            "mcp_servers"
                        ].items():
                            if server_config.get("enabled", False):
                                config["servers"].append(
                                    {
                                        "name": server_name,
                                        "path": server_config.get("path"),
                                    }
                                )
            except ImportError:
                self.logger.warning("PyYAML not available, skipping MCP config file")
            except Exception as e:
                self.logger.warning(f"Failed to load MCP config file: {e}")

        return config

    async def _initialize_servers(self) -> Dict[str, bool]:
        """Initialize all MCP servers"""
        results = {}

        for server_name, server in self.servers.items():
            try:
                success = await server.initialize()
                results[server_name] = success

                if success:
                    self.logger.info(
                        f"Successfully initialized MCP server: {server_name}"
                    )
                else:
                    self.logger.warning(
                        f"Failed to initialize MCP server: {server_name}"
                    )

            except Exception as e:
                self.logger.error(f"Error initializing MCP server {server_name}: {e}")
                results[server_name] = False

        return results

    def _enhance(self, core_result: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance core result with MCP capabilities"""
        enhancement = {
            "mcp_servers": {},
            "available_tools": {},
            "resource_access": {},
            "enhancement_applied": False,
        }

        # Get server statuses
        for server_name, server in self.servers.items():
            enhancement["mcp_servers"][server_name] = server.get_status()

        # Collect available tools from connected servers
        for server_name, server in self.servers.items():
            if server.client.connected:
                tools = []
                for capability in server._capabilities:
                    if "tool" in capability.lower():
                        tools.append(capability)
                enhancement["available_tools"][server_name] = tools

        enhancement["enhancement_applied"] = True
        return enhancement

    async def call_mcp_tool(
        self,
        server_name: str,
        tool_name: str,
        arguments: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Call a tool on a specific MCP server

        Args:
            server_name: Name of the MCP server
            tool_name: Name of the tool to call
            arguments: Tool arguments

        Returns:
            Tool result or None if call failed
        """
        if server_name not in self.servers:
            self.logger.error(f"MCP server not found: {server_name}")
            return None

        server = self.servers[server_name]
        return await server.call_tool(tool_name, arguments)

    async def get_mcp_resources(
        self, server_name: str, uri: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Get resources from a specific MCP server

        Args:
            server_name: Name of the MCP server
            uri: Optional resource URI filter

        Returns:
            List of resources or None if request failed
        """
        if server_name not in self.servers:
            self.logger.error(f"MCP server not found: {server_name}")
            return None

        server = self.servers[server_name]
        return await server.get_resources(uri)

    def get_connected_servers(self) -> List[str]:
        """Get list of connected MCP servers"""
        return [
            name for name, server in self.servers.items() if server.client.connected
        ]

    def get_available_tools(self) -> Dict[str, List[str]]:
        """Get all available tools from connected servers"""
        tools = {}
        for server_name, server in self.servers.items():
            if server.client.connected:
                server_tools = []
                for capability in server._capabilities:
                    if "tool" in capability.lower():
                        server_tools.append(capability)
                if server_tools:
                    tools[server_name] = server_tools
        return tools


# Convenience functions
def create_mcp_integration(enabled: bool = False) -> MCPIntegrationFramework:
    """Create MCP integration instance"""
    return MCPIntegrationFramework(enabled=enabled)


async def call_mcp_tool_safe(
    server_name: str, tool_name: str, arguments: Optional[Dict[str, Any]] = None
) -> Optional[Dict[str, Any]]:
    """
    Safely call MCP tool with error handling

    Args:
        server_name: Name of the MCP server
        tool_name: Name of the tool to call
        arguments: Tool arguments

    Returns:
        Tool result or None if call failed
    """
    try:
        from . import get_integration_manager

        manager = get_integration_manager()
        mcp_integration = manager.get_integration("mcp_framework")

        if mcp_integration and mcp_integration.enabled:
            return await mcp_integration.call_mcp_tool(
                server_name, tool_name, arguments
            )
        else:
            return None
    except Exception as e:
        logging.getLogger("yask.mcp.safe").error(f"Failed to call MCP tool: {e}")
        return None
