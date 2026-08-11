# RepoForge

**Reusable repository documentation and project standards.**

RepoForge applies consistent README and repository-documentation standards to projects that already have their code scaffold. Use Cookiecutter, Scientific Python Cookie, Django templates, Vite, or another generator for the project structure; use RepoForge for the public documentation layer.

**English** · [简体中文](README.zh-CN.md)

## Why RepoForge?

Project scaffolds create code structure, but repositories still need a clear public-facing documentation system. RepoForge separates those concerns:

1. scaffold the project with the best tool for the technology stack;
2. select a RepoForge project type and one independent documentation profile;
3. render a readable Markdown README from explicit configuration;
4. keep detailed project-specific manuals in `docs/` instead of turning the README into the whole documentation site.

The goal is a recognizable family style without forcing unrelated projects into one README structure.

## Implemented template families

RepoForge currently has executable renderer contracts for:

```text
scientific-python
├── minimal
├── standard
└── full

research-algorithm
├── minimal
├── standard
└── full
```

The three profiles are **independent templates**, not conditional branches inside one large README template.

`scientific-python` is the more mature family and includes profile contracts, templates, rendered examples, YAML configs, previews, and dedicated stress tests. `research-algorithm` now has its initial contract, reference notes, independent profile rules, templates, example configs, and renderer tests.

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

The renderer uses strict configuration validation: a template variable that is not declared in the YAML configuration fails visibly instead of silently producing an incomplete README.

## Previewing profiles

Approved visual previews live under:

```text
tests/previews/<project-type>/<profile>.md
```

Regenerate previews for implemented template families with:

```bash
python scripts/generate_previews.py
```

## Stress tests

Scientific Python profiles are also exercised against deliberately different package shapes:

```text
tests/stress/scientific-python/
├── README.md
├── manifest.yml
└── cases/
    ├── tiny-numerical-utility.yml
    ├── multi-method-geospatial.yml
    ├── broad-model-library.yml
    ├── theory-heavy-statistics.yml
    └── pre1-experimental-package.yml
```

These are renderer-backed contract tests rather than hand-written showcase READMEs. They are intended to catch cases where a profile becomes too rigid, too verbose, or semantically inappropriate for a real scientific package shape.

## Project types

RepoForge's template system is organized around seven project types:

- `scientific-python` — reusable scientific Python packages;
- `research-algorithm` — original methods and algorithm implementations;
- `research-experiment` — paper code, benchmarks, experiments, and reproducibility;
- `django-package` — reusable Django applications and extensions;
- `web-application` — small to large web applications;
- `frontend-library` — frontend libraries, plugins, and components;
- `desktop-application` — desktop software and cross-platform applications.

The remaining families currently have separated visual profile previews and will receive executable templates incrementally.

## Profiles

Profiles control documentation depth, but each profile is a separate artifact.

- **Minimal** — small, focused projects with the shortest complete README.
- **Standard** — the default for most maintained open-source projects.
- **Full** — broad or mature projects that need scope, method selection, validation, reproducibility, compatibility, or interpretation guidance on the project page.

## Repository structure

```text
RepoForge
├── src/repoforge/                 # renderer and CLI
├── templates/                     # project-type/profile templates
├── profiles/                      # cross-project profile rules
├── partials/                      # reusable documentation components
├── tests/
│   ├── previews/                  # approved rendered views
│   └── stress/                    # high-pressure real-shape configs
├── scripts/                       # maintenance helpers
└── docs/                          # architecture and standards
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the design.

## Design principles

- **README is an entry point, not the entire manual.**
- **Minimal, Standard, and Full are independent templates.**
- **Project type and documentation depth are separate decisions.**
- **Scientific software treats validation, reproducibility, limitations, and citation as first-class concerns.**
- **Generated output remains ordinary readable Markdown.**
- **Incomplete configuration should fail explicitly rather than create misleading documentation.**

## Tests

```bash
python -m pytest
```

GitHub Actions runs the test suite on supported Python versions and performs a CLI render smoke test.

## Status

RepoForge is in early development. `scientific-python` is the first mature renderer family; `research-algorithm` is now the second implemented family and is entering reference-case refinement and preview/snapshot hardening.

## License

MIT.
