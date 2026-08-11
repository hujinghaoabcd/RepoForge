# Research Experiment Template Contract

This family is for repositories whose main public purpose is to reproduce, evaluate, extend, or audit the experiments behind a paper or technical study.

Use `research-experiment` when the README must answer questions such as:

1. Which paper, model, or study does this repository correspond to?
2. Which datasets and exact data identities are expected?
3. Which environment and hardware assumptions matter?
4. What is the fastest command that reproduces a meaningful result?
5. What training/evaluation protocol produced the reported numbers?
6. Which baselines, seeds, metrics, and splits are part of the comparison contract?
7. Where are checkpoints, predictions, logs, and final tables written?
8. How can a reader reproduce the main table, ablations, or statistical tests?

Do **not** use this family for a reusable original method whose main identity is the algorithm itself. That belongs to `research-algorithm`.

## Independent profiles

`minimal`, `standard`, and `full` are separate artifacts. Each implemented profile should contain:

```text
PROFILE.md
README.template.md
README.example.md
config.example.yml
```

and have a matching visible preview under:

```text
tests/previews/research-experiment/<profile>.md
```

## Shared rules

- identify the paper/study immediately;
- make the fastest successful reproduction path obvious;
- separate environment setup from experiment protocol;
- state dataset identity and preprocessing assumptions explicitly when they affect comparability;
- report seeds, splits, metrics, model-selection rules, and checkpoint identity when relevant;
- distinguish training, evaluation, inference, ablation, and statistical-analysis commands;
- explain where generated artifacts are saved;
- avoid claiming reproducibility when required data, checkpoints, or configs are unavailable;
- keep long derivations and method theory in the paper or method documentation;
- keep full experiment logs and result dumps outside the README.

## Profile selection

### Minimal

Use for a focused companion repository with one main environment, one dataset path, and one dominant run/evaluate path.

### Standard

Default for most paper-code repositories. It should expose model overview, datasets, environment, quick reproduction, protocol, main results, repository structure, and citation.

### Full

Use when reproducibility depends on several of the following:

- multiple datasets;
- several baselines;
- multiple seeds;
- ablations or sensitivity studies;
- statistical significance testing;
- checkpoint/result identity;
- distributed or multi-GPU execution;
- artifact manifests;
- strict train/validation/test contracts;
- several experiment families.

## What should remain outside README

Even in Full, move these to dedicated files or archived artifacts when substantial:

- complete hyperparameter search logs;
- every command permutation;
- full tensorboard or wandb history;
- raw prediction files;
- complete result matrices;
- detailed mathematical derivations;
- reviewer-response history;
- internal development notes;
- large benchmark tables better served by generated reports.
