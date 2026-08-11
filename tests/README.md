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
templates/research-algorithm/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   ├── README.example.md
│   └── config.example.yml
├── standard/
└── full/

tests/previews/research-algorithm/
├── minimal.md
├── standard.md
└── full.md
```

The same separation should be used for every project type.

## Shared preview branding

RepoForge's own visual previews and stress renders use one test-only brand source:

```text
assets/logo.svg
        ↑
tests/branding.yml
```

The preview-relative path is `../../../assets/logo.svg`. User-facing `README.example.md` files do **not** force this brand asset; normal project configs remain free to supply their own `logo_path`.

## Previews

`tests/previews/` answers a visual question:

> What does an approved README for this project type and profile look like?

These files are intentionally readable as finished README examples rather than test fixtures full of placeholders.

## Stress suites

`tests/stress/` answers a different question:

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
└── research-experiment/
    ├── manifest.yml
    └── cases/
```

Stress cases deliberately cover edge shapes such as:

- extremely small but complete packages;
- broad method catalogues;
- pre-1.0 projects;
- theory-heavy software;
- estimand-heavy original methods;
- learned scientific geometry;
- nonlinear space-time formulations;
- one-command paper reproduction;
- checkpoint-first evaluation without retraining claims;
- compact multi-dataset benchmarks;
- full multi-baseline, five-seed, ablation, significance, and artifact-identity studies.

A stress case is passed through the normal renderer. Scientific-package and original-method suites use complete YAML cases; the experiment suite uses small override files merged onto the corresponding canonical profile config. Tests check section contracts, profile separation, unresolved Jinja, code-fence balance, branding, and rough size limits.

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

The default example checks the normal design target. Stress suites check whether the same design survives edge cases without turning Minimal into Standard, Standard into Full, or Full into a package manual or paper manuscript.

## Preview generation

For implemented template families, previews can be regenerated with:

```bash
python scripts/generate_previews.py
```

The committed previews are also checked for the canonical RepoForge SVG path. Template-family tests keep examples and generated profile structure aligned.
