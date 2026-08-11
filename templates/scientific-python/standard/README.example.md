<div align="center">


# SpatialTools

**Reproducible spatial statistics and neighborhood-based modelling in Python.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)




Documentation · Examples · API · Citation
</div>

---
## Why SpatialTools?

Many spatial analyses repeat the same tasks: define neighborhoods, construct weights, fit local models, inspect spatially varying results, and validate numerical behavior. SpatialTools provides a small, explicit API for these workflows while keeping distances, weights, fitted results, and validation choices visible.

## Features

- **Spatial weights** — Distance, k-nearest-neighbor, and explicit neighborhood structures.
- **Local models** — Reusable fitted objects with explicit spatial inputs.
- **Diagnostics** — Residual, influence, and stability summaries.
- **Interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly data.

## Installation

```bash
python -m pip install spatialtools
```

Verify the installation:

```bash
python -c "import spatialtools; print(spatialtools.__version__)"
```

## Quick Start

Fit a local model and inspect the result table.

```python
import numpy as np
import pandas as pd
from spatialtools import LocalRegression

rng = np.random.default_rng(42)
coords = rng.uniform(0, 10, size=(100, 2))
X = pd.DataFrame(rng.normal(size=(100, 2)), columns=["income", "access"])
y = 2.0 + 1.4 * X["income"] - 0.8 * X["access"]

model = LocalRegression(bandwidth=20, kernel="bisquare")
result = model.fit(X, y, coords)
print(result.to_frame().head())

```

## Methods and Capabilities

| Method / area | Purpose | Notes |
| --- | --- | --- |
| `SpatialWeights` | Build or validate neighborhoods | Distance, KNN, or explicit matrices |
| `LocalRegression` | Fit spatially varying relationships | Fixed or adaptive neighborhoods |
| `LocalDiagnostics` | Inspect fitted local behavior | Residual and influence summaries |

## Validation

SpatialTools treats numerical checks as part of its scientific contract.

- deterministic regression tests cover documented workflows
- selected methods are checked against independent reference calculations
- unsupported numerical conditions fail explicitly instead of being silently corrected

## Documentation

- **Getting Started:** docs/getting-started.md — installation and first workflows- **Examples:** examples/ — complete runnable examples- **API Reference:** docs/api.md — public classes and functions- **Validation Guide:** docs/validation.md — reference cases and limitations
## Citation

If SpatialTools contributes to academic work, cite the software.

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Support and Contributing

Use the documentation for usage guidance and the issue tracker for reproducible bugs or feature requests.
Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

SpatialTools is released under the MIT License.
