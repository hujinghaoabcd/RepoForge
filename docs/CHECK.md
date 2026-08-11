# Validating a repository with `repoforge check`

`repoforge check` is the CI-facing validation step for a repository that already has a RepoForge configuration and generated repository files.

It does **not** modify files. Use `repoforge diff` to inspect textual changes and `repoforge apply` to write them.

## Basic usage

When the repository contains `repoforge.yml` at its root:

```bash
repoforge check .
```

You can still pass an explicit config path:

```bash
repoforge check . --config config/repoforge.yml
```

Project type and profile remain explicit configuration. RepoForge does not infer them from repository contents.

## What is checked

The current check workflow validates:

- `repoforge.yml` config version and stored project type/profile;
- whether every file selected by the current RepoForge plan exists;
- whether selected whole-file-managed standards exactly match the current renderer/standards output;
- whether README-managed regions match the current configuration when `readme_management: managed-sections` is enabled;
- `CITATION.cff` YAML and core CFF structure when Citation is selected;
- GitHub Bug Report and Feature Request Issue Form YAML/structure when Issue Forms are selected;
- Issue chooser configuration shape;
- critical initialization placeholders such as `OWNER/REPOSITORY`;
- selected Code of Conduct and Security private reporting contacts;
- example Citation author/ORCID values;
- selected contribution setup commands that still point at the generic example repository.

## README behavior

New `repoforge init` configs use:

```yaml
repoforge:
  readme_management: managed-sections
```

In this mode, only the stable `identity`, `badges`, and `navigation` marker regions are RepoForge-owned in v1. Hand edits outside those markers are user-owned and do **not** make `check` fail.

If the title, configured logo/tagline, badges, or navigation inside a managed region differs from the current configuration, `check` reports README drift and points you to `repoforge diff`.

Configs without a `readme_management` key retain legacy `whole-file` behavior, where any README difference is drift.

Malformed, duplicate, or incomplete RepoForge marker sets fail closed instead of being treated as user-owned prose. See [`MANAGED_SECTIONS.md`](MANAGED_SECTIONS.md) for the complete ownership contract.

## Output

A clean repository looks like:

```text
PASS  repoforge.yml  configuration and explicit selection are valid
PASS  README.md  in sync
PASS  CONTRIBUTING.md  in sync
PASS  SECURITY.md  in sync
PASS  CITATION.cff  in sync

Summary: 10 passed, 0 warnings, 0 failed.
Repository standards are in sync.
```

A repository with managed drift or missing files looks like:

```text
PASS  repoforge.yml  configuration and explicit selection are valid
FAIL  README.md  content differs from the current RepoForge plan; run repoforge diff
FAIL  SECURITY.md  missing selected RepoForge file
WARN  repoforge.yml  Citation metadata still contains the example author/ORCID

Summary: 7 passed, 1 warning, 2 failed.
```

## Exit codes

Normal mode returns:

```text
0  no FAIL results
1  one or more FAIL results
```

Warnings are informational by default. To make warnings fail CI as well:

```bash
repoforge check . --strict
```

With `--strict`, either a WARN or FAIL result returns exit code `1`.

## Standards selection

`check`, `diff`, and `apply` share the same plan-selection options:

```bash
--standards none
--standards default
--standards recommended
--include citation
--exclude support
```

This is intentional: a file selected by `check` is the same file selected by `diff` and `apply` for the same configuration/options.

## Recommended workflow

```text
repoforge init .
        ↓
edit repoforge.yml
        ↓
repoforge diff .
        ↓
repoforge apply .
        ↓
repoforge check .
        ↓
CI
```

For repositories already under RepoForge management, normal maintenance is shorter:

```text
edit repoforge.yml / hand-edit user-owned README body
        ↓
repoforge diff .
        ↓
repoforge apply .
        ↓
repoforge check .
```

A hand edit outside managed README markers does not require a subsequent apply merely to satisfy `check`.

## GitHub Actions example

After installing RepoForge, a CI job can use:

```yaml
- name: Check repository documentation
  run: repoforge check . --strict
```

Use normal mode instead of `--strict` when placeholder-style warnings are acceptable during early Alpha development.

## Current boundary

`check` validates only files selected by the current RepoForge plan. It does not scan unrelated repository files or enforce arbitrary project coding style.

Managed Sections v1 is marker-based rather than semantic: it knows ownership boundaries for `identity`, `badges`, and `navigation`, but it does not interpret or reconcile hand-written body sections such as Overview, Methods, Features, Experiments, or Installation prose.

Other selected repository-standard files remain whole-file managed. Use `repoforge diff` to review their differences before deciding whether to update configuration or apply generated content.
