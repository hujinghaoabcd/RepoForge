<div align="center">


# GeoBoard

**A lightweight browser dashboard for exploring and sharing geospatial indicators.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#run-locally) [![Docker](https://img.shields.io/badge/docker-ready-blue)](#deploy) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


</div>

---
## Preview

<p align="center">
  <img src="docs/assets/geoboard-overview.png" alt="GeoBoard screenshot" width="800">
</p>


## Features

- Explore map-based indicators with filters and time controls.
- Share stable dashboard URLs with selected layers and views.
- Import GeoJSON datasets for lightweight team analysis.
- Run locally or deploy as a single container.

## Run Locally

Copy the example environment file, install dependencies, and start the development server.

```bash
cp .env.example .env
npm install
npm run dev
```

Open `http://localhost:3000` after the development server starts.

## Configuration

| Variable | Required | Purpose |
| --- | --- | --- |
| `DATABASE_URL` | Yes | PostgreSQL connection used by the application. |
| `APP_BASE_URL` | Yes | Public base URL used when generating shared links. |

## Deploy

The primary production path is the repository Docker image.

```bash
docker compose up -d
```

Persist the database volume and back it up before upgrades.

## License

MIT.
