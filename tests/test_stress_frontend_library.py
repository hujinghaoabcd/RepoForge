from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "frontend-library"
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
    base = load_config(TEMPLATES / "frontend-library" / profile / "config.example.yml")
    overrides = load_config(SUITE / case["overrides"])
    config = _deep_merge(base, overrides)
    config.update(load_config(BRANDING))
    return render_readme("frontend-library", profile, config, template_root=TEMPLATES)


def test_frontend_library_stress_cases_render_cleanly():
    branding = load_config(BRANDING)

    for case in _manifest():
        rendered = _render_case(case)
        line_count = len(rendered.splitlines())

        assert case["min_lines"] <= line_count <= case["max_lines"], (case["name"], line_count)
        assert branding["logo_path"] in rendered
        assert f'width="{branding["logo_width"]}"' in rendered
        assert rendered.count("```") % 2 == 0
        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_frontend_library_stress_suite_covers_all_profiles():
    assert {case["profile"] for case in _manifest()} == {"minimal", "standard", "full"}


def test_full_vanilla_library_does_not_invent_framework_or_ssr_support():
    case = next(case for case in _manifest() if case["name"] == "full-vanilla-no-frameworks")
    rendered = _render_case(case)

    assert "## Framework Adapters" not in rendered
    assert "## SSR and Non-Browser Environments" not in rendered
    assert "no React or Vue package" in rendered
    assert "No framework adapter compatibility is claimed" in rendered


def test_css_heavy_widget_keeps_required_style_contract_visible():
    case = next(case for case in _manifest() if case["name"] == "css-heavy-widget")
    rendered = _render_case(case)

    assert "style.css" in rendered
    assert "CSS custom properties" in rendered
    assert "internal class selectors" in rendered.lower()


def test_framework_adapter_keeps_peer_dependency_boundary_visible():
    case = next(case for case in _manifest() if case["name"] == "framework-adapter-plugin")
    rendered = _render_case(case)

    assert "peer dependencies" in rendered
    assert "Vue 3.4+" in rendered
    assert "## Framework Integration" in rendered
