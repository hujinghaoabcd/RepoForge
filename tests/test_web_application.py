from __future__ import annotations

from pathlib import Path

import pytest

from repoforge.renderer import load_config, render_from_config


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
PREVIEWS = ROOT / "tests" / "previews"
BRANDING = ROOT / "tests" / "branding.yml"


@pytest.mark.parametrize(
    ("profile", "required", "forbidden"),
    [
        (
            "minimal",
            ["## Features", "## Run Locally", "## Configuration", "## Deploy"],
            ["## Architecture", "## Database and Migrations", "## Observability and Operations"],
        ),
        (
            "standard",
            [
                "## Overview",
                "## Tech Stack",
                "## Local Development",
                "## Environment Variables",
                "## Database and Migrations",
                "## Deployment",
                "## Testing",
            ],
            ["## Background Jobs and Queues", "## Backup and Restore", "## Observability and Operations"],
        ),
        (
            "full",
            [
                "## Product Overview",
                "## Architecture",
                "## Configuration and Secrets",
                "## Database and Migrations",
                "## API",
                "## Authentication and Authorization",
                "## Background Jobs and Queues",
                "## File and Object Storage",
                "## Deployment",
                "## Observability and Operations",
                "## Backup and Restore",
                "## Security",
                "## Upgrade Notes",
            ],
            [],
        ),
    ],
)
def test_web_application_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "web-application" / profile
    rendered = render_from_config(
        "web-application",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert rendered.startswith("# GeoPortal")
    assert rendered.endswith("\n")
    assert rendered.count("```") % 2 == 0
    for token in required:
        assert token in rendered
    for token in forbidden:
        assert token not in rendered


def test_web_application_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "web-application" / profile
        outputs[profile] = render_from_config(
            "web-application", profile, profile_dir / "config.example.yml", template_root=TEMPLATES
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_web_application_examples_and_previews_track_renderer():
    branding = load_config(BRANDING)

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "web-application" / profile
        rendered = render_from_config(
            "web-application", profile, profile_dir / "config.example.yml", template_root=TEMPLATES
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")
        preview = (PREVIEWS / "web-application" / f"{profile}.md").read_text(encoding="utf-8")

        assert example == rendered
        assert branding["logo_path"] in preview
        assert f'width="{branding["logo_width"]}"' in preview
        assert preview.rstrip().endswith(rendered.rstrip())


def test_full_web_application_keeps_operations_visible():
    rendered = render_from_config(
        "web-application",
        "full",
        TEMPLATES / "web-application" / "full" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "PostgreSQL/PostGIS and object storage" in rendered
    assert "immutable image" in rendered
    assert "DEBUG=false" in rendered
    assert "health" in rendered.lower()
