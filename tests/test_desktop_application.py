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
                "## Features",
                "## Download and Install",
                "## Supported Platforms",
                "## Run from Source",
                "## License",
            ],
            [
                "## Architecture",
                "## Packaging and Release Engineering",
                "## Plugins and Extensions",
            ],
        ),
        (
            "standard",
            [
                "## Overview",
                "## Features",
                "## Download and Install",
                "## First Launch",
                "## Platform Compatibility",
                "## User Data and Configuration",
                "## Build from Source",
                "## Development and Testing",
                "## Documentation",
                "## Contributing",
            ],
            [
                "## Packaging and Release Engineering",
                "## Telemetry",
                "## Plugins and Extensions",
            ],
        ),
        (
            "full",
            [
                "## Why GeoDesk?",
                "## Downloads and Release Channels",
                "## Platform Compatibility",
                "## Architecture",
                "## User Data, Configuration, and Cache",
                "## Project and File Formats",
                "## Plugins and Extensions",
                "## Updates and Release Compatibility",
                "## Portable Mode",
                "## Privacy and Network Behavior",
                "## Telemetry",
                "## Security",
                "## Build from Source",
                "## Packaging and Release Engineering",
                "## Development and Testing",
                "## Backup and Migration",
                "## Troubleshooting and Diagnostics",
                "## Documentation",
            ],
            [],
        ),
    ],
)
def test_desktop_application_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "desktop-application" / profile
    rendered = render_from_config(
        "desktop-application",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert '<h1 align="center">GeoDesk</h1>' in rendered
    assert '<p align="center"><strong>' in rendered
    assert rendered.endswith("\n")
    assert rendered.count("```") % 2 == 0
    for token in required:
        assert token in rendered
    for token in forbidden:
        assert token not in rendered


def test_desktop_application_header_is_centered_and_badged():
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "desktop-application" / profile
        config = load_config(profile_dir / "config.example.yml")
        rendered = render_readme(
            "desktop-application", profile, config, template_root=TEMPLATES
        )
        first_section = rendered.split("\n## ", 1)[0]

        assert '<h1 align="center">' in first_section
        assert '<p align="center"><strong>' in first_section
        assert first_section.count('<p align="center">') >= 3
        assert len(config["badges"]) >= 4
        assert "Release" in {badge["alt"] for badge in config["badges"]} or "Latest release" in {
            badge["alt"] for badge in config["badges"]
        }
        assert any("Platform" in badge["alt"] or "build" in badge["alt"].lower() for badge in config["badges"])
        assert any(badge["alt"] == "License" for badge in config["badges"])
        for badge in config["badges"]:
            assert f'alt="{badge["alt"]}"' in first_section


def test_desktop_application_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "desktop-application" / profile
        outputs[profile] = render_from_config(
            "desktop-application",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_desktop_application_examples_and_previews_track_renderer():
    branding = load_config(BRANDING)

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "desktop-application" / profile
        config = load_config(profile_dir / "config.example.yml")
        rendered = render_readme(
            "desktop-application", profile, config, template_root=TEMPLATES
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")

        branded_config = dict(config)
        branded_config.update(branding)
        branded = render_readme(
            "desktop-application", profile, branded_config, template_root=TEMPLATES
        )
        preview = (PREVIEWS / "desktop-application" / f"{profile}.md").read_text(encoding="utf-8")

        assert example == rendered
        assert preview == branded
        assert branding["logo_path"] in preview
        assert f'width="{branding["logo_width"]}"' in preview


def test_full_desktop_application_keeps_release_and_data_contracts_visible():
    rendered = render_from_config(
        "desktop-application",
        "full",
        TEMPLATES / "desktop-application" / "full" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "signed and notarized" in rendered
    assert "schema version" in rendered
    assert "trusted Python plugins" in rendered
    assert "does not send product-usage telemetry" in rendered
    assert "Backup and Migration" in rendered
