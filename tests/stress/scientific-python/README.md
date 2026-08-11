# Scientific Python stress tests

These cases are intentionally different from the polished `SpatialTools` examples. Their purpose is to push the three Scientific Python README profiles against different package shapes and content pressures.

## Cases

| Case | Profile | Pressure being tested |
| --- | --- | --- |
| `tiny-numerical-utility` | minimal | whether a very small package stays concise and runnable |
| `multi-method-geospatial` | standard | several scientific capabilities without turning README into a catalogue |
| `broad-model-library` | full | large method family, selection guidance, data contracts, validation and API maturity |
| `theory-heavy-statistics` | full | strong interpretation boundaries and scientific assumptions without copying a paper into README |
| `pre1-experimental-package` | standard | a useful 0.x package that needs clear maturity boundaries but does not justify a Full README |

Each case has a standalone YAML configuration under `cases/`. `tests/test_stress_scientific_python.py` renders every case through the real RepoForge renderer and checks its profile contract.

The suite is deliberately not a collection of hand-authored README snapshots. The YAML is the input; the renderer output is the object under test.
