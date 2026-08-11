# Web Application README References

This file records section-level patterns from mature open-source web applications. RepoForge uses them as references, not as templates to copy wholesale.

## Twenty — product-first identity and delivery modes

Repository: https://github.com/twentyhq/twenty

Useful patterns:

- starts with logo, a clear product category, navigation, and a strong visual hero;
- explains **Why** before diving into implementation details;
- separates hosted cloud usage, app development, self-hosting, and contribution paths;
- keeps the technology stack visible but secondary to product identity.

RepoForge takeaway: a web application README is first a product landing page, then a developer/operations entrance.

## Paperless-ngx — demo, shortest deployment path, and security boundary

Repository: https://github.com/paperless-ngx/paperless-ngx

Useful patterns:

- gives a concrete product description and demo early;
- uses a screenshot to establish what the application looks like;
- makes the easiest deployment path (`docker compose`) obvious;
- pushes alternative installation methods into documentation;
- places an important data/security warning directly in the README.

RepoForge takeaway: high-impact operational warnings and the easiest supported deployment path belong on the project page.

## Documenso — local development, environment, self-hosting, and security

Repository: https://github.com/documenso/documenso

Useful patterns:

- makes product purpose and screenshot visible before developer setup;
- lists development requirements explicitly;
- provides a concrete `.env` workflow and fast local-development command;
- separates local development from Docker and self-hosted deployment;
- links dedicated security and troubleshooting guidance;
- documents access points for local services.

RepoForge takeaway: Standard/Full should distinguish local developer setup, configuration identity, and production deployment instead of blending them into one generic Installation section.

## Outline — hosted product vs self-hosted codebase vs contributor workflow

Repository: https://github.com/outline/outline

Useful patterns:

- tells ordinary users they do not need to run the source code when a hosted product is available;
- sends production hosting to dedicated documentation;
- keeps contributor development, architecture, debugging, tests, and migrations distinct;
- gives a concise logging/observability entry point instead of a full operations manual.

RepoForge takeaway: README paths should depend on audience: product user, self-hoster/operator, and contributor are different journeys.

## Immich — visual identity, demo, capability matrix, backup warning

Repository: https://github.com/immich-app/immich

Useful patterns:

- immediately communicates the application through logo + screenshot;
- exposes demo and documentation prominently;
- uses a feature matrix where platform capability differences matter;
- places a backup warning near the top because persistent user data is central to the product.

RepoForge takeaway: product screenshots and irreversible data-risk warnings deserve higher priority than large implementation diagrams.

## Section champions

| README function | Primary references | RepoForge lesson |
| --- | --- | --- |
| Product hero | Twenty / Immich | show what the application is before how it is built |
| Why / positioning | Twenty / Documenso | explain product value, not only technical stack |
| Demo | Paperless-ngx / Immich | let readers evaluate before installing when possible |
| Local development | Documenso | prerequisites → env → dependencies → app command |
| Hosted vs self-hosted | Twenty / Outline | distinguish delivery modes clearly |
| Easiest deployment | Paperless-ngx | lead with the primary supported production path |
| Configuration | Documenso | expose required config without copying a huge env reference |
| Architecture | Outline | link a dedicated architecture document for deeper detail |
| Tests/migrations | Outline | make developer correctness paths explicit |
| Security warnings | Paperless-ngx / Documenso | surface high-impact deployment/data risks |
| Backup boundary | Immich | persistent-data applications should state backup responsibility |
| Tech stack | Twenty / Documenso | useful, but subordinate to product and run/deploy paths |

## RepoForge design decision

A web application README should follow this general control flow:

```text
product identity
      ↓
screenshot / demo
      ↓
what it does
      ↓
run locally
      ↓
configuration + persistent services
      ↓
deploy / operate
      ↓
architecture + testing + security
      ↓
deeper docs
```

Minimal stops early. Standard covers the normal development/deployment contract. Full expands operationally meaningful surfaces without turning the README into an SRE handbook.

## Anti-patterns

Avoid:

- opening with a framework inventory instead of explaining the product;
- a 200-line `.env` dump in the README;
- saying only `docker compose up` without explaining persistent volumes or required configuration;
- presenting a development server as a production deployment method;
- hiding destructive migration or backup requirements;
- listing every internal microservice when a simple architecture summary would do;
- showing API, queue, object-storage, search, or payment sections for applications that do not have them;
- copying production secrets into examples;
- mixing end-user instructions with contributor setup without clear separation.
