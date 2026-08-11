# GeoPortal

**A lightweight web application for exploring and sharing geospatial datasets.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#run-locally) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

GeoPortal provides a focused browser interface for browsing map layers, inspecting feature properties, and sharing a small public catalogue.

## Features

- Interactive map and layer switcher
- Feature inspection and simple attribute search
- Shareable map views with URL state

## Run Locally

Install dependencies and start the development server.

```bash
npm install
npm run dev
```

Open: http://localhost:5173

## Configuration

- **`VITE_API_URL`** — base URL used by the browser client for data requests Example: `http://localhost:8000`.
## Deploy

Build the static frontend and publish the generated `dist/` directory behind a normal static web server.

```bash
npm run build
```

## License

GeoPortal is released under the MIT License.
