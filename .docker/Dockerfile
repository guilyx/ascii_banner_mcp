FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src/

RUN pip install --no-cache-dir -e .

# stdio by default (use with `docker run -i`); set MCP_TRANSPORT=streamable-http for HTTP
ENV MCP_TRANSPORT=stdio
EXPOSE 8000

CMD ["python", "-m", "ascii_banner_mcp.server"]
