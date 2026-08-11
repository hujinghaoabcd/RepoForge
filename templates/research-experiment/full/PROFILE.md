# Research Experiment — Full Profile

Use Full for complex reproducibility repositories where the README must coordinate multiple experiment families and preserve result identity.

## Goal

A reader should be able to understand exactly how the paper's evidence is produced, which artifacts correspond to which table/figure, and which settings matter for fair comparison.

## Default structure

```text
Paper / project identity
Highlights
Model overview
Datasets and data identity
Environment and hardware
Fastest start
Available baselines / variants
Experiment protocol
  splits
  preprocessing
  seeds
  metrics
  model selection
  tuning policy
Reproduce main results
Ablation / sensitivity
Statistical testing
Expected outputs / artifact identity
Checkpoints / predictions / logs
Documentation map
Interpretation / reproducibility boundaries
Citation
License
```

## Full-specific rules

- distinguish train, evaluate, infer, ablate, tune, and summarize commands;
- expose fair baseline-tuning policy when comparative claims depend on it;
- keep per-seed results when significance testing or uncertainty claims need them;
- identify checkpoints, predictions, configs, logs, and summary tables by stable paths or run IDs;
- disclose hardware assumptions when they affect feasibility or batch-size equivalence;
- distinguish published/pretrained checkpoints from newly trained ones;
- state which scripts regenerate paper tables and figures;
- document known nondeterminism and acceptable tolerance where exact bitwise reproduction is unrealistic.

## Full is not a lab notebook

Do not put internal trial history, failed runs, reviewer-response chronology, or every hyperparameter search result in README. Link durable experiment manifests and archived artifacts instead.
