from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config

STANDARD_TEMPLATES = {
    "code_of_conduct": ("CODE_OF_CONDUCT.template.md", "code_of_conduct"),
    "contributing": ("CONTRIBUTING.template.md", "contributing"),
    "security": ("SECURITY.template.md", "security"),
    "support": ("SUPPORT.template.md", "support"),
}
STANDARD_STATES = {"default", "recommended", "optional"}


def find_standards_root(explicit: str | Path | None = None) -> Path:
    if explicit is not None:
        root = Path(explicit).expanduser().resolve()
        if not root.is_dir():
            raise FileNotFoundError(f"Standards root does not exist: {root}")
        return root

    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    for candidate in candidates:
        root = candidate / "standards"
        if root.is_dir():
            return root

    raise FileNotFoundError(
        "Could not locate RepoForge standards. Run from a RepoForge checkout "
        "or pass --standards-root."
    )


def load_standards_matrix(
    *, standards_root: str | Path | None = None
) -> dict[str, Any]:
    root = find_standards_root(standards_root)
    return load_config(root / "matrix.yml")


def standard_plan(
    project_type: str,
    profile: str,
    *,
    standards_root: str | Path | None = None,
) -> dict[str, str]:
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

    matrix = load_standards_matrix(standards_root=standards_root)
    plan = matrix["matrix"][project_type][profile]
    invalid = set(plan.values()) - STANDARD_STATES
    if invalid:
        raise ValueError(f"Invalid standards state(s): {', '.join(sorted(invalid))}")
    return dict(plan)


def render_community_standard(
    standard_name: str,
    config: dict[str, Any],
    *,
    standards_root: str | Path | None = None,
) -> str:
    if standard_name not in STANDARD_TEMPLATES:
        raise ValueError(
            f"Unsupported community standard: {standard_name}. "
            f"Supported: {', '.join(sorted(STANDARD_TEMPLATES))}"
        )

    root = find_standards_root(standards_root)
    community_root = root / "community"
    template_name, section_name = STANDARD_TEMPLATES[standard_name]
    template_path = community_root / template_name
    if not template_path.is_file():
        raise FileNotFoundError(f"Community standard template not found: {template_path}")

    section = config.get(section_name)
    if not isinstance(section, dict):
        raise ValueError(f"Config section must be a mapping: {section_name}")

    context = {
        "project_name": config["project_name"],
        "repository_url": config.get("repository_url"),
        **section,
    }

    environment = Environment(
        loader=FileSystemLoader(community_root),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = environment.get_template(template_name)
    rendered = template.render(**context)
    return rendered.rstrip() + "\n"
