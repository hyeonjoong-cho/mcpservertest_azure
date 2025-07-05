from mcp.server.fastmcp import FastMCP

mcp = FastMCP("example_server")

@mcp.tool()
def greeting(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="streamable-http")