# Research Algorithm README references

This file records design references by **README function**, not as templates to copy wholesale.

## External reference pool

Useful families to inspect when refining this template include:

- SHAP-style method libraries — strong method identity, examples, interpretation, and citation needs;
- UMAP-style algorithm packages — motivation, conceptual method explanation, installation, examples, and paper handoff;
- POT / optimal-transport libraries — mathematical method families presented as reusable software;
- specialized scientific estimators and solvers — compact theory plus executable API examples;
- research-code repositories that evolved into maintained packages — useful for identifying what should move from paper README into package documentation.

## Internal stress cases

RepoForge's own research projects provide important counterexamples and stress cases:

- an original spatial-explanation method where the **estimand** must be explicit;
- a learned spatial metric / latent-map method where the README must distinguish the scientific idea from the implementation;
- a new nonlinear space-time model where equations are useful but a full derivation would overwhelm the README.

## Section champions to seek

When the reference pool is expanded, compare candidates specifically for:

| README function | What to look for |
| --- | --- |
| Scientific problem | explains the gap without a literature-review dump |
| Contribution | states what is new in concrete terms |
| Method overview | one figure/equation/algorithm sketch that makes the method legible |
| Quick start | runnable code that exercises the actual method |
| Interpretation | says what outputs mean and what they do not mean |
| Validation | separates implementation checks from empirical performance |
| Limitations | scientific boundary, not generic disclaimer text |
| Citation | software + paper citation without ambiguity |

## Initial RepoForge decision

The research-algorithm README should sit between a package landing page and a method paper:

- more scientific explanation than `scientific-python`;
- much less experiment protocol than `research-experiment`;
- enough formalism to identify the method precisely;
- enough software guidance to run it immediately;
- strong validation and interpretation boundaries when scientific misuse is possible.
