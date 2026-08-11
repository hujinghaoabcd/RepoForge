# Full Django Package Profile

Use this profile for mature or broad reusable Django packages whose integration surface affects several parts of a host project.

## Required public questions

A Full README should answer:

1. Why should a project adopt the package?
2. Which major capabilities are provided?
3. What is the fastest working installation and quick start?
4. Which integration hooks are mandatory or optional?
5. Which settings are operationally important?
6. Does the package own models/migrations?
7. Does it expose admin, frontend, management-command, middleware, backend, or public Python API surfaces?
8. What permission/security boundaries matter?
9. Which Django/Python/database/integration combinations are tested?
10. How is the package tested?
11. What must users review when upgrading?

## Core sections

```text
Why?
Features
Installation
Quick Start
Configuration Reference
Permissions and Security Notes
Compatibility Matrix
Testing
Upgrade Notes
Documentation
Support and Contributing
License
```

## Optional package-surface sections

The template may render these only when the package actually has that surface:

```text
Models and Migrations
Admin Integration
Public Python API
Frontend Integration
Templates / Static Assets
```

This is **not** profile mixing. Minimal, Standard, and Full remain separate templates. The optional blocks prevent Full from claiming package capabilities that do not exist.

## Target

A normal Full README should usually stay below roughly **220 rendered lines**. Exhaustive settings, API symbols, schema details, and migration history belong in docs.
