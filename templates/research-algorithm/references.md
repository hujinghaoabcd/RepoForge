# Research Algorithm README references

This file records design references by **README function**, not as templates to copy wholesale.

The `research-algorithm` family is for repositories whose public identity is a scientific or technical method. The README must explain enough of the method to make the implementation scientifically legible while still behaving like a software landing page rather than a paper manuscript.

## Core external reference pool

### SHAP — method identity and immediate examples

Repository: https://github.com/shap/shap

Useful patterns:

- opens with a precise one-line method identity: game-theoretic model explanation;
- moves quickly from method positioning to installation and concrete model examples;
- keeps the mathematical lineage visible without requiring the README to reproduce the full derivation;
- links method identity, software package, papers, and contribution workflow clearly.

RepoForge takeaway: a method README should make the **scientific object** recognizable before describing implementation breadth.

### LIME — intuition and interpretation boundary

Repository: https://github.com/marcotcr/lime

Useful patterns:

- explains what an explanation is in intuitive terms;
- uses a compact conceptual description of the local approximation rather than a literature review;
- connects screenshots and examples directly to how users should interpret outputs;
- makes the local-vs-global distinction central to understanding the method.

RepoForge takeaway: when a method can be misinterpreted, a short **interpretation contract** can be more important than a large feature list.

### UMAP — algorithm concept, paper handoff, and citation

Repository: https://github.com/lmcinnes/umap

Useful patterns:

- states the algorithm's conceptual target in plain language;
- points readers to the paper for detailed mathematics;
- keeps software use accessible even though the underlying theory is substantial;
- distinguishes citation of the software from citation of the algorithm/method papers.

RepoForge takeaway: the README should identify the formal scientific idea, then deliberately hand detailed theory to the paper or method documentation.

### DiCE — problem framing, optimization idea, and feasibility constraints

Repository: https://github.com/interpretml/DiCE

Useful patterns:

- starts from the scientific/user problem before describing the implementation;
- explains the method as an optimization problem in accessible terms;
- treats feasibility, actionability, and feature constraints as part of the method contract rather than afterthoughts;
- provides a compact end-to-end workflow after the motivation.

RepoForge takeaway: constraints that determine whether outputs are scientifically or practically meaningful belong near the core method explanation.

### PySR — Why, objective, quick start, and paper connection

Repository: https://github.com/MilesCranmer/PySR

Useful patterns:

- gives the scientific task a clear name and objective;
- has a strong `Why` section before deeper usage;
- provides a pasteable quick start using a familiar estimator API;
- keeps links to docs, forums, paper, demos, and citation highly visible;
- separates the software interface from the lower-level search-engine implementation.

RepoForge takeaway: a technically sophisticated algorithm can still present a very direct **task → objective → runnable example** path.

### Ripser.py — focused computational method and related implementations

Repository: https://github.com/scikit-tda/ripser.py

Useful patterns:

- stays focused on one computational domain and clearly enumerates supported operations;
- distinguishes the Python interface from the underlying computational engine;
- points to related implementations such as the original C++ and GPU variants;
- includes software and algorithm citations separately.

RepoForge takeaway: method provenance and implementation provenance may need separate citation paths.

### symbolic_deep_learning — paper-first implementation repository

Repository: https://github.com/MilesCranmer/symbolic_deep_learning

Useful patterns:

- makes the paper identity explicit immediately;
- exposes paper, blog, video, and demo links before implementation details;
- keeps requirements and training instructions compact.

RepoForge takeaway: this is useful as a boundary case. A repository centered on reproducing a paper belongs closer to `research-experiment`; an implementation that has become a reusable method product belongs in `research-algorithm`.

## Secondary reference pool

These are useful for individual components but should not define the whole template:

- Captum — multi-method attribution taxonomy and consistent API language;
- POT / optimal transport libraries — mathematical method families presented as reusable software;
- specialized numerical solvers — concise algorithm identity plus performance/complexity notes;
- interpretable-ML libraries — output interpretation, claim boundaries, and citation conventions;
- topology and geometry libraries — relationship between mathematical object, algorithm, and software implementation.

## Internal stress cases

RepoForge should pressure-test this family against original-method shapes rather than only polished external libraries:

1. **Estimand-heavy spatial explanation** — the README must distinguish the quantity being estimated from plotting or visualization output.
2. **Learned spatial metric / latent-map method** — the README must separate the learned geometry from physical or geographic interpretation.
3. **Nonlinear space-time method** — equations are necessary for identity, but full derivations should remain in the method paper/docs.
4. **Single narrow estimator** — should remain Minimal even if the method itself is novel.

These cases live under `tests/stress/research-algorithm/` and are renderer-backed.

## Section champions

| README function | Primary reference | RepoForge lesson |
| --- | --- | --- |
| Scientific problem | DiCE | start from the decision/scientific problem, not implementation history |
| One-line method identity | SHAP | define the scientific object immediately |
| Method intuition | LIME | explain the mechanism at the level needed for interpretation |
| Formal idea → paper handoff | UMAP | state the core concept, link detailed mathematics outward |
| Why / motivation | PySR | explain the task and why the method is useful before options |
| Quick Start | PySR / SHAP | runnable code should exercise the actual scientific method |
| Constraints / feasibility | DiCE | expose conditions that materially change validity |
| Interpretation boundary | LIME | local/global or estimand boundaries must be explicit |
| Algorithm vs implementation citation | UMAP / Ripser.py | distinguish method paper from software release when needed |
| Paper-first boundary case | symbolic_deep_learning | helps separate `research-algorithm` from `research-experiment` |

## Profile implications

### Minimal

Use when the novelty is narrow and can be identified with:

```text
Method identity
Short method statement
Installation
Quick Start
Validation summary
Citation
License
```

Novelty alone is **not** a reason to choose Full.

### Standard

Default for most original methods. It should normally add:

```text
Scientific Problem
Method Overview
one compact equation or figure when useful
Key Contributions
Validation
Limitations
Documentation
```

This is the target shape for many method papers that have become usable software.

### Full

Use only when responsible use requires several formal contracts to be visible on the project landing page:

```text
Why existing approaches are insufficient
Objective / estimand
Core formulation
Algorithm outline
Input/output interpretation
Validation categories
Sensitivity or stability boundaries
Computational characteristics
Reproducibility contract
Limitations
```

Full must still link detailed derivations, proofs, benchmark tables, and experimental protocols outward.

## Anti-patterns

Do not copy these common research-repository habits into the template:

- opening with an abstract copied directly from the paper;
- a long literature review before installation or usage;
- equations without defining what the output means;
- benchmark superiority claims presented as proof of general validity;
- mixing implementation validation with empirical performance claims;
- dumping every ablation or hyperparameter table into the README;
- treating a model architecture diagram as a substitute for a method explanation;
- citation that leaves users unsure whether to cite the method paper, software, or both.

## Current RepoForge decision

The research-algorithm README sits between a package landing page and a method paper:

- more scientific explanation than `scientific-python`;
- much less experiment protocol than `research-experiment`;
- enough formalism to identify the method precisely;
- enough software guidance to run it immediately;
- explicit validation and interpretation boundaries when misuse is possible;
- deliberate separation between **method validity**, **implementation correctness**, and **benchmark performance**.
