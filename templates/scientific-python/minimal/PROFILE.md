# Scientific Python — Minimal Profile

The Minimal profile is a complete README for a small, focused scientific Python package. It is not a truncated Standard README.

## Goal

A first-time visitor should understand the package and run one meaningful example within about one minute.

## Required structure

```text
Project name
One-line scientific tagline
Essential badges                  [optional, max 3]
One short description             [optional, max 2 sentences]

Installation
Quick Start
Documentation / key links
Citation                          [when academic use is expected]
License
```

## Required content rules

- the tagline must state what the package does, not use marketing language;
- installation should normally contain one primary command;
- the Quick Start must be self-contained apart from the installed package and declared common dependencies;
- the Quick Start should demonstrate the package's normal scientific workflow rather than a synthetic API tour;
- documentation should be one concise link or link line, not a document map;
- citation is included only when the software is intended to be cited academically;
- license must be explicit.

## Size guidance

Target roughly **40–100 rendered lines** for most projects.

Minimal should normally avoid:

- feature catalogues;
- method matrices;
- architecture descriptions;
- development installation instructions;
- validation methodology details;
- compatibility matrices;
- long limitation sections;
- changelog or roadmap content;
- exhaustive badges;
- multiple representative examples.

Those belong in Standard, Full, or linked documentation.

## Header rules

A Minimal README should prefer a plain project title. A logo is allowed only when it materially helps project identity.

Use no more than three badges by default. Good candidates are:

1. package/release status;
2. supported Python version or tests;
3. license.

Do not create a badge wall.

## Quick Start contract

The example must not contain unexplained variables such as `X`, `data`, `coords`, or `model_input` unless those variables are created in the shown snippet.

Prefer:

```python
import numpy as np
from package import Method

x = ...
y = ...
result = Method(...).fit(x, y)
print(result)
```

Avoid examples that require readers to first find another file, download a dataset, or infer hidden preprocessing.

## Minimal vs Standard

Move to Standard when the README needs any of the following to explain the package correctly:

- a real `Why` section;
- a feature list;
- several method families;
- validation claims that need explanation;
- multiple installation modes;
- representative examples beyond the Quick Start;
- explicit limitations or scientific interpretation guidance.

## Minimal vs Full

Minimal should never attempt to summarize a broad scientific platform, a large model catalogue, or a complex validation/reproducibility contract. Use Full for those cases.
