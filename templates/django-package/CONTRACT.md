# Django Package Template Contract

This family is for **reusable Django applications, extensions, middleware, authentication/permission backends, admin integrations, and Django-specific libraries** that are installed into another Django project.

Use `django-package` when the README must answer questions such as:

1. What Django problem does this package solve?
2. How is it installed into the host project's Python environment?
3. Which Django integration points are required: `INSTALLED_APPS`, middleware, URLs, authentication backends, templates, static assets, signals, or settings?
4. Does the package ship models or migrations?
5. What is the shortest working host-project setup?
6. Which public Python APIs, admin mixins, template tags, management commands, or optional integrations are supported?
7. Which Django/Python/database combinations are tested?
8. What security, permission, migration, or upgrade boundaries must a host project understand?

Do **not** use this family for a complete Django website or SaaS application whose deployment, frontend, database, observability, and operations belong to one product repository. That belongs to `web-application`.

## Independent profiles

`minimal`, `standard`, and `full` are separate artifacts. Each implemented profile contains:

```text
PROFILE.md
README.template.md
README.example.md
config.example.yml
```

with a matching visible preview under:

```text
tests/previews/django-package/<profile>.md
```

The profiles must not be implemented as one giant conditional README.

## Shared rules

- identify the package as a reusable Django component, not as a standalone site;
- show the shortest valid host-project integration path;
- make Django-specific hooks explicit rather than hiding them behind "configure as needed";
- distinguish package-owned migrations from host-project migrations;
- document middleware ordering, authentication backends, URL inclusion, template/static requirements, or signal registration when they materially affect behavior;
- publish a tested Django/Python compatibility policy;
- keep optional integrations visibly optional;
- treat permissions and security-sensitive settings as public contract when relevant;
- keep public API names and stability clear for packages that are imported from project code;
- document upgrade steps when migrations, templates, settings, or public APIs can change;
- send exhaustive setting inventories, API references, and long migration histories to dedicated documentation.

## Profile selection

### Minimal

Use for a small reusable app or extension with one installation command, a short setup sequence, one representative usage path, and a compact compatibility statement.

### Standard

Default for most maintained Django packages. It should expose:

- why the package exists;
- key features;
- installation;
- configuration/integration steps;
- quick start;
- representative usage;
- Django/Python compatibility;
- documentation and contribution entry points.

### Full

Use when the package has several host-project integration surfaces or operational boundaries, for example:

- models and package migrations;
- admin mixins or custom admin views;
- middleware ordering;
- authentication/permission backends;
- optional REST/API integration;
- bundled templates/static assets;
- security-sensitive configuration;
- multiple databases or optional dependencies;
- a public Python API used by downstream projects;
- compatibility matrices;
- deprecation and upgrade procedures.

## What should remain outside README

Even in Full, move these to dedicated documentation when substantial:

- every setting and every default;
- complete API reference;
- full model/schema documentation;
- all migration operations;
- exhaustive admin customization recipes;
- complete security threat models;
- every supported frontend framework;
- release-by-release changelog history;
- internal maintainer/release notes;
- full test matrix logs.

README should remain the package's **integration contract and landing page**, not the entire Django manual.
