from pathlib import Path

import yaml

from repoforge.renderer import load_config
from repoforge.standards import GITHUB_TEMPLATES, render_github_standard

ROOT = Path(__file__).resolve().parents[1]
STANDARDS = ROOT / "standards"
CONFIG = STANDARDS / "github" / "config.example.yml"


def test_github_standard_templates_render_cleanly():
    config = load_config(CONFIG)

    for standard_name in GITHUB_TEMPLATES:
        rendered = render_github_standard(
            standard_name,
            config,
            standards_root=STANDARDS,
        )
        assert rendered.endswith("\n")
        assert "{{" not in rendered
        assert "{%" not in rendered


def test_issue_forms_have_required_top_level_schema():
    config = load_config(CONFIG)

    for standard_name in ("bug_report", "feature_request"):
        rendered = render_github_standard(
            standard_name,
            config,
            standards_root=STANDARDS,
        )
        form = yaml.safe_load(rendered)
        assert isinstance(form["name"], str) and form["name"]
        assert isinstance(form["description"], str) and form["description"]
        assert isinstance(form["body"], list) and form["body"]

        ids = [item.get("id") for item in form["body"] if item.get("id")]
        assert len(ids) == len(set(ids))
        assert any(item.get("id") == "conduct" for item in form["body"])


def test_issue_chooser_disables_blank_issues_and_links_support_security():
    config = load_config(CONFIG)
    rendered = render_github_standard(
        "issue_config",
        config,
        standards_root=STANDARDS,
    )
    chooser = yaml.safe_load(rendered)

    assert chooser["blank_issues_enabled"] is False
    urls = {item["url"] for item in chooser["contact_links"]}
    assert "https://github.com/example/example-project/blob/main/SUPPORT.md" in urls
    assert "https://github.com/example/example-project/blob/main/SECURITY.md" in urls


def test_pull_request_template_contains_review_contracts():
    config = load_config(CONFIG)
    rendered = render_github_standard(
        "pull_request_template",
        config,
        standards_root=STANDARDS,
    )

    assert "## Summary" in rendered
    assert "## Validation" in rendered
    assert "## Compatibility and risk" in rendered
    assert "CONTRIBUTING.md" in rendered


def test_repoforge_dogfoods_github_forms():
    files = (
        ROOT / ".github" / "ISSUE_TEMPLATE" / "01-bug-report.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "02-feature-request.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml",
        ROOT / ".github" / "pull_request_template.md",
    )
    for path in files:
        assert path.is_file(), path
        assert path.read_text(encoding="utf-8").strip(), path


def test_repoforge_issue_forms_are_valid_yaml():
    for filename in ("01-bug-report.yml", "02-feature-request.yml", "config.yml"):
        path = ROOT / ".github" / "ISSUE_TEMPLATE" / filename
        parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(parsed, dict)
