from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import yaml

from .apply import PlannedFile, inspect_apply_plan

CheckLevel = Literal["PASS", "WARN", "FAIL"]

CODE_OF_CONDUCT_PLACEHOLDERS = {
    "Use a private contact method published by the project maintainers.",
    "Replace this value with a private contact channel maintained by the project.",
}
SECURITY_PLACEHOLDERS = {
    "Use the project's documented private security contact or GitHub private vulnerability reporting when available.",
    "Replace this value with the project's private security contact or GitHub private vulnerability reporting channel.",
}


@dataclass(frozen=True)
class CheckResult:
    level: CheckLevel
    subject: str
    message: str


def _result(level: CheckLevel, subject: str, message: str) -> CheckResult:
    return CheckResult(level=level, subject=subject, message=message)


def _validate_citation(path: Path) -> list[CheckResult]:
    if not path.is_file():
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [_result("FAIL", "CITATION.cff", f"invalid YAML: {exc}")]

    if not isinstance(data, dict):
        return [_result("FAIL", "CITATION.cff", "root must be a YAML mapping")]

    problems: list[str] = []
    if str(data.get("cff-version")) != "1.2.0":
        problems.append("cff-version must be 1.2.0")
    if data.get("type") != "software":
        problems.append("type must be software")
    if not isinstance(data.get("title"), str) or not data.get("title", "").strip():
        problems.append("title is required")
    authors = data.get("authors")
    if not isinstance(authors, list) or not authors:
        problems.append("at least one author is required")
    else:
        for index, author in enumerate(authors, start=1):
            if not isinstance(author, dict):
                problems.append(f"author {index} must be a mapping")
                continue
            if not author.get("family-names") or not author.get("given-names"):
                problems.append(f"author {index} requires family-names and given-names")

    if problems:
        return [_result("FAIL", "CITATION.cff", "; ".join(problems))]
    return []


def _validate_issue_form(path: Path, subject: str) -> list[CheckResult]:
    if not path.is_file():
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [_result("FAIL", subject, f"invalid YAML: {exc}")]

    if not isinstance(data, dict):
        return [_result("FAIL", subject, "root must be a YAML mapping")]

    problems: list[str] = []
    for key in ("name", "description"):
        if not isinstance(data.get(key), str) or not data.get(key, "").strip():
            problems.append(f"{key} is required")
    body = data.get("body")
    if not isinstance(body, list) or not body:
        problems.append("body must be a non-empty list")
    else:
        for index, item in enumerate(body, start=1):
            if not isinstance(item, dict) or not isinstance(item.get("type"), str):
                problems.append(f"body item {index} requires a type")

    if problems:
        return [_result("FAIL", subject, "; ".join(problems))]
    return []


def _validate_issue_config(path: Path, subject: str) -> list[CheckResult]:
    if not path.is_file():
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [_result("FAIL", subject, f"invalid YAML: {exc}")]

    if not isinstance(data, dict):
        return [_result("FAIL", subject, "root must be a YAML mapping")]
    if not isinstance(data.get("blank_issues_enabled"), bool):
        return [_result("FAIL", subject, "blank_issues_enabled must be boolean")]
    contacts = data.get("contact_links")
    if contacts is not None and not isinstance(contacts, list):
        return [_result("FAIL", subject, "contact_links must be a list")]
    return []


def _config_check(config: dict[str, Any]) -> list[CheckResult]:
    repoforge = config.get("repoforge")
    if repoforge is None:
        return [
            _result(
                "WARN",
                "repoforge.yml",
                "no repoforge selection block; command-line type/profile overrides are required",
            )
        ]
    if not isinstance(repoforge, dict):
        return [_result("FAIL", "repoforge.yml", "repoforge section must be a mapping")]
    if repoforge.get("config_version") != 1:
        return [_result("FAIL", "repoforge.yml", "unsupported or missing config_version")]
    return [_result("PASS", "repoforge.yml", "configuration and explicit selection are valid")]


def _placeholder_checks(config: dict[str, Any], plan: list[PlannedFile]) -> list[CheckResult]:
    selected_sources = {item.source for item in plan}
    results: list[CheckResult] = []

    repository_url = config.get("repository_url")
    if isinstance(repository_url, str) and "OWNER/REPOSITORY" in repository_url:
        results.append(
            _result(
                "FAIL",
                "repoforge.yml",
                "repository_url still contains the OWNER/REPOSITORY placeholder",
            )
        )

    if "community:code_of_conduct" in selected_sources:
        section = config.get("code_of_conduct")
        if isinstance(section, dict) and section.get("reporting_contact") in CODE_OF_CONDUCT_PLACEHOLDERS:
            results.append(
                _result(
                    "FAIL",
                    "repoforge.yml",
                    "Code of Conduct reporting_contact is still a generic placeholder",
                )
            )

    if "community:security" in selected_sources:
        section = config.get("security")
        if isinstance(section, dict) and section.get("reporting_contact") in SECURITY_PLACEHOLDERS:
            results.append(
                _result(
                    "FAIL",
                    "repoforge.yml",
                    "Security reporting_contact is still a generic placeholder",
                )
            )

    if "metadata:citation" in selected_sources:
        citation = config.get("citation")
        if isinstance(citation, dict):
            authors = citation.get("authors")
            if isinstance(authors, list):
                for author in authors:
                    if not isinstance(author, dict):
                        continue
                    if (
                        author.get("family_names") == "Doe"
                        and author.get("given_names") == "Jane"
                    ) or author.get("orcid") == "https://orcid.org/0000-0000-0000-0000":
                        results.append(
                            _result(
                                "WARN",
                                "repoforge.yml",
                                "Citation metadata still contains the example author/ORCID",
                            )
                        )
                        break

    if "community:contributing" in selected_sources:
        contributing = config.get("contributing")
        if isinstance(contributing, dict):
            setup = contributing.get("setup_command")
            if isinstance(setup, str) and "github.com/example/example-project" in setup:
                results.append(
                    _result(
                        "WARN",
                        "repoforge.yml",
                        "contributing.setup_command still uses the example repository URL",
                    )
                )

    return results


def check_repository(
    target: str | Path,
    plan: list[PlannedFile],
    config: dict[str, Any],
) -> list[CheckResult]:
    root = Path(target).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Target repository does not exist: {root}")

    results: list[CheckResult] = []
    results.extend(_config_check(config))

    for state in inspect_apply_plan(root, plan):
        subject = state.path.as_posix()
        if state.status == "unchanged":
            results.append(_result("PASS", subject, "in sync"))
        elif state.status == "create":
            results.append(_result("FAIL", subject, "missing selected RepoForge file"))
        else:
            results.append(
                _result(
                    "FAIL",
                    subject,
                    "content differs from the current RepoForge plan; run repoforge diff",
                )
            )

    selected_paths = {item.path.as_posix() for item in plan}
    citation = "CITATION.cff"
    bug_form = ".github/ISSUE_TEMPLATE/01-bug-report.yml"
    feature_form = ".github/ISSUE_TEMPLATE/02-feature-request.yml"
    issue_config = ".github/ISSUE_TEMPLATE/config.yml"

    if citation in selected_paths:
        results.extend(_validate_citation(root / citation))
    if bug_form in selected_paths:
        results.extend(_validate_issue_form(root / bug_form, bug_form))
    if feature_form in selected_paths:
        results.extend(_validate_issue_form(root / feature_form, feature_form))
    if issue_config in selected_paths:
        results.extend(_validate_issue_config(root / issue_config, issue_config))

    results.extend(_placeholder_checks(config, plan))
    return results


def format_check_results(results: list[CheckResult]) -> str:
    if not results:
        return "PASS  Repository has no selected checks.\n"

    lines = [f"{item.level:<4}  {item.subject}  {item.message}" for item in results]
    passed = sum(item.level == "PASS" for item in results)
    warnings = sum(item.level == "WARN" for item in results)
    failed = sum(item.level == "FAIL" for item in results)
    lines.append("")
    lines.append(f"Summary: {passed} passed, {warnings} warnings, {failed} failed.")
    if failed == 0:
        lines.append("Repository standards are in sync.")
    return "\n".join(lines) + "\n"


def check_exit_code(results: list[CheckResult], *, strict: bool = False) -> int:
    if any(item.level == "FAIL" for item in results):
        return 1
    if strict and any(item.level == "WARN" for item in results):
        return 1
    return 0
