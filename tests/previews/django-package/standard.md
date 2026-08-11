<p align="center">
  <img src="../../../assets/logo.svg" alt="django-audit-panel" width="280">
</p>

# django-audit-panel

**Reusable model-change auditing with explicit Django integration and query APIs.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Django](https://img.shields.io/badge/Django-5.2%2B-green)](#compatibility) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#compatibility) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#compatibility) [![License](https://img.shields.io/badge/license-BSD--3--Clause-green)](#license)

Features · Installation · Configuration · Quick Start · Docs

## Why django-audit-panel?

Audit requirements are often reimplemented with model signals, ad-hoc history tables, and project-specific admin views. django-audit-panel packages the recurring integration points into one reusable application while keeping registration, retention, and visibility decisions explicit.

## Features

- **Explicit model registration** — audit only the models a project opts into.
- **Structured audit entries** — record actor, action, object identity, and selected field changes.
- **Admin integration** — inspect history without building a custom back-office screen.
- **Query API** — retrieve audit events from application code without coupling to admin views.

## Installation

Install the package into the same environment as the host Django project.

```bash
python -m pip install django-audit-panel
```

## Configuration

### `INSTALLED_APPS`

Enable the reusable application.

```python
INSTALLED_APPS = [
    ...
    "audit_panel",
]
```

### URLs

Include the optional history views when the project wants browser-accessible audit pages.

```python
from django.urls import include, path

urlpatterns = [
    path("audit/", include("audit_panel.urls")),
]
```

### Migrations

Create or update the package-owned database schema.

```bash
python manage.py migrate
```

### Settings

| Setting | Default | Purpose |
| --- | --- | --- |
| `AUDIT_PANEL_RETENTION_DAYS` | `365` | number of days retained by the cleanup command. |
| `AUDIT_PANEL_TRACK_M2M` | `False` | opt into many-to-many change recording. |

## Quick Start

Register an audited model in an application configuration and then use the normal Django ORM.

```python
from django.apps import AppConfig
from audit_panel import audit

class InventoryConfig(AppConfig):
    name = "inventory"

    def ready(self):
        audit.register("inventory.Product")
```

## Usage Examples

### Query recent events

Query package records from normal application code.

```python
from audit_panel.models import AuditEntry

recent = AuditEntry.objects.for_object(product).order_by("-created_at")[:20]
```

### Prune expired history

Apply the configured retention policy from a scheduled job.

```bash
python manage.py audit_panel_prune
```

## Compatibility

The package should publish a tested compatibility window instead of saying only "works with Django".

| Django | Python | Status |
| --- | --- | --- |
| 5.2 | 3.11–3.14 | supported |
| 6.0 | 3.12–3.14 | supported |

## Documentation

- **Getting Started:** docs/getting-started.md — installation and first integration
- **Configuration:** docs/configuration.md — settings and registration options
- **API:** docs/api.md — public Python interfaces

## Contributing

Contributions are welcome. Run the package test matrix against supported Django/Python combinations before opening a pull request.

## License

django-audit-panel is released under the BSD 3-Clause License.
