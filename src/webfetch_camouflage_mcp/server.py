"""MCP Server for web fetching with browser camouflage using curl_cffi."""

import textwrap

import curl_cffi
from fastmcp import FastMCP


def create_server() -> FastMCP:
    """Create and configure the FastMCP server."""
    mcp = FastMCP(
        name="WebFetch Camouflage",
        instructions=textwrap.dedent("""
            This MCP server provides web fetching capabilities with browser camouflage.
            Use the fetch_url tool to retrieve web content while impersonating various browsers.
            The default impersonate setting is 'chrome' for realistic browser fingerprints.
        """).strip(),
    )

    @mcp.tool
    def fetch_url(url: str, impersonate: curl_cffi.BrowserTypeLiteral | None = "chrome") -> str:
        """Fetch web content from a URL with browser camouflage.

        Args:
            url: The URL to fetch
            impersonate: Browser to impersonate (default: 'chrome').
                Supported values: chrome99, chrome100, chrome101, chrome104,
                chrome107, chrome110, chrome116, chrome119, chrome120,
                chrome123, chrome124, chrome131, chrome133a, chrome136,
                chrome99_android, chrome131_android, safari153, safari155,
                safari170, safari180, safari184, safari260, safari172_ios,
                safari180_ios, safari184_ios, safari260_ios, firefox133,
                firefox135, firefox135_android, tor145, edge99, edge101,
                edge133, edge135

        Returns:
            The fetched content as a string, or an error message if the request fails.

        """
        try:
            response = curl_cffi.get(url, impersonate=impersonate)
        except curl_cffi.CurlError as e:
            return f"Error fetching URL {url}: {e!s}"
        except Exception as e:  # noqa: BLE001
            return f"Error fetching URL {url}: {e!s}"
        else:
            return response.text

    return mcp


def main() -> None:
    """Run the MCP server."""
    server = create_server()
    server.run()


if __name__ == "__main__":
    main()
