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

RepoForge's own visual previews use a compact, test-only brand layer:

```text
assets/logo.svg
assets/screenshots/repoforge-preview.webp
assets/screenshots/repoforge-workflow.webp
        ↑
tests/branding.yml
```

The preview-relative logo path is `../../../assets/logo.svg`, and the canonical Markdown display width is **160px**. Visual template families also reuse the two committed RepoForge screenshots so preview pages do not depend on missing project-specific placeholder assets.

These image overrides are **preview-only**. User-facing `README.example.md` files stay project-neutral and are free to supply their own `logo_path`, screenshot, method figure, model figure, or demo image.

## Previews

`tests/previews/` answers:

> What does an approved README for this project type and profile look like?

These files are readable finished examples rather than placeholder-heavy fixtures. They are generated through the same renderer used by the CLI and are therefore suitable as golden documentation snapshots.

Regenerate all implemented previews with:

```bash
python scripts/generate_previews.py
```

When the shared logo size or preview-only visual assets change, run:

```bash
python scripts/normalize_branding.py
```

That helper normalizes template/config logo defaults and then regenerates the full preview matrix.

## Stress suites

`tests/stress/` answers:

> Does the template remain coherent when the project shape becomes difficult?

Renderer-backed suites cover all seven families:

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
- Full-profile vanilla frontend libraries with no React/Vue adapter and no SSR guarantee;
- Windows-only desktop tools, Qt scientific workbenches, Electron offline applications, and mature plugin workstations;
- Full-profile desktop applications with no plugins, updater, portable mode, or telemetry.

The final cases protect an important RepoForge rule: **Full means deeper documentation, not fabricated infrastructure or ecosystem capabilities.**

A stress case is passed through the normal renderer. Tests check section contracts, profile separation, code-fence balance, canonical shared branding, rough size limits, and project-type-specific semantic boundaries.

## Test layers

```text
profile contract
      ↓
Jinja template + YAML config
      ↓
renderer tests
      ↓
visible example / golden preview
      ↓
stress configurations
```

The default examples check the normal design target. Stress suites check whether the same design survives edge cases without turning Minimal into Standard, Standard into Full, or Full into a manual that invents project features.
