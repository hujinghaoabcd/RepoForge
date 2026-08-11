<p align="center">
  <img src="https://raw.githubusercontent.com/hujinghaoabcd/RepoForge/main/assets/repoforge-logo.png" alt="SpatialTools" width="420">
</p>

# SpatialTools

**Reproducible spatial statistics and neighborhood-based modelling in Python.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

[Documentation](https://spatialtools.example.org) · [Examples](https://spatialtools.example.org/examples) · [API](https://spatialtools.example.org/api) · [Citation](#citation)

## Why SpatialTools?

Spatial analyses repeatedly need the same building blocks: define neighborhoods, construct weights, fit local models, inspect spatially varying results, and verify numerical behavior. Reimplementing these steps in one-off scripts makes scientific conventions and validation choices difficult to audit.

SpatialTools provides a compact Python API for these workflows while keeping coordinates, distance rules, weights, fitted results, and diagnostics explicit.

## Features

- **Spatial weights** — distance, k-nearest-neighbor, and explicit neighborhood structures.
- **Local models** — reusable fitted objects with fixed or adaptive neighborhoods.
- **Diagnostics** — residual, influence, and local stability summaries.
- **Geospatial interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly data contracts.
- **Reproducible workflows** — deterministic examples and explicit numerical validation.

## Installation

Install the stable package from PyPI:

```bash
python -m pip install spatialtools
```

Verify the installation:

```bash
python -c "import spatialtools; print(spatialtools.__version__)"
```

Optional plotting helpers are available separately:

```bash
python -m pip install "spatialtools[plot]"
```

## Quick Start

Fit a local regression and inspect the first local coefficient estimates:

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

print(result.to_frame().head())
```

## Methods and Capabilities

| Method / area | Purpose | Notes |
| --- | --- | --- |
| `SpatialWeights` | Build or validate neighborhoods | Distance, KNN, or explicit matrices |
| `LocalRegression` | Fit spatially varying relationships | Fixed or adaptive neighborhoods |
| `LocalDiagnostics` | Inspect fitted local behavior | Residual, influence, and stability summaries |

## Validation

SpatialTools treats numerical validation as part of the public scientific contract.

- deterministic regression tests cover documented workflows;
- selected calculations are checked against independent reference results;
- unsupported numerical conditions fail explicitly rather than being silently repaired.

See the [Validation Guide](https://spatialtools.example.org/validation) for reference cases, tolerances, and claim boundaries.

## Documentation

- **Getting Started:** [installation and first workflows](https://spatialtools.example.org/getting-started)
- **Examples:** [complete runnable examples](https://spatialtools.example.org/examples)
- **API Reference:** [public classes and functions](https://spatialtools.example.org/api)
- **Validation Guide:** [reference cases and limitations](https://spatialtools.example.org/validation)

## Citation

If SpatialTools contributes to academic work, cite the software and any method paper relevant to the analysis.

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Limitations

- coordinate systems and distance units must be appropriate for the selected spatial method;
- local statistical associations should not automatically be interpreted as causal effects.

## Support and Contributing

Use the documentation for usage guidance and the issue tracker for reproducible bugs or focused feature requests.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

SpatialTools is released under the MIT License.
