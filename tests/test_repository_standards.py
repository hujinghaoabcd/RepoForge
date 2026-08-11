from pathlib import Path

import pytest

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config
from repoforge.standards import (
    STANDARD_STATES,
    STANDARD_TEMPLATES,
    load_standards_matrix,
    render_community_standard,
    standard_plan,
)

ROOT = Path(__file__).resolve().parents[1]
STANDARDS = ROOT / "standards"
COMMUNITY_CONFIG = STANDARDS / "community" / "config.example.yml"


def test_standards_matrix_covers_every_project_type_and_profile():
    matrix = load_standards_matrix(standards_root=STANDARDS)
    assert set(matrix["matrix"]) == SUPPORTED_TYPES

    for project_type in SUPPORTED_TYPES:
        assert set(matrix["matrix"][project_type]) == SUPPORTED_PROFILES
        for profile in SUPPORTED_PROFILES:
            plan = matrix["matrix"][project_type][profile]
            assert set(plan) == set(STANDARD_TEMPLATES)
            assert set(plan.values()) <= STANDARD_STATES


def test_standard_plan_uses_explicit_project_type_and_profile():
    plan = standard_plan(
        "scientific-python",
        "standard",
        standards_root=STANDARDS,
    )
    assert plan == {
        "code_of_conduct": "default",
        "contributing": "default",
        "security": "default",
        "support": "recommended",
    }


def test_community_standard_templates_render_from_shared_config():
    config = load_config(COMMUNITY_CONFIG)

    for standard_name in STANDARD_TEMPLATES:
        rendered = render_community_standard(
            standard_name,
            config,
            standards_root=STANDARDS,
        )
        assert rendered.endswith("\n")
        assert "ExampleProject" in rendered
        assert "{{" not in rendered
        assert "{%" not in rendered


def test_code_of_conduct_requires_explicit_reporting_contact():
    config = load_config(COMMUNITY_CONFIG)
    del config["code_of_conduct"]["reporting_contact"]

    with pytest.raises(Exception, match="reporting_contact"):
        render_community_standard(
            "code_of_conduct",
            config,
            standards_root=STANDARDS,
        )


def test_security_requires_explicit_reporting_contact():
    config = load_config(COMMUNITY_CONFIG)
    del config["security"]["reporting_contact"]

    with pytest.raises(Exception, match="reporting_contact"):
        render_community_standard(
            "security",
            config,
            standards_root=STANDARDS,
        )


def test_repoforge_dogfoods_first_community_standards_pack():
    for filename in (
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "SUPPORT.md",
    ):
        path = ROOT / filename
        assert path.is_file(), filename
        assert path.read_text(encoding="utf-8").strip(), filename


def test_no_automatic_detection_state_exists_in_standards_api():
    with pytest.raises(ValueError, match="Unsupported project type"):
        standard_plan("auto", "standard", standards_root=STANDARDS)
