from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

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


@dataclass(frozen=True)
class PlannedFile:
    path: Path
    content: str
    source: str


@dataclass(frozen=True)
class ApplyResult:
    path: Path
    status: Literal["create", "overwrite", "unchanged"]
    source: str


def _selected(state: str, policy: StandardsPolicy) -> bool:
    if policy == "none":
        return False
    if policy == "default":
        return state == "default"
    if policy == "recommended":
        return state in {"default", "recommended"}
    raise ValueError(f"Unsupported standards policy: {policy}")


def build_apply_plan(
    project_type: str,
    profile: str,
    config: dict[str, Any],
    *,
    standards_policy: StandardsPolicy = "default",
    template_root: str | Path | None = None,
    standards_root: str | Path | None = None,
) -> list[PlannedFile]:
    files = [
        PlannedFile(
            path=Path("README.md"),
            content=render_readme(
                project_type,
                profile,
                config,
                template_root=template_root,
            ),
            source="readme",
        )
    ]

    if standards_policy == "none":
        return files

    community = standard_plan(
        project_type, profile, standards_root=standards_root
    )
    for name, state in community.items():
        if not _selected(state, standards_policy):
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
    if _selected(github["issue_forms"], standards_policy):
        for name, output in GITHUB_ISSUE_OUTPUTS.items():
            files.append(
                PlannedFile(
                    path=output,
                    content=render_github_standard(
                        name, config, standards_root=standards_root
                    ),
                    source=f"github:{name}",
                )
            )
    if _selected(github["pull_request_template"], standards_policy):
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

    metadata = metadata_plan(
        project_type, profile, standards_root=standards_root
    )
    for name, state in metadata.items():
        if not _selected(state, standards_policy):
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
        if not destination.exists():
            status: Literal["create", "overwrite", "unchanged"] = "create"
        elif destination.is_file() and destination.read_text(encoding="utf-8") == item.content:
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

    conflicts = [result.path for result in results if result.status == "overwrite"]
    if conflicts and not force:
        formatted = "\n".join(f"  - {path}" for path in conflicts)
        raise FileExistsError(
            "RepoForge will not overwrite existing files without --force:\n"
            f"{formatted}"
        )

    if dry_run:
        return results

    content_by_path = {item.path: item.content for item in plan}
    for result in results:
        if result.status == "unchanged":
            continue
        destination = root / result.path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content_by_path[result.path], encoding="utf-8")

    return results
