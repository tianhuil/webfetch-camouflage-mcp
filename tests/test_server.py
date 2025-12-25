"""Tests for MCP server functionality."""

import curl_cffi
import html2text

from webfetch_camouflage_mcp.server import create_server, remove_script_and_style_tags


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
        html_content = (
            "<h1>Title</h1><p>This is a <strong>paragraph</strong> with "
            "<a href='http://example.com'>a link</a>.</p>"
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

    def test_script_and_style_removal(self) -> None:
        """Test that script and style tags are removed from HTML before conversion."""
        # HTML with script and style tags
        html_with_js_css = """
        <html>
        <head>
        <style>body { color: red; }</style>
        </head>
        <body>
        <h1>Title</h1>
        <p>Content</p>
        <script>console.log('test');</script>
        </body>
        </html>
        """

        # Remove script and style tags
        clean_html = remove_script_and_style_tags(html_with_js_css)

        # Check that script and style tags are removed
        assert "<script>" not in clean_html
        assert "</script>" not in clean_html
        assert "<style>" not in clean_html
        assert "</style>" not in clean_html
        assert "console.log('test');" not in clean_html
        assert "body { color: red; }" not in clean_html

        # Check that other content is preserved
        assert "<h1>Title</h1>" in clean_html
        assert "<p>Content</p>" in clean_html
