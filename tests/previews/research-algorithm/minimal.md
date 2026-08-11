<div align="center">

<img src="../../../assets/logo.svg" alt="LatentMap" width="160">

# LatentMap

**A compact research method for learning task-aware latent distances.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Paper](https://img.shields.io/badge/paper-method-blue)](#citation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


</div>

---
## Installation

```bash
python -m pip install latentmap
```

## Quick Start

Learn a two-dimensional latent representation from a tiny feature matrix.

```python
import numpy as np
from latentmap import LatentMap

X = np.array([[0.0, 1.0], [1.0, 1.2], [2.0, 2.1], [3.0, 2.8]])
y = np.array([0.0, 0.2, 0.9, 1.1])
result = LatentMap(n_components=2, random_state=42).fit(X, y)
print(result.embedding_)

```

## Validation

The implementation is checked on deterministic synthetic recovery cases and fixed numerical fixtures.
- documented seeds reproduce the reference embedding within tolerance
- degenerate inputs fail explicitly instead of producing silent coordinates

## Citation

Cite the method paper when using LatentMap in research and cite the software release when the implementation matters.
Method paper: docs/paper.md
Software citation metadata: [`CITATION.cff`](CITATION.cff).

## License

LatentMap is released under the MIT License.
