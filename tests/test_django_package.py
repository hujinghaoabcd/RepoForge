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
            ["## Installation", "## Setup", "## Quick Start", "## Compatibility", "## License"],
            ["## Features", "## Configuration", "## Permissions and Security Notes", "## Upgrade Notes"],
        ),
        (
            "standard",
            ["## Why django-audit-panel?", "## Features", "## Configuration", "## Usage Examples", "## Compatibility", "## Documentation"],
            ["## Models and Migrations", "## Public Python API", "## Permissions and Security Notes", "## Upgrade Notes"],
        ),
        (
            "full",
            ["## Why django-audit-panel?", "## Configuration Reference", "## Models and Migrations", "## Admin Integration", "## Public Python API", "## Frontend Integration", "## Permissions and Security Notes", "## Compatibility Matrix", "## Testing", "## Upgrade Notes"],
            [],
        ),
    ],
)
def test_django_package_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "django-package" / profile
    rendered = render_from_config(
        "django-package",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    header = rendered.split("\n## ", 1)[0]
    assert rendered.startswith('<div align="center">')
    assert "# django-audit-panel" in header
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


def test_django_package_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "django-package" / profile
        outputs[profile] = render_from_config(
            "django-package",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_standard_django_package_exposes_multiple_integration_hooks():
    rendered = render_from_config(
        "django-package",
        "standard",
        TEMPLATES / "django-package" / "standard" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "### `INSTALLED_APPS`" in rendered
    assert "### URLs" in rendered
    assert "### Migrations" in rendered
    assert "AUDIT_PANEL_RETENTION_DAYS" in rendered


def test_full_django_package_keeps_host_project_boundaries_visible():
    rendered = render_from_config(
        "django-package",
        "full",
        TEMPLATES / "django-package" / "full" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "Host projects should not edit package migrations" in rendered
    assert "AUDIT_PANEL_REDACT_FIELDS" in rendered
    assert "host project's authentication or authorization policy" in rendered
    assert "Django REST Framework" in rendered
    assert "tox" in rendered


def test_django_package_examples_and_previews_track_renderer():
    branding = load_config(BRANDING)

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "django-package" / profile
        config = load_config(profile_dir / "config.example.yml")
        rendered = render_readme(
            "django-package", profile, config, template_root=TEMPLATES
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")

        branded_config = dict(config)
        branded_config.update(branding)
        branded = render_readme(
            "django-package", profile, branded_config, template_root=TEMPLATES
        )
        preview = (PREVIEWS / "django-package" / f"{profile}.md").read_text(encoding="utf-8")

        assert example == rendered
        assert preview == branded
        assert branding["logo_path"] in preview
        assert f'width="{branding["logo_width"]}"' in preview
