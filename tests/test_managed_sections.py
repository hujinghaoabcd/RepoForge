from copy import deepcopy
from pathlib import Path

import pytest

from repoforge.apply import apply_to_repository, build_apply_plan, inspect_apply_plan
from repoforge.check import check_repository
from repoforge.diff import build_repository_diff, format_repository_diff
from repoforge.init_config import build_init_config
from repoforge.renderer import load_config

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _managed_config():
    return build_init_config(
        "scientific-python",
        "standard",
        project_name="ManagedSpatial",
        repository_url="https://github.com/example/managed-spatial",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )


def _readme_only_plan(config):
    return build_apply_plan(
        "scientific-python",
        "standard",
        config,
        standards_policy="none",
        template_root=TEMPLATES,
        standards_root=STANDARDS,
    )


def test_new_init_configs_use_managed_sections():
    config = _managed_config()
    plan = _readme_only_plan(config)

    assert config["repoforge"]["readme_management"] == "managed-sections"
    assert plan[0].management == "managed-sections"
    assert "<!-- repoforge:start identity -->" in plan[0].content
    assert "<!-- repoforge:start badges -->" in plan[0].content
    assert "<!-- repoforge:start navigation -->" in plan[0].content


def test_unmanaged_body_edits_do_not_create_drift(tmp_path):
    config = _managed_config()
    plan = _readme_only_plan(config)
    apply_to_repository(tmp_path, plan)

    readme = tmp_path / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8")
        + "\n## Maintainer Notes\n\nThis paragraph is maintained by hand.\n",
        encoding="utf-8",
    )

    state = inspect_apply_plan(tmp_path, plan)
    assert state[0].status == "unchanged"
    assert build_repository_diff(tmp_path, plan) == []

    checks = check_repository(tmp_path, plan, config)
    assert not [item for item in checks if item.level == "FAIL"]
    assert any(
        item.level == "PASS" and item.subject == "README.md" for item in checks
    )


def test_managed_badge_update_preserves_user_body_without_force(tmp_path):
    config = _managed_config()
    plan = _readme_only_plan(config)
    apply_to_repository(tmp_path, plan)

    readme = tmp_path / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8")
        + "\n## Maintainer Notes\n\nKeep this exact user-owned text.\n",
        encoding="utf-8",
    )

    updated = deepcopy(config)
    updated["badges"] = (
        "[![Docs](https://img.shields.io/badge/docs-current-blue)](#documentation)"
    )
    updated_plan = _readme_only_plan(updated)

    rendered_diff = format_repository_diff(
        build_repository_diff(tmp_path, updated_plan)
    )
    assert "[overwrite] README.md" in rendered_diff
    assert "docs-current-blue" in rendered_diff
    assert "-Keep this exact user-owned text." not in rendered_diff

    results = apply_to_repository(tmp_path, updated_plan)
    assert results[0].status == "overwrite"
    final_text = readme.read_text(encoding="utf-8")
    assert "docs-current-blue" in final_text
    assert "Keep this exact user-owned text." in final_text


def test_edit_inside_managed_section_is_reported_as_drift(tmp_path):
    config = _managed_config()
    plan = _readme_only_plan(config)
    apply_to_repository(tmp_path, plan)

    readme = tmp_path / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace(
            "# ManagedSpatial",
            "# HandEditedTitle",
            1,
        ),
        encoding="utf-8",
    )

    checks = check_repository(tmp_path, plan, config)
    assert any(
        item.level == "FAIL"
        and item.subject == "README.md"
        and "repoforge diff" in item.message
        for item in checks
    )


def test_old_configs_remain_whole_file_by_default():
    config = load_config(
        TEMPLATES / "scientific-python" / "standard" / "config.example.yml"
    )
    plan = _readme_only_plan(config)
    assert plan[0].management == "whole-file"
    assert "<!-- repoforge:start identity -->" not in plan[0].content


def test_unmarked_existing_readme_still_requires_force_for_migration(tmp_path):
    config = _managed_config()
    plan = _readme_only_plan(config)
    (tmp_path / "README.md").write_text("# Existing hand-written README\n", encoding="utf-8")

    with pytest.raises(FileExistsError, match="--force"):
        apply_to_repository(tmp_path, plan)

    assert (tmp_path / "README.md").read_text(encoding="utf-8") == (
        "# Existing hand-written README\n"
    )


def test_incomplete_managed_markers_fail_closed(tmp_path):
    config = _managed_config()
    plan = _readme_only_plan(config)
    apply_to_repository(tmp_path, plan)

    readme = tmp_path / "README.md"
    text = readme.read_text(encoding="utf-8").replace(
        "<!-- repoforge:end badges -->",
        "",
        1,
    )
    readme.write_text(text, encoding="utf-8")

    with pytest.raises(ValueError, match="incomplete|Malformed"):
        build_repository_diff(tmp_path, plan)
