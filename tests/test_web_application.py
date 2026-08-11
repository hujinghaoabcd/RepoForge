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
            ["## Architecture", "## Testing", "## CI/CD"],
        ),
        (
            "standard",
            [
                "## Overview",
                "## Screenshots / Demo",
                "## Tech Stack",
                "## Local Development",
                "## Environment Variables",
                "## Database",
                "## Deployment",
                "## Project Structure",
                "## Testing",
            ],
            ["## CI/CD", "## Observability and Operations"],
        ),
        (
            "full",
            [
                "## Product Overview",
                "## Architecture",
                "## Configuration and Secrets",
                "## Database and Migrations",
                "## Deployment",
                "## CI/CD",
                "## Observability and Operations",
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

    # Web-product READMEs may put a screenshot/hero before the H1, as long as
    # the project identity remains explicit and unique.
    assert rendered.count("# GeoBoard\n") == 1
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
            "web-application",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_full_web_application_keeps_operational_identity_visible():
    rendered = render_from_config(
        "web-application",
        "full",
        TEMPLATES / "web-application" / "full" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "PostgreSQL + PostGIS" in rendered
    assert "Celery + Redis" in rendered
    assert "S3-compatible" in rendered
    assert "Backup / Restore Boundary" in rendered
    assert "## Authentication and Authorization" in rendered
    assert "## Background Jobs and Queues" in rendered
    assert "## Object Storage / Media" in rendered


def test_web_application_examples_and_previews_track_renderer():
    logo_path = load_config(BRANDING)["logo_path"]

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "web-application" / profile
        rendered = render_from_config(
            "web-application",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")
        preview = (PREVIEWS / "web-application" / f"{profile}.md").read_text(encoding="utf-8")

        assert example == rendered
        assert logo_path in preview
        branded = load_config(profile_dir / "config.example.yml")
        branded.update(load_config(BRANDING))
        from repoforge.renderer import render_readme

        assert preview == render_readme(
            "web-application", profile, branded, template_root=TEMPLATES
        )
