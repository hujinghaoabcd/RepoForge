from pathlib import Path

from repoforge.cli import main

ROOT = Path(__file__).resolve().parents[1]


def test_render_cli_writes_markdown(tmp_path):
    output = tmp_path / "README.md"
    config = ROOT / "templates/scientific-python/minimal/config.example.yml"

    exit_code = main(
        [
            "render",
            "scientific-python",
            "minimal",
            "--config",
            str(config),
            "--template-root",
            str(ROOT / "templates"),
            "--output",
            str(output),
        ]
    )

    assert exit_code == 0
    text = output.read_text(encoding="utf-8")
    header = text.split("\n## ", 1)[0]
    assert text.startswith('<div align="center">')
    assert "# SpatialTools" in header
    assert "img.shields.io" in header
    assert "## Quick Start" in text
