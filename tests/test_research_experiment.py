from __future__ import annotations

from pathlib import Path

import pytest

from repoforge.renderer import load_config, render_from_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"
BRANDING = ROOT / "tests" / "branding.yml"


@pytest.mark.parametrize(
    ("profile", "required", "forbidden"),
    [
        (
            "minimal",
            [
                "## Environment",
                "## Data",
                "## Run",
                "## Expected Output",
                "## Citation",
            ],
            [
                "## Experiment Protocol",
                "## Main Results",
                "## Statistical Testing",
                "## Result and Artifact Identity",
            ],
        ),
        (
            "standard",
            [
                "## Overview",
                "## Datasets",
                "## Quick Reproduction",
                "## Experiment Protocol",
                "## Main Results",
                "## Repository Structure",
            ],
            [
                "## Ablation and Sensitivity Studies",
                "## Statistical Testing",
                "## Result and Artifact Identity",
            ],
        ),
        (
            "full",
            [
                "## Datasets and Data Identity",
                "## Fastest Start",
                "## Available Models and Baselines",
                "## Experiment Protocol",
                "## Reproducing the Main Results",
                "## Ablation and Sensitivity Studies",
                "## Statistical Testing",
                "## Result and Artifact Identity",
                "## Reproducibility Boundaries",
            ],
            [],
        ),
    ],
)
def test_research_experiment_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "research-experiment" / profile
    rendered = render_from_config(
        "research-experiment",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    header = rendered.split("\n## ", 1)[0]
    assert rendered.startswith('<div align="center">')
    assert "# ForecastBench" in header
    assert "img.shields.io" in header
    assert "</div>" in header
    assert rendered.endswith("\n")
    assert "{{" not in rendered
    assert "{%" not in rendered
    assert rendered.count("```") % 2 == 0

    for token in required:
        assert token in rendered
    for token in forbidden:
        assert token not in rendered


def test_research_experiment_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "research-experiment" / profile
        outputs[profile] = render_from_config(
            "research-experiment",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_full_research_experiment_keeps_evidence_identity_visible():
    profile_dir = TEMPLATES / "research-experiment" / "full"
    rendered = render_from_config(
        "research-experiment",
        "full",
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "42, 43, 44, 45, 46" in rendered
    assert "Baseline tuning" in rendered
    assert "predictions.npz" in rendered
    assert "significance.py" in rendered
    assert "resolved config" in rendered.lower()
    assert "smoke-test" in rendered


def test_research_experiment_examples_and_previews_track_renderer():
    branding = load_config(BRANDING)

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "research-experiment" / profile
        config = load_config(profile_dir / "config.example.yml")
        rendered = render_readme(
            "research-experiment", profile, config, template_root=TEMPLATES
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")

        branded_config = dict(config)
        branded_config.update(branding)
        branded = render_readme(
            "research-experiment", profile, branded_config, template_root=TEMPLATES
        )
        preview = (PREVIEWS / "research-experiment" / f"{profile}.md").read_text(
            encoding="utf-8"
        )

        assert example == rendered
        assert preview == branded
        assert branding["logo_path"] in preview
        assert f'width="{branding["logo_width"]}"' in preview
