from __future__ import annotations

import re
from pathlib import Path

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config


ROOT = Path(__file__).resolve().parents[1]
BRANDING = ROOT / "tests" / "branding.yml"
PREVIEWS = ROOT / "tests" / "previews"
TEMPLATES = ROOT / "templates"
PLACEHOLDER = "../../../assets/placeholders/screenshot.svg"


def test_canonical_repoforge_assets_exist():
    assert (ROOT / "assets" / "logo.svg").is_file()
    assert (ROOT / "assets" / "placeholders" / "screenshot.svg").is_file()
    assert not (ROOT / "assets" / "repoforge-logo.png").exists()


def test_repository_readmes_use_compact_header_and_content_placeholder():
    for path in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = path.read_text(encoding="utf-8")
        assert 'src="assets/logo.svg"' in text
        assert 'width="160"' in text
        assert '<h1 align="center">RepoForge</h1>' in text
        assert 'src="assets/placeholders/screenshot.svg"' in text
        assert "assets/screenshots/repoforge-preview.webp" not in text
        assert "assets/screenshots/repoforge-workflow.webp" not in text
        assert "templates-21" in text

        header_end = text.index("---")
        placeholder_at = text.index('src="assets/placeholders/screenshot.svg"')
        assert placeholder_at > header_end


def test_all_previews_use_unified_centered_header():
    branding = load_config(BRANDING)
    logo_path = branding["logo_path"]
    logo_width = branding["logo_width"]

    assert logo_path == "../../../assets/logo.svg"
    assert logo_width == 160

    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            preview = PREVIEWS / project_type / f"{profile}.md"
            assert preview.is_file(), (project_type, profile)
            text = preview.read_text(encoding="utf-8")

            assert text.lstrip().startswith('<div align="center">'), (project_type, profile)
            assert logo_path in text, (project_type, profile)
            assert f'width="{logo_width}"' in text, (project_type, profile)
            assert "repoforge-logo.png" not in text, (project_type, profile)

            header_end = text.index("</div>")
            header = text[:header_end]
            assert "# " in header, (project_type, profile)
            assert "img.shields.io" in header or "actions/workflows" in header, (
                project_type,
                profile,
            )


def test_preview_media_uses_only_neutral_placeholder_and_lives_in_content():
    branding = load_config(BRANDING)
    approved_local_images = {branding["logo_path"], PLACEHOLDER}

    assert branding["method_figure"] == PLACEHOLDER
    assert branding["figure_path"] == PLACEHOLDER
    assert branding["screenshot_path"] == PLACEHOLDER
    assert branding["demo_image"] == PLACEHOLDER

    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            text = (PREVIEWS / project_type / f"{profile}.md").read_text(encoding="utf-8")
            header_end = text.index("</div>")

            for src in re.findall(r'src="([^"]+)"', text):
                if src.startswith(("http://", "https://")):
                    continue
                assert src in approved_local_images, (project_type, profile, src)

            if PLACEHOLDER in text:
                media_at = text.index(PLACEHOLDER)
                assert media_at > header_end, (project_type, profile)
                assert text.rfind("## ", header_end, media_at) != -1, (project_type, profile)


def test_visual_families_use_neutral_placeholder_in_full_preview():
    visual_families = {
        "research-algorithm",
        "research-experiment",
        "django-package",
        "web-application",
        "frontend-library",
        "desktop-application",
    }
    for project_type in visual_families:
        text = (PREVIEWS / project_type / "full.md").read_text(encoding="utf-8")
        assert PLACEHOLDER in text, project_type


def test_user_examples_do_not_force_repoforge_branding_or_placeholder():
    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            example = TEMPLATES / project_type / profile / "README.example.md"
            if not example.is_file():
                continue
            text = example.read_text(encoding="utf-8")
            assert "../../../assets/logo.svg" not in text
            assert "assets/logo.svg" not in text
            assert "assets/placeholders/screenshot.svg" not in text
            assert "repoforge-preview.webp" not in text
            assert "repoforge-workflow.webp" not in text
