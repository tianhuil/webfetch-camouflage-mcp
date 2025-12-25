# webfetch-camouflage-mcp

[![Tests](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

An MCP (Model Context Protocol) server for web fetching with browser camouflage using curl_cffi.

## Features

- Fetch web content with browser fingerprinting to avoid detection
- Support for various browser impersonation profiles
- Built with [curl_cffi](https://github.com/lexiforest/curl_cffi) for realistic TLS/HTTP2 fingerprints
- MCP protocol support for easy integration

## Quick Start

Run directly from GitHub using `uvx`:

```bash
uvx git+https://github.com/tianhuil/webfetch-camouflage-mcp.git
```

## Installation

### From Source (Development)

```bash
git clone https://github.com/tianhuil/webfetch-camouflage-mcp.git
cd webfetch-camouflage-mcp
uv sync
```

### Using uvx (One-off runs)

```bash
# Run directly from GitHub
uvx git+https://github.com/tianhuil/webfetch-camouflage-mcp.git
```

## Usage

### Running the MCP Server

```bash
# From source
uv run webfetch-camouflage-mcp

# Or using poe
poe run

# Or run the module directly
uv run python -m src.webfetch_camouflage_mcp
```

### MCP Tool Usage

The server provides a `fetch_url` tool that accepts:

- `url`: The URL to fetch (required)
- `impersonate`: Browser to impersonate (optional, defaults to "realworld")

Supported impersonation options:
- `chrome99`, `chrome100`, `chrome101`, `chrome104`, `chrome107`, `chrome110`, `chrome116`, `chrome119`, `chrome120`, `chrome123`, `chrome124`, `chrome131`, `chrome133a`, `chrome136`
- `firefox133`, `firefox135`
- `safari153`, `safari155`, `safari170`, `safari180`, `safari184`, `safari260`
- `edge99`, `edge101`, `edge133`, `edge135`

## Development

```bash
# Run tests
poe test

# Lint code
poe lint

# Format code
poe format

# Type check
poe typecheck

# Run security audit
uv run pip-audit
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
