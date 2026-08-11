# GeoPortal

**A production-oriented geospatial platform for publishing, managing, and exploring spatial data.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#testing) [![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](#testing) [![Docker](https://img.shields.io/badge/docker-ready-blue)](#deployment) [![Security](https://img.shields.io/badge/security-policy-blue)](#security) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Demo · Architecture · Development · Deployment · Operations · Security

## Product Overview

GeoPortal is a self-hostable web platform for organizations that publish geospatial catalogues and interactive maps. It combines a browser client, authenticated API, spatial database, background import workers, and object storage while keeping deployment and data-ownership boundaries explicit.

Demo: https://demo.example.org

## Features

- **Spatial catalogue** — manage vector, raster, metadata, and publication state.
- **Interactive maps** — compose map views, inspect features, and share stable links.
- **Controlled publishing** — separate public viewing, authenticated editing, and administrative operations.
- **Asynchronous imports** — process large geospatial uploads outside request/response paths.
- **Self-hosted data ownership** — keep application database and object storage under operator control.

## Architecture

The reference deployment separates user-facing HTTP traffic from stateful services and asynchronous work. Operators may replace individual infrastructure services if they preserve the documented contracts.

| Component | Technology / service | Responsibility |
| --- | --- | --- |
| **Web client** | Vue 3 + Vite + OpenLayers | browser interface, maps, and upload UX |
| **Application API** | Django + Django REST Framework | authentication, catalogue rules, and API endpoints |
| **Database** | PostgreSQL + PostGIS | accounts, metadata, and spatial records |
| **Queue / cache** | Redis | task broker, short-lived coordination, and cache data |
| **Worker** | Celery | imports, previews, and long-running geoprocessing |
| **Object storage** | S3-compatible storage | uploaded source files and generated assets |

## Local Development

### Requirements

- Docker Engine + Compose plugin
- Node.js 22+ for frontend-only development
- Python 3.12+ for backend-only development
- at least one S3-compatible bucket for full import workflows

### Bootstrap

```bash
cp .env.example .env
docker compose up -d
python manage.py migrate
npm --prefix frontend install
npm --prefix frontend run dev
```

### Local access points

- **Web UI:** http://localhost:5173
- **API:** http://localhost:8000/api/
- **Health endpoint:** http://localhost:8000/health/

## Configuration and Secrets

Copy `.env.example` for local development. Production secrets must come from the deployment secret store rather than being committed to Git.

| Variable | Required | Secret | Purpose |
| --- | --- | --- | --- |
| `DATABASE_URL` | Yes | Yes | PostgreSQL/PostGIS connection |
| `SECRET_KEY` | Yes | Yes | Django signing and security primitives |
| `REDIS_URL` | Yes | No | queue broker and cache connection |
| `S3_ENDPOINT_URL` | Yes | No | S3-compatible object-storage endpoint |
| `S3_ACCESS_KEY_ID` | Yes | Yes | object-storage credential |
| `S3_SECRET_ACCESS_KEY` | Yes | Yes | object-storage credential |

## Database and Migrations

Django migrations define application schema changes. Deployments must run migrations once per release before all application replicas are moved to code that requires the new schema. Large data backfills should be implemented as explicit operational jobs rather than hidden inside request startup.

```bash
python manage.py migrate --check
python manage.py migrate
```

## API

The authenticated JSON API serves the web client and supported integrations. Public endpoints and administrative endpoints use separate permission policies; internal worker callbacks are not part of the public API contract.

API documentation: docs/api.md

## Authentication and Authorization

GeoPortal uses session authentication for the browser and scoped tokens for supported API integrations. Authorization is role- and object-aware: authenticated access does not imply permission to publish, delete, or administer datasets.

## Background Jobs and Queues

Celery workers execute imports, preview generation, and long-running geospatial jobs. Worker concurrency and retry policy must be tuned independently from web-server concurrency. Failed jobs remain observable and should not be treated as successful uploads.

## File and Object Storage

Uploaded source files and generated artefacts are stored in S3-compatible object storage. Database backups do not include object content, so recovery plans must cover both the database and storage bucket.

## Deployment

The supported self-host deployment uses container images behind a TLS-terminating reverse proxy. Production configuration must disable debug mode and use persistent database/object-storage volumes or managed services.

### Build or pull images

Use immutable image tags for releases rather than deploying from a mutable development checkout.

```bash
docker compose -f compose.prod.yml pull
```

### Run database migrations

Apply the release schema before switching all application replicas.

```bash
docker compose -f compose.prod.yml run --rm web python manage.py migrate
```

### Start services

Start web, worker, and supporting services and then verify health checks.

```bash
docker compose -f compose.prod.yml up -d
```

### Reverse proxy and TLS

Terminate HTTPS at the reverse proxy, forward trusted proxy headers explicitly, and keep upload-size/timeouts aligned with documented import limits.

## CI/CD

CI runs unit/integration tests, frontend checks, container builds, and migration checks. Production delivery should promote an immutable tested image; CI credentials must not be copied into runtime environment files.

## Observability and Operations

### Health checks

Use `/health/` for process readiness and a deeper operator check for database, Redis, and object-storage connectivity.

```bash
curl -f https://geoportal.example.org/health/
```

### Logs

Web and worker processes emit structured logs to stdout/stderr. Preserve request/job identifiers across API and worker logs so asynchronous failures can be traced.

### Metrics and alerts

Monitor request error rate, queue depth, failed jobs, database capacity, object-storage failures, and disk/volume pressure where applicable.

## Backup and Restore

Back up PostgreSQL/PostGIS and object storage as one recovery set. Test restoration on a non-production environment. Redis is treated as transient coordination state and is not the authoritative copy of application data.

## Security

- never commit production `.env` files, signing keys, database passwords, or object-storage credentials;
- run with `DEBUG=false`, explicit allowed hosts/origins, HTTPS, and secure cookie settings in production;
- uploaded geospatial files are untrusted input and must be size-limited, validated, and processed outside privileged paths;
- public sharing links and API tokens require revocation and scope rules;
- report vulnerabilities through `SECURITY.md` rather than a public issue.

## Testing

Run backend, frontend, and integration tests. Deployment changes should also exercise migration and container smoke checks.

```bash
python -m pytest
npm --prefix frontend test
docker compose -f compose.test.yml up --abort-on-container-exit
```

## Documentation

- **Architecture:** docs/architecture.md — components, trust boundaries, and data flow
- **Local Development:** docs/development.md — frontend/backend workflows and local services
- **Deployment:** docs/deployment.md — production configuration, proxy, and service topology
- **Operations:** docs/operations.md — health, logs, metrics, backup, and restore
- **API:** docs/api.md — supported endpoints, tokens, and compatibility
- **Security:** SECURITY.md — private vulnerability reporting and security scope

## Upgrade Notes

- read release notes for schema, environment-variable, and service changes before replacing containers;
- back up the database and object storage before upgrades that include migrations or storage-format changes;
- run migrations exactly once per release and verify health checks before completing rollout;
- upgrade workers and web processes as one compatibility set unless the release notes explicitly support mixed versions.

## Contributing

Use the development guide to choose frontend, backend, or infrastructure setup. Changes to public environment variables, API contracts, migrations, or deployment topology must update the corresponding documentation and tests.

## License

GeoPortal is released under the MIT License.
