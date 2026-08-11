from __future__ import annotations

from pathlib import Path

from repoforge.renderer import (
    SUPPORTED_PROFILES,
    SUPPORTED_TYPES,
    load_config,
    render_readme,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"
BRANDING = ROOT / "tests" / "branding.yml"


def generate_previews() -> list[Path]:
    written: list[Path] = []
    branding = load_config(BRANDING)

    for project_type in sorted(SUPPORTED_TYPES):
        for profile in ("minimal", "standard", "full"):
            if profile not in SUPPORTED_PROFILES:
                continue

            profile_dir = TEMPLATES / project_type / profile
            config_path = profile_dir / "config.example.yml"
            template = profile_dir / "README.template.md"
            if not config_path.is_file() or not template.is_file():
                continue

            config = load_config(config_path)
            config.update(branding)
            rendered = render_readme(
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
