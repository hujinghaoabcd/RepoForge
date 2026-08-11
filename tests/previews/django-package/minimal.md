<p align="center">
  <img src="../../../assets/logo.svg" alt="django-audit-panel" width="280">
</p>

# django-audit-panel

**Lightweight model-change auditing for Django projects.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Django](https://img.shields.io/badge/Django-package-green)](#compatibility) [![License](https://img.shields.io/badge/license-BSD--3--Clause-green)](#license)

Installation · Setup · Quick Start · Compatibility

django-audit-panel is a reusable Django application that records selected model changes and exposes a small query API for project code.

## Installation

```bash
python -m pip install django-audit-panel
```

## Setup

### Enable the app

Add the package to the host project's installed applications.

```python
INSTALLED_APPS = [
    ...
    "audit_panel",
]
```

### Apply package migrations

Create the package-owned audit table.

```bash
python manage.py migrate
```

## Quick Start

Register a model for auditing during application startup.

```python
from audit_panel import audit

audit.register("inventory.Product")
```

## Compatibility

Use a supported Django/Python combination listed by the package release. Projects should keep this section explicit rather than relying on transitive dependency resolution.

## License

django-audit-panel is released under the BSD 3-Clause License.
