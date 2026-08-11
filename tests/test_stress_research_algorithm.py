from __future__ import annotations

from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "research-algorithm"
BRANDING = ROOT / "tests" / "branding.yml"


def _manifest() -> list[dict]:
    data = yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))
    return data["cases"]


def _render(case: dict) -> str:
    config = load_config(SUITE / case["config"])
    config.update(load_config(BRANDING))
    return render_readme(
        "research-algorithm",
        case["profile"],
        config,
        template_root=TEMPLATES,
    )


def test_research_algorithm_stress_cases_render_cleanly():
    minimum_lines = {"minimal": 35, "standard": 70, "full": 120}
    logo_url = load_config(BRANDING)["logo_path"]

    for case in _manifest():
        rendered = _render(case)

        line_count = len(rendered.splitlines())
        assert minimum_lines[case["profile"]] <= line_count <= case["max_lines"] + 6, (
            case["name"],
            line_count,
        )
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0
        assert logo_url in rendered

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
        rendered = _render(case)
        assert "## Inputs, Outputs, and Interpretation" in rendered
        assert "## Reproducibility" in rendered
