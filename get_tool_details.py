"""Utility script to inspect tools exposed by the webfetch-camouflage-mcp server."""

import json
import subprocess
from typing import Any


def get_tool_details() -> list[dict[str, Any]]:
    """Get the list of tools from the webfetch-camouflage-mcp server.

    Returns:
        List of tool dictionaries with name and description.

    """
    proc = subprocess.Popen(
        ["uv", "run", "webfetch-camouflage-mcp"],  # noqa: S607
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdin = proc.stdin
    stdout = proc.stdout
    if stdin is None or stdout is None:
        proc.terminate()
        return []

    # Initialize
    init_msg = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "inspector", "version": "1.0"},
            },
        },
    )
    stdin.write(init_msg + "\n")
    stdin.flush()

    # Skip initialize response
    _ = stdout.readline()

    # Get tools
    tools_msg = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {},
        },
    )
    stdin.write(tools_msg + "\n")
    stdin.flush()

    # Parse and display
    tools_response = stdout.readline().strip()
    tools_data = json.loads(tools_response)
    tools = tools_data["result"]["tools"]

    proc.terminate()

    return tools


if __name__ == "__main__":
    tools = get_tool_details()
    for tool in tools:
        print(f"Tool: {tool['name']}")  # noqa: T201
        print(f"Description: {tool['description']}")  # noqa: T201
