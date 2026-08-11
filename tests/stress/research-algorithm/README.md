# Research Algorithm stress tests

This directory pressure-tests the `research-algorithm` family with method shapes that commonly make research READMEs collapse into paper abstracts, equation dumps, or experiment logs.

## Cases

| Case | Profile | Main pressure |
| --- | --- | --- |
| `single-novel-estimator` | Minimal | novel method that should still remain small |
| `estimand-heavy-spatial-explanation` | Standard | the estimand and interpretation boundary must be explicit |
| `learned-spatial-metric` | Full | learned geometry, scientific meaning, and out-of-distribution boundaries |
| `nonlinear-spacetime-method` | Full | several equations and algorithm stages without copying a paper |

Each case is a YAML renderer configuration under `cases/` and is listed in `manifest.yml` with structural expectations.

## What these tests protect

The stress suite checks that:

- every case renders with `StrictUndefined`;
- unresolved Jinja expressions do not leak into output;
- required profile sections remain present;
- sections from the wrong profile do not appear;
- code fences remain balanced;
- Minimal remains materially smaller than Full;
- equations do not replace explanation or interpretation contracts;
- method validity, implementation validation, and benchmark performance remain conceptually separate.

These are structural stress cases, not claims about real scientific methods.
