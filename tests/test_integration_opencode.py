"""Integration tests for Opencode MCP tool integration.

These tests require the `opencode` CLI to be installed locally and are excluded
from CI. Run them explicitly with: pytest -m integration
"""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent


def _find_opencode() -> str | None:
    """Return the absolute path to the opencode binary, or None if not found."""
    found = shutil.which("opencode")
    if found:
        return found
    fallback = Path.home() / ".opencode" / "bin" / "opencode"
    return str(fallback) if fallback.is_file() else None


@pytest.mark.integration
class TestOpencodeIntegration:
    """Integration tests verifying Opencode can call webfetch-camouflage-mcp."""

    def test_fetch_url_tool_called(self) -> None:
        """Test that Opencode invokes fetch_url and returns content from the target URL."""
        opencode = _find_opencode()
        if opencode is None:
            pytest.skip("opencode binary not found")

        mcp_config: dict[str, object] = {
            "mcp": {
                "webfetch-camouflage": {
                    "type": "local",
                    "command": [
                        "uv",
                        "run",
                        "--directory",
                        str(PROJECT_ROOT),
                        "webfetch-camouflage-mcp",
                    ],
                },
            },
        }

        env = os.environ.copy()
        env["OPENCODE_CONFIG_CONTENT"] = json.dumps(mcp_config)

        result = subprocess.run(  # noqa: S603
            [
                opencode,
                "run",
                (
                    "Fetch https://example.com impersonating Chrome and report page title"
                ),
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
            env=env,
        )

        assert result.returncode == 0, (
            f"opencode exited with code {result.returncode}. stderr: {result.stderr[:500]}"
        )

        # Assert that the tool was called
        assert '"tool":"webfetch-camouflage_fetch_url"' in result.stdout.replace(" ", "")
        # Assert that the tool returned content
        assert 'This domain is for use in documentation examples' in result.stdout
        # Assert that the tool impersonated Chrome
        assert "chrome" in result.stdout.lower()


if __name__ == '__main__':
    TestOpencodeIntegration().test_fetch_url_tool_called()