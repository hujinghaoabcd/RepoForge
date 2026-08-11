<div align="center">

<img src="../../../assets/logo.svg" alt="GeoDesk" width="160">

# GeoDesk

**A lightweight cross-platform desktop viewer for local geospatial datasets.**

<a href="https://github.com/example/geodesk/releases"><img src="https://img.shields.io/badge/release-v0.4.0-blue" alt="Release"></a> <a href="#supported-platforms"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey" alt="Platforms"></a> <a href="#run-from-source"><img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build"></a> <a href="#license"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
<a href="#download-and-install">Download</a> · <a href="docs/">Docs</a> · <a href="https://github.com/example/geodesk/issues">Issues</a></div>

---

## Features

- **Local-first maps** — open GeoPackage, GeoJSON, Shapefile, and GeoTIFF datasets without a server.
- **Layer inspection** — toggle layers, inspect attributes, and view basic metadata.
- **Cross-platform desktop UI** — the same project format works on Windows, macOS, and Linux.

## Preview

<p align="center">
  <img src="../../../assets/placeholders/screenshot.svg" alt="GeoDesk screenshot" width="760">
</p>


## Download and Install

Download the latest signed or packaged build from the Releases page. Choose the package that matches your operating system.

| Platform | Package | Link |
| --- | --- | --- |
| Windows | x64 installer | Releases / `GeoDesk-Setup-x64.exe` |
| macOS | universal DMG | Releases / `GeoDesk-universal.dmg` |
| Linux | AppImage | Releases / `GeoDesk-x86_64.AppImage` |

## Supported Platforms

- **Windows:** Windows 11 x64
- **macOS:** macOS 13+ on Apple Silicon or Intel
- **Linux:** recent x86_64 desktop distributions with FUSE support for AppImage

## Run from Source

```bash
python -m pip install -e .
python -m geodesk
```

## License

GeoDesk is released under the MIT License.
