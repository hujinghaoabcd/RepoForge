# Scientific Python Template Contract

This contract defines the intended README structure for reusable scientific Python packages.

## Audience

Primary readers include:

- researchers evaluating whether the package fits a scientific task;
- users who need to install and run a first example quickly;
- developers who need links to API, contribution, and validation documentation;
- authors who need correct citation and reproducibility information.

## Primary question

A first-time visitor should be able to answer, within a short scan:

1. What scientific problem does this package address?
2. Why would I use it instead of writing the method myself or using an existing package?
3. How do I install it?
4. What is the smallest useful example?
5. What methods/capabilities are supported?
6. Where are the complete docs and API?
7. How has the implementation been validated?
8. How should I cite it?

## Standard profile: section order

```text
Header / optional logo
Project name
One-line scientific positioning
Badges and key links
Language switch (when maintained)

Why <Project>?
Features
Installation
Quick Start
Methods / Capabilities          [conditional]
Representative Example         [conditional]
Validation                     [conditional; recommended for numerical packages]
Documentation
Citation                       [recommended for research software]
Limitations                    [conditional]
Support / Contributing
License
```

This order is based on the curated reference analysis in [`references.md`](references.md).

## Required sections

For `standard` scientific Python packages:

- project identity and one-line positioning;
- scientific motivation or clear problem statement;
- key capabilities;
- installation;
- minimal executable quick start;
- documentation link/map;
- license.

## Conditionally required sections

Use when relevant:

- **Validation** — when numerical/statistical correctness is scientifically material;
- **Citation** — when the package is intended for academic use;
- **Methods / Models** — when the package exposes multiple scientific methods;
- **Limitations** — when outputs can be easily over-interpreted or methods have important validity boundaries;
- **Examples / Gallery** — when visual or workflow examples communicate usage better than API prose;
- **Data** — when bundled datasets or strict data contracts are central to usage.

## Content that should normally move to docs

When substantial, do not keep these in the README:

- full mathematical derivations;
- complete model-by-model manuals;
- exhaustive API listings;
- full benchmark tables;
- long implementation-stage status reports;
- detailed release engineering instructions;
- complete validation protocols;
- large troubleshooting sections.

The README may summarize these topics and link to the authoritative document.

## Profile mapping

### Minimal

Use for small, focused scientific utilities or intentionally concise mature project portals:

```text
Header
What it does
Installation
Quick example
Docs/support
Citation (if relevant)
License
```

### Standard

Default structure described above. This is the first implemented template profile.

### Full

May additionally surface concise summaries of:

- method selection;
- data contracts;
- validation scope;
- reproducibility guarantees;
- compatibility/API stability;
- architecture when it helps users understand extension points.

Detailed material still belongs in `docs/`.

## Reference-analysis dimensions

Each external reference case is evaluated by section, not copied wholesale.

Compare at least:

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
- README length and what is deliberately moved elsewhere.

See [`references.md`](references.md) for the current curated pool and section-by-section decisions.

## Internal stress tests

Existing research packages are used as practical regression cases, especially where their current README styles differ substantially. The template should improve consistency without erasing project-specific scientific identity.

Current stress-test categories include:

- broad model libraries;
- focused scientific tools;
- packages with many executable workflows;
- packages whose current README contains development-stage detail;
- theory-heavy statistical packages;
- original research methods requiring interpretation boundaries.

## Implemented artifacts

```text
templates/scientific-python/
├── CONTRACT.md
├── references.md
├── README.template.md
└── README.example.md
```

The corresponding structural previews live in:

```text
tests/previews/scientific-python.md
```

## Status

**First standard-profile draft implemented.**

Next steps:

1. define a machine-readable example configuration;
2. implement the smallest Jinja renderer;
3. generate `minimal`, `standard`, and `full` outputs automatically;
4. compare generated output with approved golden snapshots;
5. stress-test the standard profile against representative real scientific packages.
