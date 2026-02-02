"""MCP server for ASCII banner generation using pyfiglet."""

import os

from mcp.server.fastmcp import FastMCP
from pyfiglet import FigletFont, FontError, FontNotFound, figlet_format

mcp = FastMCP(
    "ASCII Banner",
    instructions="Generate ASCII art banners from any string using pyfiglet fonts.",
)


@mcp.tool()
def get_fonts() -> list[str]:
    """List all available pyfiglet font names.

    Returns a list of font identifiers that can be used with generate_banner.
    Use this to discover which fonts (e.g. 'slant', 'standard', 'block') are available.
    """
    return FigletFont.getFonts()


@mcp.tool()
def generate_banner(text: str, font: str = "standard") -> str:
    """Generate an ASCII art banner from the given string.

    Args:
        text: The string to render as ASCII art (e.g. "Hello", "MCP").
        font: Name of the pyfiglet font. Use get_fonts() to list available fonts.
              Default is "standard". Common options: "slant", "block", "bubble", "big".

    Returns:
        The ASCII art banner as a multi-line string.
    """
    try:
        return figlet_format(text, font=font)
    except FontNotFound as e:
        return f"Error: font '{font}' not found. Use get_fonts() to list available fonts.\n{e}"
    except FontError as e:
        return f"Error rendering with font '{font}': {e}"


def main() -> None:
    """Run the MCP server (stdio or streamable-http via MCP_TRANSPORT)."""
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    if transport not in ("stdio", "streamable-http"):
        transport = "stdio"
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
