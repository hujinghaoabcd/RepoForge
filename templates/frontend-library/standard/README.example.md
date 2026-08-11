<div align="center">


# MapWidget

**A framework-neutral TypeScript layer-control widget with events, theming, and map-library adapters.**

[![npm](https://img.shields.io/badge/npm-package-red)](#installation) [![TypeScript](https://img.shields.io/badge/TypeScript-ready-blue)](#api-overview) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#development-and-testing) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


Demo · Install · Quick Start · API · Compatibility
</div>

---
## Why MapWidget?

Map applications repeatedly rebuild layer switching, visibility state, keyboard behavior, and map-engine glue. MapWidget keeps the UI framework-neutral and exposes small adapters rather than requiring a new application framework.

## Features

- **Framework-neutral core** — use the widget from vanilla TypeScript or wrap it in an application framework.
- **Map adapters** — optional bindings keep Leaflet and MapLibre synchronization outside the core state model.
- **Accessible controls** — keyboard navigation and labelled interactive elements are part of the public behavior.
- **Themeable CSS** — customize documented CSS variables without copying package styles.

## Demo

https://example.org/map-widget/demo

## Preview


## Installation

```bash
npm install @geo-ui/map-widget
```

Import `@geo-ui/map-widget/style.css` once before mounting the widget.

## Quick Start

```ts
import { MapWidget } from "@geo-ui/map-widget"
import "@geo-ui/map-widget/style.css"

const widget = new MapWidget({
  target: document.querySelector("#layers")!,
  layers: [
    { id: "roads", label: "Roads", visible: true },
    { id: "water", label: "Water", visible: false },
  ],
})

widget.on("change", ({ id, visible }) => console.log(id, visible))
```

## API Overview

| API | Purpose |
| --- | --- |
| `MapWidget(options)` | create and mount a layer-control instance. |
| `select(id)` | move the active selection to one layer. |
| `setVisible(id, visible)` | update layer visibility state. |
| `on(event, listener)` | subscribe to documented widget events. |

## Styling and Theming

The package ships one namespaced stylesheet and documented CSS custom properties. DOM class names not listed in the styling guide are implementation details.

## Framework Integration

- **Leaflet:** official adapter synchronizes widget state with Leaflet layers. — docs/adapters/leaflet.md
- **MapLibre GL JS:** official adapter synchronizes style-layer visibility. — docs/adapters/maplibre.md

## Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
| **Browsers** | current evergreen releases | ES2020 modules and standard DOM APIs |
| **TypeScript** | 5.4+ | declarations ship with the package |
| **Leaflet adapter** | Leaflet 1.9+ | optional peer dependency |
| **MapLibre adapter** | MapLibre GL JS 5+ | optional peer dependency |

## Development and Testing

```bash
pnpm install
pnpm dev
```

```bash
pnpm test
pnpm test:e2e
```

## Documentation

- **Getting Started:** docs/getting-started.md — install, CSS, and first widget
- **API:** docs/api.md — public methods, options, and events
- **Adapters:** docs/adapters.md — Leaflet and MapLibre integrations

## License

MapWidget is released under the MIT License.
