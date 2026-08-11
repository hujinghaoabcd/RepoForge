# RepoForge preview and stress tests

This directory is the visual and regression-test area for RepoForge templates.

RepoForge models README generation along two axes:

- **project type**: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, `frontend-library`, `desktop-application`;
- **profile**: `minimal`, `standard`, `full`.

That gives **21 independent preview combinations**.

## Rule: profiles are separate artifacts

`minimal`, `standard`, and `full` are separate templates, configurations, rendered examples, and visible previews. They are not three conditional views inside one giant file.

## Shared preview branding

RepoForge previews and stress renders use one test-only brand source:

```text
assets/logo.svg
        ↑
tests/branding.yml
```

The preview-relative path is `../../../assets/logo.svg`, and the shared Markdown display width is **280px**. User-facing examples remain free to supply their own branding.

## Previews

`tests/previews/` answers:

> What does an approved README for this project type and profile look like?

The committed previews are readable rendered outputs rather than placeholder-heavy fixtures.

## Stress suites

All seven renderer families have stress suites:

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
├── django-package/
├── web-application/
├── frontend-library/
└── desktop-application/
```

Stress cases deliberately cover edge shapes such as:

- extremely small and broad scientific packages;
- estimand-heavy original methods and learned scientific geometry;
- one-command reproduction and multi-seed experiment repositories;
- Django middleware/backends without the usual model/admin surface;
- web monoliths without API, queue, object storage, search, or email services;
- frontend libraries without React/Vue adapters or SSR guarantees;
- Windows-only desktop utilities;
- Qt scientific workbenches and Electron offline editors;
- mature plugin-capable desktop workstations;
- Full Windows desktop applications with no plugins, updater, portable mode, or telemetry.

The edge cases protect one important rule: **Full means deeper documentation, not fabricated infrastructure, ecosystem integrations, platforms, or product capabilities.**

Desktop tests additionally lock the top-of-README visual contract: project title, tagline, badge group, and navigation must remain centered, while RepoForge preview branding remains 280px.

## Test layers

```text
profile contract
      ↓
Jinja template + YAML config
      ↓
renderer tests
      ↓
visible example / preview
      ↓
stress configurations
```

Stress cases pass through the normal renderer. Tests check section contracts, profile separation, code-fence balance, canonical branding, rough size limits, and family-specific semantic boundaries.

## Preview generation

Regenerate previews with:

```bash
python scripts/generate_previews.py
```

Committed previews are checked against the canonical RepoForge SVG path and configured logo width, while family tests keep examples aligned with renderer output.
