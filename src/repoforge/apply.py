from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from .managed_readme import (
    build_managed_readme,
    has_complete_managed_sections,
    merge_managed_sections,
    readme_management_mode,
)
from .renderer import render_readme
from .standards import (
    github_plan,
    metadata_plan,
    render_community_standard,
    render_github_standard,
    render_metadata_standard,
    standard_plan,
)

StandardsPolicy = Literal["none", "default", "recommended"]
FileManagement = Literal["whole-file", "managed-sections"]

COMMUNITY_OUTPUTS = {
    "code_of_conduct": Path("CODE_OF_CONDUCT.md"),
    "contributing": Path("CONTRIBUTING.md"),
    "security": Path("SECURITY.md"),
    "support": Path("SUPPORT.md"),
}

METADATA_OUTPUTS = {
    "citation": Path("CITATION.cff"),
    "changelog": Path("CHANGELOG.md"),
}

GITHUB_ISSUE_OUTPUTS = {
    "bug_report": Path(".github/ISSUE_TEMPLATE/01-bug-report.yml"),
    "feature_request": Path(".github/ISSUE_TEMPLATE/02-feature-request.yml"),
    "issue_config": Path(".github/ISSUE_TEMPLATE/config.yml"),
}

PULL_REQUEST_OUTPUT = Path(".github/pull_request_template.md")

STANDARD_KEYS = {
    *COMMUNITY_OUTPUTS,
    "issue_forms",
    "pull_request_template",
    *METADATA_OUTPUTS,
}


@dataclass(frozen=True)
class PlannedFile:
    path: Path
    content: str
    source: str
    management: FileManagement = "whole-file"


@dataclass(frozen=True)
class ApplyResult:
    path: Path
    status: Literal["create", "overwrite", "unchanged"]
    source: str


def _selected(
    name: str,
    state: str,
    policy: StandardsPolicy,
    include: set[str],
    exclude: set[str],
) -> bool:
    if name in exclude:
        return False
    if name in include:
        return True
    if policy == "none":
        return False
    if policy == "default":
        return state == "default"
    if policy == "recommended":
        return state in {"default", "recommended"}
    raise ValueError(f"Unsupported standards policy: {policy}")


def _validate_overrides(include: set[str], exclude: set[str]) -> None:
    unknown = (include | exclude) - STANDARD_KEYS
    if unknown:
        raise ValueError(f"Unknown repository standard(s): {', '.join(sorted(unknown))}")
    overlap = include & exclude
    if overlap:
        raise ValueError(
            f"Repository standard cannot be both included and excluded: "
            f"{', '.join(sorted(overlap))}"
        )


def _readme_plan(
    project_type: str,
    profile: str,
    config: dict[str, Any],
    *,
    template_root: str | Path | None = None,
) -> PlannedFile:
    rendered = render_readme(
        project_type,
        profile,
        config,
        template_root=template_root,
    )
    management = readme_management_mode(config)
    if management == "managed-sections":
        rendered = build_managed_readme(rendered, config)
    return PlannedFile(
        path=Path("README.md"),
        content=rendered,
        source="readme",
        management=management,
    )


def build_apply_plan(
    project_type: str,
    profile: str,
    config: dict[str, Any],
    *,
    standards_policy: StandardsPolicy = "default",
    include: set[str] | None = None,
    exclude: set[str] | None = None,
    template_root: str | Path | None = None,
    standards_root: str | Path | None = None,
) -> list[PlannedFile]:
    include_set = set(include or ())
    exclude_set = set(exclude or ())
    _validate_overrides(include_set, exclude_set)

    files = [
        _readme_plan(
            project_type,
            profile,
            config,
            template_root=template_root,
        )
    ]

    community = standard_plan(project_type, profile, standards_root=standards_root)
    selected_community = {
        name
        for name, state in community.items()
        if _selected(name, state, standards_policy, include_set, exclude_set)
    }
    for name in COMMUNITY_OUTPUTS:
        if name not in selected_community:
            continue
        files.append(
            PlannedFile(
                path=COMMUNITY_OUTPUTS[name],
                content=render_community_standard(
                    name, config, standards_root=standards_root
                ),
                source=f"community:{name}",
            )
        )

    github = github_plan(project_type, profile, standards_root=standards_root)
    issue_forms_selected = _selected(
        "issue_forms",
        github["issue_forms"],
        standards_policy,
        include_set,
        exclude_set,
    )
    pull_request_selected = _selected(
        "pull_request_template",
        github["pull_request_template"],
        standards_policy,
        include_set,
        exclude_set,
    )

    if issue_forms_selected:
        github_config = deepcopy(config)
        issue_forms = github_config.get("issue_forms")
        if not isinstance(issue_forms, dict):
            raise ValueError("Config section must be a mapping: issue_forms")
        issue_forms["support_link_enabled"] = "support" in selected_community
        issue_forms["security_link_enabled"] = "security" in selected_community
        for name, output in GITHUB_ISSUE_OUTPUTS.items():
            files.append(
                PlannedFile(
                    path=output,
                    content=render_github_standard(
                        name, github_config, standards_root=standards_root
                    ),
                    source=f"github:{name}",
                )
            )

    if pull_request_selected:
        files.append(
            PlannedFile(
                path=PULL_REQUEST_OUTPUT,
                content=render_github_standard(
                    "pull_request_template",
                    config,
                    standards_root=standards_root,
                ),
                source="github:pull_request_template",
            )
        )

    metadata = metadata_plan(project_type, profile, standards_root=standards_root)
    for name in METADATA_OUTPUTS:
        state = metadata[name]
        if not _selected(name, state, standards_policy, include_set, exclude_set):
            continue
        files.append(
            PlannedFile(
                path=METADATA_OUTPUTS[name],
                content=render_metadata_standard(
                    name, config, standards_root=standards_root
                ),
                source=f"metadata:{name}",
            )
        )

    paths = [item.path for item in files]
    if len(paths) != len(set(paths)):
        raise RuntimeError("Apply plan contains duplicate output paths.")
    return files


def materialize_planned_content(destination: Path, item: PlannedFile) -> str:
    """Resolve the exact content that diff/apply/check should compare or write."""
    if item.management == "whole-file" or not destination.is_file():
        return item.content
    existing = destination.read_text(encoding="utf-8")
    return merge_managed_sections(existing, item.content)


def _managed_update_is_safe(destination: Path, item: PlannedFile) -> bool:
    if item.management != "managed-sections" or not destination.is_file():
        return False
    return has_complete_managed_sections(destination.read_text(encoding="utf-8"))


def inspect_apply_plan(
    target: str | Path,
    plan: list[PlannedFile],
) -> list[ApplyResult]:
    root = Path(target).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Target repository does not exist: {root}")

    results: list[ApplyResult] = []
    for item in plan:
        destination = root / item.path
        desired = materialize_planned_content(destination, item)
        if not destination.exists():
            status: Literal["create", "overwrite", "unchanged"] = "create"
        elif destination.is_file() and destination.read_text(encoding="utf-8") == desired:
            status = "unchanged"
        else:
            status = "overwrite"
        results.append(ApplyResult(item.path, status, item.source))
    return results


def apply_to_repository(
    target: str | Path,
    plan: list[PlannedFile],
    *,
    force: bool = False,
    dry_run: bool = False,
) -> list[ApplyResult]:
    root = Path(target).expanduser().resolve()
    results = inspect_apply_plan(root, plan)

    if dry_run:
        return results

    item_by_path = {item.path: item for item in plan}
    conflicts: list[Path] = []
    for result in results:
        if result.status != "overwrite":
            continue
        destination = root / result.path
        item = item_by_path[result.path]
        if not _managed_update_is_safe(destination, item):
            conflicts.append(result.path)

    if conflicts and not force:
        formatted = "\n".join(f"  - {path}" for path in conflicts)
        raise FileExistsError(
            "RepoForge will not overwrite existing files without --force:\n"
            f"{formatted}"
        )

    for result in results:
        if result.status == "unchanged":
            continue
        destination = root / result.path
        destination.parent.mkdir(parents=True, exist_ok=True)
        desired = materialize_planned_content(destination, item_by_path[result.path])
        destination.write_text(desired, encoding="utf-8")

    return results
