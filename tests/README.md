# Tests

## Unit tests

Run automatically in CI via `uv run poe test` (or plain `pytest`).

| File | What it covers |
|------|----------------|
| `test_fetch.py` | Raw HTTP fetching — curl_cffi vs requests, browser impersonation, timeouts |
| `test_server.py` | MCP server construction, tool registration, HTML-to-markdown conversion |

## Integration tests

**Not run in CI.** Require the respective AI CLI to be installed locally.
Each test starts the MCP server from the local source tree and prompts the
model to call `fetch_url` on `https://example.com`, then asserts the response
contains content from that page.

| File | Tool required | Isolation mechanism |
|------|---------------|---------------------|
| `test_integration_claude.py` | `claude` (Claude Code) | `--mcp-config <tmpfile> --strict-mcp-config` — global config is ignored entirely |
| `test_integration_opencode.py` | `opencode` | `OPENCODE_CONFIG_CONTENT` env var — merged last, no files modified |

### Running integration tests

```bash
# Both integration tests
pytest -m integration

# One tool at a time
pytest tests/test_integration_claude.py -m integration
pytest tests/test_integration_opencode.py -m integration
```
