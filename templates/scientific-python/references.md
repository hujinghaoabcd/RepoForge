# Scientific Python README reference analysis

This document records the curated reference cases used to design RepoForge's `scientific-python` README template.

The goal is **not** to copy one repository. Each project is treated as a reference for specific README decisions: project identity, scientific motivation, quick start, examples, documentation handoff, validation, citation, support, and scope control.

## 1. Packaging and repository standards

These projects define the engineering baseline around which the README lives.

| Reference | What RepoForge should learn from it | Role |
| --- | --- | --- |
| [scientific-python/cookie](https://github.com/scientific-python/cookie) | Modern Scientific Python repository structure, tests/docs/CI expectations, README as one part of a larger project contract, support for Copier/Cookiecutter/Cruft | Primary engineering baseline |
| [pyOpenSci/pyos-package-template](https://github.com/pyOpenSci/pyos-package-template) | Research-oriented Python packaging workflow, explicit minimal/full generation modes, package + tests + docs as the basic unit | Secondary engineering baseline |

RepoForge should not recreate these project scaffolds. It should generate and maintain the repository-facing documentation layer that can sit on top of them.

---

## 2. Core README case studies

### xarray — scientific motivation / `Why?`

Repository: <https://github.com/pydata/xarray>

**Best reference for:** explaining why a scientific abstraction exists.

Useful pattern:

```text
Project identity
↓
What the package does
↓
Why the underlying scientific/data problem needs it
↓
Concrete capability examples
↓
Documentation / contribution / community
```

RepoForge decision:

- `Why <Project>?` is part of the standard scientific-package vocabulary.
- It is especially useful when the package introduces a scientific abstraction rather than merely wrapping an existing API.
- The section should explain the problem and design value, not become a literature review.

### pandas — header + feature inventory

Repository: <https://github.com/pandas-dev/pandas>

**Best reference for:** mature package identity and a compact capabilities list.

Useful elements:

- strong project identity at the top;
- grouped status/package/meta badges;
- short `What is it?` explanation;
- clear feature inventory;
- documentation, help, development and contribution handoff.

RepoForge decision:

- badge groups should be limited to information that helps users judge installability, quality or project status;
- features should be user-facing capabilities, not internal module names.

### Rasterio — code-first scientific example

Repository: <https://github.com/rasterio/rasterio>

**Best reference for:** moving from a short domain description to a meaningful executable example quickly.

RepoForge decision:

- a scientific package should normally show one representative code path near the top;
- the first example should demonstrate the package's central scientific operation, not an artificial `hello world`.

### Shapely — concise usage-oriented README

Repository: <https://github.com/shapely/shapely>

**Best reference for:** API clarity through small executable snippets and interoperability examples.

RepoForge decision:

- when an API is naturally compositional, a few small snippets may communicate more than a long feature list;
- interoperability belongs in the README only when it is central to expected workflows.

### PyGMT — visual identity + Why + Quickstart

Repository: <https://github.com/GenericMappingTools/pygmt>

**Best reference for:** a polished Earth-science package front page.

Useful pattern:

```text
Visual identity
↓
Why PyGMT?
↓
Dependencies
↓
Quickstart with visible scientific output
↓
Documentation / gallery / citation
```

RepoForge decision:

- visual packages may place a representative result image or gallery link near the top;
- `Why?` and `Quick Start` should remain distinct: one explains value, the other demonstrates use.

### Astropy — README as project portal

Repository: <https://github.com/astropy/astropy>

**Best reference for:** keeping a mature scientific project's README deliberately compact.

Useful elements:

- project identity and ecosystem purpose;
- installation;
- contribution entry points;
- explicit acknowledgement/citation handoff;
- detailed material delegated to project documentation.

RepoForge decision:

- a `full` README is not an excuse to copy the documentation site into GitHub;
- citation can be summarized in the README while authoritative citation metadata remains in `CITATION.cff` or dedicated docs.

### PyMC — features + complete scientific example + citation

Repository: <https://github.com/pymc-devs/pymc>

**Best reference for:** showing a rich scientific library without hiding its research context.

Useful elements:

- feature list;
- substantial representative example;
- separate getting-started paths;
- first-class `Citing` section with publication/DOI information;
- support/community routes.

RepoForge decision:

- packages with a companion paper should make citation first-class;
- the README may contain one representative workflow even when the documentation contains a larger example gallery.

### ObsPy — scientific references and DOI treatment

Repository: <https://github.com/obspy/obspy>

**Best reference for:** connecting software, domain literature and versioned research citation.

Useful elements:

- domain-specific project definition;
- a compact executable example;
- references to core software papers;
- concept DOI and version-specific DOI guidance.

RepoForge decision:

- research software may distinguish a software citation, method/paper citation and archived-version DOI;
- multiple citation targets should be explained rather than presented as an undifferentiated BibTeX wall.

### matscipy — balanced small/medium scientific package

Repository: <https://github.com/libAtoms/matscipy>

**Best reference for:** a realistic research-group scientific package rather than a giant ecosystem project.

Useful pattern:

```text
What the toolbox covers
↓
Quick start
↓
Documentation
↓
Help / contribution
↓
Tests / development
↓
Dependencies
↓
Citation
```

RepoForge decision:

- this is a strong scale reference for `standard` packages;
- development details should remain concise and link to `CONTRIBUTING.md` when they become long.

### OSMnx — concise focused package portal

Repository: <https://github.com/gboeing/osmnx>

**Best reference for:** a short README that still covers scientific identity, citation, getting started, installation, support and license.

RepoForge decision:

- not every mature scientific package needs a long README;
- `minimal` and `standard` profiles should be capable of producing a polished project portal without losing research-specific citation information.

---

## 3. Secondary reference pool

The following repositories remain useful comparison cases but do not need to define the first template version by themselves:

- [NumPy](https://github.com/numpy/numpy) — mature foundational library and documentation handoff;
- [SciPy](https://github.com/scipy/scipy) — scientific-computing ecosystem positioning;
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) — algorithm-library identity, installation and contribution pathways;
- [scikit-image](https://github.com/scikit-image/scikit-image) — scientific image processing and gallery-driven documentation;
- [GeoPandas](https://github.com/geopandas/geopandas) — concise GIS library portal;
- [Cartopy](https://github.com/SciTools/cartopy) — scientific visualization and examples;
- [ArviZ](https://github.com/arviz-devs/arviz) — statistics ecosystem positioning and citation;
- [Nilearn](https://github.com/nilearn/nilearn) — example/gallery-heavy scientific ML;
- [MDAnalysis](https://github.com/MDAnalysis/mdanalysis) — community, citation and scientific software sustainability;
- [PyKrige](https://github.com/GeoStat-Framework/PyKrige) — focused geostatistical method package;
- [GSTools](https://github.com/GeoStat-Framework/GSTools) — geostatistics toolbox with multiple methods;
- [Verde](https://github.com/fatiando/verde) — modern geoscience package organization.

These remain useful when stress-testing future choices, especially for GIS and statistical packages.

---

## 4. Internal stress-test projects

RepoForge should also be tested against real packages with different maturity and scope:

| Project | What it stresses |
| --- | --- |
| `pyGWRx` | large method catalogue, documentation portal, validation, bilingual docs, citation |
| `pySurveying` | approachable `Why?`, 30-second start, method coverage, release scope |
| `pyKDEX` | many related scientific workflows and executable examples |
| `pyGeoHet` | moving development-stage detail out of the README |
| `pySTARMAx` | moving mathematical/theoretical depth into docs without losing scientific clarity |
| `SpatialSHAP` | original method, estimand definition, validation and interpretation boundaries |

These projects should not dictate the template. They are regression cases used to ensure that RepoForge improves consistency without erasing scientific identity.

---

## 5. Section-by-section reference winners

This is the current working selection, not a permanent ranking.

| README concern | Primary reference(s) | RepoForge direction |
| --- | --- | --- |
| Engineering baseline | Scientific Python Cookie, pyOpenSci | README must fit a complete tests/docs/CI project structure |
| Header / identity | PyGMT, pandas | clear identity; useful badges only; visual output when relevant |
| One-line positioning | Rasterio, OSMnx | domain + action + object, without marketing filler |
| Scientific motivation | xarray | explain the problem before listing implementation detail |
| Features | pandas, PyMC, matscipy | user-visible capability groups |
| Installation | Astropy, matscipy | shortest supported path first; details in docs |
| Quick start | Rasterio, PyGMT | representative executable scientific workflow |
| API / interoperability | Shapely | small composable snippets where appropriate |
| Documentation handoff | Astropy, xarray | README is a portal, not the manual |
| Citation | ObsPy, PyMC, Astropy | citation is a first-class research-software concern |
| Support | OSMnx, Astropy | separate usage questions, bug reports and contribution routes |
| Scope control | Astropy, OSMnx | mature projects can stay concise |

---

## 6. First design decisions for RepoForge

The first `scientific-python / standard` template should follow this order:

```text
Header / optional logo
Project name
One-line scientific positioning
Badges + key links
Language switch (optional)

Why <Project>?
Features
Installation
Quick Start
Methods / Capabilities        [conditional]
Representative Example       [conditional]
Validation                   [conditional but recommended for numerical packages]
Documentation
Citation                     [recommended for research software]
Support / Contributing
License
```

### Keep in README

- scientific problem and package value;
- supported high-level capability groups;
- shortest supported installation route;
- one first useful workflow;
- concise validation scope;
- documentation and citation routes.

### Move to docs

- long mathematical derivations;
- exhaustive API inventories;
- model-by-model manuals;
- complete benchmark tables;
- long validation protocols;
- detailed release engineering;
- development-stage logs and roadmap history;
- large troubleshooting guides.

### Profile interpretation

- **minimal** — focused scientific utility or mature project portal;
- **standard** — default for most reusable research packages;
- **full** — broader package with method selection, validation, reproducibility or compatibility information, while still delegating deep documentation to `docs/`.

---

## 7. Next step

Use these decisions to create:

```text
templates/scientific-python/
├── CONTRACT.md
├── references.md
├── README.template.md
└── README.example.md
```

The template and example should then be checked against the three preview profiles under `tests/previews/scientific-python.md`.
