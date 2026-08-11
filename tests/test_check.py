from copy import deepcopy
from pathlib import Path

from repoforge.apply import apply_to_repository, build_apply_plan
from repoforge.check import check_exit_code, check_repository
from repoforge.renderer import load_config

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "examples" / "apply" / "scientific-python-standard.yml"
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _config(*, example_author: bool = False):
    config = deepcopy(load_config(CONFIG))
    config["repoforge"] = {
        "config_version": 1,
        "project_type": "scientific-python",
        "profile": "standard",
    }
    config["code_of_conduct"]["reporting_contact"] = "conduct@example.org"
    config["security"]["reporting_contact"] = "security@example.org"
    if not example_author:
        config["citation"]["authors"] = [
            {
                "family_names": "Smith",
                "given_names": "Alex",
                "orcid": None,
                "affiliation": "Example Lab",
            }
        ]
    return config


def _plan(config):
    return build_apply_plan(
        "scientific-python",
        "standard",
        config,
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )


def test_check_passes_for_in_sync_repository(tmp_path):
    config = _config()
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)

    results = check_repository(tmp_path, plan, config)

    assert not [item for item in results if item.level == "FAIL"]
    assert not [item for item in results if item.level == "WARN"]
    assert any(
        item.level == "PASS" and item.subject == "README.md" for item in results
    )
    assert check_exit_code(results) == 0


def test_check_fails_when_selected_file_is_missing(tmp_path):
    config = _config()
    plan = _plan(config)

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "FAIL"
        and item.subject == "README.md"
        and "missing" in item.message
        for item in results
    )
    assert check_exit_code(results) == 1


def test_check_fails_when_managed_file_drifted(tmp_path):
    config = _config()
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)
    (tmp_path / "README.md").write_text("# hand edited\n", encoding="utf-8")

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "FAIL"
        and item.subject == "README.md"
        and "repoforge diff" in item.message
        for item in results
    )


def test_check_reports_invalid_citation_structure(tmp_path):
    config = _config()
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)
    (tmp_path / "CITATION.cff").write_text("authors: [\n", encoding="utf-8")

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "FAIL"
        and item.subject == "CITATION.cff"
        and "invalid YAML" in item.message
        for item in results
    )


def test_check_reports_invalid_issue_form_structure(tmp_path):
    config = _config()
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)
    issue_form = tmp_path / ".github/ISSUE_TEMPLATE/01-bug-report.yml"
    issue_form.write_text("name: Broken\ndescription: Broken form\nbody: [\n", encoding="utf-8")

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "FAIL"
        and item.subject == ".github/ISSUE_TEMPLATE/01-bug-report.yml"
        and "invalid YAML" in item.message
        for item in results
    )


def test_check_fails_for_critical_reporting_placeholders(tmp_path):
    config = _config()
    config["security"]["reporting_contact"] = (
        "Use the project's documented private security contact or GitHub private "
        "vulnerability reporting when available."
    )
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "FAIL"
        and item.subject == "repoforge.yml"
        and "Security reporting_contact" in item.message
        for item in results
    )


def test_check_warns_for_example_citation_author_and_strict_fails(tmp_path):
    config = _config(example_author=True)
    plan = _plan(config)
    apply_to_repository(tmp_path, plan)

    results = check_repository(tmp_path, plan, config)

    assert any(
        item.level == "WARN"
        and item.subject == "repoforge.yml"
        and "Citation metadata" in item.message
        for item in results
    )
    assert check_exit_code(results) == 0
    assert check_exit_code(results, strict=True) == 1
