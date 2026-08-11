# Research Algorithm Template Contract

This family is for repositories whose primary identity is an **original scientific or technical method** rather than a general-purpose package or a paper experiment bundle.

Typical examples include a new estimator, decomposition, optimization method, explanation method, spatial model, or algorithmic framework whose implementation is intended to be understood and reused beyond one experiment script.

## Core distinction

Use `research-algorithm` when the README must answer:

1. What scientific or technical problem is the method designed to solve?
2. What is new about the method or formulation?
3. What exactly does the implementation compute?
4. How can a reader run a minimal example?
5. What evidence supports the implementation or claim?
6. What are the method's validity and interpretation boundaries?
7. How should the method and software be cited?

Do **not** use this family for repositories centered on reproducing a paper's benchmark tables, datasets, seeds, baselines, and experiment commands. Those belong to `research-experiment`.

## Independent profiles

`minimal`, `standard`, and `full` are separate templates with separate profile contracts, configs, examples, and snapshots.

```text
templates/research-algorithm/
├── CONTRACT.md
├── references.md
├── minimal/
├── standard/
└── full/
```

## Shared rules

- scientific contribution must be stated more precisely than marketing language;
- the first runnable example should appear early;
- equations belong in README only when they clarify the method's identity or output contract;
- detailed derivations, proofs, long pseudocode, and full experiment tables belong in `docs/` or the paper;
- validation claims must state what was checked rather than saying only that results are "correct";
- limitations and interpretation boundaries should be visible when misuse is plausible;
- citation should distinguish software citation from method-paper citation when both exist.

## Profile selection

### Minimal

Use for a focused method implementation with one dominant operation and a small public surface.

### Standard

Default for an original method that needs motivation, a method overview, contributions, a runnable example, validation, limitations, and citation.

### Full

Use when responsible use requires concise explanation of the formal objective/estimand, algorithm stages, interpretation contract, validation dimensions, computational characteristics, or reproducibility guarantees.

## What should remain outside README

Even in Full, move these to authoritative documentation when substantial:

- complete proofs and derivations;
- every theorem or proposition;
- full API reference;
- exhaustive benchmark tables;
- full ablation and sensitivity result sets;
- complete hyperparameter grids;
- internal implementation-stage logs;
- release engineering procedures.
