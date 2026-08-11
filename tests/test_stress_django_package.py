from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.renderer import load_config, render_readme


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
SUITE = ROOT / "tests" / "stress" / "django-package"
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
    base = load_config(TEMPLATES / "django-package" / profile / "config.example.yml")
    overrides = load_config(SUITE / case["overrides"])
    config = _deep_merge(base, overrides)
    config.update(load_config(BRANDING))
    return render_readme("django-package", profile, config, template_root=TEMPLATES)


def test_django_package_stress_cases_render_cleanly():
    logo_path = load_config(BRANDING)["logo_path"]

    for case in _manifest():
        rendered = _render_case(case)
        line_count = len(rendered.splitlines())

        assert case["min_lines"] <= line_count <= case["max_lines"], (case["name"], line_count)
        assert logo_path in rendered
        assert "{{" not in rendered
        assert "{%" not in rendered
        assert rendered.count("```") % 2 == 0
        for heading in case["required_sections"]:
            assert heading in rendered, (case["name"], heading)
        for heading in case["forbidden_sections"]:
            assert heading not in rendered, (case["name"], heading)


def test_django_package_stress_suite_covers_all_profiles():
    assert {case["profile"] for case in _manifest()} == {"minimal", "standard", "full"}


def test_middleware_order_is_a_visible_integration_contract():
    case = next(case for case in _manifest() if case["name"] == "middleware-ordering-package")
    rendered = _render_case(case)
    assert "RequestIDMiddleware" in rendered
    assert "near the top" in rendered


def test_permission_backend_keeps_all_required_django_hooks():
    case = next(case for case in _manifest() if case["name"] == "permission-backend-package")
    rendered = _render_case(case)
    assert "AUTHENTICATION_BACKENDS" in rendered
    assert "ObjectPermissionBackend" in rendered
    assert "python manage.py migrate" in rendered


def test_full_profile_does_not_invent_absent_package_surfaces():
    case = next(case for case in _manifest() if case["name"] == "full-middleware-no-models")
    rendered = _render_case(case)
    assert "## Permissions and Security Notes" in rendered
    assert "## Upgrade Notes" in rendered
    assert "## Models and Migrations" not in rendered
    assert "## Admin Integration" not in rendered
    assert "## Public Python API" not in rendered
    assert "## Frontend Integration" not in rendered
    assert "### Templates / Static Assets" not in rendered


def test_full_admin_extension_keeps_migration_permission_and_api_identity():
    case = next(case for case in _manifest() if case["name"] == "full-admin-extension")
    rendered = _render_case(case)
    assert "OperationRun" in rendered
    assert "registry.operation" in rendered
    assert "Permission-gated execution" in rendered
    assert "template overrides" in rendered.lower()
