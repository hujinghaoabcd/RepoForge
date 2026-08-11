<p align="center">
  <img src="../../../assets/logo.svg" alt="django-audit-panel" width="280">
</p>

# django-audit-panel

**A production-oriented reusable Django auditing application with admin, API, retention, and integration contracts.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Django](https://img.shields.io/badge/Django-tested-green)](#compatibility-matrix) [![Python](https://img.shields.io/badge/Python-tested-blue)](#compatibility-matrix) [![Tests](https://img.shields.io/badge/tests-matrix-brightgreen)](#testing) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-BSD--3--Clause-green)](#license)

Why · Features · Setup · API · Security · Compatibility · Upgrade

## Why django-audit-panel?

Auditing is deceptively cross-cutting. A reusable package must coordinate model registration, migrations, admin visibility, request/user attribution, retention, templates, permissions, and stable query APIs without taking ownership of the host project's authentication or authorization policy. django-audit-panel exposes those boundaries explicitly.

## Features

- **Selective audit registration** — opt models and fields into tracking instead of globally recording every change.
- **Actor-aware events** — attach authenticated users or explicit service actors when the host project supplies them.
- **Admin history views** — inspect object events using Django admin permissions.
- **Stable query surface** — consume audit records through documented managers and helper functions.
- **Retention controls** — prune old records with a management command and project-owned scheduling.
- **Optional frontend assets** — provide a small timeline component without replacing the host design system.

## Installation

### Stable install

```bash
python -m pip install django-audit-panel
```

### Optional integrations

```bash
python -m pip install "django-audit-panel[drf]"
```

## Quick Start

Install the app, migrate its database tables, register a model, and use the supplied manager to inspect history.

```python
from audit_panel import audit
from audit_panel.models import AuditEntry

audit.register("inventory.Product", fields=["name", "price"])
history = AuditEntry.objects.for_object(product)
```

## Configuration Reference

### Application Setup

Enable the reusable app.

```python
INSTALLED_APPS = [
    ...
    "audit_panel",
]
```

### URLs

Include the package views only when the host project exposes them.

```python
from django.urls import include, path

urlpatterns = [
    path("audit/", include("audit_panel.urls")),
]
```

### Settings

| Setting | Default | Required | Purpose |
| --- | --- | --- | --- |
| `AUDIT_PANEL_RETENTION_DAYS` | `365` | No | retention window used by the cleanup command. |
| `AUDIT_PANEL_TRACK_M2M` | `False` | No | enable many-to-many event tracking for registered models. |
| `AUDIT_PANEL_ACTOR_RESOLVER` | `request.user` | No | dotted path used to resolve an actor from request context. |
| `AUDIT_PANEL_REDACT_FIELDS` | `[]` | No | field names that must never be persisted in change payloads. |

### Templates / Static Assets

The package ships namespaced templates and static files under `audit_panel/`. Override templates through Django's normal template-loader precedence. Projects that do not expose the bundled views do not need the frontend assets.

## Models and Migrations

`AuditEntry` is package-owned schema and migrations are shipped with the application. Host projects should not edit package migrations. Integrations that require extra domain data should use their own models and references rather than adding columns to `AuditEntry`.

```bash
python manage.py migrate
```

## Admin Integration

Register the supplied mixin only on models whose history should be visible in Django admin. Normal Django model permissions remain the first authorization layer.

```python
from django.contrib import admin
from audit_panel.admin import AuditAdminMixin

@admin.register(Product)
class ProductAdmin(AuditAdminMixin, admin.ModelAdmin):
    audit_fields = ("name", "price")
```

## Public Python API

| API | Purpose | Stability |
| --- | --- | --- |
| `audit.register(...)` | register a model and tracked fields. | public |
| `AuditEntry.objects.for_object(...)` | return events for a model instance. | public |
| `record_event(...)` | create an explicit application/service event. | public |
| `audit_panel.signals.*` | extension hooks for advanced integrations. | advanced / documented |

## Frontend Integration

The optional timeline view uses namespaced templates and static assets. It does not bundle a frontend framework. SPA or API-first projects should use the optional DRF serializer/view integration and render events in their own frontend.

## Permissions and Security Notes

- audit history can contain sensitive values; use `AUDIT_PANEL_REDACT_FIELDS` and avoid tracking secrets, tokens, or password-equivalent material.
- exposing audit views requires explicit host-project authorization; installation alone must not make history public.
- actor attribution is evidence about application context, not proof of real-world identity.
- retention and deletion obligations remain the responsibility of the host project.
- package templates and API endpoints should be reviewed when deploying behind custom authentication middleware or tenant boundaries.

## Compatibility Matrix

Full-profile Django packages should publish a matrix for Django, Python, database, and optional integrations that materially affect behavior.

| Package | Supported / tested range | Notes |
| --- | --- | --- |
| **Django** | 5.2, 6.0 | exercised in CI |
| **Python** | 3.11–3.14 | version support follows the release policy |
| **PostgreSQL** | supported Django versions | primary integration database |
| **SQLite** | supported Django versions | tests and local development |
| **Django REST Framework** | optional | installed only with the `drf` extra |

## Testing

Run the fast package suite locally, then use the declared matrix runner before release.

```bash
python -m pytest
```

```bash
tox
```

## Upgrade Notes

- run `python manage.py migrate` after upgrading whenever the release contains package migrations.
- review release notes for setting renames, deprecated public APIs, and compatibility-window changes.
- template overrides may require review when package markup changes.
- never copy new package migrations into the host project; depend on the released application migrations.

## Documentation

- **Installation:** docs/installation.md — package and host-project setup
- **Configuration Reference:** docs/configuration.md — settings, URLs, templates, and integrations
- **Public API:** docs/api.md — supported Python interfaces and extension points
- **Security:** docs/security.md — sensitive fields, authorization, and deployment boundaries
- **Upgrade Guide:** docs/upgrading.md — migrations, deprecations, and template changes

## Support and Contributing

Report reproducible integration bugs with Django/Python versions and the smallest host-project setup that demonstrates the problem. Contributions should add tests to the relevant compatibility matrix and document any new public setting or API.

## License

django-audit-panel is released under the BSD 3-Clause License.
