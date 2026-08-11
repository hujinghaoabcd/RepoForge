from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "desktop-application"
BRANDING = ROOT / "tests" / "branding.yml"


def _manifest() -> list[dict]:
    return yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))["cases"]


def _deep_merge(base: dict, overrides: dict) -> dict:
    merged = deepcopy(base)
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged


def _render_case(case: dict) -> str:
    profile = case["profile"]
    base = load_config(TEMPLATES / "desktop-application" / profile / "config.example.yml")
    overrides = load_config(SUITE / case["overrides"])
    config = _deep_merge(base, overrides)
    config.update(load_config(BRANDING))
    return render_readme("desktop-application", profile, config, template_root=TEMPLATES)


def test_desktop_application_stress_cases_render_cleanly():
    branding = load_config(BRANDING)

    for case in _manifest():
        rendered = _render_case(case)
        line_count = len(rendered.splitlines())
        header = rendered.split("\n## ", 1)[0]

        assert case["min_lines"] <= line_count <= case["max_lines"], (case["name"], line_count)
        assert branding["logo_path"] in rendered
        assert f'width="{branding["logo_width"]}"' in rendered
        assert header.startswith('<div align="center">')
        assert "img.shields.io" in header
        assert "</div>" in header
        assert rendered.count("```") % 2 == 0
        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_desktop_application_stress_suite_covers_all_profiles():
    assert {case["profile"] for case in _manifest()} == {"minimal", "standard", "full"}


def test_windows_only_utility_does_not_invent_other_platforms():
    case = next(case for case in _manifest() if case["name"] == "windows-only-utility")
    rendered = _render_case(case)

    assert "Windows 11 x64" in rendered
    assert "macOS" not in rendered
    assert "Linux" not in rendered


def test_full_windows_application_does_not_invent_desktop_capabilities():
    case = next(case for case in _manifest() if case["name"] == "full-windows-no-plugins")
    rendered = _render_case(case)

    assert "## Plugins and Extensions" not in rendered
    assert "## Updates and Release Compatibility" not in rendered
    assert "## Portable Mode" not in rendered
    assert "## Telemetry" not in rendered
    assert "only supported desktop operating system" in rendered
    assert "signed x64 installer" in rendered


def test_desktop_badges_remain_inside_centered_header():
    for case in _manifest():
        rendered = _render_case(case)
        header = rendered.split("\n## ", 1)[0]
        assert header.startswith('<div align="center">')
        assert "img.shields.io" in header
        assert header.index("img.shields.io") < header.index("</div>")
