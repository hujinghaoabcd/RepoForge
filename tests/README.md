# RepoForge preview and stress tests

This directory is the visual and regression-test area for RepoForge templates.

RepoForge models README generation along two axes:

- **project type**: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, `frontend-library`, `desktop-application`;
- **profile**: `minimal`, `standard`, `full`.

That gives **21 independent preview combinations**.

## Rule: profiles are separate artifacts

`minimal`, `standard`, and `full` are not three conditional views inside one preview file. Each implemented profile has its own template, rendered example, configuration, and visible preview.

For example:

```text
templates/django-package/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   ├── README.example.md
│   └── config.example.yml
├── standard/
└── full/

tests/previews/django-package/
├── minimal.md
├── standard.md
└── full.md
```

The same separation is required for every project type.

## Shared preview branding

RepoForge's own visual previews and stress renders use one test-only brand source:

```text
assets/logo.svg
        ↑
tests/branding.yml
```

The preview-relative path is `../../../assets/logo.svg`. User-facing `README.example.md` files do **not** force this brand asset; normal project configs remain free to supply their own `logo_path`.

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
│   ├── manifest.yml
│   └── cases/
├── research-algorithm/
│   ├── manifest.yml
│   └── cases/
├── research-experiment/
│   ├── manifest.yml
│   └── cases/
└── django-package/
    ├── manifest.yml
    └── cases/
```

Stress cases deliberately cover edge shapes such as:

- extremely small but complete scientific packages;
- broad method catalogues and theory-heavy software;
- estimand-heavy original methods and learned scientific geometry;
- one-command paper reproduction and checkpoint-first evaluation;
- multi-dataset, multi-baseline, multi-seed experiment repositories;
- tiny Django template-tag applications;
- Django middleware where ordering changes correctness;
- authorization backends requiring multiple host-project hooks;
- broad Admin extensions with models, migrations, APIs, templates, and permissions;
- Full-profile Django middleware packages with **no models, migrations, admin, or frontend surface**.

The last case protects an important RepoForge rule: **Full means deeper documentation, not fabricated capabilities.**

A stress case is passed through the normal renderer. Tests check section contracts, profile separation, unresolved Jinja, code-fence balance, canonical preview branding, rough size limits, and project-type-specific semantic boundaries.

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

Committed previews are checked for the canonical RepoForge SVG path, while template-family tests keep examples aligned with actual renderer output.
