<div align="center">

<img src="../../../assets/logo.svg" alt="GeoDesk" width="160">

# GeoDesk

**A cross-platform GIS desktop application for browsing, styling, and organizing local spatial data.**

<a href="https://github.com/example/geodesk/releases"><img src="https://img.shields.io/badge/release-v1.2.0-blue" alt="Latest release"></a> <a href="#platform-compatibility"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey" alt="Platforms"></a> <a href="#development-and-testing"><img src="https://img.shields.io/badge/tests-passing-brightgreen" alt="Tests"></a> <a href="docs/"><img src="https://img.shields.io/badge/docs-online-blue" alt="Docs"></a> <a href="#license"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
<a href="#download-and-install">Download</a> · <a href="docs/">Documentation</a> · <a href="CHANGELOG.md">Changelog</a> · <a href="https://github.com/example/geodesk/issues">Issues</a></div>

---

## Overview

GeoDesk is a local-first desktop GIS for analysts who need to inspect and organize common vector and raster datasets without deploying a server. The application uses one project file across supported desktop platforms and keeps user data under explicit per-user directories.

## Features

- **Vector and raster viewing** — open common geospatial formats and compose them into desktop map projects.
- **Styling and inspection** — control layer visibility, symbols, labels, identify results, and metadata.
- **Saved projects** — preserve layer order, paths, view state, and application-level project settings.
- **Local-first workflow** — normal browsing and project editing work without an account or cloud service.

## Download and Install

| Platform | Recommended package | Notes | Link |
| --- | --- | --- | --- |
| **Windows 11** | x64 `.exe` installer | per-user install; signed release build | https://github.com/example/geodesk/releases |
| **macOS 13+** | universal `.dmg` | notarized application bundle | https://github.com/example/geodesk/releases |
| **Linux** | x86_64 AppImage | portable package for common desktop distributions | https://github.com/example/geodesk/releases |

## First Launch

On first launch, GeoDesk creates its user configuration directory and an empty recent-project list. Open a dataset directly or create a `.geodesk` project. No account is required.

## Preview

<p align="center">
  <img src="../../../assets/placeholders/screenshot.svg" alt="GeoDesk screenshot" width="760">
</p>


## Platform Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
| **Windows** | Windows 11 x64 | installer builds tested in CI release jobs |
| **macOS** | macOS 13+ | Apple Silicon and Intel universal application bundle |
| **Linux** | Ubuntu 24.04 / Fedora 42 class desktops | AppImage is the maintained binary distribution |
| **Project files** | GeoDesk 1.x | minor releases preserve backward-readable project metadata |

## User Data and Configuration

| Data | Location / rule | Purpose |
| --- | --- | --- |
| **Configuration** | platform user-config directory / `GeoDesk` | preferences, recent files, UI state |
| **Cache** | platform user-cache directory / `GeoDesk` | thumbnails and disposable map cache |
| **Projects** | user-selected `.geodesk` files | portable project metadata; back these up with referenced data when needed |

## Build from Source

Source builds use Python 3.12+, PySide6, GDAL-compatible Python wheels or system libraries, and the repository development extras.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m geodesk
```

## Development and Testing

```bash
python -m pip install -e '.[dev]'
python -m geodesk
```

```bash
python -m pytest
python -m ruff check .
```

## Documentation

- **User Guide:** docs/user-guide.md — projects, layers, styling, and preferences
- **Build Guide:** docs/building.md — platform prerequisites and source builds
- **Release Notes:** CHANGELOG.md — user-visible changes and compatibility notes

## Contributing

Read `CONTRIBUTING.md` before changing UI behavior, project-file schema, packaging metadata, or platform support. User-facing behavior changes should include documentation and tests.

## License

GeoDesk is released under the MIT License.
