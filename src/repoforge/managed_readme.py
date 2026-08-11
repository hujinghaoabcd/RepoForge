from __future__ import annotations

import re
from typing import Any

READ_ME_MODES = {"whole-file", "managed-sections"}
MANAGED_SECTION_NAMES = ("identity", "badges", "navigation")

_HEADER_PREFIX = '<div align="center">\n\n'
_HEADER_CLOSE = "</div>"
_SECTION_RE = re.compile(
    r"<!-- repoforge:start (?P<name>[a-z0-9-]+) -->\n"
    r"(?P<body>.*?)"
    r"<!-- repoforge:end (?P=name) -->",
    re.DOTALL,
)


def readme_management_mode(config: dict[str, Any]) -> str:
    repoforge = config.get("repoforge")
    if not isinstance(repoforge, dict):
        return "whole-file"
    mode = repoforge.get("readme_management", "whole-file")
    if mode not in READ_ME_MODES:
        raise ValueError(
            f"Unsupported README management mode: {mode}. "
            f"Supported: {', '.join(sorted(READ_ME_MODES))}"
        )
    return mode


def _managed_block(name: str, content: str) -> str:
    normalized = content.strip("\n")
    return (
        f"<!-- repoforge:start {name} -->\n"
        f"{normalized}\n"
        f"<!-- repoforge:end {name} -->"
    )


def _identity_content(config: dict[str, Any]) -> str:
    project_name = config.get("project_name")
    tagline = config.get("tagline")
    if not isinstance(project_name, str) or not project_name.strip():
        raise ValueError("Managed README identity requires project_name.")
    if not isinstance(tagline, str) or not tagline.strip():
        raise ValueError("Managed README identity requires tagline.")

    lines: list[str] = []
    logo_path = config.get("logo_path")
    if logo_path:
        width = config.get("logo_width", 160)
        lines.append(
            f'<img src="{logo_path}" alt="{project_name}" width="{width}">'
        )
        lines.append("")
    lines.extend([f"# {project_name}", "", f"**{tagline}**"])
    return "\n".join(lines)


def _badges_content(config: dict[str, Any]) -> str:
    badges = config.get("badges")
    if badges is None:
        return ""
    if isinstance(badges, str):
        return badges
    if isinstance(badges, list):
        rendered: list[str] = []
        for badge in badges:
            if not isinstance(badge, dict):
                raise ValueError("Managed README badge entries must be mappings.")
            image = badge.get("image")
            link = badge.get("link")
            alt = badge.get("alt")
            if not all(isinstance(value, str) and value for value in (image, link, alt)):
                raise ValueError(
                    "Managed README badge entries require non-empty alt, image, and link."
                )
            rendered.append(f'<a href="{link}"><img src="{image}" alt="{alt}"></a>')
        return " ".join(rendered)
    raise ValueError("Managed README badges must be a string, list, or null.")


def _navigation_content(config: dict[str, Any]) -> str:
    parts: list[str] = []
    language_switch = config.get("language_switch")
    if language_switch:
        if not isinstance(language_switch, str):
            raise ValueError("Managed README language_switch must be a string or null.")
        parts.append(language_switch)

    navigation = config.get("navigation")
    if isinstance(navigation, str) and navigation:
        parts.append(navigation)
    elif isinstance(navigation, list):
        rendered: list[str] = []
        for item in navigation:
            if not isinstance(item, dict):
                raise ValueError("Managed README navigation entries must be mappings.")
            label = item.get("label")
            link = item.get("link")
            if not all(isinstance(value, str) and value for value in (label, link)):
                raise ValueError(
                    "Managed README navigation entries require non-empty label and link."
                )
            rendered.append(f'<a href="{link}">{label}</a>')
        if rendered:
            parts.append(" · ".join(rendered))
    elif navigation is not None:
        raise ValueError("Managed README navigation must be a string, list, or null.")

    return "\n\n".join(parts)


def _split_centered_header(generated: str) -> tuple[str, str]:
    if not generated.startswith(_HEADER_PREFIX):
        raise ValueError("Managed README requires RepoForge's centered header contract.")
    close_index = generated.find(_HEADER_CLOSE)
    if close_index < 0:
        raise ValueError("Managed README centered header has no closing </div>.")
    tail_index = close_index + len(_HEADER_CLOSE)
    return generated[:tail_index], generated[tail_index:]


def build_managed_readme(generated: str, config: dict[str, Any]) -> str:
    """Convert a normal rendered README into a managed-header README.

    The body after the shared centered header remains ordinary Markdown and is not
    managed in v1.
    """
    _, tail = _split_centered_header(generated)
    blocks = [
        _managed_block("identity", _identity_content(config)),
        _managed_block("badges", _badges_content(config)),
        _managed_block("navigation", _navigation_content(config)),
    ]
    return _HEADER_PREFIX + "\n\n".join(blocks) + "\n" + _HEADER_CLOSE + tail


def _sections(text: str) -> dict[str, str]:
    matches = list(_SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for match in matches:
        name = match.group("name")
        if name in sections:
            raise ValueError(f"Duplicate RepoForge managed section: {name}")
        sections[name] = match.group(0)
    return sections


def _has_marker_syntax(text: str) -> bool:
    return "<!-- repoforge:start " in text or "<!-- repoforge:end " in text


def has_complete_managed_sections(text: str) -> bool:
    sections = _sections(text)
    if not sections:
        if _has_marker_syntax(text):
            raise ValueError("Malformed RepoForge managed section markers in README.md")
        return False
    expected = set(MANAGED_SECTION_NAMES)
    if set(sections) != expected:
        raise ValueError(
            "README.md has an incomplete RepoForge managed section set. "
            "Expected: " + ", ".join(MANAGED_SECTION_NAMES)
        )
    return True


def merge_managed_sections(existing: str, desired: str) -> str:
    """Replace desired managed regions while preserving all unmanaged text.

    If the existing README has no managed markers, the desired complete README is
    returned. Apply will still treat that as an overwrite and keep its normal
    safety barrier unless the caller explicitly forces the migration.
    """
    desired_sections = _sections(desired)
    expected = set(MANAGED_SECTION_NAMES)
    if set(desired_sections) != expected:
        raise ValueError(
            "Generated managed README does not contain the expected sections: "
            + ", ".join(MANAGED_SECTION_NAMES)
        )

    if not has_complete_managed_sections(existing):
        return desired

    existing_sections = _sections(existing)
    merged = existing
    for name in MANAGED_SECTION_NAMES:
        merged = merged.replace(existing_sections[name], desired_sections[name], 1)
    return merged
