<div align="center">


# MapWidget

**A modular TypeScript map-control toolkit with a framework-neutral core, official adapters, and explicit runtime contracts.**

[![npm](https://img.shields.io/badge/npm-packages-red)](#packages-and-installation) [![TypeScript](https://img.shields.io/badge/TypeScript-ready-blue)](#typescript-support) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#development-and-testing) [![Bundle](https://img.shields.io/badge/tree--shaking-supported-blue)](#bundle-and-tree-shaking) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


Demo · Packages · API · Adapters · Compatibility · Accessibility
</div>

---
## Why MapWidget?

Layer-control UI becomes complex when applications need stable state, keyboard interaction, theming, multiple map engines, framework wrappers, and predictable package boundaries. MapWidget separates a small framework-neutral core from optional integrations.

## Features

- **Core state and DOM widget** — dependency-light package for vanilla browser applications.
- **Official map adapters** — Leaflet and MapLibre bindings keep engine-specific code out of core.
- **Framework adapters** — React and Vue packages expose lifecycle-safe wrappers around the same core contract.
- **Typed public APIs** — declarations and exported event types ship with every maintained package.
- **Accessible interaction model** — keyboard and focus behavior are tested as part of component behavior.

## Live Demo

https://example.org/map-widget/playground

## Preview


## Packages and Installation

| Package | Use when | Install |
| --- | --- | --- |
| `@geo-ui/map-widget` | framework-neutral core and DOM widget | `npm install @geo-ui/map-widget` |
| `@geo-ui/map-widget-leaflet` | Leaflet synchronization adapter | `npm install @geo-ui/map-widget @geo-ui/map-widget-leaflet leaflet` |
| `@geo-ui/map-widget-maplibre` | MapLibre GL JS synchronization adapter | `npm install @geo-ui/map-widget @geo-ui/map-widget-maplibre maplibre-gl` |
| `@geo-ui/map-widget-react` | React component wrapper | `npm install @geo-ui/map-widget-react react` |
| `@geo-ui/map-widget-vue` | Vue component wrapper | `npm install @geo-ui/map-widget-vue vue` |

DOM packages require `@geo-ui/map-widget/style.css`. Framework adapters use the same CSS contract, and peer dependencies are not bundled into adapter packages.

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

widget.on("visibilitychange", ({ id, visible }) => console.log({ id, visible }))
```

## API Overview

| API family | Purpose | Stability |
| --- | --- | --- |
| `MapWidget` | create, update, and destroy the DOM widget. | public |
| `LayerItem` | typed layer identity, label, visibility, and disabled state. | public |
| `WidgetEventMap` | event payload types for selection and visibility changes. | public |
| `createStore` | use state management without rendering the built-in DOM widget. | public |

## Events and Lifecycle

| Event / hook | When it fires | Typical use |
| --- | --- | --- |
| `visibilitychange` | layer visibility changes | synchronize map-engine layer visibility |
| `select` | active layer selection changes | update inspectors or detail panels |
| `destroy` | widget teardown completes | release adapter subscriptions |

## Styling, Themes, and CSS Contract

The supported styling surface is a documented set of CSS custom properties and data attributes. Internal class names are not a compatibility contract.

## Framework Adapters

| Adapter | Package / status | Notes |
| --- | --- | --- |
| **Leaflet** | @geo-ui/map-widget-leaflet | official; Leaflet remains a peer dependency |
| **MapLibre GL JS** | @geo-ui/map-widget-maplibre | official; MapLibre remains a peer dependency |
| **React** | @geo-ui/map-widget-react | official lifecycle wrapper |
| **Vue** | @geo-ui/map-widget-vue | official lifecycle wrapper |

## TypeScript Support

Packages ship declaration files from the same source as runtime exports. Public option, event, and adapter types follow the package semantic-versioning policy.

## Bundle and Tree-Shaking

ESM builds are side-effect free except for the explicit CSS entry. Named JavaScript exports are designed to tree-shake. Size claims belong in a reproducible size report.

## SSR and Non-Browser Environments

The core state store can be imported without a browser, but DOM widget construction requires `document`. Framework wrappers defer DOM work until client mount.

## Browser Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
| **Browsers** | current and previous evergreen releases | tested DOM, keyboard, and pointer interactions |
| **TypeScript** | 5.4+ | declaration tests run in CI |
| **React adapter** | React 18+ | optional peer dependency |
| **Vue adapter** | Vue 3.4+ | optional peer dependency |
| **Leaflet adapter** | Leaflet 1.9+ | optional peer dependency |
| **MapLibre adapter** | MapLibre GL JS 5+ | optional peer dependency |

## Accessibility

Keyboard navigation, visible focus, accessible names, and disabled-state behavior are tested for the built-in widget. Applications that replace markup or styles must preserve those semantics.

## Examples

- **Vanilla TypeScript:** examples/vanilla/ — core widget, CSS, and events
- **Leaflet:** examples/leaflet/ — synchronize visibility with a Leaflet map
- **MapLibre:** examples/maplibre/ — control style-layer visibility
- **React:** examples/react/ — controlled component lifecycle
- **Vue:** examples/vue/ — reactive wrapper and events

## Development and Testing

The repository is a pnpm workspace. Core behavior uses unit tests, adapters use integration fixtures, and browser interaction uses Playwright.

```bash
pnpm install
pnpm build
pnpm dev
```

```bash
pnpm test
pnpm test:type
pnpm test:e2e
```

## Release and Versioning Policy

Public JavaScript/TypeScript APIs and documented CSS variables follow Semantic Versioning. Peer-dependency support windows and deprecated APIs are announced in release notes.

## Documentation

- **Getting Started:** docs/getting-started.md — package choice, install, CSS, and first widget
- **API Reference:** docs/api.md — public options, methods, events, and types
- **Framework Adapters:** docs/adapters.md — React, Vue, Leaflet, and MapLibre contracts
- **Styling:** docs/styling.md — CSS variables, states, and supported customization
- **Accessibility:** docs/accessibility.md — keyboard/focus behavior and downstream responsibilities
- **Migration Guide:** docs/migrations.md — breaking changes and version transitions

## Contributing

Contributions should include tests at the layer they change. New public exports, CSS variables, events, adapters, or peer-dependency ranges must update documentation and versioning notes.

## License

MapWidget is released under the MIT License.
