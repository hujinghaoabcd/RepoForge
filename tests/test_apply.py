from pathlib import Path

import pytest
import yaml

from repoforge.apply import apply_to_repository, build_apply_plan, inspect_apply_plan
from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config
from repoforge.standards import github_plan, load_github_matrix

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _combined_scientific_standard_config() -> dict:
    config = load_config(TEMPLATES / "scientific-python" / "standard" / "config.example.yml")
    community = load_config(STANDARDS / "community" / "config.example.yml")
    github = load_config(STANDARDS / "github" / "config.example.yml")
    metadata = load_config(STANDARDS / "metadata" / "config.example.yml")

    config["repository_url"] = "https://github.com/example/spatialtools"
    for name in ("code_of_conduct", "contributing", "security", "support"):
        config[name] = community[name]
    for name in ("issue_forms", "pull_request"):
        config[name] = github[name]
    config["changelog"] = metadata["changelog"]

    readme_citation = dict(config["citation"])
    readme_citation.update(metadata["citation"])
    readme_citation["repository_code"] = config["repository_url"]
    config["citation"] = readme_citation
    return config


def test_github_matrix_covers_every_project_type_and_profile():
    matrix = load_github_matrix(standards_root=STANDARDS)
    assert set(matrix["matrix"]) == SUPPORTED_TYPES
    for project_type in SUPPORTED_TYPES:
        assert set(matrix["matrix"][project_type]) == SUPPORTED_PROFILES
        for profile in SUPPORTED_PROFILES:
            assert set(matrix["matrix"][project_type][profile]) == {
                "issue_forms",
                "pull_request_template",
            }


def test_apply_plan_default_policy_selects_only_defaults():
    plan = build_apply_plan(
        "scientific-python",
        "standard",
        _combined_scientific_standard_config(),
        standards_policy="default",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )
    paths = {item.path.as_posix() for item in plan}

    assert "README.md" in paths
    assert "CODE_OF_CONDUCT.md" in paths
    assert "CONTRIBUTING.md" in paths
    assert "SECURITY.md" in paths
    assert "SUPPORT.md" not in paths
    assert "CITATION.cff" in paths
    assert "CHANGELOG.md" in paths
    assert ".github/ISSUE_TEMPLATE/01-bug-report.yml" in paths
    assert ".github/ISSUE_TEMPLATE/02-feature-request.yml" in paths
    assert ".github/ISSUE_TEMPLATE/config.yml" in paths
    assert ".github/pull_request_template.md" in paths


def test_apply_plan_recommended_policy_adds_recommendations():
    plan = build_apply_plan(
        "scientific-python",
        "standard",
        _combined_scientific_standard_config(),
        standards_policy="recommended",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )
    paths = {item.path.as_posix() for item in plan}
    assert "SUPPORT.md" in paths


def test_apply_plan_none_policy_is_readme_only():
    config = load_config(TEMPLATES / "scientific-python" / "minimal" / "config.example.yml")
    plan = build_apply_plan(
        "scientific-python",
        "minimal",
        config,
        standards_policy="none",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )
    assert [item.path.as_posix() for item in plan] == ["README.md"]


def test_apply_creates_selected_files_in_empty_repository(tmp_path):
    plan = build_apply_plan(
        "scientific-python",
        "standard",
        _combined_scientific_standard_config(),
        standards_policy="default",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )
    results = apply_to_repository(tmp_path, plan)

    assert all(result.status == "create" for result in results)
    for item in plan:
        assert (tmp_path / item.path).read_text(encoding="utf-8") == item.content

    citation = yaml.safe_load((tmp_path / "CITATION.cff").read_text(encoding="utf-8"))
    assert citation["title"] == "SpatialTools"


def test_apply_preflight_refuses_conflicts_before_writing_anything(tmp_path):
    (tmp_path / "README.md").write_text("hand-written README\n", encoding="utf-8")
    plan = build_apply_plan(
        "scientific-python",
        "standard",
        _combined_scientific_standard_config(),
        standards_policy="default",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )

    with pytest.raises(FileExistsError, match="README.md"):
        apply_to_repository(tmp_path, plan)

    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "hand-written README\n"
    assert not (tmp_path / "CODE_OF_CONDUCT.md").exists()


def test_apply_dry_run_reports_overwrite_without_writing(tmp_path):
    (tmp_path / "README.md").write_text("existing\n", encoding="utf-8")
    plan = build_apply_plan(
        "scientific-python",
        "minimal",
        load_config(TEMPLATES / "scientific-python" / "minimal" / "config.example.yml"),
        standards_policy="none",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )

    results = apply_to_repository(tmp_path, plan, dry_run=True)
    assert results[0].status == "overwrite"
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "existing\n"


def test_apply_force_overwrites_conflicting_file(tmp_path):
    (tmp_path / "README.md").write_text("existing\n", encoding="utf-8")
    plan = build_apply_plan(
        "scientific-python",
        "minimal",
        load_config(TEMPLATES / "scientific-python" / "minimal" / "config.example.yml"),
        standards_policy="none",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )

    results = apply_to_repository(tmp_path, plan, force=True)
    assert results[0].status == "overwrite"
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == plan[0].content


def test_apply_marks_identical_file_unchanged(tmp_path):
    plan = build_apply_plan(
        "scientific-python",
        "minimal",
        load_config(TEMPLATES / "scientific-python" / "minimal" / "config.example.yml"),
        standards_policy="none",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )
    (tmp_path / "README.md").write_text(plan[0].content, encoding="utf-8")

    results = inspect_apply_plan(tmp_path, plan)
    assert results[0].status == "unchanged"


def test_github_plan_is_explicit_not_detected():
    assert github_plan("web-application", "standard", standards_root=STANDARDS) == {
        "issue_forms": "default",
        "pull_request_template": "default",
    }
