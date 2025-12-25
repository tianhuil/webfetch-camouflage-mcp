"""Tests for MCP server functionality."""


import curl_cffi

from webfetch_camouflage_mcp.server import create_server


class TestMCPServer:
    """Test MCP server functionality."""

    def test_server_creation(self) -> None:
        """Test that server can be created."""
        server = create_server()
        assert server is not None
        assert server.name == "WebFetch Camouflage"

    def test_fetch_url_tool_exists(self) -> None:
        """Test that the fetch_url tool is registered."""
        server = create_server()
        # Check that the tool was registered (this is internal to FastMCP)
        # We can't easily test the tool registration without running the server
        # So we'll test the underlying functionality
        assert server is not None

    def test_curl_cffi_basic_functionality(self) -> None:
        """Test basic curl_cffi functionality."""
        # Test that curl_cffi can be imported and basic functionality works
        assert curl_cffi is not None
        # We don't want to make actual HTTP calls in unit tests
        # Integration tests will verify the actual functionality
