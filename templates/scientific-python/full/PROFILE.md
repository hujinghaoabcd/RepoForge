# Scientific Python — Full Profile

The Full profile is for mature or broad scientific Python packages whose public README must communicate more than installation and a first example.

Full is appropriate when users need concise guidance about scientific scope, method selection, data contracts, validation, reproducibility, or API stability before they can use the package responsibly.

## Goal

A first-time visitor should be able to understand the package as a scientific software product: what it covers, what it deliberately does not cover, how its major methods differ, how to start, how results are validated, and where authoritative documentation lives.

## Default structure

```text
Optional logo
Project name
One-line scientific positioning
Core badges
Language switch / key navigation

What <Project> is
Why use it?
Scientific scope
Features
Installation
Five-minute example
Method catalogue                  [when several methods exist]
Choosing a method                 [when selection is non-trivial]
Data contracts and conventions    [when scientifically material]
Representative workflow           [optional]
Validation and reproducibility
Examples                          [optional]
Documentation
Project status and API stability  [when relevant]
Limitations / interpretation boundaries
Citation
Support and Contributing
License
```

## Required content rules

- distinguish package identity (`What`) from motivation (`Why`) and validity boundary (`Scientific scope`);
- summarize broad capability without reproducing the full model/API handbook;
- expose method-selection guidance when several scientific methods can be confused or misused;
- state data, coordinate, unit, missing-value, or result-object conventions when they affect scientific validity;
- summarize validation and reproducibility evidence separately from feature claims;
- surface project maturity or API stability when users must account for it;
- state concise scientific interpretation boundaries when outputs are easy to over-interpret;
- keep detailed theory, exhaustive benchmarks, and developer procedures in `docs/`.

## Size guidance

Target roughly **180–400 rendered lines** for most broad scientific packages.

A Full README may exceed this when a compact model table or executable workflow is genuinely useful, but length alone is not a reason to choose Full.

## Header rules

A logo is appropriate for established package identity but remains optional.

Use roughly **4–8 badges**. Typical choices are:

- PyPI/release;
- tests/CI;
- coverage when meaningful;
- supported Python;
- documentation;
- DOI/archive;
- license;
- project status only when it communicates a real public contract.

Avoid badges that merely decorate the page.

## Scientific scope contract

The scope section should answer three questions:

1. What scientific workflows are in scope?
2. What adjacent tasks are deliberately out of scope?
3. Which choices remain the user's scientific responsibility?

This is especially important for spatial, statistical, simulation, optimization, and machine-learning software.

## Method catalogue contract

Use a compact table when the package exposes multiple major models or methods. The table should help users choose, not reproduce API documentation.

Useful columns include:

```text
Method | Purpose | New-data operation | Important boundary
```

Do not list every helper function.

## Method-selection contract

Include `Choosing a Method` when users could reasonably select the wrong algorithm from the catalogue.

Prefer a small decision table or a few scientifically meaningful rules. Detailed theory belongs in the method guide.

## Data-contract contract

Surface conventions only when they materially affect scientific correctness, for example:

- observation axis and array shape;
- CRS and distance units;
- missing-value behavior;
- normalization/scaling ownership;
- time indexing;
- spatial-weight conventions;
- fitted-result and prediction semantics.

## Validation and reproducibility contract

Summarize the strongest available evidence and how reproducibility is protected. Examples include:

- independent reference calculations;
- external software comparisons;
- analytical or textbook cases;
- regression fixtures;
- deterministic seeds;
- pinned example data;
- CI across supported platforms or Python versions;
- explicit failure behavior.

Do not paste complete benchmark or validation tables into the README.

## Project status and API stability

Use this section when pre-1.0 status, experimental modules, compatibility commitments, or deprecation rules affect users.

Do not use it as a development diary. Stage numbers, current coding tasks, and implementation handoff notes belong in roadmaps or developer documentation.

## Full is still a portal

The following should normally remain outside the README even in Full:

- complete mathematical derivations;
- every model parameter and return field;
- exhaustive public API inventories;
- full validation protocols;
- long benchmark/result tables;
- complete release engineering instructions;
- internal development stages;
- detailed troubleshooting.

The Full README should make those resources discoverable, not duplicate them.
