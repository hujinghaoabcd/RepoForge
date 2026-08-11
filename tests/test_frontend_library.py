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
            ["## Install", "## Quick Start", "## Browser Support"],
            ["## API Overview", "## Framework Integration", "## Bundle and Tree-Shaking"],
        ),
        (
            "standard",
            [
                "## Why MapWidget?",
                "## Features",
                "## Installation",
                "## Quick Start",
                "## API Overview",
                "## Styling and Theming",
                "## Framework Integration",
                "## Compatibility",
                "## Development and Testing",
            ],
            ["## Packages and Installation", "## SSR and Non-Browser Environments", "## Accessibility"],
        ),
        (
            "full",
            [
                "## Packages and Installation",
                "## Events and Lifecycle",
                "## Styling, Themes, and CSS Contract",
                "## Framework Adapters",
                "## TypeScript Support",
                "## Bundle and Tree-Shaking",
                "## SSR and Non-Browser Environments",
                "## Browser Compatibility",
                "## Accessibility",
                "## Release and Versioning Policy",
            ],
            [],
        ),
    ],
)
def test_frontend_library_profiles_render(profile, required, forbidden):
    profile_dir = TEMPLATES / "frontend-library" / profile
    rendered = render_from_config(
        "frontend-library",
        profile,
        profile_dir / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert rendered.startswith("# MapWidget")
    assert rendered.endswith("\n")
    assert rendered.count("```") % 2 == 0
    for token in required:
        assert token in rendered
    for token in forbidden:
        assert token not in rendered


def test_frontend_library_profiles_have_distinct_depth():
    outputs = {}
    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "frontend-library" / profile
        outputs[profile] = render_from_config(
            "frontend-library",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )

    assert len(outputs["minimal"].splitlines()) < len(outputs["standard"].splitlines())
    assert len(outputs["standard"].splitlines()) < len(outputs["full"].splitlines())


def test_frontend_library_examples_and_previews_track_renderer():
    branding = load_config(BRANDING)

    for profile in ("minimal", "standard", "full"):
        profile_dir = TEMPLATES / "frontend-library" / profile
        rendered = render_from_config(
            "frontend-library",
            profile,
            profile_dir / "config.example.yml",
            template_root=TEMPLATES,
        )
        example = (profile_dir / "README.example.md").read_text(encoding="utf-8")
        preview = (PREVIEWS / "frontend-library" / f"{profile}.md").read_text(encoding="utf-8")

        assert example == rendered
        assert branding["logo_path"] in preview
        assert f'width="{branding["logo_width"]}"' in preview
        assert preview.rstrip().endswith(rendered.rstrip())


def test_full_frontend_library_keeps_distribution_contracts_visible():
    rendered = render_from_config(
        "frontend-library",
        "full",
        TEMPLATES / "frontend-library" / "full" / "config.example.yml",
        template_root=TEMPLATES,
    )

    assert "peer dependency" in rendered
    assert "tree-shake" in rendered
    assert "client mount" in rendered
    assert "Semantic Versioning" in rendered
    assert "keyboard" in rendered.lower()
