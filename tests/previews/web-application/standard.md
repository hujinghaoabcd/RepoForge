<div align="center">

<img src="../../../assets/logo.svg" alt="GeoBoard" width="160">

# GeoBoard

**A deployable geospatial dashboard for teams that publish, compare, and monitor spatial indicators.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#testing) [![Docker](https://img.shields.io/badge/docker-ready-blue)](#deployment) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)


Demo · Features · Local Development · Deployment · Documentation
</div>

---
## Overview

GeoBoard combines a browser map, a small application API, and PostgreSQL/PostGIS persistence so teams can publish repeatable spatial dashboards without maintaining a separate GIS desktop workflow for every viewer.

**Demo:** https://demo.example.org

## Screenshots / Demo

<p align="center">
  <img src="../../../assets/placeholders/screenshot.svg" alt="GeoBoard screenshot" width="760">
</p>


The overview page combines the map, indicator filters, saved views, and dataset status in one workspace.

## Features

- **Map-first exploration** — browse spatial indicators, categories, and time slices.
- **Saved dashboards** — store shareable combinations of layers, filters, and map position.
- **Dataset imports** — load validated GeoJSON datasets into project workspaces.
- **Role-aware editing** — separate viewers from users allowed to publish or replace datasets.
- **Container deployment** — run the application and database with a supported Compose setup.

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
| **Frontend** | React + TypeScript | interactive dashboard and map UI |
| **Backend** | Django + Django REST Framework | application API and access control |
| **Database** | PostgreSQL + PostGIS | users, dashboards, datasets, and spatial queries |
| **Runtime** | Docker Compose | repeatable local/self-host deployment |

## Local Development

### Requirements

- Node.js 22+
- Python 3.12+
- PostgreSQL/PostGIS, or Docker for the development stack

### Start

```bash
cp .env.example .env
docker compose up -d db
python -m pip install -r requirements/dev.txt
npm install
npm run dev
```

The frontend is available at `http://localhost:3000`; the API runs at `http://localhost:8000`.

## Environment Variables

Keep secrets out of version control. The README lists only variables needed to understand the development contract; see `.env.example` for the complete set.

| Variable | Required | Purpose |
| --- | --- | --- |
| `DATABASE_URL` | Yes | PostgreSQL/PostGIS connection. |
| `SECRET_KEY` | Yes | server-side signing secret; use a unique production value. |
| `APP_BASE_URL` | Yes | public application URL. |
| `CORS_ALLOWED_ORIGINS` | Development-dependent | allowed browser origins when frontend/API run separately. |

## Database

Database migrations are versioned with the application. Apply them after pulling a release that changes schema.

```bash
python manage.py migrate
```

```bash
python manage.py seed_demo
```

## Deployment

The supported self-host path uses the production Docker Compose definition.

```bash
docker compose -f compose.production.yml up -d
```

Back up PostgreSQL and uploaded datasets before production upgrades. TLS termination belongs at the reverse proxy or ingress layer.

## Project Structure

```text
frontend/       # React application
backend/        # Django project and API
docs/           # deployment and operator guides
compose.yml     # development services
compose.production.yml
```

## Testing

```bash
python -m pytest
npm test
```

Run backend and frontend tests before opening a pull request. End-to-end browser tests are documented separately.

## Documentation

- **Development:** docs/development.md — local setup and debugging
- **Configuration:** docs/configuration.md — complete environment-variable reference
- **Deployment:** docs/deployment.md — production Compose and reverse-proxy setup
- **Operations:** docs/operations.md — backup, restore, and upgrade procedures

## License

MIT.
