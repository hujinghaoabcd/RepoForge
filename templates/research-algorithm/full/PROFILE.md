# Research Algorithm — Full Profile

Use Full when responsible use of the method requires more than motivation and a quick example: the formal target, algorithm stages, interpretation contract, validation dimensions, computational behavior, or reproducibility guarantees must be visible from the repository landing page.

## Goal

A reader should understand the method as both a research contribution and a reusable software artifact without turning the README into the full paper.

## Default structure

```text
Logo / method figure
Project name
One-line contribution
Badges / paper / docs / citation links

Scientific problem
Why existing approaches are insufficient
Proposed method
  Objective / estimand
  Core formulation
  Algorithm outline
Key contributions
Installation
Five-minute example
Inputs, outputs, and interpretation
Validation
Computational characteristics
Reproducibility
Limitations
Documentation
Citation
Support / Contributing
License
```

## Rules

- identify the formal target precisely when ambiguity would change scientific interpretation;
- keep equations compact and selective; derivations belong in the paper or theory docs;
- algorithm outline should explain stages, not reproduce implementation code line by line;
- interpretation should distinguish what the returned quantities mean from claims the method does not support;
- Validation may summarize analytical recovery, synthetic recovery, external comparisons, sensitivity, and numerical tests, but full tables live elsewhere;
- computational characteristics should communicate scaling or major bottlenecks only when relevant;
- reproducibility should explain how the documented claims can be regenerated;
- limitations remain scientific and methodological, not generic legal disclaimers.

Target roughly 180–420 rendered lines.
