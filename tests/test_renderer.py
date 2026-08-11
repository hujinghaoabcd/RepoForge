from pathlib import Path

import pytest

from repoforge.renderer import load_config, render_from_config, render_readme

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


@pytest.mark.parametrize(
    ("profile", "required", "forbidden"),
    [
        (
            "minimal",
            ["## Installation", "## Quick Start", "## Documentation", "## License"],
            ["## Features", "## Method catalogue", "## Scientific scope"],
        ),
        (
            "standard",
            ["## Why SpatialTools?", "## Features", "## Methods and Capabilities", "## Validation"],
            ["## Scientific scope", "## Project status and API stability"],
        ),
        (
            "full",
            [
                "## What SpatialTools is",
                "## Scientific scope",
                "## Method catalogue",
                "## Choosing a method",
                "## Validation and reproducibility",
                "## Project status and API stability",
            ],
            [],
        ),
    ],
)
def test_scientific_python_profiles_render_independently(profile, required, forbidden):
    config_path = TEMPLATES / "scientific-python" / profile / "config.example.yml"
    rendered = render_from_config(
        "scientific-python",
        profile,
        config_path,
        template_root=TEMPLATES,
    )

    assert rendered.startswith("# SpatialTools")
    assert rendered.endswith("\n")
    for heading in required:
        assert heading in rendered
    for heading in forbidden:
        assert heading not in rendered


def test_each_profile_uses_its_own_template_file():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "scientific-python" / profile
        outputs[profile] = render_from_config(
            "scientific-python",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(set(outputs.values())) == 3
    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_strict_config_rejects_missing_required_field():
    config_path = TEMPLATES / "scientific-python" / "minimal" / "config.example.yml"
    config = load_config(config_path)
    config.pop("project_name")

    with pytest.raises(Exception, match="project_name"):
        render_readme(
            "scientific-python",
            "minimal",
            config,
            template_root=TEMPLATES,
        )


def test_unsupported_project_type_is_rejected():
    with pytest.raises(ValueError, match="Unsupported project type"):
        render_readme("unknown", "minimal", {}, template_root=TEMPLATES)
