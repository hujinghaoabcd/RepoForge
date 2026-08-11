<p align="center">
  <img src="../../../assets/logo.svg" alt="LatentMap" width="160">
</p>

<p align="center">
  <img src="../../../assets/screenshots/repoforge-workflow.webp" alt="LatentMap method overview" width="780">
</p>

# LatentMap

**A research method for learning task-aware latent geometry with explicit optimization, interpretation, and validation contracts.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](#installation) [![Paper](https://img.shields.io/badge/paper-method-blue)](#citation) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#validation) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Paper · Method Guide · Validation · Examples · API · Citation

## Scientific Problem

Many scientific workflows assume that observed-space Euclidean distance is the relevant notion of similarity. When the task depends on structure that is not aligned with that metric, neighborhoods and downstream local models can be poorly matched to the scientific target.

## Why Existing Approaches Are Insufficient

Fixed metrics cannot adapt to task-specific structure, while generic representation learning can produce embeddings whose scientific meaning is unclear. LatentMap treats the learned geometry itself as a documented model object with explicit training objective, distance semantics, and downstream-use boundaries.

## Proposed Method

### Objective / estimand

LatentMap learns a parameterized mapping whose latent distances improve a documented task objective while preserving an explicit regularization contract.

$$\theta^* = \arg\min_\theta \; \mathcal{L}_{task}(f_\theta(X), y) + \lambda\,\mathcal{R}(\theta).$$

### Core Formulation

Each observation is mapped into a latent coordinate system. Downstream neighborhoods are defined from distances in that learned space rather than assumed directly from the original feature coordinates.

$$z_i=f_\theta(x_i), \qquad d_{ij}^{(z)}=\lVert z_i-z_j\rVert_2.$$

### Algorithm Outline

1. **Prepare inputs** — validate feature, target, scaling, and deterministic seed contracts.
2. **Learn the map** — optimize the task objective and regularization terms.
3. **Construct latent geometry** — expose fitted embeddings and latent-distance operations.
4. **Validate** — evaluate recovery, stability, and downstream behavior under documented cases.
5. **Apply downstream** — use latent distances only in workflows whose interpretation matches the trained objective.

## Key Contributions

- reframes distance selection as a learnable scientific modelling component
- exposes latent geometry as an inspectable fitted object rather than a hidden neural representation
- separates representation learning from downstream neighborhood construction
- documents validation and interpretation boundaries for the learned metric

## Installation

### Stable install

```bash
python -m pip install latentmap
```

### Development install

```bash
git clone https://github.com/example/latentmap.git
cd latentmap
python -m pip install -e ".[dev,docs]"
```

## Five-Minute Example

Learn a latent geometry from a small task and inspect the fitted coordinates.

```python
import numpy as np
from latentmap import LatentMap

rng = np.random.default_rng(42)
X = rng.normal(size=(80, 4))
y = X[:, 0] - 0.5 * X[:, 1] + rng.normal(scale=0.1, size=80)

model = LatentMap(n_components=2, regularization=0.05, random_state=42)
result = model.fit(X, y)

print(result.embedding_.shape)
print(result.pairwise_distances()[:3, :3])

```

## Inputs, Outputs, and Interpretation

| Contract | Meaning | Boundary |
| --- | --- | --- |
| **embedding_** | learned coordinates for observations used during fitting | axes need not correspond to physical dimensions |
| **pairwise_distances** | task-aware distances induced by the learned representation | valid only relative to the fitted objective and preprocessing contract |
| **transform** | map supported new observations into the learned space | extrapolation outside the training distribution requires separate validation |

## Validation

LatentMap treats implementation validation, synthetic recovery, downstream utility, and sensitivity as separate evidence categories.

### Analytical and numerical checks

Small deterministic cases check distance calculations, regularization behavior, and fitted-object consistency.

### Synthetic recovery

Controlled simulations test whether known task-relevant structure is recovered under documented signal and noise settings.

### Reference comparisons

Fixed-metric and standard representation baselines provide context without being treated as proof of universal superiority.

### Sensitivity

Representation dimension, regularization, initialization, and scaling are varied to identify unstable regimes.

See docs/validation/index.md for complete protocols, tolerances, and archived evidence.

## Computational Characteristics

The dominant cost is representation optimization plus pairwise or neighborhood distance evaluation. The README should report order-of-growth or practical bottlenecks only when they are measured and relevant; detailed benchmarks belong in the performance documentation.

## Reproducibility

- documented examples use fixed random seeds
- synthetic generators and reference fixtures are versioned with the repository
- validation commands record package version and configuration
- paper-facing experiments are separated from unit tests and archived result artifacts

## Limitations

- learned geometry is conditional on the objective, training distribution, preprocessing, and model capacity
- latent axes are not automatically physical, causal, or geographically meaningful
- improved downstream prediction does not by itself validate scientific interpretation of the embedding
- out-of-distribution transformation requires separate evidence

## Documentation

- **Method Guide:** docs/method/index.md — formulation, assumptions, and interpretation- **Validation Guide:** docs/validation/index.md — recovery, sensitivity, references, and claim boundaries- **Examples:** examples/ — complete runnable workflows- **API Reference:** docs/api.md — fitted objects and public operations- **Reproducibility Guide:** docs/reproducibility.md — commands, seeds, configs, and archived evidence
## Citation

Cite the LatentMap method paper for the scientific contribution and the software release when this implementation contributes materially to the analysis.

Method paper: docs/paper.md
Software citation metadata: [`CITATION.cff`](CITATION.cff).

## Support and Contributing

Use the method and validation guides for scientific interpretation questions and the issue tracker for reproducible software defects.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

LatentMap is released under the MIT License.
