from __future__ import annotations

from pathlib import Path

from repoforge.renderer import render_from_config

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"


def generate_scientific_python_previews() -> list[Path]:
    written: list[Path] = []
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "scientific-python" / profile
        rendered = render_from_config(
            "scientific-python",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )
        output = PREVIEWS / "scientific-python" / f"{profile}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        written.append(output)
    return written


def main() -> int:
    for path in generate_scientific_python_previews():
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
