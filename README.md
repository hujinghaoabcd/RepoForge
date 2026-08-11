<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="280">
</p>

<h1 align="center">RepoForge</h1>

<p align="center"><strong>Reusable repository documentation and project standards.</strong></p>

<p align="center">
  <a href="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml"><img src="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="#implemented-template-families"><img src="https://img.shields.io/badge/templates-7%20families-blue" alt="7 template families"></a>
  <a href="#tests"><img src="https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue" alt="Python 3.11–3.13"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

RepoForge applies consistent README and repository-documentation standards to projects that already have their code scaffold. Use Cookiecutter, Scientific Python Cookie, Django templates, Vite, or another generator for project structure; use RepoForge for the public documentation layer.

## Why RepoForge?

Project scaffolds create code structure, but repositories still need a clear public-facing documentation system. RepoForge separates those concerns:

1. scaffold the project with the best tool for the technology stack;
2. select a RepoForge project type and one independent documentation profile;
3. render a readable Markdown README from explicit YAML configuration;
4. keep detailed manuals in `docs/` instead of turning the README into the whole documentation site.

The goal is a recognizable family style without forcing unrelated projects into one README structure.

## Implemented template families

RepoForge now has all **seven initial executable renderer families**, each with independent `minimal`, `standard`, and `full` templates:

```text
scientific-python
├── minimal
├── standard
└── full

research-algorithm
├── minimal
├── standard
└── full

research-experiment
├── minimal
├── standard
└── full

django-package
├── minimal
├── standard
└── full

web-application
├── minimal
├── standard
└── full

frontend-library
├── minimal
├── standard
└── full

desktop-application
├── minimal
├── standard
└── full
```

The profiles are **independent templates**, not conditional views inside one giant README template.

- `scientific-python` — reusable scientific software packages;
- `research-algorithm` — original scientific or technical methods;
- `research-experiment` — paper code, benchmark studies, and reproducibility repositories;
- `django-package` — reusable Django applications and extensions;
- `web-application` — complete deployable browser products and systems;
- `frontend-library` — reusable browser libraries, plugins, components, hooks, and adapters;
- `desktop-application` — installable desktop products for Windows, macOS, Linux, or a deliberate subset of those platforms.

Each family has a contract, reference analysis, profile rules, Jinja templates, YAML example configs, rendered examples, branded previews, renderer tests, and deliberately difficult stress cases.

## Quick start

Install RepoForge from a source checkout:

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

Render a template by project type and profile:

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render research-experiment full \
  --config templates/research-experiment/full/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render web-application full \
  --config templates/web-application/full/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render frontend-library standard \
  --config templates/frontend-library/standard/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render desktop-application standard \
  --config templates/desktop-application/standard/config.example.yml \
  --output README.generated.md
```

The renderer uses strict Jinja configuration validation: missing template variables fail visibly instead of silently producing incomplete documentation.

## Previewing profiles

Approved visual previews live under:

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge's own previews use one repository brand source:

```text
assets/logo.svg
```

The shared preview configuration renders the RepoForge logo at **280 px**. User-facing `README.example.md` files remain brand-neutral so generated projects can supply their own logo and dimensions.

Regenerate previews with:

```bash
python scripts/generate_previews.py
```

## Stress tests

Renderer-backed stress suites now cover all seven families:

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

They deliberately exercise project shapes that make generic README designs fail. Examples include Full web monoliths without queues or APIs, Full vanilla frontend libraries without framework adapters or SSR, and Full Windows desktop applications without plugins, auto-update, portable mode, or telemetry.

These cases protect a core RepoForge rule: **Full means deeper documentation, not fabricated capabilities or infrastructure.**

## Project types

RepoForge's initial matrix contains seven project types:

- `scientific-python` — reusable scientific Python packages;
- `research-algorithm` — original methods and algorithm implementations;
- `research-experiment` — paper code, benchmarks, experiments, and reproducibility;
- `django-package` — reusable Django applications and extensions;
- `web-application` — small to large deployable web applications;
- `frontend-library` — frontend libraries, plugins, and components;
- `desktop-application` — installable desktop software and cross-platform applications.

## Profiles

Profiles control documentation depth, but each profile is a separate artifact.

- **Minimal** — the shortest complete README for a small, focused project.
- **Standard** — the default for most maintained open-source projects.
- **Full** — a deeper landing page for mature projects with broader compatibility, integration, validation, security, deployment, packaging, or upgrade boundaries.

Profile depth is independent from project breadth. A Full project does not have to support every platform, framework, service, adapter, plugin system, or distribution channel.

## Desktop application header contract

Desktop product READMEs make the user-facing product recognizable before build details. Their identity block keeps the following centered:

```text
Logo / application icon
Project name
One-line product description
Release / platform / build / license badges
Download / Docs / Issues navigation
Screenshot when available
```

Desktop Full templates then add only real capabilities such as project formats, plugins, update channels, portable mode, privacy/telemetry, signing, migration, and troubleshooting.

## Repository structure

```text
RepoForge
├── assets/                         # RepoForge brand assets
├── src/repoforge/                  # renderer and CLI
├── templates/                      # project-type/profile templates
├── profiles/                       # cross-project profile rules
├── partials/                       # reusable documentation components
├── tests/
│   ├── previews/                   # approved rendered views
│   └── stress/                     # difficult real-shape configurations
├── scripts/                        # maintenance helpers
└── docs/                           # architecture and standards
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the design.

## Design principles

- **README is an entry point, not the entire manual.**
- **Minimal, Standard, and Full are independent templates.**
- **Project type and documentation depth are separate decisions.**
- **Meaningful badges belong near the project identity rather than being scattered through the README.**
- **Scientific software treats validation, reproducibility, limitations, and citation as first-class concerns.**
- **Experiment repositories make data identity, protocol, seeds, result identity, and reproduction commands explicit.**
- **Django packages make host-project integration hooks, compatibility, migrations, security, and upgrade boundaries explicit.**
- **Web applications separate product identity, local development, configuration, persistent data, deployment, operations, and security.**
- **Frontend libraries keep installation, CSS/peer dependencies, APIs, adapters, runtime compatibility, bundle, and accessibility contracts explicit when they apply.**
- **Desktop applications foreground downloads, supported platforms, product visuals, user data, packaging, and release compatibility.**
- **Full profiles must not invent capabilities that a project does not have.**
- **Generated output remains ordinary readable Markdown.**
- **Incomplete configuration should fail explicitly rather than create misleading documentation.**

## Tests

```bash
python -m pytest
```

GitHub Actions runs the suite on Python 3.11, 3.12, and 3.13 and performs CLI render smoke tests for all seven template families.

## Status

RepoForge is in early development, but the complete initial **7 project types × 3 profiles = 21 template combinations** are now represented. The next stage is to harden project detection, configuration ergonomics, apply/diff/check workflows, and cross-family visual consistency.

## License

MIT.
