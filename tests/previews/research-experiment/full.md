<p align="center">
  <img src="../../../assets/logo.svg" alt="ForecastBench" width="280">
</p>

# ForecastBench

**A full reproducibility repository for multi-dataset, multi-seed traffic forecasting experiments.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#environment-and-hardware) [![Paper](https://img.shields.io/badge/paper-study-blue)](#citation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#reproducibility-boundaries) [![Reproducibility](https://img.shields.io/badge/reproducibility-full-brightgreen)](#experiment-protocol) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Paper · Data · Protocol · Main Results · Ablations · Artifacts · Citation

Paper: docs/paper.md

## Highlights

- one command family reproduces the proposed model across four benchmark datasets
- baseline tuning uses a documented shared search policy rather than ad-hoc per-model choices
- main claims are reported over five fixed seeds with per-seed predictions retained
- ablation, sensitivity, and significance analyses use versioned experiment manifests

## Model Overview

ForecastBench evaluates a graph-based spatiotemporal forecasting model and a controlled set of temporal, graph, and adaptive-graph baselines under one shared data and evaluation contract.

## Datasets and Data Identity

| Dataset | Role | Expected path | Identity / preprocessing |
| --- | --- | --- | --- |
| **PeMSD3** | benchmark | `data/PeMSD3/data.npz` | 5-minute flow observations; chronological 60/20/20 split; train-only Z-score statistics |
| **PeMSD4** | benchmark | `data/PeMSD4/data.npz` | same preprocessing contract; dataset-specific graph metadata versioned with the input |
| **PeMSD7** | benchmark | `data/PeMSD7/data.npz` | same preprocessing contract; large-node benchmark used to expose scalability limits |
| **PeMSD8** | benchmark | `data/PeMSD8/data.npz` | same preprocessing contract; reference dataset for examples and smoke checks |

## Environment and Hardware

Install the pinned experiment environment. Exact package versions and CUDA/PyTorch build information should be captured in the lock file or environment export used for published runs.

```bash
python -m pip install -r requirements-lock.txt
```

Published main runs assume one CUDA-capable GPU per training process. Multi-GPU launchers may parallelize independent dataset/seed jobs, but they must not silently change per-run batch size or optimization semantics.

## Fastest Start

```bash
python scripts/train.py --config configs/main/pemsd8.yml --seed 42 --epochs 2 --smoke-test
```

A successful smoke run writes a resolved config, one checkpoint, and metric JSON under `results/smoke/pemsd8/` without claiming paper-level performance.

## Available Models and Baselines

| Model | Role | Config | Tuning policy |
| --- | --- | --- | --- |
| **ProposedModel** | proposed method | `configs/main/{dataset}.yml` | primary hyperparameters fixed by the paper protocol; dataset-specific values must be declared in config |
| **STGCN** | graph baseline | `configs/baselines/stgcn.yml` | shared baseline search budget with validation-only model selection |
| **DCRNN** | recurrent graph baseline | `configs/baselines/dcrnn.yml` | shared baseline search budget with validation-only model selection |
| **AGCRN** | adaptive graph baseline | `configs/baselines/agcrn.yml` | shared baseline search budget with validation-only model selection |
| **GRU** | temporal baseline | `configs/baselines/gru.yml` | shared hidden-size/dropout search budget on the validation split |

## Experiment Protocol

- **Input / horizon:** 12 historical 5-minute steps predict the next 12 steps
- **Split:** chronological 60% train / 20% validation / 20% test for every dataset
- **Preprocessing:** flow-only input; Z-score parameters fitted on training data and reused unchanged for validation/test
- **Seeds:** 42, 43, 44, 45, 46 for the main model and significance-bearing baseline comparisons
- **Metrics:** MAE, RMSE, and MAPE reported overall and by forecast horizon
- **Model selection:** select the best validation MAE checkpoint per seed, then evaluate that checkpoint once on test data
- **Baseline tuning:** each tunable baseline receives a documented equal search budget; test metrics are never used for hyperparameter selection
- **Gradient / training controls:** gradient clipping, early stopping, learning-rate schedule, and maximum epochs are declared in resolved configs and saved with each run

## Reproducing the Main Results

### Run the proposed model on all datasets and seeds

Execute the canonical experiment manifest. Independent jobs may be parallelized externally without changing the per-run configuration.

```bash
python scripts/run_manifest.py manifests/main_5seeds.yml
```

### Run the comparison baselines

Train and evaluate the approved baseline configurations under the same split, preprocessing, seed, and metric contract.

```bash
python scripts/run_manifest.py manifests/baselines_5seeds.yml
```

### Rebuild the main result table

Aggregate only completed, identity-checked result records into the paper-facing summary table.

```bash
python scripts/summarize.py manifests/main_table.yml --output reports/main_table.csv
```

## Ablation and Sensitivity Studies

### Ablation study

Run the declared component-removal variants with the same seed and data protocol as the full model.

```bash
python scripts/run_manifest.py manifests/ablation_5seeds.yml
```

### Sensitivity analysis

Evaluate selected hierarchy, regularization, or architectural parameters without reusing the test split for selection.

```bash
python scripts/run_manifest.py manifests/sensitivity.yml
```

### Horizon-wise analysis

Aggregate saved predictions to compare error growth across the 12 forecast horizons.

```bash
python scripts/analyze_horizons.py results/ --manifest manifests/main_5seeds.yml
```

## Statistical Testing

Significance tests use paired per-seed metrics for runs that share the same dataset, split, target, horizon, and seed identity. The test name, alternative, correction policy, and effect-size summary belong in the generated report rather than being inferred from mean values alone.

```bash
python scripts/significance.py --manifest manifests/significance.yml --output reports/significance.csv
```

## Result and Artifact Identity

| Artifact | Stable location / rule | Purpose |
| --- | --- | --- |
| **Resolved configuration** | `results/{dataset}/{model}/seed-{seed}/config.resolved.yml` | exact parameters used by the run |
| **Best checkpoint** | `results/{dataset}/{model}/seed-{seed}/checkpoints/best.pt` | validation-selected model evaluated on the test split |
| **Per-seed metrics** | `results/{dataset}/{model}/seed-{seed}/metrics.json` | auditable MAE/RMSE/MAPE values and run identity |
| **Predictions** | `results/{dataset}/{model}/seed-{seed}/predictions.npz` | horizon-wise analysis, significance checks, and paper-figure regeneration |
| **Training log** | `results/{dataset}/{model}/seed-{seed}/train.jsonl` | optimization diagnostics and selected-checkpoint trace |
| **Aggregated report** | `reports/main_table.csv` | generated paper-facing summary, never the sole source of raw evidence |

## Published Checkpoints and Predictions

- **Reference checkpoints:** releases/<paper-version>/checkpoints/ — selected published checkpoints for evaluation without retraining
- **Reference predictions:** releases/<paper-version>/predictions/ — predictions used to regenerate reported horizon-wise and significance analyses
- **Experiment manifests:** manifests/ — versioned definitions connecting dataset, model, seed, and analysis families

## Expected Results

Example values below illustrate the table contract only. A real repository must populate them from identity-checked per-seed result files and should report dispersion when the paper makes stochastic-comparison claims.

| Dataset | Model | Seeds | Metric | Summary |
| --- | --- | --- | --- | --- |
| PeMSD8 | ProposedModel | 5 | MAE | 15.2 ± 0.1 |
| PeMSD8 | STGCN | 5 | MAE | 16.4 ± 0.2 |
| PeMSD4 | ProposedModel | 5 | MAE | 19.1 ± 0.2 |

## Documentation Map

- **Reproduction Guide:** docs/REPRODUCIBILITY.md — end-to-end server and local workflows
- **Dataset Guide:** docs/DATASETS.md — source, preprocessing, graph metadata, and checksums
- **Baseline Protocol:** docs/BASELINES.md — tuning budgets, approved configurations, and fairness rules
- **Experiment Manifests:** manifests/ — executable definitions of main, baseline, ablation, and sensitivity runs
- **Result Identity:** docs/RESULTS.md — run IDs, checkpoint selection, predictions, and report generation

## Reproducibility Boundaries

- exact floating-point values may vary across GPU architecture and library builds; published tolerances should be documented where bitwise equality is unrealistic
- a result is not considered paper-reproducible unless dataset identity, resolved config, checkpoint, seed, and metric implementation are all known
- smoke-test commands verify plumbing only and must not be compared with paper metrics
- aggregated means are insufficient for significance claims when per-seed or paired outputs are required
- baseline fairness depends on the declared tuning budget and model-selection rule, not only on using the same train/test split

## Citation

Cite the study paper for the reported scientific results and cite the software release or archive when this codebase is used to reproduce or extend them.

Paper: docs/paper.md

Software citation metadata: [`CITATION.cff`](CITATION.cff).

## License

ForecastBench is released under the MIT License.
