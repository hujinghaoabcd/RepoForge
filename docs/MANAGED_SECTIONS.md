# Managed README sections

RepoForge supports two README ownership modes:

```yaml
repoforge:
  readme_management: whole-file
```

and:

```yaml
repoforge:
  readme_management: managed-sections
```

New configs created by `repoforge init` use `managed-sections`. Existing configs that do not declare a mode keep the historical `whole-file` behavior for backward compatibility.

## Why managed sections exist

Whole-file rendering is useful when RepoForge owns the complete README, but it is too strict for repositories where maintainers continue to edit project prose by hand. In whole-file mode, any manual README edit is drift.

Managed Sections v1 changes that ownership boundary. RepoForge manages only a few stable header regions and preserves every other byte of the existing README.

## Managed regions in v1

The first version intentionally manages only:

```text
identity
badges
navigation
```

They appear inside the shared centered README header:

```md
<div align="center">

<!-- repoforge:start identity -->
# Project Name

**Project tagline**
<!-- repoforge:end identity -->

<!-- repoforge:start badges -->
...
<!-- repoforge:end badges -->

<!-- repoforge:start navigation -->
...
<!-- repoforge:end navigation -->

</div>
```

`identity` includes the configured logo when present, project name, and tagline. `badges` contains the configured badge row. `navigation` contains the language switch and/or project navigation supported by that template family.

Everything after the centered header remains user-owned in v1. RepoForge does not manage Overview, Features, Methods, Experiments, Installation prose, screenshots, API documentation, limitations, or other body sections.

## Editing the README by hand

After the first managed apply, this is safe:

```md
## Maintainer Notes

This section is written and maintained manually.
```

A later:

```bash
repoforge check .
```

still reports the README as in sync because the edit is outside RepoForge-managed markers.

If a configured badge or navigation link changes, run:

```bash
repoforge diff .
repoforge apply .
```

The diff contains only the managed-region change plus normal context lines, and `apply` preserves the hand-written body.

## Managed edits do not require `--force`

When `README.md` already contains the complete RepoForge managed marker set, changes to those managed regions are safe section replacements. `repoforge apply` can update them without `--force`.

Other repository-standard files remain whole-file managed and retain the existing conflict rules.

## Migrating an existing unmarked README

RepoForge does not guess how to merge an arbitrary unmarked README.

If `readme_management: managed-sections` is enabled but the existing README has no RepoForge markers, `diff` shows the full proposed managed README and normal `apply` refuses to overwrite it.

Migration therefore remains explicit:

```bash
repoforge diff .
repoforge apply . --force
```

Only use `--force` after reviewing the full migration diff. For a valuable hand-written README that does not already follow the RepoForge generated structure, preserve or manually re-integrate its content before forcing migration.

Once the markers exist, later unmanaged body edits are preserved automatically.

## Fail-closed marker handling

RepoForge never guesses through malformed marker state. It raises an error for:

- duplicate managed section names;
- incomplete managed section sets;
- stray or malformed RepoForge marker syntax.

This prevents partial marker damage from silently replacing an unexpected region of the README.

## `diff`, `apply`, and `check` share the same merge

Managed-section behavior is implemented below the three repository workflows. For the same configuration and standards selection:

```text
existing README
      +
current generated managed regions
      ↓
materialized target README
      ├── repoforge diff
      ├── repoforge apply
      └── repoforge check
```

There is no separate merge algorithm for each command.

## Legacy whole-file mode

A config with no `readme_management` key behaves as:

```yaml
repoforge:
  readme_management: whole-file
```

In that mode, the complete generated README is still the contract. Any manual edit to the file is drift, and an overwrite still requires the normal `--force` safety barrier.

You can also select whole-file behavior explicitly when that stronger ownership model is desirable.

## Current boundary

Managed Sections v1 is intentionally conservative. It does not yet manage repository links, citation/footer blocks, or semantic body sections. Those should only be added when their ownership and merge behavior are stable enough to remain predictable across all seven project families.
