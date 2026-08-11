<p align="center">
  <strong>SpatialTools</strong>
</p>

# SpatialTools

**Reproducible spatial statistics and neighborhood-based modelling in Python.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation)
[![License](https://img.shields.io/badge/license-MIT-green)](#license)

Documentation · Examples · API · Citation

## Why SpatialTools?

Many spatial analyses share the same core tasks: define a neighborhood, construct weights, fit a local model, inspect spatially varying results, and validate numerical behavior. These steps are often reimplemented in one-off scripts with inconsistent conventions.

SpatialTools provides a small, explicit Python API for reusable spatial workflows while keeping distance metrics, weighting rules, fitted results, and validation choices visible to the user.

## Features

- **Spatial weights** — distance, k-nearest-neighbor, and user-supplied neighborhood structures.
- **Local models** — reusable fit/predict result objects with explicit spatial inputs.
- **Diagnostics** — local residual, influence, and stability summaries.
- **Interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly inputs and outputs.
- **Reproducible examples** — deterministic examples with explicit random seeds.

## Installation

Install the latest stable release from PyPI:

```bash
python -m pip install spatialtools
```

Verify the installation:

```bash
python -c "import spatialtools; print(spatialtools.__version__)"
```

### Optional features

```bash
python -m pip install "spatialtools[plot]"  # plotting helpers
```

```bash
python -m pip install "spatialtools[all]"   # all user-facing extras
```

## Quick Start

Fit a simple local spatial model and inspect the result table:

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
print(result.to_frame().head())
```

The first README example should be executable, scientifically meaningful, and representative of the package's normal workflow.

## Methods and capabilities

| Method / area | Purpose | Notes |
| --- | --- | --- |
| `SpatialWeights` | Build or validate neighborhood weights | Distance, KNN, or explicit matrices |
| `LocalRegression` | Fit spatially varying regression relationships | Fixed or adaptive neighborhoods |
| `LocalDiagnostics` | Inspect local residual and influence behavior | Designed for fitted result objects |

## Representative Example

A complete workflow can include geospatial data, model fitting, diagnostics, and export:

```python
import geopandas as gpd
from spatialtools import LocalRegression

frame = gpd.read_file("observations.gpkg")
coords = np.column_stack([frame.geometry.x, frame.geometry.y])

model = LocalRegression(bandwidth=30, kernel="bisquare")
result = model.fit(frame[["income", "access"]], frame["target"], coords)

output = frame.join(result.to_frame())
output.to_file("local_results.gpkg")
```

See the Examples documentation for complete, runnable workflows.

## Validation

SpatialTools treats numerical validation as part of the public scientific contract.

- deterministic unit and regression tests cover documented workflows;
- selected methods are compared with independent reference calculations;
- edge cases such as singular neighborhoods and missing inputs are tested explicitly;
- validation scope and unsupported claims are documented separately from feature descriptions.

See the Validation Guide for reference cases, tolerances, and known boundaries.

## Documentation

- **Getting Started:** installation, data conventions, and first workflows
- **Examples:** complete runnable scientific examples
- **API Reference:** public classes, functions, signatures, and return objects
- **Method Guide:** scientific assumptions and method-selection guidance
- **Validation Guide:** numerical references, test scope, and limitations

## Citation

If SpatialTools contributes to academic work, cite the software and the method paper when applicable.

```bibtex
@software{spatialtools_2026,
  title  = {SpatialTools: Reproducible spatial statistics in Python},
  author = {Example Author},
  year   = {2026}
}
```

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Limitations

- coordinate systems and distance units must be scientifically appropriate for the selected method;
- local statistical associations should not be interpreted automatically as causal effects;
- advanced model-specific theory and validity conditions belong in the Method Guide, not in this README.

## Support and Contributing

Use the documentation for usage guidance and the issue tracker for reproducible bugs or feature requests.

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

SpatialTools is released under the MIT License.
