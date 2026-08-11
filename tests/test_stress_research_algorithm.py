from __future__ import annotations

from pathlib import Path

import yaml

from repoforge.renderer import render_from_config


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "research-algorithm"


def _manifest() -> list[dict]:
    data = yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))
    return data["cases"]


def test_research_algorithm_stress_cases_render_cleanly():
    minimum_lines = {"minimal": 35, "standard": 70, "full": 120}

    for case in _manifest():
        rendered = render_from_config(
            "research-algorithm",
            case["profile"],
            SUITE / case["config"],
            template_root=TEMPLATES,
        )

        line_count = len(rendered.splitlines())
        assert minimum_lines[case["profile"]] <= line_count <= case["max_lines"], (
            case["name"],
            line_count,
        )
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0

        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_research_algorithm_stress_suite_covers_all_profiles():
    profiles = {case["profile"] for case in _manifest()}
    assert profiles == {"minimal", "standard", "full"}


def test_research_algorithm_stress_suite_has_distinct_method_shapes():
    cases = _manifest()
    assert len(cases) >= 4
    assert len({case["name"] for case in cases}) == len(cases)


def test_novelty_does_not_force_full_profile():
    cases = {case["name"]: case for case in _manifest()}
    assert cases["single-novel-estimator"]["profile"] == "minimal"
    assert cases["estimand-heavy-spatial-explanation"]["profile"] == "standard"


def test_full_cases_keep_interpretation_contracts_visible():
    for case in _manifest():
        if case["profile"] != "full":
            continue
        rendered = render_from_config(
            "research-algorithm",
            case["profile"],
            SUITE / case["config"],
            template_root=TEMPLATES,
        )
        assert "## Inputs, Outputs, and Interpretation" in rendered
        assert "## Reproducibility" in rendered
