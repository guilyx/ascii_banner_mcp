# Config examples

Copy the example that matches your setup and adjust paths or URLs.

- **`mcp-config.example.json`** — MCP client config (Cursor, Claude Desktop, etc.) using stdio. Set `command` to your `python` (or full path to venv Python) and `args` to `["-m", "ascii_banner_mcp.server"]`.
- **`mcp-config-streamable-http.example.json`** — For streamable-http (e.g. Docker or MCP Inspector): server URL `http://localhost:8000/mcp`. Use when the server runs with `MCP_TRANSPORT=streamable-http`.
