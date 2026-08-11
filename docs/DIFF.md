# Reviewing RepoForge changes with `repoforge diff`

`repoforge diff` shows the exact text changes represented by the current RepoForge apply plan without writing any repository file.

It uses the same explicit project type/profile selection, configuration, standards matrices, and include/exclude overrides as `repoforge apply`.

## Typical workflow

After initialization and editing `repoforge.yml`:

```bash
repoforge diff /path/to/project \
  --config /path/to/project/repoforge.yml
```

Then apply only after reviewing the output:

```bash
repoforge apply /path/to/project \
  --config /path/to/project/repoforge.yml
```

## Output states

Only files selected by the current apply plan are considered.

A new file is shown as:

```text
[create] CONTRIBUTING.md
--- /dev/null
+++ b/CONTRIBUTING.md
@@ ...
+...
```

A differing existing file is shown as:

```text
[overwrite] README.md
--- a/README.md
+++ b/README.md
@@ ...
- existing text
+ generated text
```

Files whose current content exactly matches RepoForge output are hidden by default. If every selected file already matches, the command prints:

```text
No changes.
```

Use:

```bash
--show-unchanged
```

to list matching files as `[unchanged]` entries.

## Context lines

Unified diffs use three unchanged context lines by default.

Change that with:

```bash
repoforge diff . --config repoforge.yml --context 6
```

or request compact hunks with:

```bash
repoforge diff . --config repoforge.yml --context 0
```

The context value must be zero or greater.

## Standards selection

`diff` deliberately mirrors `apply`:

```bash
--standards none
--standards default
--standards recommended
--include citation
--exclude support
```

This means a reviewed diff corresponds to the same repository plan that `apply` will later use, provided the same configuration and selection flags are supplied.

## Explicit project selection

A configuration created by `repoforge init` stores its project type and profile, so the common form is:

```bash
repoforge diff . --config repoforge.yml
```

You may still pass explicit one-off overrides:

```bash
repoforge diff . \
  --type scientific-python \
  --profile full \
  --config repoforge.yml
```

RepoForge does not infer the project type.

## Safety boundary

`repoforge diff` never writes target repository files.

It does not:

- delete unrelated repository files;
- compare files that are not part of the selected RepoForge plan;
- perform semantic or managed-section merges inside hand-written documents;
- imply that `apply --force` is safe for a hand-maintained file.

For existing repositories, review `overwrite` sections carefully before using `repoforge apply --force`.

The intended workflow is:

```text
repoforge init
      ↓
edit repoforge.yml
      ↓
repoforge diff
      ↓
review exact text changes
      ↓
repoforge apply
```
