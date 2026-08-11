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


def test_web_application_stress_suite_covers_all_profiles():
    assert {case["profile"] for case in _manifest()} == {"minimal", "standard", "full"}


def test_full_profile_does_not_invent_distributed_services():
    case = next(case for case in _manifest() if case["name"] == "full-single-process-no-api")
    rendered = _render_case(case)

    assert "## API" not in rendered
    assert "## Authentication and Authorization" not in rendered
    assert "## Background Jobs and Queues" not in rendered
    assert "## File and Object Storage" not in rendered
    assert "## CI/CD" not in rendered
    assert "PostgreSQL" in rendered
    assert "## Backup and Restore" in rendered


def test_multiservice_full_keeps_state_and_worker_boundaries():
    case = next(case for case in _manifest() if case["name"] == "multiservice-geospatial-platform")
    rendered = _render_case(case)

    assert "Redis" in rendered
    assert "Celery" in rendered
    assert "S3-compatible" in rendered
    assert "database and storage bucket" in rendered.lower()


def test_standard_deployment_is_not_the_development_server():
    case = next(case for case in _manifest() if case["name"] == "sqlite-monolith")
    rendered = _render_case(case)

    deployment = rendered.split("## Deployment", 1)[1]
    assert "gunicorn" in deployment
    assert "runserver" not in deployment
