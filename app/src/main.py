import os
import logging

from fastmcp import FastMCP
from dotenv import load_dotenv

mcp = FastMCP("MCP Server", stateless_http=True)
load_dotenv()
env = os.getenv("ENV", "development")


@mcp.tool()
def execute_server() -> str:
    print("[tool] [execute_server] - Executing server tool.")
    return "Server is running"


@mcp.prompt()
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    print("[prompt] [summarize_request] - Generating summary prompt.")
    return f"Please summarize the following text demimited by <>:\n\n<{text}>"


@mcp.resource("config://app")
def get_config() -> dict:
    print("[resource] [config://app] - Fetching app configuration.")
    return {
        "environment": env,
        "debug": os.getenv("DEBUG", "False") == "True"
    }


if __name__ == "__main__":
    # mcp.run()
    mcp.run(transport="http", host="127.0.0.1", port=8000)