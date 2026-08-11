# Applying RepoForge to an existing repository

`repoforge apply` is the repository-level workflow built on top of the README renderer and repository standards packs.

It does **not** infer project type. You select the project type and profile explicitly.

## Basic workflow

Start from a combined RepoForge YAML configuration. A runnable example is available at:

```text
examples/apply/scientific-python-standard.yml
```

Preview the actions first:

```bash
repoforge apply /path/to/project \
  --type scientific-python \
  --profile standard \
  --config examples/apply/scientific-python-standard.yml \
  --dry-run
```

Then apply them:

```bash
repoforge apply /path/to/project \
  --type scientific-python \
  --profile standard \
  --config examples/apply/scientific-python-standard.yml
```

## What gets written

`README.md` is always part of the plan.

Repository standards are selected from three policy matrices:

```text
standards/matrix.yml             # community health
standards/github/matrix.yml      # issue / pull-request collaboration
standards/metadata/matrix.yml    # citation / changelog metadata
```

The default policy writes only standards marked `default` for the chosen project type/profile.

Use:

```bash
--standards none
```

to apply only the README, or:

```bash
--standards recommended
```

to include both `default` and `recommended` standards.

## Explicit overrides

An optional or recommended standard can be added explicitly:

```bash
--include citation
```

A selected standard can be suppressed explicitly:

```bash
--exclude support
```

Available logical standard names are:

```text
code_of_conduct
contributing
security
support
issue_forms
pull_request_template
citation
changelog
```

An item cannot be included and excluded at the same time.

## Safe overwrite behavior

RepoForge builds and renders the complete plan before it writes any file.

Each destination is classified as:

```text
create
unchanged
overwrite
```

If any selected destination already exists with different content, normal apply fails **before writing any selected file**.

Use:

```bash
--dry-run
```

to inspect conflicts without modifying the repository.

Use:

```bash
--force
```

only when you intentionally want RepoForge to replace differing selected files.

`--force` does not delete unrelated repository files.

## Combined configuration

The apply configuration is intentionally one YAML document.

README templates read the fields they need. Repository standards read their own sections such as:

```yaml
code_of_conduct:
contributing:
security:
support:
issue_forms:
pull_request:
citation:
changelog:
```

Extra keys are harmless to a README template. This lets a future `repoforge init` generate one `repoforge.yml` rather than several unrelated configuration files.

Some standards intentionally require explicit project-owned information. In particular, Code of Conduct and Security templates require a private reporting contact/channel. RepoForge should not invent those values.

## Current boundary

`apply` manages only the files selected by the current plan. It does not yet perform managed-section updates inside an existing hand-written README, semantic merges, or automatic repository backups.

For an existing repository with valuable hand-written standard files, use `--dry-run`, review the reported `overwrite` paths, and do not use `--force` until the generated output has been compared with the existing content.

A dedicated `repoforge diff` command can later present textual diffs on top of the same plan without changing this safety model.
