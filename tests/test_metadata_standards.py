from pathlib import Path

import yaml

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config
from repoforge.standards import (
    METADATA_TEMPLATES,
    STANDARD_STATES,
    load_metadata_matrix,
    metadata_plan,
    render_metadata_standard,
)

ROOT = Path(__file__).resolve().parents[1]
STANDARDS = ROOT / "standards"
CONFIG = STANDARDS / "metadata" / "config.example.yml"


def test_metadata_matrix_covers_every_project_type_and_profile():
    matrix = load_metadata_matrix(standards_root=STANDARDS)
    assert set(matrix["matrix"]) == SUPPORTED_TYPES

    for project_type in SUPPORTED_TYPES:
        assert set(matrix["matrix"][project_type]) == SUPPORTED_PROFILES
        for profile in SUPPORTED_PROFILES:
            plan = matrix["matrix"][project_type][profile]
            assert set(plan) == set(METADATA_TEMPLATES)
            assert set(plan.values()) <= STANDARD_STATES


def test_metadata_plan_prioritizes_research_citation_and_software_changelog():
    research = metadata_plan(
        "research-experiment", "standard", standards_root=STANDARDS
    )
    frontend = metadata_plan(
        "frontend-library", "standard", standards_root=STANDARDS
    )

    assert research["citation"] == "default"
    assert frontend["citation"] == "optional"
    assert frontend["changelog"] == "default"


def test_citation_template_renders_valid_basic_cff_yaml():
    config = load_config(CONFIG)
    rendered = render_metadata_standard(
        "citation", config, standards_root=STANDARDS
    )
    citation = yaml.safe_load(rendered)

    assert citation["cff-version"] == "1.2.0"
    assert citation["type"] == "software"
    assert citation["title"] == "ExampleProject"
    assert citation["version"] == "1.2.0"
    assert citation["repository-code"] == "https://github.com/example/example-project"
    assert citation["authors"][0]["family-names"] == "Doe"
    assert citation["authors"][0]["given-names"] == "Jane"
    assert "doi" not in citation


def test_changelog_uses_unreleased_and_omits_empty_change_types():
    config = load_config(CONFIG)
    rendered = render_metadata_standard(
        "changelog", config, standards_root=STANDARDS
    )

    assert rendered.startswith("# Changelog\n")
    assert "## [Unreleased]" in rendered
    assert "### Added" in rendered
    assert "Initial public changelog structure." in rendered
    for empty_heading in (
        "### Changed",
        "### Deprecated",
        "### Removed",
        "### Fixed",
        "### Security",
    ):
        assert empty_heading not in rendered


def test_empty_unreleased_changelog_uses_guidance_comment_not_fake_entries():
    config = load_config(CONFIG)
    for key in config["changelog"]["unreleased"]:
        config["changelog"]["unreleased"][key] = []

    rendered = render_metadata_standard(
        "changelog", config, standards_root=STANDARDS
    )

    assert "## [Unreleased]" in rendered
    assert "<!-- Add only non-empty change sections" in rendered
    assert "Initial public changelog" not in rendered


def test_repoforge_dogfoods_changelog_without_forcing_citation():
    changelog = ROOT / "CHANGELOG.md"
    assert changelog.is_file()
    text = changelog.read_text(encoding="utf-8")
    assert text.startswith("# Changelog")
    assert "## [Unreleased]" in text
