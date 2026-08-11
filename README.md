<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="160">
</p>

<h1 align="center">RepoForge</h1>

<p align="center">
  <strong>Reusable README templates and repository documentation standards.</strong>
</p>

<p align="center">
  <a href="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml/badge.svg"></a>
  <a href="pyproject.toml"><img alt="Version" src="https://img.shields.io/badge/version-0.1.0a1-174D5B.svg"></a>
  <a href="#template-matrix"><img alt="README templates" src="https://img.shields.io/badge/templates-21-139C5A.svg"></a>
  <a href="pyproject.toml"><img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-174D5B.svg"></a>
  <a href="#project-status"><img alt="Status" src="https://img.shields.io/badge/Status-Alpha-F4B942.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-139C5A.svg"></a>
</p>

<p align="center">
  <strong>7 project types</strong> · <strong>3 independent profiles</strong> · YAML + Jinja2 · renderer-backed previews · stress-tested contracts
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#template-matrix">Templates</a> ·
  <a href="#profiles">Profiles</a> ·
  <a href="#repository-standards">Standards</a> ·
  <a href="#preview">Previews</a> ·
  <a href="docs/ARCHITECTURE.md">Architecture</a> ·
  <a href="docs/RELEASE.md">Release</a> ·
  <a href="#tests-and-stress-suites">Tests</a>
</p>

---

## What RepoForge is

**RepoForge is a repository-documentation layer for projects that already have code.** It renders a project-facing `README.md` from an explicit project type, an independent documentation profile, a Jinja template, and YAML configuration.

It is intentionally **not another project scaffold**. Use Cookiecutter, Scientific Python Cookie, Django templates, Vite, Astro, Electron, Qt, or another generator for source layout; use RepoForge after that to make the repository's public documentation consistent, readable, and reviewable.

```text
Project scaffold
Cookiecutter / Scientific Python Cookie / Django / Vite / Qt / ...
        ↓
Existing repository
        ↓
RepoForge documentation layer
        ↓
README + documentation structure + repository standards
```

The current executable core is deliberately small: **Jinja2 + YAML + a strict renderer + a CLI**. Missing template variables fail visibly instead of silently producing incomplete documentation.

## Why RepoForge?

Repositories from different ecosystems need different information, but they still benefit from a recognizable documentation system. RepoForge separates three decisions that are often mixed together:

- **Project structure** — owned by the project's scaffold or framework.
- **Project type** — determines which information belongs on the landing page.
- **Documentation depth** — controlled by an independent `minimal`, `standard`, or `full` template.

This prevents two common failure modes: one generic README forced onto every project, and a single giant conditional template that becomes difficult to understand or test.

RepoForge follows several practical rules:

- README is the **landing page**, not the entire manual.
- Minimal, Standard, and Full are **separate template artifacts**.
- Full means **deeper documentation**, not invented capabilities.
- Scientific packages expose validation, reproducibility, limitations, and citation when they matter.
- Experiment repositories expose data identity, protocol, seeds, results, and reproduction commands.
- Web and desktop products foreground how users actually run, install, deploy, or upgrade them.
- Generated output remains ordinary Markdown that can still be edited by humans.

## Preview

<p align="center">
  <img src="assets/placeholders/screenshot.svg" alt="RepoForge preview placeholder" width="820">
</p>

<p align="center"><em>Reserved for real RepoForge screenshots. The committed placeholder intentionally contains no mock interface or fabricated product output.</em></p>

## Template matrix

RepoForge currently implements the complete initial **7 project types × 3 profiles = 21 README templates**.

| Project type | Best fit | README emphasis |
| --- | --- | --- |
| `scientific-python` | reusable scientific Python packages | scientific fit, install, quick example, methods, validation, docs, citation |
| `research-algorithm` | original methods and algorithm implementations | scientific problem, method, formulation, validation, limitations, citation |
| `research-experiment` | paper code, benchmarks, reproducibility repositories | data identity, environment, protocol, seeds, results, reproduction |
| `django-package` | reusable Django apps and extensions | host-project integration, settings, compatibility, migrations, security |
| `web-application` | deployable browser products and systems | product, local run, configuration, database, deployment, operations |
| `frontend-library` | browser libraries, plugins, components, adapters | install/import, CSS, API, events, adapters, browser/SSR/types/bundle contracts |
| `desktop-application` | installable Windows/macOS/Linux software | screenshots, downloads, platforms, user data, packaging, upgrades, troubleshooting |

Every family contains three independent directories:

```text
templates/<project-type>/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   ├── README.example.md
│   └── config.example.yml
├── standard/
└── full/
```

Each family also has a `CONTRACT.md` and a `references.md` explaining the design boundary and the real projects used as references.

## Profiles

| Profile | Use it when | Goal |
| --- | --- | --- |
| **Minimal** | a small, focused, early, internal, or single-purpose project | shortest complete landing page |
| **Standard** | a maintained open-source project with normal user/developer needs | default balance of clarity and depth |
| **Full** | a mature project with broader scientific, compatibility, deployment, packaging, security, or upgrade contracts | deeper landing page without turning README into the manual |

A Full project does **not** have to support every platform, framework, service, adapter, plugin system, or distribution channel. Optional sections appear only when the project actually maintains those capabilities.

## Quick start

The Python distribution is named `repoforge-standards`; the import package and CLI remain `repoforge`. For a published release:

```bash
python -m pip install repoforge-standards
repoforge --version
```

For unreleased development or contributing, install from source:

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

Render a README by selecting a project type and profile:

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

Other examples:

```bash
repoforge render research-experiment full \
  --config templates/research-experiment/full/config.example.yml \
  --output README.generated.md

repoforge render web-application full \
  --config templates/web-application/full/config.example.yml \
  --output README.generated.md

repoforge render desktop-application standard \
  --config templates/desktop-application/standard/config.example.yml \
  --output README.generated.md
```

The output is ordinary Markdown. You can review it with Git, edit project-specific prose, and move deeper material into `docs/`.

Initialize one combined project config with an explicit type/profile:

```bash
repoforge init /path/to/project \
  --type scientific-python \
  --profile standard \
  --name MyPackage \
  --repository-url https://github.com/example/my-package
```

Review `repoforge.yml`, inspect the exact text changes, then apply it:

```bash
repoforge diff /path/to/project --config /path/to/project/repoforge.yml
repoforge apply /path/to/project --config /path/to/project/repoforge.yml --dry-run
repoforge apply /path/to/project --config /path/to/project/repoforge.yml
repoforge check /path/to/project
```

`init` records the explicit project type/profile in the config, so normal `diff`, `apply`, and `check` do not need to repeat them. RepoForge refuses to overwrite differing selected files unless `--force` is supplied. See [`docs/INIT.md`](docs/INIT.md), [`docs/DIFF.md`](docs/DIFF.md), [`docs/APPLY.md`](docs/APPLY.md), [`docs/CHECK.md`](docs/CHECK.md), and [`docs/RELEASE.md`](docs/RELEASE.md).

## How rendering works

```text
config.example.yml
        +
README.template.md
        +
project type / profile
        ↓
 strict RepoForge renderer
        ↓
 generated README.md
```

The renderer uses Jinja2 `StrictUndefined`. A template that requires missing configuration fails instead of silently rendering an incomplete section.

The current CLI implements `repoforge render`, explicit `repoforge init`, review-first `repoforge diff`, safety-first `repoforge apply`, and CI-facing `repoforge check`. Repository standards are selected from explicit project type/profile matrices; automatic project detection is intentionally not part of the design.

## Previews and golden outputs

Approved rendered previews live under:

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge's preview suite uses one shared brand source and one neutral media placeholder:

```text
assets/logo.svg
assets/placeholders/screenshot.svg
        ↑
tests/branding.yml
```

The canonical README logo display width is **160 px**. Preview-only media uses the deliberately empty placeholder above; user-facing `README.example.md` files remain project-neutral and may supply their own real logo, screenshots, diagrams, or demo media.

Regenerate the preview matrix with:

```bash
python scripts/generate_previews.py
```

## Tests and stress suites

Run the complete suite with:

```bash
python -m pytest
```

GitHub Actions runs the tests on Python **3.11, 3.12, and 3.13**, performs CLI render smoke tests for all seven template families, and exercises the full `init → diff → apply → check` workflow against a temporary repository, including an intentional drift failure.

Renderer-backed stress suites live under:

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

They deliberately exercise shapes that break generic README designs: tiny packages, theory-heavy algorithms, multi-seed experiments, Django middleware without models, web monoliths without queues/APIs, vanilla frontend libraries without framework adapters/SSR, and Full desktop applications without plugins or auto-update.

The invariant is simple:

> **Full means deeper documentation, not fabricated capabilities or infrastructure.**

## Repository standards

RepoForge now includes a first repository-health pack beside the README matrix:

- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — participation and conduct expectations;
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow and template-change rules;
- [`SECURITY.md`](SECURITY.md) — private vulnerability reporting and supported-version policy;
- [`SUPPORT.md`](SUPPORT.md) — where usage questions, bugs, security reports, and conduct concerns belong.

Reusable repository standards now live in three packs:

- [`standards/community/`](standards/community/) — Code of Conduct, contributing, security, and support;
- [`standards/github/`](standards/github/) — Issue Forms and pull-request templates;
- [`standards/metadata/`](standards/metadata/) — `CITATION.cff` and `CHANGELOG.md`.

Each pack has explicit policy rules for project type/profile combinations. The standards layer intentionally does **not** infer project type.

## Repository structure

```text
RepoForge
├── assets/                         # logo and README visuals
├── src/repoforge/                  # renderer and CLI
├── templates/                      # 7 project families × 3 profiles
├── profiles/                       # cross-project profile rules
├── standards/                      # repository community/security/support contracts
├── partials/                       # reusable documentation components
├── tests/
│   ├── previews/                   # approved rendered views
│   └── stress/                     # difficult real-shape configurations
├── scripts/                        # preview and maintenance helpers
└── docs/                           # architecture and standards
```

Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the architecture and template-system boundaries.

## Design principles

- **README is an entry point, not the entire manual.**
- **Minimal, Standard, and Full are independent templates.**
- **Project type and documentation depth are separate decisions.**
- **The first screen should establish identity, useful badges, and navigation before detail.**
- **Badges should communicate maintained facts, not decorate the page.**
- **Full profiles must not invent project capabilities.**
- **Examples and previews are renderer-backed so design regressions are testable.**
- **Incomplete configuration should fail explicitly.**
- **Generated output remains readable, editable Markdown.**

## Usability today

RepoForge is **usable now for explicit, configuration-driven README rendering and repository-standard application**. From a source checkout you select one of the seven project types and a profile, provide one combined YAML configuration, and either render a README alone or apply the selected repository pack to an existing repository.

Available now:

- `repoforge render`;
- `repoforge init` for one combined, explicitly typed `repoforge.yml`;
- `repoforge diff` for unified, no-write review of the exact selected apply plan;
- `repoforge apply` with `--dry-run`, safe conflict preflight, `--force`, and standards policy overrides;
- `repoforge check` for CI-facing config, drift, CFF/Issue Form, and placeholder validation;
- Managed Sections v1 for README `identity`, `badges`, and `navigation`, while body prose remains user-owned;
- 7 project types × 3 independent profiles;
- community, GitHub collaboration, citation, and changelog standards;
- strict Jinja/YAML validation;
- committed examples and golden previews;
- renderer-backed stress tests and Python 3.11–3.13 CI.

Not implemented yet:

- semantic management/merging of README body sections beyond the v1 header regions;
- production PyPI publication; `0.1.0a1` packaging and Trusted Publishing automation are prepared under the `repoforge-standards` distribution name, but the index release has not been executed yet.

So the current release is already useful as a **README and repository-standards application tool**, but it intentionally remains explicit rather than becoming a zero-configuration project detector.

## Project status

RepoForge is an **Alpha** project. The initial template layer is complete: all 21 project-type/profile combinations are represented, the renderer is executable, previews are committed, and each family has contract and stress coverage.

The repository standards packs plus `init`, `diff`, `apply`, and `check` are implemented. Managed Sections v1 preserves hand-edited README body prose while maintaining the stable header regions. Version `0.1.0a1` is package-ready with verified wheel/sdist builds and Trusted Publishing automation; the remaining release step is the first TestPyPI/PyPI publication after publisher setup.

The currently supported CLI commands are `repoforge render`, `repoforge init`, `repoforge diff`, `repoforge apply`, and `repoforge check`. New `init` configs use `readme_management: managed-sections`; see [`docs/MANAGED_SECTIONS.md`](docs/MANAGED_SECTIONS.md).

## Contributing

RepoForge treats template changes as documentation-design changes. When changing a contract or template:

1. keep Minimal / Standard / Full independent;
2. update the matching example and golden preview;
3. add or update a stress case when the change affects a semantic boundary;
4. run the full test suite before merging.

New project families should be added only when they have a genuinely different README contract rather than being a technology-name alias for an existing family.

## License

RepoForge is released under the [MIT License](LICENSE).
