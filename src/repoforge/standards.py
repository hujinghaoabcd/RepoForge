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

GITHUB_TEMPLATES = {
    "bug_report": ("ISSUE_TEMPLATE/bug_report.template.yml", "issue_forms"),
    "feature_request": ("ISSUE_TEMPLATE/feature_request.template.yml", "issue_forms"),
    "issue_config": ("ISSUE_TEMPLATE/config.template.yml", "issue_forms"),
    "pull_request_template": ("pull_request_template.template.md", "pull_request"),
}

METADATA_TEMPLATES = {
    "citation": ("CITATION.template.cff", "citation"),
    "changelog": ("CHANGELOG.template.md", "changelog"),
}

STANDARD_STATES = {"default", "recommended", "optional"}


def find_standards_root(explicit: str | Path | None = None) -> Path:
    if explicit is not None:
        root = Path(explicit).expanduser().resolve()
        if not root.is_dir():
            raise FileNotFoundError(f"Standards root does not exist: {root}")
        return root

    packaged_root = Path(__file__).resolve().parent / "_data" / "standards"
    if packaged_root.is_dir():
        return packaged_root

    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    for candidate in candidates:
        root = candidate / "standards"
        if root.is_dir():
            return root

    raise FileNotFoundError(
        "Could not locate RepoForge standards. Reinstall repoforge-standards "
        "or pass --standards-root."
    )


def _validate_project_type_and_profile(project_type: str, profile: str) -> None:
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


def _validate_plan(plan: dict[str, Any]) -> dict[str, str]:
    invalid = set(plan.values()) - STANDARD_STATES
    if invalid:
        raise ValueError(f"Invalid standards state(s): {', '.join(sorted(invalid))}")
    return dict(plan)


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
    _validate_project_type_and_profile(project_type, profile)
    matrix = load_standards_matrix(standards_root=standards_root)
    return _validate_plan(matrix["matrix"][project_type][profile])


def load_github_matrix(
    *, standards_root: str | Path | None = None
) -> dict[str, Any]:
    root = find_standards_root(standards_root)
    return load_config(root / "github" / "matrix.yml")


def github_plan(
    project_type: str,
    profile: str,
    *,
    standards_root: str | Path | None = None,
) -> dict[str, str]:
    _validate_project_type_and_profile(project_type, profile)
    matrix = load_github_matrix(standards_root=standards_root)
    return _validate_plan(matrix["matrix"][project_type][profile])


def load_metadata_matrix(
    *, standards_root: str | Path | None = None
) -> dict[str, Any]:
    root = find_standards_root(standards_root)
    return load_config(root / "metadata" / "matrix.yml")


def metadata_plan(
    project_type: str,
    profile: str,
    *,
    standards_root: str | Path | None = None,
) -> dict[str, str]:
    _validate_project_type_and_profile(project_type, profile)
    matrix = load_metadata_matrix(standards_root=standards_root)
    return _validate_plan(matrix["matrix"][project_type][profile])


def _render_standard_template(
    *,
    root: Path,
    template_name: str,
    context: dict[str, Any],
) -> str:
    template_path = root / template_name
    if not template_path.is_file():
        raise FileNotFoundError(f"Standard template not found: {template_path}")

    environment = Environment(
        loader=FileSystemLoader(root),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = environment.get_template(template_name)
    rendered = template.render(**context)
    return rendered.rstrip() + "\n"


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

    root = find_standards_root(standards_root) / "community"
    template_name, section_name = STANDARD_TEMPLATES[standard_name]
    section = config.get(section_name)
    if not isinstance(section, dict):
        raise ValueError(f"Config section must be a mapping: {section_name}")

    context = {
        "project_name": config["project_name"],
        "repository_url": config.get("repository_url"),
        **section,
    }
    return _render_standard_template(root=root, template_name=template_name, context=context)


def render_github_standard(
    standard_name: str,
    config: dict[str, Any],
    *,
    standards_root: str | Path | None = None,
) -> str:
    if standard_name not in GITHUB_TEMPLATES:
        raise ValueError(
            f"Unsupported GitHub standard: {standard_name}. "
            f"Supported: {', '.join(sorted(GITHUB_TEMPLATES))}"
        )

    root = find_standards_root(standards_root) / "github"
    template_name, section_name = GITHUB_TEMPLATES[standard_name]
    section = config.get(section_name)
    if not isinstance(section, dict):
        raise ValueError(f"Config section must be a mapping: {section_name}")

    context = {
        "project_name": config["project_name"],
        "repository_url": config["repository_url"],
        **section,
    }
    return _render_standard_template(root=root, template_name=template_name, context=context)


def render_metadata_standard(
    standard_name: str,
    config: dict[str, Any],
    *,
    standards_root: str | Path | None = None,
) -> str:
    if standard_name not in METADATA_TEMPLATES:
        raise ValueError(
            f"Unsupported metadata standard: {standard_name}. "
            f"Supported: {', '.join(sorted(METADATA_TEMPLATES))}"
        )

    root = find_standards_root(standards_root) / "metadata"
    template_name, section_name = METADATA_TEMPLATES[standard_name]
    section = config.get(section_name)
    if not isinstance(section, dict):
        raise ValueError(f"Config section must be a mapping: {section_name}")

    context = {
        "project_name": config["project_name"],
        "repository_url": config["repository_url"],
        **section,
    }
    return _render_standard_template(root=root, template_name=template_name, context=context)
