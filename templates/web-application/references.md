# Web Application README References

This file records patterns from mature deployable web-application repositories. RepoForge extracts section-level lessons rather than copying one project wholesale.

## Plausible Analytics

Repository: https://github.com/plausible/analytics

Useful patterns:

- product identity, links, and screenshot appear before implementation details;
- clearly distinguishes managed cloud from self-hosted community operation;
- explains product motivation and user-facing capabilities;
- gives operators an explicit ownership boundary for self-hosting;
- exposes the technology stack without turning README into an architecture manual.

RepoForge takeaway: a web-application README is a **product landing page plus an operational entrance**, not just a developer setup file.

## Immich

Repository: https://github.com/immich-app/immich

Useful patterns:

- strong product logo/tagline/screenshot hierarchy;
- demo, docs, installation, roadmap, and contribution links are easy to find;
- a critical backup warning is placed prominently because operational misuse can lose user data;
- feature coverage is visible while detailed installation moves to authoritative docs.

RepoForge takeaway: safety-critical operational responsibilities such as backup must not be hidden deep in deployment documentation.

## Outline

Repository: https://github.com/outline/outline

Useful patterns:

- distinguishes hosted usage, self-hosting, and contributing;
- routes production installation to a hosting guide;
- links a dedicated architecture document;
- documents development logging/debugging, tests, and database migrations;
- keeps README relatively compact despite being a mature full-stack application.

RepoForge takeaway: Full should expose architecture and operations boundaries while still handing detailed procedures to docs.

## Documenso

Repository: https://github.com/documenso/documenso

Useful patterns:

- product identity, screenshot, community links, and technology stack are clear;
- local-development prerequisites and `.env` bootstrap are explicit;
- lists local service access points;
- separates Docker/self-hosting from developer setup;
- links security policy and troubleshooting guidance.

RepoForge takeaway: a maintained application should make its local runtime contract and supported deployment entry points concrete.

## Section champions

| README function | Reference | Lesson |
| --- | --- | --- |
| Product-first opening | Plausible / Immich | show the application before internals |
| Demo + screenshot | Immich | let visitors understand the product quickly |
| Hosted vs self-hosted boundary | Plausible / Outline | distinguish ways of consuming the product |
| Local developer bootstrap | Documenso | prerequisites, env file, services, and access points |
| Architecture handoff | Outline | high-level architecture in README, depth in docs |
| Migration visibility | Outline | schema changes are an operator/developer contract |
| Backup warning | Immich | surface data-loss responsibilities prominently |
| Self-hosting operations | Plausible / Documenso | deployment changes responsibility, not just location |
| Security handoff | Documenso | link private vulnerability reporting clearly |

## RepoForge design decision

The web-application flow is:

```text
product identity / screenshot
        ↓
features and demo
        ↓
local development contract
        ↓
configuration + persistent services
        ↓
deployment contract
        ↓
operations / security / upgrade boundaries
        ↓
authoritative docs
```

## Anti-patterns

Avoid:

- beginning with `npm install` before saying what the product is;
- treating `npm run dev` or Django's development server as production deployment;
- pasting every environment variable into README;
- documenting credentials using realistic secret values;
- hiding migrations, object storage, or background workers from the deployment path;
- saying "Docker ready" without identifying persistent data and upgrade responsibilities;
- listing Redis, S3, queues, APIs, or authentication in Full when the project does not have them;
- treating backup as somebody else's problem for a self-hosted stateful application.
