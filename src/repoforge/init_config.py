from __future__ import annotations

import re
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from .renderer import (
    SUPPORTED_PROFILES,
    SUPPORTED_TYPES,
    find_template_root,
    load_config,
)
from .standards import find_standards_root

COMMUNITY_SECTIONS = (
    "code_of_conduct",
    "contributing",
    "security",
    "support",
)
GITHUB_SECTIONS = ("issue_forms", "pull_request")
METADATA_SECTIONS = ("citation", "changelog")


class _ReadableDumper(yaml.SafeDumper):
    pass


def _represent_string(dumper: yaml.SafeDumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_ReadableDumper.add_representer(str, _represent_string)


def _slugify(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", value)
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-")
    return value.lower() or "project"


def _deep_fill(base: dict[str, Any], extra: dict[str, Any]) -> dict[str, Any]:
    """Fill missing nested keys without overwriting profile-specific values."""
    result = deepcopy(base)
    for key, value in extra.items():
        if key not in result:
            result[key] = deepcopy(value)
        elif isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_fill(result[key], value)
    return result


def _replace_project_identity(value: Any, old_name: str, new_name: str) -> Any:
    """Replace the example project's identity while preserving all other example prose."""
    if isinstance(value, dict):
        return {
            key: _replace_project_identity(item, old_name, new_name)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_replace_project_identity(item, old_name, new_name) for item in value]
    if not isinstance(value, str) or old_name == new_name:
        return value

    old_slug = _slugify(old_name)
    new_slug = _slugify(new_name)
    old_compact = old_slug.replace("-", "")
    new_compact = new_slug.replace("-", "")

    replacements = (
        (old_name, new_name),
        (old_name.lower(), new_name.lower()),
        (old_slug, new_slug),
        (old_compact, new_compact),
    )
    result = value
    for source, target in replacements:
        if source:
            result = result.replace(source, target)
    return result


def _selection_from_config(config: dict[str, Any]) -> tuple[str | None, str | None]:
    repoforge = config.get("repoforge")
    if not isinstance(repoforge, dict):
        return None, None
    project_type = repoforge.get("project_type")
    profile = repoforge.get("profile")
    return (
        project_type if isinstance(project_type, str) else None,
        profile if isinstance(profile, str) else None,
    )


def resolve_project_selection(
    config: dict[str, Any],
    project_type: str | None = None,
    profile: str | None = None,
) -> tuple[str, str]:
    configured_type, configured_profile = _selection_from_config(config)
    resolved_type = project_type or configured_type
    resolved_profile = profile or configured_profile

    if resolved_type not in SUPPORTED_TYPES:
        if resolved_type is None:
            raise ValueError(
                "Project type is required. Pass --type or initialize the config with repoforge init."
            )
        raise ValueError(f"Unsupported project type: {resolved_type}")
    if resolved_profile not in SUPPORTED_PROFILES:
        if resolved_profile is None:
            raise ValueError(
                "Profile is required. Pass --profile or initialize the config with repoforge init."
            )
        raise ValueError(f"Unsupported profile: {resolved_profile}")
    return resolved_type, resolved_profile


def build_init_config(
    project_type: str,
    profile: str,
    *,
    project_name: str,
    repository_url: str | None = None,
    template_root: str | Path | None = None,
    standards_root: str | Path | None = None,
) -> dict[str, Any]:
    if project_type not in SUPPORTED_TYPES:
        raise ValueError(f"Unsupported project type: {project_type}")
    if profile not in SUPPORTED_PROFILES:
        raise ValueError(f"Unsupported profile: {profile}")

    templates = find_template_root(template_root)
    standards = find_standards_root(standards_root)

    readme = load_config(
        templates / project_type / profile / "config.example.yml"
    )
    original_name = readme.get("project_name")
    if not isinstance(original_name, str) or not original_name:
        raise ValueError(
            f"README example config has no project_name: {project_type}/{profile}"
        )

    readme = _replace_project_identity(readme, original_name, project_name)
    readme["project_name"] = project_name

    community = load_config(standards / "community" / "config.example.yml")
    github = load_config(standards / "github" / "config.example.yml")
    metadata = load_config(standards / "metadata" / "config.example.yml")

    config: dict[str, Any] = {
        "repoforge": {
            "config_version": 1,
            "project_type": project_type,
            "profile": profile,
            "readme_management": "managed-sections",
        },
        **readme,
    }

    repo_url = repository_url or "https://github.com/OWNER/REPOSITORY"
    config["repository_url"] = repo_url

    for section_name in COMMUNITY_SECTIONS:
        section = community.get(section_name)
        if isinstance(section, dict):
            existing = config.get(section_name)
            config[section_name] = _deep_fill(
                existing if isinstance(existing, dict) else {}, section
            )

    for section_name in GITHUB_SECTIONS:
        section = github.get(section_name)
        if isinstance(section, dict):
            existing = config.get(section_name)
            config[section_name] = _deep_fill(
                existing if isinstance(existing, dict) else {}, section
            )

    for section_name in METADATA_SECTIONS:
        section = metadata.get(section_name)
        if isinstance(section, dict):
            existing = config.get(section_name)
            config[section_name] = _deep_fill(
                existing if isinstance(existing, dict) else {}, section
            )

    # Normalize the repository-linked defaults so the generated starter config
    # does not retain the example repository from standards/config.example.yml.
    contributing = config.get("contributing")
    if isinstance(contributing, dict):
        contributing["issue_url"] = f"{repo_url}/issues"

    support = config.get("support")
    if isinstance(support, dict):
        for channel in support.get("support_channels", []):
            if isinstance(channel, dict) and channel.get("name") == "Repository issues":
                channel["location"] = f"{repo_url}/issues"

    citation = config.get("citation")
    if isinstance(citation, dict):
        citation["repository_code"] = repo_url
        if citation.get("url") == "https://example.org/example-project":
            citation["url"] = repo_url

    return config


def dump_init_config(config: dict[str, Any]) -> str:
    body = yaml.dump(
        config,
        Dumper=_ReadableDumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    ).rstrip()
    header = (
        "# Generated by RepoForge.\n"
        "# Review project-specific prose, commands, URLs, contacts, authors, and badges before apply.\n"
        "# Project type is explicit; RepoForge does not auto-detect it.\n"
        "# New configs manage only stable README header sections; body prose remains user-owned.\n\n"
    )
    return header + body + "\n"


def init_repository_config(
    target: str | Path,
    project_type: str,
    profile: str,
    *,
    project_name: str | None = None,
    repository_url: str | None = None,
    output: str | Path = "repoforge.yml",
    force: bool = False,
    template_root: str | Path | None = None,
    standards_root: str | Path | None = None,
) -> Path:
    root = Path(target).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Target repository does not exist: {root}")

    destination = Path(output)
    if not destination.is_absolute():
        destination = root / destination
    destination = destination.expanduser().resolve()

    if destination.exists() and not force:
        raise FileExistsError(
            f"RepoForge config already exists: {destination}. Use --force to replace it."
        )

    name = project_name or root.name
    config = build_init_config(
        project_type,
        profile,
        project_name=name,
        repository_url=repository_url,
        template_root=template_root,
        standards_root=standards_root,
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(dump_init_config(config), encoding="utf-8")
    return destination
