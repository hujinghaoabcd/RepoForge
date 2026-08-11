<p align="center">
  <img src="../../../assets/logo.svg" alt="GeoBoard" width="160">
</p>

<p align="center">
  <img src="../../../assets/screenshots/repoforge-preview.webp" alt="GeoBoard product overview" width="780">
</p>

# GeoBoard

**A production-oriented geospatial collaboration platform for publishing, reviewing, and operating spatial dashboards.**

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#testing) [![Docker](https://img.shields.io/badge/docker-supported-blue)](#deployment) [![Security](https://img.shields.io/badge/security-policy-blue)](#security) [![Docs](https://img.shields.io/badge/docs-online-blue)](#documentation) [![License](https://img.shields.io/badge/license-MIT-green)](#license)

Demo · Architecture · Development · Deployment · Operations · Security · Docs

## Product Overview

GeoBoard is a complete browser application for teams that publish spatial indicators and maintain shared geospatial workspaces. It combines a React client, Django API, spatial database, background processing, object storage, and operational controls while keeping deployment contracts explicit.

**Demo:** https://demo.example.org

## Screenshots / Demo

The main workspace combines the map, dataset catalogue, saved dashboards, review status, and publishing controls.

## Features

- **Workspace-based publishing** — organize datasets and dashboards by team workspace.
- **Spatial dataset lifecycle** — upload, validate, version, and retire geospatial layers.
- **Saved analytical views** — persist filters, map state, indicators, and sharing rules.
- **Role-based access** — separate viewers, editors, publishers, and administrators.
- **Background imports** — move expensive validation and ingestion outside request/response execution.
- **Auditable releases** — record who published a dashboard or replaced a dataset version.

## Architecture

The production system is split by operational responsibility rather than by repository folder alone.

| Component | Technology / service | Responsibility |
| --- | --- | --- |
| **Web client** | React + TypeScript | interactive map, dashboards, and administration UI |
| **Application API** | Django + DRF | domain logic, permissions, APIs, and orchestration |
| **Primary database** | PostgreSQL + PostGIS | application state and spatial queryable data |
| **Task workers** | Celery + Redis | imports, validation, exports, and notifications |
| **Object storage** | S3-compatible storage | uploaded source files and generated exports |
| **Edge** | reverse proxy / ingress | TLS termination, routing, and request limits |

## Tech Stack

- **Python / Django** — backend application and REST API.
- **React / TypeScript** — browser client.
- **PostgreSQL / PostGIS** — transactional and spatial persistence.
- **Celery / Redis** — asynchronous task execution.
- **S3-compatible object storage** — uploaded and generated artifacts.
- **Docker** — supported deployment and development packaging.

## Local Development

### Requirements

- Python 3.12+
- Node.js 22+
- Docker 27+ with Compose plugin
- PostgreSQL/PostGIS, Redis, and S3-compatible storage (provided by the development Compose stack)

### Bootstrap

```bash
cp .env.example .env
docker compose up -d db redis object-storage
python -m pip install -r requirements/dev.txt
npm install
python manage.py migrate
npm run dev
```

Run backend and worker processes using the commands documented in `docs/development.md`; the web client is served at `http://localhost:3000`.

## Configuration and Secrets

Treat `.env.example` as the machine-readable inventory. The README only surfaces groups that materially affect application identity or safe deployment. Production secrets must come from the deployment platform, not committed files.

| Group | Variable | Required | Purpose |
| --- | --- | --- | --- |
| Core | `SECRET_KEY` | Yes | server-side signing secret. |
| Core | `APP_BASE_URL` | Yes | canonical external URL. |
| Database | `DATABASE_URL` | Yes | PostgreSQL/PostGIS connection. |
| Queue | `REDIS_URL` | Yes | task broker/cache endpoint. |
| Storage | `S3_ENDPOINT_URL` | Yes | object-storage endpoint. |
| Storage | `S3_BUCKET` | Yes | bucket for uploaded and generated files. |
| Email | `EMAIL_URL` | Production-dependent | transactional email provider connection. |

## Database and Migrations

Schema changes are shipped as Django migrations and must be applied as part of each release rollout. Do not run application replicas against mixed schema versions unless a release explicitly documents compatibility.

```bash
python manage.py migrate
```

### Backup / Restore Boundary

Back up PostgreSQL and object storage as one logical application dataset. A database-only backup may reference objects that no longer exist, while an object-only backup cannot reconstruct permissions, metadata, or versions. Test restore procedures outside production.

## Public API / Webhooks

The browser client uses the same versioned application API exposed to approved integrations. Webhook consumers must tolerate retries and verify signatures.

- **API guide:** docs/api.md
- **Webhooks:** docs/webhooks.md

## Authentication and Authorization

Authentication can be local or delegated to an external identity provider. Authorization remains workspace/role based inside GeoBoard. SSO authentication does not automatically grant workspace access. Production deployments should review cookie, proxy-header, origin, and tenant-boundary settings together.

## Background Jobs and Queues

Celery workers execute dataset validation, imports, exports, and notification tasks. Web processes should remain able to serve read-only pages when long-running jobs are backed up, while operations that require a completed import remain pending.

```bash
celery -A geoboard worker -l info
```

## Object Storage / Media

Uploaded source files and generated exports live in S3-compatible object storage. Buckets are private by default; downloads are authorized by the application and served through short-lived URLs.

## Email

Transactional email is optional for local development but required for production flows that send invitations, password resets, and publishing notifications.

## Deployment

Two deployment paths are first-class. Both assume an external TLS endpoint and persistent PostgreSQL/object-storage backups.

### Docker Compose

Recommended for a single-host self-managed deployment.

```bash
docker compose -f compose.production.yml pull
docker compose -f compose.production.yml up -d
python manage.py migrate
```

### Container Platform

Use the published images on Kubernetes or another orchestrator; keep migrations as an explicit release step rather than running them independently in every replica.

```bash
helm upgrade --install geoboard deploy/helm/geoboard
```

## CI/CD

CI runs linting, unit/integration tests, frontend tests, build verification, and migration checks. Release pipelines build immutable images; production deployment credentials remain outside repository workflows.

## Observability and Operations

- **Health** — expose separate liveness/readiness checks for web and worker processes.
- **Logs** — emit structured application logs without secrets or raw uploaded data.
- **Metrics** — track request errors/latency, queue depth, failed jobs, database health, and storage failures.
- **Backups** — monitor successful database and object-storage backups and periodically test restore.
- **Capacity** — watch database growth, object-storage usage, and worker queue delay.

## Security

- Never commit production secrets or `.env` files.
- Terminate TLS at a trusted reverse proxy/ingress and configure forwarded-host/proto handling explicitly.
- Keep uploaded source files private unless a project intentionally publishes them.
- Validate archive and geospatial uploads before background processing; enforce file-size and extraction limits.
- Review CORS/CSRF/origin settings together when frontend and API use different hosts.
- Report vulnerabilities privately through the repository security policy rather than public issues.

## Testing

Run backend, frontend, integration, and migration checks before release. Use end-to-end tests for critical authentication, permissions, upload, and publishing flows.

```bash
python -m pytest
npm test
```

```bash
npm run test:e2e
```

## Upgrade Notes

- Read release notes before upgrading across minor/major versions.
- Back up PostgreSQL and object storage before applying schema or data migrations.
- Apply database migrations once per rollout and wait for completion before scaling the new application version.
- Review deprecated environment variables and reverse-proxy settings during each upgrade.
- Run post-upgrade health checks and one representative upload/publish workflow before declaring the release complete.

## Documentation

- **Architecture:** docs/architecture.md — component boundaries and data flows
- **Development:** docs/development.md — full local process layout and debugging
- **Configuration:** docs/configuration.md — complete environment-variable reference
- **Deployment:** docs/deployment.md — Compose, ingress, volumes, and production requirements
- **Operations:** docs/operations.md — health, logs, metrics, backup, restore, and incident hints
- **Security:** SECURITY.md — vulnerability reporting and supported versions

## Contributing

Open an issue or discussion before large architectural changes. Contributions should include tests for behavior changes, migrations when schema changes, and documentation for new production configuration.

## License

MIT.
