# SpatialTools

**A compact Python package for reproducible spatial analysis.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![License](https://img.shields.io/badge/License-MIT-green)](#license)

Small, explicit spatial-analysis utilities with NumPy/pandas-friendly inputs.

## Installation

```bash
python -m pip install spatialtools
```

## Quick Start

```python
from spatialtools import LocalRegression

model = LocalRegression(bandwidth=20, kernel="bisquare")
result = model.fit(X, y, coords)
print(result.to_frame().head())
```

## Documentation

See the project documentation for examples and API details.

## Citation

Citation metadata is available in `CITATION.cff`.

## License

MIT.
