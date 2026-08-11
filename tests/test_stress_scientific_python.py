from __future__ import annotations

from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "scientific-python"
BRANDING = ROOT / "tests" / "branding.yml"


def _manifest() -> list[dict]:
    data = yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))
    return data["cases"]


def _render(case: dict) -> str:
    config = load_config(SUITE / case["config"])
    config.update(load_config(BRANDING))
    return render_readme(
        "scientific-python",
        case["profile"],
        config,
        template_root=TEMPLATES,
    )


def test_scientific_python_stress_cases_render_cleanly():
    logo_url = load_config(BRANDING)["logo_path"]

    for case in _manifest():
        rendered = _render(case)

        line_count = len(rendered.splitlines())
        assert case["min_lines"] <= line_count <= case["max_lines"] + 6, (
            case["name"],
            line_count,
        )
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0
        assert logo_url in rendered

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
