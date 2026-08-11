# Research Experiment — Standard Profile

Standard is the default for most paper-code repositories.

## Goal

A reader should be able to reproduce the main experimental path without reading the whole paper or guessing hidden settings.

## Default structure

```text
Paper / project identity
Model overview
Datasets
Environment
Quick reproduction
Experiment protocol
Main results
Repository structure
Citation
License
```

## Protocol contract

Standard should normally state:

- train/validation/test split or official split identity;
- preprocessing that affects comparability;
- evaluation metrics;
- seed policy when randomness is material;
- model-selection or checkpoint-selection rule;
- primary command for training and/or evaluation;
- expected output directory.

## Keep outside Standard

Move to Full when the public README must coordinate several datasets, many baselines, multi-seed tables, ablations, significance tests, distributed execution, or complex artifact identity.
