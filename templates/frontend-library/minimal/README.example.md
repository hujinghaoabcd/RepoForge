<div align="center">


# MapWidget

**A tiny TypeScript layer-control widget for browser maps.**

[![npm](https://img.shields.io/badge/npm-package-red)](#install) [![TypeScript](https://img.shields.io/badge/TypeScript-ready-blue)](#quick-start) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


</div>

---
## Install

```bash
npm install @geo-ui/map-widget
```

Import the package CSS once in the application entry point with `import "@geo-ui/map-widget/style.css"`.

## Quick Start

```ts
import { MapWidget } from "@geo-ui/map-widget"
import "@geo-ui/map-widget/style.css"

const widget = new MapWidget({
  target: document.querySelector("#layers")!,
  layers: ["roads", "buildings", "water"],
})

widget.select("roads")
```

## Browser Support

Current evergreen desktop and mobile browsers with ES2020 module support.

## License

MapWidget is released under the MIT License.
