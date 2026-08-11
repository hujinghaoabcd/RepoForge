from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "web-application"
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
    base = load_config(TEMPLATES / "web-application" / profile / "config.example.yml")
    overrides = load_config(SUITE / case["overrides"])
    config = _deep_merge(base, overrides)
    config.update(load_config(BRANDING))
    return render_readme("web-application", profile, config, template_root=TEMPLATES)


def test_web_application_stress_cases_render_cleanly():
    logo_path = load_config(BRANDING)["logo_path"]

    for case in _manifest():
        rendered = _render_case(case)
        line_count = len(rendered.splitlines())

        assert case["min_lines"] <= line_count <= case["max_lines"], (case["name"], line_count)
        assert logo_path in rendered
        assert rendered.count("```") % 2 == 0

        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_web_application_stress_suite_covers_all_profiles():
    assert {case["profile"] for case in _manifest()} == {"minimal", "standard", "full"}


def test_full_monolith_does_not_invent_optional_services():
    case = next(
        case for case in _manifest()
        if case["name"] == "full-monolith-no-optional-services"
    )
    rendered = _render_case(case)

    assert "## Authentication and Authorization" in rendered
    assert "## Public API / Webhooks" not in rendered
    assert "## Background Jobs and Queues" not in rendered
    assert "## Object Storage / Media" not in rendered
    assert "## Search" not in rendered
    assert "## Email" not in rendered


def test_multiservice_case_keeps_operator_contract():
    case = next(case for case in _manifest() if case["name"] == "self-hosted-multiservice")
    rendered = _render_case(case)

    assert "## Background Jobs and Queues" in rendered
    assert "## Object Storage / Media" in rendered
    assert "## Public API / Webhooks" in rendered
    assert "PostgreSQL and object storage must be backed up together" in rendered


def test_minimal_case_does_not_grow_into_developer_manual():
    case = next(case for case in _manifest() if case["name"] == "tiny-internal-dashboard")
    rendered = _render_case(case)

    assert "## Architecture" not in rendered
    assert "## Testing" not in rendered
    assert "## CI/CD" not in rendered
    assert "No database or persistent application state is required." in rendered
