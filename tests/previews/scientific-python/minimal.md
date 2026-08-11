<div align="center">

<img src="../../../assets/logo.svg" alt="SpatialTools" width="160">

# SpatialTools

**A compact Python package for reproducible spatial analysis.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![License](https://img.shields.io/badge/License-MIT-green)](#license)


</div>

---
## Installation

```bash
python -m pip install spatialtools
```

## Quick Start

```python
import numpy as np
from spatialtools import LocalRegression

rng = np.random.default_rng(42)
coords = rng.uniform(0, 10, size=(12, 2))
X = rng.normal(size=(12, 2))
y = 2.0 + 1.4 * X[:, 0] - 0.8 * X[:, 1]

result = LocalRegression(bandwidth=6, kernel="bisquare").fit(X, y, coords)
print(result.to_frame().head())

```

## Documentation

See the project documentation for examples and API details.

## Citation

Citation metadata is available in `CITATION.cff`.

## License

MIT.
