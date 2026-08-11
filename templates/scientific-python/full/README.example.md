<div align="center">


# SpatialTools

**A research-oriented Python library for spatial statistics, local modelling, diagnostics, and reproducible geospatial workflows.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation-and-reproducibility) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


English · 简体中文


Documentation · Examples · API · Citation
</div>

---
## What SpatialTools is

SpatialTools is a reusable scientific Python package for neighborhood-based spatial analysis. It provides common numerical foundations for spatial weights, local regression, diagnostics, result objects, and geospatial export while keeping scientific conventions explicit.

## Why use it?

Many research workflows repeatedly reimplement neighborhood construction, weighting, local fitting, diagnostics, and export. SpatialTools packages these steps into a documented and testable interface without hiding distance, bandwidth, weighting, or validation choices.

## Scientific scope

SpatialTools targets local and neighborhood-based exploratory or inferential spatial workflows. It is not a general-purpose GIS platform and does not silently choose coordinate systems, distance units, neighborhoods, or causal interpretations.

## Features

- **Spatial weights** — Distance, k-nearest-neighbor, and explicit neighborhood structures.
- **Local models** — Reusable fit and prediction-result objects.
- **Diagnostics** — Residual, influence, stability, and local-quality summaries.
- **Geospatial interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly contracts.
- **Reproducibility** — Deterministic examples, explicit random seeds, and reference comparisons.

## Installation

### Stable release

```bash
python -m pip install spatialtools
```

### Optional features

```bash
python -m pip install "spatialtools[plot]"  # plotting helpers
```

### Development install

```bash
git clone https://github.com/example/spatialtools.git
cd spatialtools
python -m pip install -e ".[dev,docs]"
```

## Five-minute example

Fit a representative local model.

```python
import numpy as np
import pandas as pd
from spatialtools import LocalRegression

rng = np.random.default_rng(42)
coords = rng.uniform(0, 10, size=(100, 2))
X = pd.DataFrame(rng.normal(size=(100, 2)), columns=["income", "access"])
y = 2.0 + 1.4 * X["income"] - 0.8 * X["access"]
y += rng.normal(scale=0.3, size=100)

model = LocalRegression(bandwidth=20, kernel="bisquare")
result = model.fit(X, y, coords)
print(result.summary())

```

## Method catalogue

| Method / area | Purpose | New-data operation | Important boundary |
| --- | --- | --- | --- |
| `SpatialWeights` | Construct or validate neighborhoods | transform | Distance, KNN, or explicit matrices |
| `LocalRegression` | Estimate spatially varying relationships | predict | Fixed or adaptive neighborhoods |
| `LocalDiagnostics` | Evaluate fitted local behavior | inspect | Residual and influence summaries |

## Choosing a method

Use explicit spatial weights when the neighborhood graph is scientifically defined in advance. Use distance or KNN neighborhoods when local interaction is represented by geometric proximity.

## Data contracts and conventions

- coordinate reference systems and distance units must be explicit
- arrays use observations along the first axis
- missing data are never silently imputed
- fitted results preserve model and neighborhood metadata

## Representative workflow

A geospatial workflow can fit, inspect, and export results.

```python
import geopandas as gpd
import numpy as np
from spatialtools import LocalRegression

frame = gpd.read_file("observations.gpkg")
coords = np.column_stack([frame.geometry.x, frame.geometry.y])
result = LocalRegression(bandwidth=30).fit(
    frame[["income", "access"]], frame["target"], coords
)
frame.join(result.to_frame()).to_file("local_results.gpkg")

```


## Validation and reproducibility

SpatialTools separates scientific validation claims from feature descriptions.

- deterministic tests cover documented workflows and edge cases
- selected numerical results are checked against independent calculations
- reference fixtures are versioned with the code
- unsupported numerical conditions fail explicitly

## Examples

- **Basic local model:** examples/01_basic.py — minimal end-to-end workflow- **GeoDataFrame workflow:** examples/02_geodataframe.py — fit, inspect, and export geospatial results- **Validation example:** examples/03_validation.py — independent numerical comparison
## Documentation

- **Getting Started:** docs/getting-started.md — installation, conventions, and first workflows- **Method Guide:** docs/methods.md — assumptions and method-selection guidance- **Examples:** examples/ — complete runnable scientific workflows- **API Reference:** docs/api.md — public classes and functions- **Validation Guide:** docs/validation.md — reference cases and known boundaries- **Development Guide:** docs/development.md — testing and release workflow
## Project status and API stability

SpatialTools is a research-oriented 0.x package. Public APIs are documented and tested, but incompatible changes may occur before 1.0.

## Limitations and interpretation boundaries

- inappropriate coordinate systems or distance units can invalidate neighborhoods
- local associations are not automatically causal effects
- unsupported data contracts are rejected rather than guessed

## Citation

If SpatialTools contributes to academic work, cite the software and relevant method paper when applicable.

```bibtex
@software{spatialtools_2026,
  title  = {SpatialTools: Reproducible spatial statistics in Python},
  author = {Example Author},
  year   = {2026}
}
```

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Support and Contributing

Use the documentation for usage guidance and the issue tracker for reproducible bugs or feature requests.
Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

SpatialTools is released under the MIT License.
