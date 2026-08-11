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
- whether selected files exactly match the current renderer/standards output;
- `CITATION.cff` YAML and core CFF structure when Citation is selected;
- GitHub Bug Report and Feature Request Issue Form YAML/structure when Issue Forms are selected;
- Issue chooser configuration shape;
- critical initialization placeholders such as `OWNER/REPOSITORY`;
- selected Code of Conduct and Security private reporting contacts;
- example Citation author/ORCID values;
- selected contribution setup commands that still point at the generic example repository.

The README header, badges, navigation, and profile-specific content are covered by the exact generated-content comparison. If a managed README differs from the current template/config output, `check` fails and points you to `repoforge diff` for the textual change.

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

A repository with drift or missing files looks like:

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
edit repoforge.yml / update RepoForge
        ↓
repoforge diff .
        ↓
repoforge apply .
        ↓
repoforge check .
```

## GitHub Actions example

After installing RepoForge, a CI job can use:

```yaml
- name: Check repository documentation
  run: repoforge check . --strict
```

Use normal mode instead of `--strict` when placeholder-style warnings are acceptable during early Alpha development.

## Current boundary

`check` validates only files selected by the current RepoForge plan. It does not scan unrelated repository files, enforce arbitrary project coding style, or semantically merge hand-written README sections.

Because current RepoForge management is whole-file based, a hand-edited managed file is intentionally reported as drift. Use `repoforge diff` to review the difference before deciding whether to update the config, retain the hand-written file, or apply the generated version.
