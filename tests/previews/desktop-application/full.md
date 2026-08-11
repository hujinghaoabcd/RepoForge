<p align="center">
  <img src="../../../assets/logo.svg" alt="GeoDesk" width="280">
</p>
<h1 align="center">GeoDesk</h1>
<p align="center"><strong>A production-oriented cross-platform GIS workstation with local projects, optional Python plugins, and explicit release compatibility.</strong></p>
<p align="center">
  <a href="https://github.com/example/geodesk/releases"><img src="https://img.shields.io/badge/release-v2.0.0-blue" alt="Latest release"></a>
  <a href="#platform-compatibility"><img src="https://img.shields.io/badge/Windows-passing-brightgreen" alt="Windows build"></a>
  <a href="#platform-compatibility"><img src="https://img.shields.io/badge/macOS-passing-brightgreen" alt="macOS build"></a>
  <a href="#platform-compatibility"><img src="https://img.shields.io/badge/Linux-passing-brightgreen" alt="Linux build"></a>
  <a href="#development-and-testing"><img src="https://img.shields.io/badge/tests-passing-brightgreen" alt="Tests"></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
</p>
<p align="center">
  <a href="#downloads-and-release-channels">Download</a> ·  <a href="docs/user-guide.md">User Guide</a> ·  <a href="docs/plugins.md">Plugins</a> ·  <a href="docs/building.md">Build</a> ·  <a href="https://github.com/example/geodesk/issues">Issues</a></p>
<p align="center">
  <img src="docs/images/geodesk-workspace.png" alt="GeoDesk screenshot" width="940">
</p>

## Why GeoDesk?

Desktop GIS projects become difficult to maintain when project files, native geospatial dependencies, user configuration, plugins, and release packaging evolve independently. GeoDesk keeps those contracts explicit while remaining local-first and usable without a service account.

## Features

- **Local GIS workspace** — compose vector and raster layers, inspect attributes, style maps, and save portable project metadata.
- **Stable project schema** — project metadata uses an explicit schema version with documented migration rules.
- **Optional Python plugins** — trusted user-installed plugins extend importers and tools through a versioned plugin API.
- **Cross-platform releases** — Windows installers, notarized macOS bundles, and Linux AppImages are built from one release tag.
- **Transparent network behavior** — core project editing is offline; optional update checks and online basemap requests are documented separately.

## Downloads and Release Channels

| Platform / channel | Package | Support level | Link |
| --- | --- | --- | --- |
| **Windows stable** | signed x64 installer | maintained | https://github.com/example/geodesk/releases |
| **macOS stable** | signed and notarized universal DMG | maintained | https://github.com/example/geodesk/releases |
| **Linux stable** | x86_64 AppImage | maintained | https://github.com/example/geodesk/releases |
| **Nightly** | CI artifacts | testing only; no migration guarantee | docs/nightly-builds.md |

## Platform Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
| **Windows** | Windows 11 x64 | signed installer; GPU driver requirements follow Qt support |
| **macOS** | macOS 13+ | universal bundle for Apple Silicon and Intel |
| **Linux** | glibc-based x86_64 desktop systems | maintained AppImage; distro packages may have separate support policies |
| **Project schema** | v2 reads current v2 and migrates documented v1 projects | save-after-migration upgrades the project metadata version |

## Architecture

GeoDesk separates UI state, domain/project state, geospatial I/O, and optional extension loading so platform packaging does not become part of the project-file contract.

| Component | Technology | Responsibility |
| --- | --- | --- |
| **Desktop UI** | PySide6 / Qt | windows, docks, map canvas, dialogs, shortcuts, and native desktop integration |
| **Project core** | Python dataclasses + versioned schema | project state, layer registry, serialization, and migration |
| **Geospatial I/O** | GDAL / Rasterio / GeoPandas-compatible adapters | local vector/raster access and metadata translation |
| **Plugin host** | Python entry-point loader | optional trusted tool/importer extensions behind a versioned API |

## User Data, Configuration, and Cache

| Data | Location / rule | Purpose / backup status |
| --- | --- | --- |
| **Preferences** | platform user-config directory / `GeoDesk` | back up only when preserving application preferences |
| **Cache** | platform cache directory / `GeoDesk` | disposable thumbnails, indexes, and network tile cache |
| **Plugin directory** | platform user-data directory / `GeoDesk/plugins` | user-installed code; restore only from trusted sources |
| **Projects** | user-selected `.geodesk` files | versioned metadata; back up together with externally referenced datasets when required |

## Project and File Formats

- **`.geodesk`:** JSON-based project metadata containing layer references, style state, view state, and schema version. — backward migration is documented between supported major schema versions.
- **Imported datasets:** source geospatial files remain external rather than being silently copied into the project. — supported formats depend on the packaged GDAL stack.

## Plugins and Extensions

GeoDesk can load trusted Python plugins from its user plugin directory. The plugin API is versioned separately from internal modules. Plugins run with the user's application permissions, so users should install them only from sources they trust.

## Updates and Release Compatibility

Stable releases may perform a version-check request when update checks are enabled. Nightly builds are separate testing artifacts. Project schema migrations are documented in release notes; a nightly build must not be treated as a safe upgrade path for irreplaceable projects.

## Portable Mode

A portable launch mode can redirect configuration and cache paths beneath the application directory for USB/lab deployments. Portable mode does not make externally referenced project datasets portable by itself.

## Privacy and Network Behavior

Core local project editing does not require an account. Network access occurs only for user-configured online layers, explicit update checks, or plugins that implement network features. The application does not upload local project files as part of normal operation.

## Telemetry

GeoDesk does not send product-usage telemetry. Crash reports are not uploaded automatically; diagnostic bundles are generated locally and attached by the user when reporting an issue.

## Security

- Release installers and application bundles are signed where the target platform supports project-maintained signing.
- User-installed plugins execute trusted code with the same filesystem permissions as the application.
- Project files are data, but external file references and plugin settings must still be treated cautiously when opening projects from unknown sources.
- Security reports should follow `SECURITY.md` instead of public issue disclosure.

## Build from Source

Full source builds require Python 3.12+, Qt/PySide6, a compatible GDAL runtime, and platform packaging prerequisites when producing distributable artifacts. Development builds do not require signing credentials.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m geodesk
```

## Packaging and Release Engineering

Release artifacts are produced from an annotated release tag. Packaging jobs pin the native geospatial runtime, run tests before packaging, and keep signing credentials outside repository configuration.

### Validate release tree

run unit, UI smoke, schema-migration, and package metadata checks before creating installers.

```bash
python -m pytest
```

### Build platform package

invoke the platform packaging recipe without embedding developer-local paths.

```bash
python tools/package.py --platform current
```

### Sign and publish

signing/notarization occurs only in protected release jobs; checksums accompany published artifacts.


## Development and Testing

Unit tests protect project serialization and migrations, UI tests cover critical desktop workflows, and packaging smoke tests start the produced application on each maintained platform.

```bash
python -m pip install -e '.[dev]'
python -m geodesk --debug
```

```bash
python -m pytest
python -m ruff check .
python tools/check_project_migrations.py
```

## Backup and Migration

Back up `.geodesk` project files and any external datasets they reference. Preferences are optional; cache is disposable. Before major-version upgrades, copy irreplaceable projects and read the migration notes. Plugin directories should be restored from trusted package sources rather than blindly copied between major versions.

## Troubleshooting and Diagnostics

- **Application fails to start:** launch with `--debug`, inspect the local log directory, and verify packaged Qt/GDAL libraries are present before deleting user settings.
- **Project opens with missing layers:** check whether external dataset paths moved; project migration does not copy source data.
- **Plugin causes startup errors:** start with plugins disabled, remove or upgrade the incompatible plugin, then re-enable plugins individually.
- **Rendering differs across machines:** compare GeoDesk version, packaged GDAL/Qt versions, GPU driver, fonts, and project style resources.

## Documentation

- **User Guide:** docs/user-guide.md — projects, layers, styles, preferences, and shortcuts
- **Project Format:** docs/project-format.md — schema versions and migration policy
- **Plugin Guide:** docs/plugins.md — trusted plugin installation and public extension API
- **Build Guide:** docs/building.md — platform prerequisites and developer builds
- **Release Engineering:** docs/releasing.md — packaging, signing, checksums, and release channels
- **Privacy:** docs/privacy.md — network requests, update checks, and diagnostic data

## Contributing

Changes to project schema, plugin API, platform support, packaging, data locations, or network behavior require corresponding tests and documentation. See `CONTRIBUTING.md` for the development workflow.

## License

GeoDesk is released under the MIT License.
