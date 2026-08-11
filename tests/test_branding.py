from __future__ import annotations

from pathlib import Path

from repoforge.renderer import SUPPORTED_PROFILES, SUPPORTED_TYPES, load_config


ROOT = Path(__file__).resolve().parents[1]
BRANDING = ROOT / "tests" / "branding.yml"
PREVIEWS = ROOT / "tests" / "previews"
TEMPLATES = ROOT / "templates"


def test_canonical_repoforge_logo_exists():
    assert (ROOT / "assets" / "logo.svg").is_file()
    assert not (ROOT / "assets" / "repoforge-logo.png").exists()


def test_repository_readmes_use_canonical_svg_logo():
    for path in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = path.read_text(encoding="utf-8")
        assert 'src="assets/logo.svg"' in text
        assert 'width="280"' in text
        assert "repoforge-logo.png" not in text


def test_all_implemented_previews_use_one_brand_source():
    branding = load_config(BRANDING)
    logo_path = branding["logo_path"]
    logo_width = branding["logo_width"]

    assert logo_path == "../../../assets/logo.svg"
    assert logo_width == 280

    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            preview = PREVIEWS / project_type / f"{profile}.md"
            assert preview.is_file(), (project_type, profile)
            text = preview.read_text(encoding="utf-8")
            assert logo_path in text, (project_type, profile)
            assert f'width="{logo_width}"' in text, (project_type, profile)
            assert "repoforge-logo.png" not in text, (project_type, profile)


def test_user_examples_do_not_force_repoforge_branding():
    for project_type in SUPPORTED_TYPES:
        for profile in SUPPORTED_PROFILES:
            example = TEMPLATES / project_type / profile / "README.example.md"
            if not example.is_file():
                continue
            text = example.read_text(encoding="utf-8")
            assert "../../../assets/logo.svg" not in text
            assert "assets/logo.svg" not in text
