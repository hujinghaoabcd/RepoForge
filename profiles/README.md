# Documentation Profiles

Profiles control README depth without changing the project's semantic type.

## Core rule

`minimal`, `standard`, and `full` are **independent template artifacts**.

They are not three branches inside one oversized README template. For every project type, RepoForge should use this shape:

```text
templates/<project-type>/
├── minimal/
│   └── README.template.md
├── standard/
│   └── README.template.md
└── full/
    └── README.template.md
```

Each profile has its own configuration, rendered example, and golden snapshot. A change to Minimal must not implicitly change Standard or Full output.

Profiles may share small reusable partials, but section order, required fields, and overall README depth belong to the profile itself.

## Minimal

For demos, prototypes, focused utilities, and small plugins.

Typical content:

- identity and one-line description;
- essential badges or links;
- short feature summary;
- quickest installation/run path;
- one useful example or screenshot;
- documentation/support link if available;
- license.

## Standard

Default for most maintained open-source projects.

Adds, where relevant:

- Why / motivation;
- structured capabilities;
- installation variants;
- quick start and representative examples;
- documentation map;
- validation/testing summary;
- citation for research software;
- contributing/support entry points.

## Full

For mature research software, complex applications, and reproducible experiment repositories.

May additionally surface concise summaries of:

- architecture;
- reproducibility;
- deployment;
- security;
- compatibility;
- benchmark/validation scope;
- operational or scientific limitations.

A `full` README is not permission to duplicate the entire documentation site. Detailed material should still move into `docs/` and be linked from the README.
