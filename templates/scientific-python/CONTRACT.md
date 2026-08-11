# Scientific Python Template Contract

This contract defines README structures for reusable scientific Python packages.

## Core rule: profiles are independent

`minimal`, `standard`, and `full` are three separate templates. They are not one large Jinja template controlled by profile-condition branches.

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
```

Each profile may evolve independently and must have its own rendered golden snapshot under `tests/previews/scientific-python/`.

## Audience

Primary readers include researchers evaluating fit, users installing and running a first example, developers locating API and contribution guidance, and authors needing citation and reproducibility information.

## Common questions

Regardless of profile depth, a first-time visitor should quickly understand:

1. what scientific problem the package addresses;
2. how to install it;
3. how to run a useful first example;
4. where the authoritative documentation lives;
5. how to cite it when academic use is expected.

Additional questions belong to Standard or Full depending on project maturity and scientific complexity.

## Minimal profile

Use for small, focused scientific utilities.

Expected structure:

```text
Project name
One-line positioning
Light badge set
Short introduction
Installation
Quick Start
Documentation
Citation (when relevant)
License
```

Minimal deliberately omits large capability matrices, architecture, detailed validation prose, model-selection guidance, development setup, and long limitation sections.

## Standard profile

Default for most reusable scientific Python packages.

Expected structure:

```text
Optional logo
Project name
One-line scientific positioning
Badges / navigation
Why <Project>?
Features
Installation
Quick Start
Methods / capabilities
Validation (when scientifically material)
Documentation
Citation
Support / Contributing
License
```

Standard should be complete enough for a normal package user without becoming a manual.

## Full profile

Use for mature, broad, or scientifically complex packages.

Expected structure:

```text
Logo / project identity
One-line scientific positioning
Badges / language / navigation
What <Project> Is
Why Use It?
Scientific Scope
Features
Installation
  Stable release
  Optional features
  Development install
Five-Minute Example
Method Catalogue
Choosing a Method
Data Contracts and Conventions
Representative Workflow
Validation and Reproducibility
Examples
Documentation
Project Status and API Stability
Limitations
Citation
Support / Contributing
License
```

Full still treats README as an entry point. Long theory, exhaustive API listings, benchmark tables, complete validation protocols, troubleshooting, and release engineering belong in `docs/`.

## Shared content principles

- the first useful code example must appear early;
- installation commands must be copyable;
- scientific assumptions and limitations must not be hidden by marketing language;
- citation metadata should use `CITATION.cff` when appropriate;
- detailed material should link to authoritative documentation rather than being duplicated in README;
- badge density should scale with the profile instead of becoming decorative clutter.

## Reference-analysis dimensions

Reference cases are compared by component rather than copied wholesale:

- header/logo presentation;
- tagline quality;
- badge density;
- navigation links;
- Why/Introduction structure;
- Features structure;
- installation clarity;
- time-to-first-example;
- example quality;
- API/documentation handoff;
- validation/reliability communication;
- citation treatment;
- contributing/support treatment;
- README length and deliberate documentation handoff.

See `references.md` for the current reference pool and design decisions.

## Status

The three scientific-Python profiles are now structurally separated. The next renderer must select exactly one profile directory and render exactly one README from that profile.
