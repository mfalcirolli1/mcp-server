# AI Coding Agent Instructions for MCP Server

## Project Overview
This is a **Model Context Protocol (MCP) Server** built with FastMCP—a stateless HTTP server that exposes tools, prompts, and resources to AI clients. The server runs on HTTP (not stdio) making it suitable for cloud/remote deployments.

**Key Architecture**: `app/src/main.py` is the single entry point. The server is intentionally minimal and stateless—all configuration comes from environment variables.

## Core Concepts & Patterns

### FastMCP Decorators
The project uses three decorator types (from `fastmcp` library):
- `@mcp.tool()` → exposes functions as callable tools to clients
- `@mcp.prompt()` → provides templated prompts (generate system/user messages)
- `@mcp.resource()` → exposes static/computed resources with URI-based access (e.g., `config://app`)

**Example from codebase**: The `get_config()` resource reads `ENV` and `DEBUG` env vars and exposes them as `config://app`.

### Environment-Driven Configuration
- Config is **read at server startup** from `.env` file (via `python-dotenv`)
- Current settings: `ENV=dev`, `DEBUG=True`
- Always check environment before hardcoding values
- Use `os.getenv("KEY", "default")` pattern—see `main.py` line 6-7

### HTTP Transport
- Server runs on `127.0.0.1:8000` (TCP localhost)
- Uses `transport="http"` parameter—critical for remote/cloud scenarios
- Stateless design: each request is independent (no global state)

## Development Workflow

### Setup
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Server
```bash
python app/src/main.py
# Server starts at http://127.0.0.1:8000
```

### Adding New Tools/Prompts/Resources
1. Add a function with appropriate decorator in `app/src/main.py`
2. Decorate with `@mcp.tool()`, `@mcp.prompt()`, or `@mcp.resource("scheme://path")`
3. Return value is automatically serialized to JSON by FastMCP
4. Example: To add a tool, follow the pattern of `execute_server()` (lines 12-13)

## Key Files & Responsibilities
- **[app/src/main.py](app/src/main.py)**: All server logic—tools, prompts, resources, and HTTP startup
- **[requirements.txt](requirements.txt)**: Dependencies (fastmcp, python-dotenv, requests, numpy)
- **[.env](.env)**: Environment variables (ENV, DEBUG flags)
- **[app/test/](app/test/)**: Test directory (currently empty—follow standard unittest or pytest structure)

## Critical Gotchas
- Do **not** introduce state/caching between requests—the `stateless_http=True` parameter enforces stateless design
- Avoid long-running operations without timeouts (MCP expects responsive servers)
- Resource URIs must follow scheme format: `scheme://identifier` (e.g., `config://app`, not `config/app`)
- Always test HTTP transport locally before deployment

## Testing & Debugging
- Debugging: Set `DEBUG=True` in `.env` and run `python app/src/main.py` directly to see logs
- Testing: Tests should go in `app/test/` (e.g., `test_tools.py`, `test_resources.py`)
- Client testing: Use MCP client libraries (e.g., SDK for your language) or curl to `http://127.0.0.1:8000`

## Deployment Considerations
- This is HTTP-based (not stdio), making it cloud-friendly
- Environment variables can be injected at runtime (no rebuild needed)
- Ensure port 8000 is accessible to MCP clients
