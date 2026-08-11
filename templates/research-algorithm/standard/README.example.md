<div align="center">


# LatentMap

**A research method for learning task-aware latent distances and interpretable low-dimensional structure.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Paper](https://img.shields.io/badge/paper-method-blue)](#citation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


Paper · Documentation · Examples · API · Citation
</div>

---
## Scientific Problem

Many workflows rely on fixed Euclidean distance even when the scientific task depends on a different notion of similarity. LatentMap addresses this mismatch by learning a representation whose geometry is optimized for a documented task objective.

## Method Overview

LatentMap learns a mapping from observed features into a lower-dimensional latent space, then evaluates neighborhood structure using distances in that learned space. The learned geometry is part of the model and must be interpreted together with the training objective.

$$z_i = f_\theta(x_i), \qquad d_{ij}^{(z)} = \lVert z_i-z_j \rVert_2.$$


## Key Contributions

- learns task-aware latent distances instead of assuming a fixed observed-space metric
- exposes the learned embedding and distance contract as inspectable model outputs
- separates optimization, validation, and downstream neighborhood construction
- provides deterministic synthetic recovery fixtures for documented settings

## Installation

Install the maintained package from PyPI.

```bash
python -m pip install latentmap
```

## Quick Start

Fit LatentMap on a small synthetic regression-style task and inspect the learned embedding.

```python
import numpy as np
from latentmap import LatentMap

X = np.array([[0.0, 1.0], [1.0, 1.2], [2.0, 2.1], [3.0, 2.8], [4.0, 4.2]])
y = np.array([0.0, 0.2, 0.9, 1.1, 1.8])

model = LatentMap(n_components=2, random_state=42)
result = model.fit(X, y)
print(result.embedding_)

```

## Validation

LatentMap separates implementation validation from downstream predictive performance claims.
- deterministic fixtures check the optimization and distance contracts
- synthetic recovery cases verify expected neighborhood ordering under documented settings
- degenerate inputs and unsupported objectives fail explicitly

See docs/validation.md for complete validation scope and tolerances.

## Limitations

- the learned latent geometry depends on the supplied objective and training data
- a visually separated embedding does not by itself establish causal or physical structure
- downstream scientific conclusions remain sensitive to the choice of objective and model capacity

## Documentation

- **Method Guide:** docs/method.md — scientific formulation and assumptions- **Examples:** examples/ — complete runnable workflows- **Validation Guide:** docs/validation.md — recovery cases, tolerances, and claim boundaries- **API Reference:** docs/api.md — public implementation surface
## Citation

Cite the LatentMap method paper for the scientific method and the software release when the implementation contributes materially to the work.

Method paper: docs/paper.md
Software citation metadata: [`CITATION.cff`](CITATION.cff).

## Support and Contributing

Use the documentation for method questions and the issue tracker for reproducible software defects.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

LatentMap is released under the MIT License.
