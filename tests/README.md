# RepoForge preview tests

This directory is the visual and regression-test area for RepoForge templates.

RepoForge models README generation along two axes:

- **project type**: `scientific-python`, `research-algorithm`, `research-experiment`, `django-package`, `web-application`, `frontend-library`, `desktop-application`;
- **profile**: `minimal`, `standard`, `full`.

That gives **21 independent preview combinations**.

## Rule: profiles are separate artifacts

`minimal`, `standard`, and `full` are not three conditional views inside one preview file. Each profile has its own template, rendered example, configuration, and golden snapshot.

For example:

```text
templates/scientific-python/
├── minimal/
│   ├── README.template.md
│   └── README.example.md
├── standard/
│   ├── README.template.md
│   └── README.example.md
└── full/
    ├── README.template.md
    └── README.example.md

tests/previews/scientific-python/
├── minimal.md
├── standard.md
└── full.md
```

The same separation should be used for every project type.

## Why keep previews in tests?

These files serve two purposes:

1. **Visual review now** — each concrete profile can be opened and reviewed as a finished README.
2. **Golden snapshots later** — once the renderer is implemented, each configuration can be rendered and compared with its own approved snapshot.

## Future automated contract

```text
one profile config
      +
one profile template
      ↓
RepoForge renderer
      ↓
one generated README
      ↓
compare with the matching golden snapshot
```

A Minimal template change must not implicitly modify Standard or Full output. Changes to snapshots are therefore explicit documentation-design changes.
