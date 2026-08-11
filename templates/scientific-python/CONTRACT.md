# Scientific Python Template Contract

This contract defines README structures for reusable scientific Python packages.

## Core rule: profiles are independent

`minimal`, `standard`, and `full` are three separate templates. They are not one large Jinja template controlled by profile-condition branches.

```text
templates/scientific-python/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   └── README.example.md
├── standard/
│   ├── PROFILE.md
│   ├── README.template.md
│   └── README.example.md
└── full/
    ├── PROFILE.md
    ├── README.template.md
    └── README.example.md
```

Each profile evolves independently and has its own rendered golden snapshot under `tests/previews/scientific-python/`.

## Choosing a profile

| Profile | Use when | README should answer |
| --- | --- | --- |
| **Minimal** | the package is small, focused, and needs little explanation beyond one workflow | What is it? How do I install it? What is the fastest useful example? |
| **Standard** | the package is a maintained reusable scientific library with several user-visible capabilities | Why does it exist? What can it do? How is it validated? Where are the docs? |
| **Full** | the package is broad, mature, or scientifically complex and responsible use requires scope, selection, convention, or reproducibility guidance | What is in scope? Which method should I choose? What conventions and boundaries matter? How stable and reproducible is the software? |

Do not choose Full merely because a project is important. Choose it only when the additional sections materially help users use the package correctly.

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

See [`minimal/PROFILE.md`](minimal/PROFILE.md) for the complete contract.

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
Methods / capabilities       [when useful]
Validation                   [recommended for numerical/statistical software]
Documentation
Citation                     [recommended for research software]
Limitations                  [only when concise and important]
Support / Contributing
License
```

Standard should be complete enough for a normal package user without becoming a manual.

See [`standard/PROFILE.md`](standard/PROFILE.md) for the complete contract.

## Full profile

Use for mature, broad, or scientifically complex packages.

Expected structure:

```text
Optional logo
Project name
One-line scientific positioning
Badges / language / navigation
What <Project> is
Why use it?
Scientific scope
Features
Installation
  Stable release
  Optional features
  Development install
Five-minute example
Method catalogue
Choosing a method
Data contracts and conventions
Representative workflow
Validation and reproducibility
Examples
Documentation
Project status and API stability
Limitations and interpretation boundaries
Citation
Support / Contributing
License
```

Full still treats README as an entry point. Long theory, exhaustive API listings, benchmark tables, complete validation protocols, troubleshooting, and release engineering belong in `docs/`.

See [`full/PROFILE.md`](full/PROFILE.md) for the complete contract.

## Shared content principles

- the first useful code example must appear early;
- installation commands must be copyable;
- Quick Start examples must define the inputs they use;
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

See [`references.md`](references.md) for the current reference pool and design decisions.

## Status

The three scientific-Python profiles are independently defined and have independent templates, examples, and preview snapshots. A future renderer must select exactly one profile directory and render exactly one README from that profile.
