<p align="center">
  <strong>SpatialTools</strong>
</p>

# SpatialTools

**A research-oriented Python library for spatial statistics, local modelling, diagnostics, and reproducible geospatial workflows.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation-and-reproducibility) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

English · 简体中文 · Documentation · Examples · API · Citation

## What SpatialTools Is

SpatialTools is a reusable scientific Python package for neighborhood-based spatial analysis. It provides common numerical foundations for spatial weights, local regression, diagnostics, result objects, and geospatial export while keeping scientific conventions explicit.

## Why Use It?

Many research workflows repeatedly reimplement neighborhood construction, weighting, local fitting, diagnostics, and export. SpatialTools packages these steps into a documented and testable interface without hiding distance, bandwidth, weighting, or validation choices.

## Scientific Scope

SpatialTools targets local and neighborhood-based exploratory or inferential spatial workflows. It is not a general-purpose GIS platform and does not silently choose coordinate systems, distance units, neighborhoods, or causal interpretations for the user.

## Features

- **Spatial weights** — distance, k-nearest-neighbor, and explicit neighborhood structures.
- **Local models** — reusable fit and prediction-result objects.
- **Diagnostics** — residual, influence, stability, and local-quality summaries.
- **Geospatial interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly contracts.
- **Reproducibility** — deterministic examples, explicit random seeds, and reference comparisons.

## Installation

### Stable release

```bash
python -m pip install spatialtools
```

### Optional features

```bash
python -m pip install "spatialtools[plot]"
```

### Development install

```bash
git clone https://github.com/example/spatialtools.git
cd spatialtools
python -m pip install -e ".[dev,docs]"
```

## Five-Minute Example

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

## Method Catalogue

| Method / area | Purpose | New-data operation | Notes |
| --- | --- | --- | --- |
| `SpatialWeights` | Construct or validate neighborhoods | transform | Distance, KNN, or explicit matrices |
| `LocalRegression` | Estimate spatially varying relationships | predict | Fixed or adaptive neighborhoods |
| `LocalDiagnostics` | Evaluate fitted local behavior | inspect | Residual and influence summaries |

## Choosing a Method

Use explicit spatial weights when the neighborhood graph is scientifically defined in advance. Use distance or KNN neighborhoods when local interaction is represented by geometric proximity.

## Data Contracts and Conventions

- coordinate reference systems and distance units must be explicit;
- arrays use observations along the first axis;
- missing data are never silently imputed;
- fitted results preserve model and neighborhood metadata.

## Representative Workflow

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

## Validation and Reproducibility

- deterministic tests cover documented workflows and edge cases;
- selected numerical results are checked against independent calculations;
- reference fixtures are versioned with the code;
- unsupported numerical conditions fail explicitly.

## Examples

- **Basic local model:** minimal end-to-end workflow
- **GeoDataFrame workflow:** fit, inspect, and export geospatial results
- **Validation example:** independent numerical comparison

## Documentation

- **Getting Started:** installation, conventions, and first workflows
- **Method Guide:** assumptions and method-selection guidance
- **Examples:** complete runnable scientific workflows
- **API Reference:** public classes and functions
- **Validation Guide:** reference cases and known boundaries
- **Development Guide:** testing and release workflow

## Project Status and API Stability

SpatialTools is a research-oriented 0.x package. Public APIs are documented and tested, but incompatible changes may occur before 1.0.

## Limitations

- inappropriate coordinate systems or distance units can invalidate neighborhoods;
- local associations are not automatically causal effects;
- unsupported data contracts are rejected rather than guessed.

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

Use the documentation for usage guidance and the issue tracker for reproducible bugs or feature requests. Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

SpatialTools is released under the MIT License.
