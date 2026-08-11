from __future__ import annotations

import re
from pathlib import Path

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config


ROOT = Path(__file__).resolve().parents[1]
BRANDING = ROOT / "tests" / "branding.yml"
PREVIEWS = ROOT / "tests" / "previews"
TEMPLATES = ROOT / "templates"


def test_canonical_repoforge_assets_exist():
    assert (ROOT / "assets" / "logo.svg").is_file()
    assert (ROOT / "assets" / "screenshots" / "repoforge-preview.webp").is_file()
    assert (ROOT / "assets" / "screenshots" / "repoforge-workflow.webp").is_file()
    assert not (ROOT / "assets" / "repoforge-logo.png").exists()


def test_repository_readmes_use_compact_centered_header_and_real_screenshots():
    for path in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = path.read_text(encoding="utf-8")
        assert 'src="assets/logo.svg"' in text
        assert 'width="160"' in text
        assert '<h1 align="center">RepoForge</h1>' in text
        assert 'src="assets/screenshots/repoforge-preview.webp"' in text
        assert 'src="assets/screenshots/repoforge-workflow.webp"' in text
        assert "templates-21" in text
        assert "repoforge-logo.png" not in text


def test_all_previews_use_compact_shared_brand_source():
    branding = load_config(BRANDING)
    logo_path = branding["logo_path"]
    logo_width = branding["logo_width"]

    assert logo_path == "../../../assets/logo.svg"
    assert logo_width == 160

    approved_local_images = {
        logo_path,
        branding["method_figure"],
        branding["figure_path"],
        branding["screenshot_path"],
        branding["demo_image"],
    }

    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            preview = PREVIEWS / project_type / f"{profile}.md"
            assert preview.is_file(), (project_type, profile)
            text = preview.read_text(encoding="utf-8")
            assert logo_path in text, (project_type, profile)
            assert f'width="{logo_width}"' in text, (project_type, profile)
            assert "repoforge-logo.png" not in text, (project_type, profile)

            for src in re.findall(r'src="([^"]+)"', text):
                if src.startswith(("http://", "https://")):
                    continue
                assert src in approved_local_images, (project_type, profile, src)


def test_visual_families_use_uploaded_preview_assets():
    expected = {
        "research-algorithm": "../../../assets/screenshots/repoforge-workflow.webp",
        "research-experiment": "../../../assets/screenshots/repoforge-workflow.webp",
        "django-package": "../../../assets/screenshots/repoforge-preview.webp",
        "web-application": "../../../assets/screenshots/repoforge-preview.webp",
        "frontend-library": "../../../assets/screenshots/repoforge-preview.webp",
        "desktop-application": "../../../assets/screenshots/repoforge-preview.webp",
    }
    for project_type, image in expected.items():
        text = (PREVIEWS / project_type / "full.md").read_text(encoding="utf-8")
        assert image in text, project_type


def test_user_examples_do_not_force_repoforge_branding():
    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            example = TEMPLATES / project_type / profile / "README.example.md"
            if not example.is_file():
                continue
            text = example.read_text(encoding="utf-8")
            assert "../../../assets/logo.svg" not in text
            assert "assets/logo.svg" not in text
            assert "repoforge-preview.webp" not in text
            assert "repoforge-workflow.webp" not in text
