# SpatialTools

**A research-oriented Python library for spatial statistics, local modelling, diagnostics, and reproducible geospatial workflows.**

[![PyPI](https://img.shields.io/badge/PyPI-package-blue)](#installation) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation-and-reproducibility) [![Coverage](https://img.shields.io/badge/coverage-reported-blue)](#validation-and-reproducibility) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

English · 简体中文

[Documentation](https://spatialtools.example.org) · [Method Guide](https://spatialtools.example.org/methods) · [Examples](https://spatialtools.example.org/examples) · [API](https://spatialtools.example.org/api) · [Citation](#citation)

## What SpatialTools is

SpatialTools is a reusable scientific Python package for neighborhood-based spatial analysis. It provides common numerical foundations for spatial weights, local regression, diagnostics, structured result objects, and geospatial export while keeping scientific conventions explicit.

## Why use it?

Many research workflows repeatedly reimplement neighborhood construction, weighting, local fitting, diagnostics, and export. That duplication makes scientific assumptions, data conventions, and numerical validation difficult to audit.

SpatialTools packages these recurring steps into a documented and testable interface without hiding distance, bandwidth, weighting, or validation choices.

## Scientific scope

SpatialTools targets local and neighborhood-based exploratory or inferential spatial workflows. It is not a general-purpose GIS platform and does not silently choose coordinate systems, distance units, neighborhoods, missing-data policies, or causal interpretations for the user.

## Features

- **Spatial weights** — distance, k-nearest-neighbor, and explicit neighborhood structures.
- **Local models** — reusable fit and prediction-result objects with fixed or adaptive neighborhoods.
- **Diagnostics** — residual, influence, stability, and local-quality summaries.
- **Geospatial interoperability** — NumPy, pandas, GeoPandas, and Shapely-friendly contracts.
- **Reproducibility** — deterministic examples, explicit random seeds, and versioned reference comparisons.
- **Explicit failure behavior** — unsupported data and numerical conditions are rejected instead of silently guessed.

## Installation

### Stable release

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

### Development install

```bash
git clone https://github.com/example/spatialtools.git
cd spatialtools
python -m pip install -e ".[dev,docs]"
```

## Five-minute example

Fit a local regression, inspect its diagnostics, and export the local result table:

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

## Method catalogue

| Method / area | Purpose | New-data operation | Important boundary |
| --- | --- | --- | --- |
| `SpatialWeights` | Construct or validate neighborhoods | transform | Does not choose a scientifically appropriate graph for the user |
| `LocalRegression` | Estimate spatially varying relationships | predict | Requires meaningful coordinates, units, and neighborhood scale |
| `LocalDiagnostics` | Evaluate fitted local behavior | inspect | Diagnostic association is not causal evidence |

## Choosing a method

| Scientific need | Start with | Guidance |
| --- | --- | --- |
| Neighborhood graph defined by theory or design | explicit `SpatialWeights` | Preserve the supplied graph rather than rebuilding it from distance |
| Proximity-based neighborhood | distance or KNN weights | Choose distance units and scale before fitting |
| Spatially varying continuous relationship | `LocalRegression` | Treat bandwidth and kernel as scientific modelling choices |
| Assess fitted local stability | `LocalDiagnostics` | Interpret diagnostics alongside model assumptions and sample support |

Detailed method assumptions and selection guidance live in the [Method Guide](https://spatialtools.example.org/methods).

## Data contracts and conventions

- coordinate reference systems and distance units must be explicit;
- arrays use observations along the first axis;
- missing observations are never silently imputed;
- fitted result objects preserve model, neighborhood, and data-contract metadata;
- geospatial export keeps geometry handling explicit rather than embedding hidden projection logic.

## Representative workflow

A normal geospatial workflow can read observations, fit a model, attach local outputs, and export the result:

```python
import geopandas as gpd
import numpy as np
from spatialtools import LocalRegression

frame = gpd.read_file("observations.gpkg")
coords = np.column_stack([frame.geometry.x, frame.geometry.y])

result = LocalRegression(
    bandwidth=30,
    kernel="bisquare",
).fit(frame[["income", "access"]], frame["target"], coords)

output = frame.join(result.to_frame())
output.to_file("local_results.gpkg")
```

See the [GeoDataFrame workflow](https://spatialtools.example.org/examples/geodataframe) for the complete executable example.

## Validation and reproducibility

SpatialTools separates scientific validation evidence from feature claims.

- deterministic tests cover documented workflows and edge cases;
- selected numerical results are checked against independent calculations;
- reference fixtures and example data are versioned with the code;
- examples use explicit random seeds where stochastic data are involved;
- unsupported numerical conditions fail explicitly rather than being silently repaired;
- supported Python versions are exercised in CI before release.

See the [Validation Guide](https://spatialtools.example.org/validation) for reference cases, tolerances, and claim boundaries.

## Examples

- **Basic local model:** [minimal end-to-end workflow](https://spatialtools.example.org/examples/basic)
- **GeoDataFrame workflow:** [fit, inspect, and export spatial results](https://spatialtools.example.org/examples/geodataframe)
- **Validation example:** [compare against an independent calculation](https://spatialtools.example.org/examples/validation)

## Documentation

- **Getting Started:** [installation, conventions, and first workflows](https://spatialtools.example.org/getting-started)
- **Method Guide:** [assumptions and method-selection guidance](https://spatialtools.example.org/methods)
- **Examples:** [complete runnable scientific workflows](https://spatialtools.example.org/examples)
- **API Reference:** [public classes, functions, signatures, and return objects](https://spatialtools.example.org/api)
- **Validation Guide:** [numerical references, tolerances, and known boundaries](https://spatialtools.example.org/validation)
- **Development Guide:** [tests, documentation, releases, and contribution workflow](https://spatialtools.example.org/development)

## Project status and API stability

SpatialTools is a research-oriented 0.x package. Public APIs are documented and tested, but incompatible changes may still occur before a 1.0 release. Release notes identify changes to public behaviour, data contracts, and supported methods.

## Limitations and interpretation boundaries

- inappropriate coordinate systems or distance units can invalidate spatial neighborhoods;
- local associations are not automatically causal effects;
- method-specific inferential assumptions must be checked before reporting results;
- unsupported data contracts are rejected rather than guessed;
- the README summarizes scientific boundaries, while complete method-specific limitations live in the Method Guide.

## Citation

If SpatialTools contributes to academic work, cite the software and the relevant method paper when applicable.

```bibtex
@software{spatialtools_2026,
  title  = {SpatialTools: Reproducible spatial statistics in Python},
  author = {Example Author},
  year   = {2026}
}
```

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Support and Contributing

Use the documentation for usage guidance and the issue tracker for reproducible bugs or focused feature requests.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

SpatialTools is released under the MIT License.
