# ASCII Banner MCP Server

A classical [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that generates ASCII art banners from any string using [pyfiglet](https://github.com/pwaller/pyfiglet).

## Features

- **`get_fonts`** — List all available pyfiglet font names (via `FigletFont.getFonts()`).
- **`generate_banner`** — Render a string as ASCII art with a chosen font (via `figlet_format(text, font=...)`).

## Requirements

- Python ≥ 3.10
- `mcp`, `pyfiglet`

## Installation

From the project root:

```bash
pip install -e .
```

For development (tests):

```bash
pip install -e ".[dev]"
```

## Usage

### Run the server (stdio)

MCP clients typically run the server as a subprocess and talk over stdio:

```bash
python -m ascii_banner_mcp.server
```

Or after install:

```bash
ascii-banner-mcp
```

### Config example

Copy and adjust one of the examples in [`config/`](config/):

- **stdio (local):** [`config/mcp-config.example.json`](config/mcp-config.example.json) — `command` + `args` for Cursor, Claude Desktop, etc.
- **streamable-http (e.g. Docker):** [`config/mcp-config-streamable-http.example.json`](config/mcp-config-streamable-http.example.json) — `url: "http://localhost:8000/mcp"` when the server runs over HTTP.

### Configure your MCP client

Add the server to your MCP client config (e.g. Cursor, Claude Desktop). Example (stdio):

```json
{
  "mcpServers": {
    "ascii-banner": {
      "command": "python",
      "args": ["-m", "ascii_banner_mcp.server"]
    }
  }
}
```

If you use a virtualenv, use the full path to that Python:

```json
{
  "mcpServers": {
    "ascii-banner": {
      "command": "/path/to/venv/bin/python",
      "args": ["-m", "ascii_banner_mcp.server"]
    }
  }
}
```

### Tools

| Tool             | Description |
|------------------|-------------|
| `get_fonts`      | Returns a list of available font names. Use this to discover fonts for `generate_banner`. |
| `generate_banner`| Renders `text` as ASCII art. Parameters: `text` (required), `font` (optional, default `"standard"`). Use fonts from `get_fonts()` (e.g. `"slant"`, `"block"`, `"big"`). |

Example (equivalent to your snippet):

```python
from pyfiglet import figlet_format
print(figlet_format("Hello", font="slant"))
```

Via this MCP server: call `generate_banner` with `text="Hello"` and `font="slant"`.

### MCP Inspector

Use [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) to test and debug the server.

**Option 1 — stdio (local process)**  
1. Run the Inspector: `npx @modelcontextprotocol/inspector`  
2. In the UI, add a server with **Stdio** transport.  
3. Set **Command** to `python` (or full path to your Python/venv).  
4. Set **Args** to `-m`, `ascii_banner_mcp.server`.  
5. Ensure the project is installed (`pip install -e .`) or set **cwd** to the project root and use `python -m ascii_banner_mcp.server`.

**Option 2 — streamable-http (Docker or local)**  
1. Start the server over HTTP:
   - **Docker:** `docker compose -f .docker/docker-compose.yml up --build` (see [Docker](#docker) below).  
   - **Local:** `MCP_TRANSPORT=streamable-http python -m ascii_banner_mcp.server` (serves at `http://127.0.0.1:8000/mcp`).  
2. Run the Inspector: `npx @modelcontextprotocol/inspector`  
3. Add a server with **Streamable HTTP** (or URL) and set the URL to `http://localhost:8000/mcp`.

**Custom ports (Inspector):**  
`CLIENT_PORT=8080 SERVER_PORT=9000 npx @modelcontextprotocol/inspector`

### Docker

Run the MCP server in a container. Use the [`.docker/`](.docker/) setup:

**stdio (default)** — client runs the container and talks via stdin/stdout:

```bash
docker build -f .docker/Dockerfile -t ascii-banner-mcp .
docker run -i --rm ascii-banner-mcp
```

**streamable-http (for Inspector or URL-based clients):**

```bash
docker compose -f .docker/docker-compose.yml up --build
```

Server is at `http://localhost:8000/mcp`. Use [`config/mcp-config-streamable-http.example.json`](config/mcp-config-streamable-http.example.json) or point MCP Inspector at that URL.

## Development

- **Tests:** `pytest`
- **Lint:** `ruff check src tests`
- **Format:** `black src tests`
- **Pre-commit:** Black, Ruff, and conventional-commit message checks (e.g. `feat:`, `fix:`). Install: `pip install -e ".[dev]"` then `pre-commit install` and `pre-commit install --hook-type commit-msg`. Run manually: `pre-commit run --all-files`.

## License

MIT
