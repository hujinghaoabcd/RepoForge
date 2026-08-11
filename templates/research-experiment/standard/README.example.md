# ForecastBench

**Reproducible benchmark code for short-horizon traffic forecasting across standard sensor datasets.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#environment) [![Paper](https://img.shields.io/badge/paper-study-blue)](#citation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#environment) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Paper · Data · Reproduction · Results · Citation

Paper: docs/paper.md

## Overview

ForecastBench is a paper-oriented repository for reproducing the main training and evaluation path of a traffic forecasting study. The README documents the experiment contract; detailed model theory remains in the paper and method documentation.

## Model Overview

The study predicts the next 12 traffic-flow steps from the previous 12 observations using a graph-based spatiotemporal forecasting model and a fixed benchmark protocol.

## Datasets

| Dataset | Role | Expected path | Notes |
| --- | --- | --- | --- |
| **PeMSD8** | main benchmark | `data/PeMSD8/data.npz` | 5-minute flow observations with the documented train/validation/test split |
| **PeMSD4** | secondary benchmark | `data/PeMSD4/data.npz` | same preprocessing contract as the main benchmark |

## Environment

Install the reference Python environment before running training or evaluation.

```bash
python -m pip install -r requirements.txt
```

Hardware note: The canonical configuration is designed for one CUDA-capable GPU; CPU execution is supported for smoke tests but not representative training time.

## Quick Reproduction

### Train the main configuration

Train the proposed model on the main benchmark using the reference configuration.

```bash
python scripts/train.py --config configs/main/pemsd8.yml --seed 42
```

### Evaluate a checkpoint

Evaluate the selected checkpoint without retraining.

```bash
python scripts/evaluate.py --config configs/main/pemsd8.yml --checkpoint results/pemsd8/best.pt
```

## Experiment Protocol

- **Split:** 60% train / 20% validation / 20% test in chronological order
- **Preprocessing:** Z-score normalization fitted on the training split only; flow is the prediction target
- **Seeds:** one documented reference seed for the Standard profile; use Full when multi-seed inference is part of the claim
- **Metrics:** MAE, RMSE, and MAPE over the 12-step prediction horizon
- **Model selection:** select the checkpoint with the best validation MAE and evaluate the test split once

## Main Results

The table is a compact sanity target for the example repository. Published projects should replace these placeholders with verified values and preserve the underlying result files.

| Setting | Metric | Value |
| --- | --- | ---: |
| PeMSD8 / proposed | MAE | 15.20 |
| PeMSD8 / proposed | RMSE | 24.60 |
| PeMSD4 / proposed | MAE | 19.10 |

## Outputs

Training writes checkpoints, resolved configuration, logs, and metric JSON files under `results/<dataset>/`. Evaluation writes test metrics next to the selected checkpoint.

## Repository Structure

```text
configs/       experiment configurations
data/          benchmark inputs
models/        model definitions
scripts/       train and evaluate entry points
results/       checkpoints, logs, and metrics
docs/          protocol and reproducibility notes
```

## Citation

Cite the study paper for the experimental results and the software release when this implementation is used directly.

Paper: docs/paper.md
Software citation metadata: [`CITATION.cff`](CITATION.cff).

## License

ForecastBench is released under the MIT License.
