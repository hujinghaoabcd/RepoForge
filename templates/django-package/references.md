# Django Package README references

This file records reusable patterns from mature Django package repositories. The goal is not to clone any one README, but to identify which information is consistently useful for host-project integration.

## Core external references

### django-filter — compact reusable-app contract

Repository: https://github.com/carltongibson/django-filter

Useful patterns:

- states the reusable Django purpose immediately;
- keeps installation and `INSTALLED_APPS` setup close together;
- gives a small executable-style usage example early;
- documents a versioning/stability policy and supported Django/Python window;
- surfaces an important optional integration (Django REST Framework) without turning the README into the full manual.

RepoForge takeaway: Minimal and Standard should make the first working host-project integration extremely short.

### Django Debug Toolbar — support range, screenshot, and documentation routing

Repository: https://github.com/django-commons/django-debug-toolbar

Useful patterns:

- exposes package/version, test, coverage, documentation, Python, and Django support badges;
- uses a screenshot because the feature is visual;
- states the supported Django range directly;
- calls out a meaningful async/concurrency limitation instead of implying universal support;
- routes detailed installation/configuration to dedicated docs.

RepoForge takeaway: visual packages may need a screenshot, and compatibility limitations belong near the package identity.

### django-allauth — rationale, breadth, demos, and configuration surface

Repository: https://github.com/pennersr/django-allauth

Useful patterns:

- explains why the package exists before listing its broad feature set;
- separates local/social/enterprise authentication capabilities into understandable groups;
- links demos, docs, issue/help channels, and translations prominently;
- makes configuration and security-related capabilities part of the public package story;
- shows why a broad Django package needs more than a short install snippet.

RepoForge takeaway: Full should support a strong `Why?`, broad features, configuration boundaries, security, and optional integrations without becoming a product-deployment README.

### django-import-export — dual admin/programmatic use and extensibility

Repository: https://github.com/django-import-export/django-import-export

Useful patterns:

- distinguishes programmatic usage from Django Admin integration;
- uses media/screenshots for a UI-facing integration;
- organizes a large feature catalogue around user-visible capabilities;
- exposes permissions, supported databases, extensibility, optional Celery integration, testing, docs, security reporting, and release notes;
- provides concrete use cases rather than only API names.

RepoForge takeaway: packages with both Python APIs and admin/UI integration should document both surfaces explicitly.

### django-guardian — multi-step configuration and admin integration

Repository: https://github.com/django-guardian/django-guardian

Useful patterns:

- gives an exact configuration sequence: installed app, authentication backend, migrations;
- follows configuration with a compact working permissions example;
- documents a distinct admin integration path;
- keeps the README focused on how a host project adopts the package.

RepoForge takeaway: `Configuration` should support several named Django integration steps rather than assuming every package only needs `INSTALLED_APPS`.

### django-cors-headers — middleware ordering and security-sensitive settings

Repository: https://github.com/adamchainz/django-cors-headers

Useful patterns:

- publishes explicit Python/Django requirements;
- documents both `INSTALLED_APPS` and middleware insertion;
- explains that middleware order changes correctness;
- separates required configuration from optional settings;
- puts strong warnings next to security-sensitive "allow all" behavior;
- explains interaction with Django's CSRF configuration.

RepoForge takeaway: Django package READMEs must be able to represent ordering constraints and security boundaries, not just package installation.

## Section champions

| README function | Primary reference | RepoForge lesson |
| --- | --- | --- |
| Minimal reusable-app identity | django-filter | one sentence should explain what is reusable and why |
| First setup path | django-filter / django-guardian | installation and Django hooks must be copyable |
| Visual integration | Django Debug Toolbar / django-import-export | screenshots are useful when the package changes admin/UI behavior |
| Rationale / Why | django-allauth | broad packages need a reasoned problem statement |
| Configuration steps | django-guardian / django-cors-headers | support apps, backends, middleware, URLs, migrations, and settings |
| Middleware/order constraints | django-cors-headers | ordering is part of correctness |
| Public API + admin duality | django-import-export | package code and admin UI can be separate surfaces |
| Compatibility/stability | django-filter / Django Debug Toolbar | publish support policy, not vague compatibility claims |
| Permissions/security | django-allauth / django-guardian / django-cors-headers | security-sensitive behavior belongs in the public contract |
| Docs and upgrade routing | django-import-export | README should route detail into maintained documentation |

## RepoForge design decision

A `django-package` README is a **host-project integration contract**:

```text
package identity
      ↓
install
      ↓
Django integration hooks
      ↓
first working usage
      ↓
public package surfaces
      ↓
compatibility + security + upgrades
      ↓
full docs
```

It is different from a `web-application` README, which owns deployment and operation of an application.

## Anti-patterns

Avoid:

- treating a reusable app as if users should run the repository as a standalone website;
- saying only `pip install ...` when middleware, URLs, backends, or migrations are required;
- hiding middleware-order requirements;
- copying a complete settings reference into README;
- documenting package migrations as if the host project should edit or copy them;
- claiming "supports Django" without a tested version policy;
- exposing admin or API views without permission/security notes;
- mixing optional integrations into the mandatory setup path;
- documenting private implementation modules as stable public API;
- turning Full into a complete deployment guide for a host site.
