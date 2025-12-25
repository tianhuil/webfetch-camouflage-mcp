"""MCP Server for web fetching with browser camouflage using curl_cffi."""

import textwrap

import curl_cffi
import html2text
from fastmcp import FastMCP


def create_server() -> FastMCP:
    """Create and configure the FastMCP server."""
    mcp = FastMCP(
        name="WebFetch Camouflage",
        instructions=textwrap.dedent("""
            This MCP server provides web fetching capabilities with browser camouflage.
            Use the fetch_url tool to retrieve web content while impersonating various browsers.
            Content is automatically converted from HTML to clean Markdown format.
            The default impersonate setting is 'realworld' for realistic browser fingerprints.
        """).strip(),
    )

    @mcp.tool
    def fetch_url(url: str, impersonate: str | None = "realworld") -> str:
        """Fetch web content from a URL with browser camouflage.

        Args:
            url: The URL to fetch
            impersonate: Browser to impersonate (default: 'realworld').
                Can be any string - curl_cffi will attempt to use the corresponding
                browser fingerprint. Common values include: chrome99, chrome100,
                chrome101, chrome104, chrome107, chrome110, chrome116, chrome119,
                chrome120, chrome123, chrome124, chrome131, chrome133a, chrome136,
                chrome99_android, chrome131_android, safari153, safari155,
                safari170, safari180, safari184, safari260, safari172_ios,
                safari180_ios, safari184_ios, safari260_ios, firefox133,
                firefox135, firefox135_android, tor145, edge99, edge101,
                edge133, edge135

        Returns:
            The fetched content converted to Markdown format, or an error message
            if the request fails.

        """
        try:
            response = curl_cffi.get(url, impersonate=impersonate)  # type: ignore[arg-type]
        except curl_cffi.CurlError as e:
            return f"Error fetching URL {url}: {e!s}"
        except Exception as e:  # noqa: BLE001
            return f"Error fetching URL {url}: {e!s}"
        else:
            # Convert HTML to Markdown
            h = html2text.HTML2Text()
            h.ignore_links = False  # Keep links as Markdown links
            h.ignore_images = False  # Keep images as Markdown images
            h.ignore_tables = False  # Convert tables to Markdown
            return h.handle(response.text)

    return mcp


def main() -> None:
    """Run the MCP server."""
    server = create_server()
    server.run()


if __name__ == "__main__":
    main()
