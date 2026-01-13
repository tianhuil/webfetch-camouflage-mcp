import json
import subprocess


def get_tool_details():
    proc = subprocess.Popen(
        ["uv", "run", "webfetch-camouflage-mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

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
    proc.stdin.write(init_msg + "\n")
    proc.stdin.flush()

    # Skip initialize response
    _ = proc.stdout.readline()

    # Get tools
    tools_msg = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {},
        },
    )
    proc.stdin.write(tools_msg + "\n")
    proc.stdin.flush()

    # Parse and display
    tools_response = proc.stdout.readline().strip()
    tools_data = json.loads(tools_response)

    for tool in tools_data["result"]["tools"]:
        print(f"Tool: {tool['name']}")
        print(f"Description: {tool['description']}")

    proc.terminate()


if __name__ == "__main__":
    get_tool_details()
