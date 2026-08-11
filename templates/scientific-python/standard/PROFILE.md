# Scientific Python — Standard Profile

The Standard profile is the default README for a maintained, reusable scientific Python package.

It should explain **why the package exists**, show the main capabilities, get a user to a first result quickly, and communicate enough validation and citation information to support scientific use.

## Goal

A first-time visitor should be able to decide whether the package fits their task and complete a representative first workflow without reading the full documentation site.

## Default structure

```text
Optional logo
Project name
One-line scientific positioning
Core badges
Key navigation links

Why <Project>?
Features
Installation
Quick Start
Methods and Capabilities          [when several methods exist]
Validation                        [recommended for numerical/statistical software]
Documentation
Citation                          [recommended for research software]
Limitations                       [only when concise and important]
Support and Contributing
License
```

## Required content rules

- explain the scientific problem or workflow in `Why`, not the development history;
- keep Features focused on user-visible capabilities rather than implementation internals;
- provide one primary installation path and, only when useful, a small number of optional extras;
- make the Quick Start self-contained and representative;
- use a compact method/capability table only when it helps readers choose among multiple scientific operations;
- summarize validation evidence without reproducing the full validation protocol;
- link to the authoritative documentation instead of duplicating manuals;
- include academic citation guidance when expected users are researchers.

## Size guidance

Target roughly **100–220 rendered lines** for most packages.

A Standard README may be longer when code blocks or a compact capability table genuinely improve first-use understanding, but it should not become a documentation site.

## Header rules

A logo is optional. If present, it should appear once and should not be followed by a second decorative text rendering of the project name.

Use roughly **3–6 badges**. Prefer badges that answer practical questions:

- package/release;
- tests or CI;
- supported Python;
- documentation;
- DOI when relevant;
- license.

Keep navigation to one concise line such as:

```text
Documentation · Examples · API · Citation
```

## Why section

`Why <Project>?` should normally be one or two short paragraphs:

1. identify the recurring scientific problem, friction, or gap;
2. explain the package's approach and boundary.

Avoid generic claims such as “fast, powerful, easy to use” unless they are made concrete.

## Features section

Prefer **4–8 capabilities**. Each item should use the pattern:

```text
Capability — user-visible purpose or scientific value.
```

Do not list internal modules simply because they exist.

## Quick Start contract

The snippet must create or load every required input that is not obvious from the import itself. A reader should not need to search the repository to discover what `X`, `coords`, or another variable means.

The example should normally fit on one screen and demonstrate the package's dominant workflow.

## Validation contract

For numerical, statistical, geospatial, simulation, or scientific-model packages, Standard should normally include a short Validation section covering the strongest available evidence, for example:

- independent reference calculations;
- analytical or textbook cases;
- regression tests;
- cross-package comparisons;
- explicit failure behavior.

Detailed tolerances, benchmark datasets, and claim boundaries belong in dedicated validation documentation.

## When to use Full instead

Move to Full when the README must summarize several of these to represent the package honestly:

- a broad method/model catalogue;
- method-selection guidance;
- multiple data contracts;
- reproducibility guarantees;
- API stability or compatibility policy;
- substantial scientific interpretation boundaries;
- several installation or deployment modes;
- project status that affects scientific use.
