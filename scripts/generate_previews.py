from __future__ import annotations

from pathlib import Path

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, render_from_config

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"


def generate_previews() -> list[Path]:
    written: list[Path] = []
    for project_type in sorted(SUPPORTED_TYPES):
        for profile in ("minimal", "standard", "full"):
            if profile not in SUPPORTED_PROFILES:
                continue
            profile_dir = TEMPLATES / project_type / profile
            config = profile_dir / "config.example.yml"
            template = profile_dir / "README.template.md"
            if not config.is_file() or not template.is_file():
                continue

            rendered = render_from_config(
                project_type,
                profile,
                config,
                template_root=TEMPLATES,
            )
            output = PREVIEWS / project_type / f"{profile}.md"
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered, encoding="utf-8")
            written.append(output)
    return written


def main() -> int:
    for path in generate_previews():
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
