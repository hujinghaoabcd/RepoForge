# Research experiment stress suite

This suite tests whether the independent `research-experiment` profiles remain useful across substantially different paper-code shapes.

Unlike the canonical `ForecastBench` examples, stress cases store only **overrides** on top of each profile's `config.example.yml`. This keeps the cases small while still exercising the real renderer and complete template contract.

Current shapes:

- `one-command-reproduction` — Minimal: one dataset, one command, one auditable output;
- `checkpoint-first-evaluation` — Standard: published checkpoint evaluation without pretending to reproduce the whole training study;
- `compact-multidataset-benchmark` — Standard: several datasets and a main protocol without significance/ablation machinery;
- `multi-seed-baseline-study` — Full: many baselines, five seeds, ablation, significance, predictions, and artifact identity.

Every stress render also receives RepoForge's test-only branding from `tests/branding.yml`. User project examples and normal renderer configs remain free to provide their own logo.
