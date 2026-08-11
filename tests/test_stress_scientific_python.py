from __future__ import annotations

from pathlib import Path

import yaml

from repoforge.renderer import render_from_config


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "scientific-python"


def _manifest() -> list[dict]:
    data = yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))
    return data["cases"]


def test_scientific_python_stress_cases_render_cleanly():
    for case in _manifest():
        rendered = render_from_config(
            "scientific-python",
            case["profile"],
            SUITE / case["config"],
            template_root=TEMPLATES,
        )

        line_count = len(rendered.splitlines())
        assert case["min_lines"] <= line_count <= case["max_lines"], (
            case["name"],
            line_count,
        )
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0

        for token in case["must_have"]:
            assert token in rendered, (case["name"], token)
        for token in case["must_not_have"]:
            assert token not in rendered, (case["name"], token)


def test_stress_suite_covers_all_scientific_python_profiles():
    profiles = {case["profile"] for case in _manifest()}
    assert profiles == {"minimal", "standard", "full"}


def test_stress_suite_has_multiple_distinct_package_shapes():
    cases = _manifest()
    assert len(cases) >= 5
    assert len({case["name"] for case in cases}) == len(cases)
