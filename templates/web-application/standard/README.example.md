# GeoPortal

**A deployable geospatial web application for managing, exploring, and sharing map layers.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#testing) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#testing) [![Docker](https://img.shields.io/badge/docker-ready-blue)](#deployment) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Demo · Features · Local Development · Deployment · Docs

## Overview

GeoPortal combines a browser map interface with a small API and relational database. It is intended to be run as an application: users interact with the deployed service, while contributors develop the frontend and backend together.

Demo: https://demo.example.org

## Features

- **Layer catalogue** — publish project-approved vector and raster layers.
- **Interactive exploration** — filter, inspect, and share map views from the browser.
- **Role-aware editing** — restrict layer management operations to authenticated maintainers.
- **Import workflow** — upload supported geospatial files and track import status.

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
| **Frontend** | Vue 3 + Vite | browser UI and map interactions |
| **Backend** | Django + Django REST Framework | API, authentication, and business rules |
| **Database** | PostgreSQL + PostGIS | application and spatial data |

## Local Development

### Requirements

- Node.js 22+
- Python 3.12+
- PostgreSQL 16+ with PostGIS
- Docker Compose (recommended for local services)

### Start the application

```bash
cp .env.example .env
docker compose up -d db
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Local access

- **Application:** http://localhost:8000
- **API:** http://localhost:8000/api/

## Environment Variables

| Variable | Required | Purpose | Example |
| --- | --- | --- | --- |
| `DATABASE_URL` | Yes | PostgreSQL/PostGIS connection string | `postgresql://geoportal:geoportal@localhost:5432/geoportal` |
| `SECRET_KEY` | Yes | Django cryptographic signing key | `change-me-in-production` |
| `DEBUG` | No | development debug mode only | `true` |

## Database and Migrations

Schema changes are managed through Django migrations. Run migrations after pulling changes that modify the application schema; do not point local development commands at a production database.

```bash
python manage.py migrate
```

## Deployment

The reference deployment builds the frontend, collects Django static assets, and runs the application behind a production HTTP server. Use the project Docker Compose deployment for a small self-hosted instance.

```bash
docker compose -f compose.prod.yml up -d
```

## Project Structure

```text
frontend/        Vue application
backend/         Django project and apps
docs/            operator and developer guides
compose.yml      local services
compose.prod.yml reference self-host deployment
```

## Testing

Run backend and frontend checks before submitting changes.

```bash
python -m pytest
npm --prefix frontend test
```

## Documentation

- **Development:** docs/development.md — local setup and contributor workflow
- **Deployment:** docs/deployment.md — production configuration and upgrades
- **API:** docs/api.md — HTTP endpoints and authentication

## License

GeoPortal is released under the MIT License.
