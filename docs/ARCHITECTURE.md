# RepoForge Architecture

This document defines the initial architecture of RepoForge. It is intentionally small enough to evolve while the template corpus is still being researched.

## 1. Problem separation

RepoForge treats project creation and repository presentation as separate concerns.

```text
Project scaffold
Cookiecutter / Scientific Python Cookie / Vite / Django / other generators
        ↓
Existing repository
        ↓
RepoForge standards layer
        ↓
README + repository documentation structure
        ↓
Project-specific content
```

RepoForge should therefore be applicable to an existing repository without requiring that repository to have been created by RepoForge.

## 2. Three axes

A rendered repository is determined by three independent axes.

### 2.1 Project type

The project type defines *what information matters*.

Initial types:

```text
scientific-python
research-algorithm
research-experiment
django-package
web-application
frontend-library
desktop-application
```

### 2.2 Profile

The profile defines *how much information belongs in the README*.

```text
minimal
standard
full
```

A profile must never silently change the semantic identity of a project type.

### 2.3 Partials

Partials are reusable documentation sections that may be selected by project type, profile, or detected repository capabilities.

Examples:

```text
header
badges
installation
quickstart
screenshots
architecture
deployment
api
testing
validation
reproducibility
citation
contributing
security
roadmap
license
```

## 3. Repository layout

Target layout during the template-research stage:

```text
RepoForge/
├── README.md
├── README.zh-CN.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── STYLE_GUIDE.md            # later
│   └── REFERENCE_CASES.md        # later
├── templates/
│   ├── scientific-python/
│   ├── research-algorithm/
│   ├── research-experiment/
│   ├── django-package/
│   ├── web-application/
│   ├── frontend-library/
│   └── desktop-application/
├── profiles/
│   ├── minimal.md
│   ├── standard.md
│   └── full.md
└── partials/
    └── ...
```

A Python CLI package may be added after the template contracts stabilize. RepoForge should not prematurely lock its content model to an implementation framework.

## 4. Template contract

Each project-type template should eventually define:

1. **Audience** — who the README is written for;
2. **Primary question** — what a first-time visitor needs to understand immediately;
3. **Required sections** — sections expected in every project of this type;
4. **Optional sections** — capability-dependent content;
5. **Excluded content** — information that should be moved to `docs/`, `CHANGELOG`, `ROADMAP`, etc.;
6. **Minimal / standard / full mappings**;
7. **Reference cases** — mature open-source projects that justify the structure;
8. **Example output** — a complete rendered README example.

## 5. README boundary

RepoForge adopts the following default boundary:

### Keep in README

- project identity and one-line positioning;
- key links and badges;
- why the project exists;
- primary capabilities;
- installation or download path;
- shortest useful quick start;
- documentation navigation;
- validation/reproducibility summary when scientifically relevant;
- citation when scientifically relevant;
- contribution/support/license entry points.

### Move out of README when substantial

- full theory and mathematical derivations;
- complete API manuals;
- exhaustive configuration references;
- full deployment and operations handbooks;
- long development histories;
- stage-by-stage implementation logs;
- complete benchmark tables;
- detailed release procedures;
- troubleshooting encyclopedias.

The README should remain a project entrance, not become the entire documentation site.

## 6. Detection versus declaration

RepoForge should distinguish between information that can be detected and information that must be declared.

### Safe candidates for detection

- Python project: `pyproject.toml`;
- Node project: `package.json`;
- Django indicators: `manage.py`, settings modules;
- tests: `tests/`, pytest configuration, frontend test scripts;
- CI: `.github/workflows/`;
- documentation: `docs/`, MkDocs, Sphinx, Docusaurus, VitePress;
- packaging and publish metadata;
- license files;
- citation metadata.

### Must normally be declared by the author

- one-line project positioning;
- scientific motivation;
- claimed novelty;
- intended audience;
- interpretation boundaries;
- screenshots or representative figures;
- paper/DOI information not already present in reliable metadata.

RepoForge must not invent scientific claims, project status, compatibility, or citations from weak signals.

## 7. Update strategy

Version 0.x should first support one-time application cleanly. Template synchronization for already customized repositories is a separate problem.

Possible later strategies include:

- managed section markers;
- three-way template updates;
- Copier-style update metadata;
- explicit `repoforge check` diagnostics without automatic rewriting.

The first release should favor predictable output over clever automatic updates.

## 8. First implementation target

The first template to stabilize is:

```text
scientific-python + standard
```

Reference research should compare mature scientific Python repositories and several real research packages, then extract section-level best practices rather than copying one project's README wholesale.
