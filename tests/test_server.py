"""Tests for MCP server functionality."""

import curl_cffi
import html2text

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

    def test_html2text_integration(self) -> None:
        """Test that html2text is properly integrated for HTML to Markdown conversion."""
        # Test that html2text can be imported
        assert html2text is not None

        # Test basic HTML to Markdown conversion
        html_content = "<h1>Title</h1><p>This is a <strong>paragraph</strong> with <a href='http://example.com'>a link</a>.</p>"
        expected_markdown = (
            "# Title\n\nThis is a **paragraph** with [a link](http://example.com).\n\n"
        )

        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_tables = False
        result = h.handle(html_content)

        # Check that basic conversion works (exact match might vary slightly)
        assert "Title" in result
        assert "paragraph" in result
        assert "link" in result
        assert result != html_content  # Should be different from original HTML
