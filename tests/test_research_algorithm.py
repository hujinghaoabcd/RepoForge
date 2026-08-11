from __future__ import annotations

from pathlib import Path

import pytest

from repoforge.renderer import render_from_config


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"


@pytest.mark.parametrize(
    ("profile", "required", "forbidden"),
    [
        (
            "minimal",
            ["# LatentMap", "## Quick Start", "## Validation", "## Citation"],
            ["## Scientific Problem", "## Key Contributions", "## Computational Characteristics"],
        ),
        (
            "standard",
            [
                "## Scientific Problem",
                "## Method Overview",
                "## Key Contributions",
                "## Validation",
                "## Limitations",
            ],
            ["## Why Existing Approaches Are Insufficient", "## Computational Characteristics"],
        ),
        (
            "full",
            [
                "## Scientific Problem",
                "## Why Existing Approaches Are Insufficient",
                "## Proposed Method",
                "### Objective / estimand",
                "### Algorithm Outline",
                "## Inputs, Outputs, and Interpretation",
                "## Computational Characteristics",
                "## Reproducibility",
            ],
            [],
        ),
    ],
)
def test_research_algorithm_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "research-algorithm" / profile
    rendered = render_from_config(
        "research-algorithm",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "{{" not in rendered
    assert "{%" not in rendered
    assert rendered.count("```") % 2 == 0

    for token in required:
        assert token in rendered
    for token in forbidden:
        assert token not in rendered


def test_research_algorithm_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "research-algorithm" / profile
        outputs[profile] = render_from_config(
            "research-algorithm",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_research_algorithm_examples_match_visible_previews():
    for profile in ("minimal", "standard", "full"):
        example = (
            TEMPLATES / "research-algorithm" / profile / "README.example.md"
        ).read_text(encoding="utf-8")
        preview = (PREVIEWS / "research-algorithm" / f"{profile}.md").read_text(
            encoding="utf-8"
        )

        assert example == preview
        assert "# LatentMap" in preview
        assert "MethodX" not in preview
