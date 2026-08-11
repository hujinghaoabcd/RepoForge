<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="280">
</p>

# RepoForge

**Reusable repository documentation and project standards.**

RepoForge applies consistent README and repository-documentation standards to projects that already have their code scaffold. Use Cookiecutter, Scientific Python Cookie, Django templates, Vite, or another generator for project structure; use RepoForge for the public documentation layer.

**English** · [简体中文](README.zh-CN.md)

## Why RepoForge?

Project scaffolds create code structure, but repositories still need a clear public-facing documentation system. RepoForge separates those concerns:

1. scaffold the project with the best tool for the technology stack;
2. select a RepoForge project type and one independent documentation profile;
3. render a readable Markdown README from explicit YAML configuration;
4. keep detailed manuals in `docs/` instead of turning the README into the whole documentation site.

The goal is a recognizable family style without forcing unrelated projects into one README structure.

## Implemented template families

RepoForge currently has six executable renderer families:

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
```

The three profiles are **independent templates**, not conditional views inside one giant README template.

- `scientific-python` — reusable scientific software packages;
- `research-algorithm` — original scientific or technical methods;
- `research-experiment` — paper code, benchmark studies, and reproducibility repositories;
- `django-package` — reusable Django applications, extensions, middleware, backends, and admin integrations;
- `web-application` — complete browser products and deployable web systems, from small monoliths to multi-service self-hosted applications;
- `frontend-library` — reusable browser libraries, plugins, components, hooks, and framework/map-engine adapters.

Each implemented family has a contract, reference analysis, independent profile rules, Jinja templates, YAML example configs, rendered examples, branded previews, renderer tests, and deliberately difficult stress cases.

## Quick start

Install RepoForge from a source checkout:

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

Render a Scientific Python README:

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

Render an original research-method README:

```bash
repoforge render research-algorithm standard \
  --config templates/research-algorithm/standard/config.example.yml \
  --output README.generated.md
```

Render a reproducible paper-experiment README:

```bash
repoforge render research-experiment full \
  --config templates/research-experiment/full/config.example.yml \
  --output README.generated.md
```

Render a reusable Django package README:

```bash
repoforge render django-package standard \
  --config templates/django-package/standard/config.example.yml \
  --output README.generated.md
```

Render a full web-application README:

```bash
repoforge render web-application full \
  --config templates/web-application/full/config.example.yml \
  --output README.generated.md
```

Render a frontend library README:

```bash
repoforge render frontend-library standard \
  --config templates/frontend-library/standard/config.example.yml \
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

The shared preview configuration currently renders the RepoForge logo at **280 px**. User-facing `README.example.md` files remain brand-neutral so generated projects can supply their own `logo_path` and size.

Regenerate previews for implemented template families with:

```bash
python scripts/generate_previews.py
```

## Stress tests

Renderer-backed stress suites live under:

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
├── django-package/
├── web-application/
└── frontend-library/
```

They deliberately exercise project shapes that make a generic README design fail. The frontend-library suite includes a tiny DOM utility, a CSS-heavy widget, a framework adapter, a multi-package UI toolkit, and a Full vanilla library with **no React/Vue adapters and no SSR guarantee**.

That last case protects a core RepoForge rule: **Full means deeper documentation, not fabricated capabilities or infrastructure.**

## Project types

RepoForge's target template system is organized around seven project types:

- `scientific-python` — reusable scientific Python packages;
- `research-algorithm` — original methods and algorithm implementations;
- `research-experiment` — paper code, benchmarks, experiments, and reproducibility;
- `django-package` — reusable Django applications and extensions;
- `web-application` — small to large deployable web applications;
- `frontend-library` — frontend libraries, plugins, and components;
- `desktop-application` — desktop software and cross-platform applications.

The remaining family, `desktop-application`, will be implemented using the same contracts and tests.

## Profiles

Profiles control documentation depth, but each profile is a separate artifact.

- **Minimal** — the shortest complete README for a small, focused project.
- **Standard** — the default for most maintained open-source projects.
- **Full** — a deeper landing page for mature projects with broader integration, compatibility, validation, reproducibility, security, deployment, or upgrade boundaries.

For frontend libraries specifically, profile depth is independent from ecosystem breadth: a Full vanilla TypeScript library does not need React/Vue adapters, SSR support, or multiple packages unless those capabilities are actually maintained.

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
- **Scientific software treats validation, reproducibility, limitations, and citation as first-class concerns.**
- **Experiment repositories make data identity, protocol, seeds, result identity, and reproduction commands explicit.**
- **Django packages make host-project integration hooks, compatibility, migrations, security, and upgrade boundaries explicit.**
- **Web applications separate product identity, local development, configuration, persistent data, deployment, operations, and security.**
- **Frontend libraries keep install/import/CSS/peer-dependency, API/event, adapter, browser, TypeScript, SSR, bundle, accessibility, and versioning contracts explicit when they actually apply.**
- **Full profiles must not invent capabilities that a project does not have.**
- **Generated output remains ordinary readable Markdown.**
- **Incomplete configuration should fail explicitly rather than create misleading documentation.**

## Tests

```bash
python -m pytest
```

GitHub Actions runs the suite on Python 3.11, 3.12, and 3.13 and performs CLI render smoke tests for every implemented family.

## Status

RepoForge is in early development. Six template families are executable: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, and `frontend-library`. The final planned family is `desktop-application`.

## License

MIT.
