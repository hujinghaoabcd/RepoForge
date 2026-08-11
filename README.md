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

## Current implementation

The first executable template family is:

```text
scientific-python
├── minimal
├── standard
└── full
```

The three profiles are **independent templates**, not conditional branches inside one large README template.

Each profile contains:

```text
PROFILE.md
README.template.md
README.example.md
config.example.yml
```

## Quick start

Install RepoForge from a source checkout:

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

Render the Minimal scientific-Python README:

```bash
repoforge render scientific-python minimal \
  --config templates/scientific-python/minimal/config.example.yml \
  --output README.generated.md
```

Render Standard:

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

Render Full:

```bash
repoforge render scientific-python full \
  --config templates/scientific-python/full/config.example.yml \
  --output README.generated.md
```

The renderer uses strict configuration validation: a template variable that is not declared in the YAML configuration fails visibly instead of silently producing an incomplete README.

## Previewing profiles

Approved visual previews live under:

```text
tests/previews/<project-type>/<profile>.md
```

For the implemented scientific-Python family:

```text
tests/previews/scientific-python/
├── minimal.md
├── standard.md
└── full.md
```

Regenerate scientific-Python previews from their current templates and example configurations with:

```bash
python scripts/generate_previews.py
```

## Planned project types

RepoForge's template system is organized around seven project types:

- `scientific-python` — reusable scientific Python packages;
- `research-algorithm` — original methods and algorithm implementations;
- `research-experiment` — paper code, benchmarks, experiments, and reproducibility;
- `django-package` — reusable Django applications and extensions;
- `web-application` — small to large web applications;
- `frontend-library` — frontend libraries, plugins, and components;
- `desktop-application` — desktop software and cross-platform applications.

Only `scientific-python` has a working renderer contract today; the other families currently have separated visual profile previews and will receive templates incrementally.

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
│   └── previews/                  # approved rendered views
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

RepoForge is in early development. The `scientific-python` family is the first implemented renderer target; the next work is snapshot synchronization and additional project families.

## License

MIT.
