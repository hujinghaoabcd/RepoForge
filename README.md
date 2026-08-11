# RepoForge

**Reusable repository documentation and project standards.**

RepoForge is a reusable system for applying consistent documentation and repository standards to existing software and research projects. It is designed to work *after* a project scaffold has been created by tools such as Cookiecutter, Scientific Python Cookie, Vite, Django templates, or other generators.

**English** · [简体中文](README.zh-CN.md)

## Why RepoForge?

Project scaffolds are good at creating code structure, but repositories still need a clear public-facing documentation layer. RepoForge separates those concerns:

1. **Scaffold the project** with the tool best suited to the technology stack.
2. **Apply RepoForge** to add a consistent README and repository-documentation structure.
3. **Keep project-specific content** such as algorithms, screenshots, deployment notes, experiments, and API details in the generated structure.

The goal is not to make every README identical. The goal is to give different project types a common family style while preserving the information each type actually needs.

## Planned project types

RepoForge starts with seven documentation templates:

- `scientific-python` — reusable scientific Python packages;
- `research-algorithm` — original methods and algorithm implementations;
- `research-experiment` — paper code, benchmarks, experiments, and reproducibility;
- `django-package` — reusable Django applications and extensions;
- `web-application` — small to large web applications;
- `frontend-library` — frontend libraries, plugins, and components;
- `desktop-application` — desktop software and cross-platform applications.

## Profiles

Each project type can be rendered at one of three documentation depths:

- **minimal** — demos, small tools, prototypes, and focused plugins;
- **standard** — the default for most maintained open-source projects;
- **full** — mature research software, large applications, and complex reproducible projects.

Profiles control depth, not project identity. For example, a small and a large website both use `web-application`, but with different profiles.

## Architecture

RepoForge is organized around three reusable layers:

```text
RepoForge
├── templates/   # project-type README structures
├── profiles/    # minimal / standard / full depth rules
├── partials/    # reusable sections such as badges, citation, testing, deployment
└── docs/        # design decisions and authoring standards
```

The intended future command-line workflow is:

```bash
repoforge apply .
repoforge apply . --type scientific-python --profile standard
repoforge check .
```

RepoForge should inspect metadata such as `pyproject.toml`, `package.json`, Django project files, tests, documentation, and CI configuration where possible, then ask only for information that cannot be inferred safely.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the initial design.

## Design principles

- **README is an entry point, not the entire manual.** Detailed theory, APIs, deployment guides, and development notes should move into `docs/` when they become substantial.
- **Project type and project size are separate dimensions.** Do not duplicate templates just because one project is larger than another.
- **Reusable sections should be shared.** Installation, badges, citation, testing, security, deployment, and contribution guidance should not be rewritten from scratch in every template.
- **Research software needs research-specific metadata.** Validation, reproducibility, limitations, and citation are first-class concerns where relevant.
- **Generated files remain readable Markdown.** RepoForge should not require a proprietary format to understand or maintain the resulting repository.

## Status

RepoForge is in initial design and template-research stage. The first implementation target is the `scientific-python` template, using mature scientific Python projects and existing research packages as reference cases.

## License

A project license will be selected before the first public release.
