# ForecastBench

**Minimal reproducible code for a short-horizon traffic forecasting study.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#environment) [![Paper](https://img.shields.io/badge/paper-study-blue)](#citation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Paper: docs/paper.md

## Environment

Create the reference environment from the locked requirements used for the study.

```bash
python -m pip install -r requirements.txt
```

## Data

Place the prepared benchmark array in the expected data directory. The Minimal profile assumes preprocessing is already documented with the dataset artifact.

Expected path: `data/benchmark.npz`

## Run

Run the canonical experiment configuration.

```bash
python scripts/run.py --config configs/main.yml
```

## Expected Output

The command writes metrics and the selected checkpoint under `results/main/`.

Expected sanity check: `results/main/metrics.json` exists and contains the study metric keys.

## Citation

Cite the study paper when using the reported experiment and cite the software release when the implementation matters.

Paper: docs/paper.md


Software citation metadata: [`CITATION.cff`](CITATION.cff).

## License

ForecastBench is released under the MIT License.
