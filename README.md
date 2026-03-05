# webfetch-camouflage-mcp

[![Tests](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Give your AI coding assistant reliable access to web pages that block standard HTTP clients.

Webfetch Camouflage is an MCP server for fetching web content with browser camouflage using [curl_cffi](https://github.com/lexiforest/curl_cffi). It mimics real browser TLS/HTTP2 fingerprints to bypass bot detection, returning clean Markdown output converted from HTML.

## Installation

<details>
<summary>Cursor</summary>

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "webfetch-camouflage": {
      "command": "uvx",
      "args": ["git+https://github.com/tianhuil/webfetch-camouflage-mcp.git"]
    }
  }
}
```

</details>

<details>
<summary>Claude Code</summary>

```bash
claude mcp add-json webfetch-camouflage '{"command":"uvx","args":["git+https://github.com/tianhuil/webfetch-camouflage-mcp.git"]}'
```

</details>

<details>
<summary>VSCode</summary>

```bash
code --add-mcp '{"name":"webfetch-camouflage","command":"uvx","args":["git+https://github.com/tianhuil/webfetch-camouflage-mcp.git"]}'
```

</details>

<details>
<summary>Gemini CLI</summary>

```bash
gemini mcp add webfetch-camouflage uvx -- git+https://github.com/tianhuil/webfetch-camouflage-mcp.git
```

</details>

<details>
<summary>Codex CLI</summary>

```bash
codex mcp add webfetch-camouflage -- uvx git+https://github.com/tianhuil/webfetch-camouflage-mcp.git
```

</details>

<details>
<summary>Opencode</summary>

Add to `opencode.json`:

**macOS/Linux**: `~/.local/share/opencode/opencode.json`
**Windows**: `%LOCALAPPDATA%\opencode\opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "webfetch-camouflage": {
      "type": "local",
      "command": ["uvx", "git+https://github.com/tianhuil/webfetch-camouflage-mcp.git"],
      "enabled": true
    }
  }
}
```

</details>

## Tool reference

The `fetch_url` tool accepts:

- `url` (required): URL to fetch
- `impersonate` (optional, default `"chrome"`): browser profile to impersonate
- `timeout` (optional, default `10`): request timeout in seconds
- `max_chars` (optional): maximum characters to return; truncates with `...` if set

Supported impersonation profiles:

- **Chrome**: `chrome99`, `chrome100`, `chrome101`, `chrome104`, `chrome107`, `chrome110`, `chrome116`, `chrome119`, `chrome120`, `chrome123`, `chrome124`, `chrome131`, `chrome133a`, `chrome136`
- **Firefox**: `firefox133`, `firefox135`
- **Safari**: `safari153`, `safari155`, `safari170`, `safari180`, `safari184`, `safari260`
- **Edge**: `edge99`, `edge101`, `edge133`, `edge135`


## Notes on Development

### Setup

```bash
git clone https://github.com/tianhuil/webfetch-camouflage-mcp.git
cd webfetch-camouflage-mcp
uv sync
```

### Running the server

```bash
uv run webfetch-camouflage-mcp
```

### Available tasks

```bash
poe test       # Run tests
poe lint       # Lint code
poe format     # Format code
poe typecheck  # Type check
uv run pip-audit  # Security audit
```

### MCP server testing

Test the server directly via JSON-RPC:

```bash
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}}' | uv run webfetch-camouflage-mcp

echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}}' | uvx git+https://github.com/tianhuil/webfetch-camouflage-mcp.git
```

Or use the helper script:

```bash
uv run python get_tool_details.py
```
