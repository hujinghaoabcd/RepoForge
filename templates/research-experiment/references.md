# Research Experiment README references

This file records reference patterns for paper-code and reproducibility repositories.

## Core external references

### Papers with Code — research-code completeness

Repository: https://github.com/paperswithcode/releasing-research-code

Useful patterns:

- treats README structure as part of research-code completeness;
- emphasizes dependencies, pretrained models, data, training, evaluation, and expected results;
- provides a checklist mindset rather than assuming that releasing source files is enough for reproducibility.

RepoForge takeaway: `research-experiment` needs an explicit reproducibility contract, not merely installation instructions.

### DETR — data preparation, training, evaluation, and resource disclosure

Repository: https://github.com/facebookresearch/detr

Useful patterns:

- identifies the paper and method immediately;
- distinguishes code identity from library identity;
- gives concrete dataset layout;
- provides separate commands for training and evaluation;
- reports representative hardware/time requirements and settings that materially affect reproduced numbers.

RepoForge takeaway: experiment READMEs should surface the exact operational path from data to metrics.

### StyleGAN2-ADA PyTorch — artifact identity and metrics

Repository: https://github.com/NVlabs/stylegan2-ada-pytorch

Useful patterns:

- documents pretrained artifacts and data formats explicitly;
- explains how training output directories encode configuration identity;
- states where checkpoints, images, logs, and metric files are written;
- documents metric commands and notes that evaluation randomness can change repeated values;
- distinguishes correctness, performance, and compatibility claims.

RepoForge takeaway: output files and metric identity are first-class reproducibility metadata.

### guided-diffusion — paper code, checkpoints, and use boundaries

Repository: https://github.com/openai/guided-diffusion

Useful patterns:

- starts by stating exactly which paper/codebase the repository implements;
- makes released checkpoints discoverable;
- keeps model-use limitations adjacent to checkpoint use;
- separates pretrained-model usage from training workflows.

RepoForge takeaway: released checkpoints and their intended use should be easy to find without forcing every user to retrain.

## Internal stress cases

The family should later be pressure-tested against:

- one-paper / one-dataset small companion code;
- multiple datasets with a fixed benchmark protocol;
- many baselines with fair tuning rules;
- multi-seed experiments with significance tests;
- expensive multi-GPU training with pretrained checkpoints;
- ablation/sensitivity suites;
- repositories where predictions and result identities must be archived for paper tables.

## Section champions

| README function | Primary reference | RepoForge lesson |
| --- | --- | --- |
| Code-completeness contract | Papers with Code | release the information required to reproduce, not just source files |
| Dataset layout | DETR | show exact expected paths when data identity matters |
| Training command | DETR | provide a canonical command before optional variants |
| Evaluation command | DETR / StyleGAN2-ADA | keep evaluation distinct from training |
| Hardware/time expectations | DETR | disclose material resource assumptions |
| Artifact/output identity | StyleGAN2-ADA | explain checkpoints, logs, predictions, metrics, and directories |
| Metric variability | StyleGAN2-ADA | document randomness and evaluation conventions |
| Pretrained checkpoints | guided-diffusion | support evaluation/inference without mandatory retraining |
| Usage/limitation boundary | guided-diffusion | released models may need a use note separate from reproducibility |

## RepoForge design decision

The research-experiment README is an **experiment control surface**:

```text
paper/study identity
      ↓
data + environment identity
      ↓
fastest reproduction command
      ↓
protocol and comparison contract
      ↓
results / expected outputs
      ↓
artifact identity
      ↓
full docs and archived evidence
```

It should be less theoretical than `research-algorithm` and more operational than `scientific-python`.

## Anti-patterns

Avoid:

- pasting the paper abstract and calling that a README;
- one giant command block with no explanation of what each experiment does;
- result tables without dataset split, seed, metric, or checkpoint identity;
- saying "same settings as the paper" when the settings are not machine-readable or discoverable;
- mixing training and test data preparation;
- silently tuning baselines differently from the proposed method;
- requiring retraining when a published checkpoint is sufficient for evaluation;
- storing only mean metrics when significance claims require per-seed outputs;
- describing current development progress instead of the reproducible public workflow.
