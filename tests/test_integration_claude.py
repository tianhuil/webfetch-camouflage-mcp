"""Integration tests for Claude Code MCP tool integration.

These tests require the `claude` CLI to be installed locally and are excluded
from CI. Run them explicitly with: pytest -m integration
"""

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent


def _find_claude() -> str | None:
    """Return the absolute path to the claude binary, or None if not found."""
    found = shutil.which("claude")
    if found:
        return found
    fallback = Path.home() / ".local" / "bin" / "claude"
    return str(fallback) if fallback.is_file() else None


@pytest.mark.integration
class TestClaudeIntegration:
    """Integration tests verifying Claude Code can call webfetch-camouflage-mcp."""

    def test_fetch_url_tool_called(self) -> None:
        """Test that Claude invokes fetch_url and returns content from the target URL."""
        claude = _find_claude()
        if claude is None:
            pytest.skip("claude binary not found")

        mcp_config: dict[str, object] = {
            "mcpServers": {
                "webfetch-camouflage": {
                    "command": "uv",
                    "args": [
                        "run",
                        "--directory",
                        str(PROJECT_ROOT),
                        "webfetch-camouflage-mcp",
                    ],
                },
            },
        }

        result = subprocess.run(  # noqa: S603
            [
                claude,
                "-p",
                (
                    "Fetch https://example.com impersonating Chrome and report page title"
                ),
                "--mcp-config",
                json.dumps(mcp_config),
                # Do not load global MCPs
                "--strict-mcp-config",
                "--allowedTools",
                "mcp__webfetch-camouflage__fetch_url",
                "--no-session-persistence",
                "--output-format",
                "json",
                '--model',
                'sonnet',
                '--verbose'
            ],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )

        assert result.returncode == 0, (
            f"claude exited with code {result.returncode}. stderr: {result.stderr[:500]}"
        )

        # Assert that the tool was called
        assert '"name":"mcp__webfetch-camouflage__fetch_url"' in result.stdout.replace(" ", "")
        # Assert that the tool returned content
        assert 'This domain is for use in documentation examples' in result.stdout
        # Assert that the tool impersonated Chrome
        assert "chrome" in result.stdout.lower()

if __name__ == '__main__':
    TestClaudeIntegration().test_fetch_url_tool_called()