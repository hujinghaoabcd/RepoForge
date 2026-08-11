from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

SUPPORTED_TYPES = {"scientific-python", "research-algorithm", "research-experiment"}
SUPPORTED_PROFILES = {"minimal", "standard", "full"}


def find_template_root(explicit: str | Path | None = None) -> Path:
    if explicit is not None:
        root = Path(explicit).expanduser().resolve()
        if not root.is_dir():
            raise FileNotFoundError(f"Template root does not exist: {root}")
        return root

    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    for candidate in candidates:
        root = candidate / "templates"
        if root.is_dir():
            return root

    raise FileNotFoundError(
        "Could not locate RepoForge templates. Run from a RepoForge checkout "
        "or pass --template-root."
    )


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path).expanduser().resolve()
    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError("Config root must be a YAML mapping.")
    return data


def render_readme(
    project_type: str,
    profile: str,
    config: dict[str, Any],
    *,
    template_root: str | Path | None = None,
) -> str:
    if project_type not in SUPPORTED_TYPES:
        raise ValueError(
            f"Unsupported project type: {project_type}. "
            f"Supported: {', '.join(sorted(SUPPORTED_TYPES))}"
        )
    if profile not in SUPPORTED_PROFILES:
        raise ValueError(
            f"Unsupported profile: {profile}. "
            f"Supported: {', '.join(sorted(SUPPORTED_PROFILES))}"
        )

    root = find_template_root(template_root)
    profile_dir = root / project_type / profile
    template_path = profile_dir / "README.template.md"
    if not template_path.is_file():
        raise FileNotFoundError(f"README template not found: {template_path}")

    environment = Environment(
        loader=FileSystemLoader(profile_dir),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = environment.get_template("README.template.md")
    rendered = template.render(**config)
    return rendered.rstrip() + "\n"


def render_from_config(
    project_type: str,
    profile: str,
    config_path: str | Path,
    *,
    template_root: str | Path | None = None,
) -> str:
    return render_readme(
        project_type,
        profile,
        load_config(config_path),
        template_root=template_root,
    )
