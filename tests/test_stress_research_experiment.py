from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "research-experiment"
BRANDING = ROOT / "tests" / "branding.yml"


def _manifest() -> list[dict]:
    data = yaml.safe_load((SUITE / "manifest.yml").read_text(encoding="utf-8"))
    return data["cases"]


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
    base = load_config(TEMPLATES / "research-experiment" / profile / "config.example.yml")
    overrides = load_config(SUITE / case["overrides"])
    config = _deep_merge(base, overrides)
    config.update(load_config(BRANDING))
    return render_readme(
        "research-experiment",
        profile,
        config,
        template_root=TEMPLATES,
    )


def test_research_experiment_stress_cases_render_cleanly():
    logo_path = load_config(BRANDING)["logo_path"]

    for case in _manifest():
        rendered = _render_case(case)
        line_count = len(rendered.splitlines())

        assert case["min_lines"] <= line_count <= case["max_lines"], (
            case["name"],
            line_count,
        )
        assert logo_path in rendered
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0

        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_research_experiment_stress_suite_covers_all_profiles():
    profiles = {case["profile"] for case in _manifest()}
    assert profiles == {"minimal", "standard", "full"}


def test_checkpoint_evaluation_does_not_claim_full_training_reproduction():
    case = next(case for case in _manifest() if case["name"] == "checkpoint-first-evaluation")
    rendered = _render_case(case)

    assert "without retraining" in rendered
    assert "does not claim published training time" in rendered
    assert "## Statistical Testing" not in rendered
    assert "## Ablation and Sensitivity Studies" not in rendered


def test_full_stress_case_keeps_seed_baseline_and_artifact_identity():
    case = next(case for case in _manifest() if case["name"] == "multi-seed-baseline-study")
    rendered = _render_case(case)

    assert "42, 43, 44, 45, 46" in rendered
    assert "**MTGNN**" in rendered
    assert "predictions.npz" in rendered
    assert "significance.py" in rendered
    assert "identity.json" in rendered
