from pathlib import Path

import pytest

from repoforge.apply import build_apply_plan
from repoforge.renderer import load_config

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _config() -> dict:
    config = load_config(TEMPLATES / "scientific-python" / "standard" / "config.example.yml")
    community = load_config(STANDARDS / "community" / "config.example.yml")
    github = load_config(STANDARDS / "github" / "config.example.yml")
    metadata = load_config(STANDARDS / "metadata" / "config.example.yml")

    config["repository_url"] = "https://github.com/example/spatialtools"
    for name in ("code_of_conduct", "contributing", "security", "support"):
        config[name] = community[name]
    config["issue_forms"] = github["issue_forms"]
    config["pull_request"] = github["pull_request"]
    config["changelog"] = metadata["changelog"]

    citation = dict(config["citation"])
    citation.update(metadata["citation"])
    citation["repository_code"] = config["repository_url"]
    config["citation"] = citation
    return config


def _plan(policy="default", include=None, exclude=None):
    return build_apply_plan(
        "scientific-python",
        "standard",
        _config(),
        standards_policy=policy,
        include=set(include or ()),
        exclude=set(exclude or ()),
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )


def _content(plan, path: str) -> str:
    return next(item.content for item in plan if item.path.as_posix() == path)


def test_issue_chooser_links_only_selected_default_policies():
    plan = _plan("default")
    chooser = _content(plan, ".github/ISSUE_TEMPLATE/config.yml")

    assert "SECURITY.md" in chooser
    assert "SUPPORT.md" not in chooser


def test_recommended_policy_adds_support_link_to_issue_chooser():
    plan = _plan("recommended")
    chooser = _content(plan, ".github/ISSUE_TEMPLATE/config.yml")

    assert "SECURITY.md" in chooser
    assert "SUPPORT.md" in chooser


def test_explicit_exclude_removes_default_standard_and_chooser_link():
    plan = _plan("default", exclude={"security"})
    paths = {item.path.as_posix() for item in plan}
    chooser = _content(plan, ".github/ISSUE_TEMPLATE/config.yml")

    assert "SECURITY.md" not in paths
    assert "SECURITY.md" not in chooser


def test_explicit_include_can_enable_optional_or_recommended_standard():
    plan = _plan("none", include={"citation"})
    paths = {item.path.as_posix() for item in plan}

    assert paths == {"README.md", "CITATION.cff"}


def test_include_and_exclude_same_standard_is_rejected():
    with pytest.raises(ValueError, match="both included and excluded"):
        _plan("default", include={"security"}, exclude={"security"})
