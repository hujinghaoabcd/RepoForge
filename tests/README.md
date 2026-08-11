# RepoForge preview and stress tests

This directory is the visual and regression-test area for RepoForge templates.

RepoForge models README generation along two axes:

- **project type**: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, `frontend-library`, `desktop-application`;
- **profile**: `minimal`, `standard`, `full`.

That gives **21 independent preview combinations**.

## Rule: profiles are separate artifacts

`minimal`, `standard`, and `full` are not three conditional views inside one preview file. Each implemented profile has its own template, rendered example, configuration, and visible preview.

The same separation is required for every project type.

## Shared preview branding

RepoForge's own visual previews and stress renders use one test-only brand source:

```text
assets/logo.svg
        ↑
tests/branding.yml
```

The preview-relative path is `../../../assets/logo.svg`, and the current shared Markdown display width is **280px**. User-facing `README.example.md` files do **not** force this brand asset; normal project configs remain free to supply their own `logo_path`.

## Previews

`tests/previews/` answers:

> What does an approved README for this project type and profile look like?

These files are readable finished examples rather than placeholder-heavy fixtures.

## Stress suites

`tests/stress/` answers:

> Does the template remain coherent when the project shape becomes difficult?

Current renderer-backed suites include:

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
├── django-package/
├── web-application/
└── frontend-library/
```

Stress cases deliberately cover edge shapes such as:

- extremely small but complete scientific packages;
- broad method catalogues and theory-heavy software;
- estimand-heavy original methods and learned scientific geometry;
- one-command paper reproduction and checkpoint-first evaluation;
- multi-dataset, multi-baseline, multi-seed experiment repositories;
- tiny Django template-tag applications and middleware ordering constraints;
- authorization backends and broad Admin extensions;
- Full-profile Django middleware packages with no models or admin surface;
- tiny internal web dashboards, server-rendered monoliths, split frontend/API systems, and self-hosted multi-service applications;
- Full-profile web monoliths with no API, queue, object storage, search, or email service;
- tiny DOM utilities and CSS-heavy frontend widgets;
- framework adapter packages with explicit peer dependencies;
- multi-package UI toolkits with TypeScript, SSR, tree-shaking, and accessibility contracts;
- Full-profile vanilla frontend libraries with no React/Vue adapter and no SSR guarantee.

The final cases protect an important RepoForge rule: **Full means deeper documentation, not fabricated infrastructure or ecosystem capabilities.**

A stress case is passed through the normal renderer. Tests check section contracts, profile separation, code-fence balance, canonical 280px preview branding, rough size limits, and project-type-specific semantic boundaries.

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

The default example checks the normal design target. Stress suites check whether the same design survives edge cases without turning Minimal into Standard, Standard into Full, or Full into a manual that invents project features.

## Preview generation

For implemented template families, regenerate previews with:

```bash
python scripts/generate_previews.py
```

Committed previews are checked for the canonical RepoForge SVG path and configured logo width, while template-family tests keep examples aligned with actual renderer output.
