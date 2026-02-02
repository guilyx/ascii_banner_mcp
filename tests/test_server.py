"""Tests for the ASCII Banner MCP server tools."""


from ascii_banner_mcp.server import generate_banner, get_fonts


class TestGetFonts:
    """Tests for get_fonts tool."""

    def test_returns_list(self) -> None:
        fonts = get_fonts()
        assert isinstance(fonts, list)
        assert len(fonts) > 0

    def test_all_elements_are_strings(self) -> None:
        fonts = get_fonts()
        assert all(isinstance(f, str) for f in fonts)

    def test_contains_common_fonts(self) -> None:
        fonts = get_fonts()
        for name in ("standard", "slant", "block", "big"):
            assert name in fonts, f"Expected font '{name}' in {fonts[:10]}..."


class TestGenerateBanner:
    """Tests for generate_banner tool."""

    def test_generates_ascii_art(self) -> None:
        result = generate_banner("Hi", font="standard")
        assert isinstance(result, str)
        assert len(result) > 0
        assert "\n" in result
        # ASCII art uses block chars, not literal "Hi"
        assert result.strip()

    def test_default_font_is_standard(self) -> None:
        result = generate_banner("A")
        assert result
        assert "\n" in result

    def test_slant_font(self) -> None:
        result = generate_banner("Hello", font="slant")
        assert isinstance(result, str)
        assert len(result) > 10
        assert "\n" in result

    def test_unknown_font_returns_error_message(self) -> None:
        result = generate_banner("x", font="nonexistent_font_xyz")
        assert "Error" in result
        assert "nonexistent_font_xyz" in result
        assert "get_fonts" in result
