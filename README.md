# webfetch-camouflage-mcp

[![Tests](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/tianhuil/webfetch-camouflage-mcp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<p style="font-size: 24px; font-weight: 600;">Give your AI coding assistant reliable access to web pages that block standard HTTP clients.</p>

<table style="border-collapse: collapse; width: 100%; margin: 20px 0;">
  <tr>
    <td style="width: 50%; padding: 15px; vertical-align: top;">
      <div style="overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; background: #fff; box-shadow: 0 0 60px -8px rgba(239, 68, 68, 0.45); transition: transform 0.2s;">
        <div style="position: relative; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #e2e8f0; background: #f8fafc; padding: 10px 16px;">
          <div style="position: absolute; left: 16px; display: flex; gap: 6px;">
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #ff5f57;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #febc2e;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #28c840;"></span>
          </div>
          <span style="font-size: 11px; color: #64748b;">Standard HTTP Client</span>
        </div>
        <div style="padding: 16px;">
          <div style="display: flex; flex-direction: column; gap: 12px; font-family: monospace; font-size: 12px;">
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #f1f5f9; color: #64748b;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              </div>
              <p style="color: #dc2626;">fetching example.com...</p>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #fef2f2; color: #dc2626;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>
              </div>
              <p style="color: #991b1b;">Error: 404 - Blocked by bot detection</p>
            </div>
          </div>
        </div>
      </div>
    </td>
    <td style="width: 50%; padding: 15px; vertical-align: top;">
      <div style="overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; background: #fff; box-shadow: 0 0 60px -8px rgba(34, 197, 94, 0.45); transition: transform 0.2s;">
        <div style="position: relative; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #e2e8f0; background: #f8fafc; padding: 10px 16px;">
          <div style="position: absolute; left: 16px; display: flex; gap: 6px;">
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #ff5f57;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #febc2e;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #28c840;"></span>
          </div>
          <span style="font-size: 11px; color: #64748b;">Webfetch Camouflage</span>
        </div>
        <div style="padding: 16px;">
          <div style="display: flex; flex-direction: column; gap: 12px; font-family: monospace; font-size: 12px;">
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #f1f5f9; color: #64748b;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              </div>
              <p style="color: #16a34a;">fetching example.com...</p>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #dcfce7; color: #16a34a;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>
              </div>
              <p style="color: #166534;">Success: 200 OK - Page fetched!</p>
            </div>
          </div>
        </div>
      </div>
    </td>
  </tr>
</table>

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
