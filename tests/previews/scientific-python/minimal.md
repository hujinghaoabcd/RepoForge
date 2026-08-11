<p align="center">
  <img src="../../../assets/logo.svg" alt="SpatialTools" width="280">
</p>

# SpatialTools

**Compact spatial neighborhood analysis for Python.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![License](https://img.shields.io/badge/License-MIT-green)](#license)

Small, explicit spatial-analysis utilities with NumPy-friendly inputs and reproducible results.

## Installation

```bash
python -m pip install spatialtools
```

## Quick Start

```python
import numpy as np
from spatialtools import LocalRegression

rng = np.random.default_rng(42)
coords = rng.uniform(0, 10, size=(40, 2))
X = rng.normal(size=(40, 2))
y = 1.5 + 2.0 * X[:, 0] - 0.5 * X[:, 1]
y += rng.normal(scale=0.2, size=40)

result = LocalRegression(bandwidth=12).fit(X, y, coords)
print(result.to_frame().head())
```

## Documentation

[Documentation](https://spatialtools.example.org) · [Examples](https://spatialtools.example.org/examples) · [API](https://spatialtools.example.org/api)

## Citation

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## License

MIT.
