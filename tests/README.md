# RepoForge preview tests

This directory is the visual and regression-test area for RepoForge templates.

RepoForge currently models README generation along two axes:

- **project type**: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, `frontend-library`, `desktop-application`;
- **profile**: `minimal`, `standard`, `full`.

That gives **21 preview combinations**.

## Layout

```text
tests/
├── README.md
├── preview-matrix.yml
└── previews/
    ├── scientific-python.md
    ├── research-algorithm.md
    ├── research-experiment.md
    ├── django-package.md
    ├── web-application.md
    ├── frontend-library.md
    └── desktop-application.md
```

Each file under `previews/` shows the intended rendered README structure for all three profiles of one project type.

## Why keep previews in tests?

These files serve two purposes:

1. **Visual review now** — template structure can be discussed before the CLI exists.
2. **Golden snapshots later** — once the renderer is implemented, automated tests can generate README output and compare it with approved snapshots.

The preview files are intentionally structural. They show section order, emphasis and expected depth, while project-specific prose remains placeholder content.

## Future automated contract

A future test should conceptually do:

```text
config + template + profile
        ↓
RepoForge renderer
        ↓
generated README
        ↓
compare with approved golden snapshot
```

Changes to an approved snapshot should therefore be reviewed as a documentation-design change, not treated as incidental test output.
