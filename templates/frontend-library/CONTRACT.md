# Frontend Library Template Contract

This family is for reusable browser-facing libraries, plugins, components, hooks, renderers, and framework adapters distributed for other applications to consume.

Use `frontend-library` when the primary user installs/imports the package into another frontend project. Use `web-application` when the repository itself is the deployable product.

## Primary questions

A frontend-library README should answer:

1. What UI/browser problem does the library solve?
2. Which package should a consumer install?
3. What is the shortest copyable example that produces a visible or useful result?
4. Is CSS, an asset, a peer dependency, or another setup step required?
5. Which public APIs, events, lifecycle hooks, or framework adapters matter?
6. Which browser, TypeScript, SSR, accessibility, and bundler boundaries apply?
7. Is the package tree-shakeable, split into subpackages, or available through a CDN?
8. What compatibility/versioning rules should consumers know before upgrading?

## Independent profiles

`minimal`, `standard`, and `full` are separate templates, each with its own profile rules, Jinja template, YAML config, rendered example, and visible preview.

## Shared rules

- optimize the first screen for installation and a working usage example;
- show any required CSS/import side effect next to the first example;
- distinguish core packages from framework adapters and optional add-ons;
- document browser/platform requirements instead of saying only "modern browsers" when compatibility matters;
- do not claim SSR, accessibility, tree-shaking, zero dependencies, or framework compatibility unless the project actually guarantees it;
- route exhaustive API reference and large example galleries to documentation;
- keep application deployment and server operations out of this family.

## Profile selection

### Minimal

Small single-purpose packages with one install target and a tiny public surface.

### Standard

Default for maintained libraries that have documentation, several options/events, styling or framework integration, and an explicit compatibility contract.

### Full

Use when consumers must understand multiple packages/adapters, public API families, lifecycle/events, CSS/theming, SSR, TypeScript, tree-shaking/bundle behavior, accessibility, browser matrices, migration/versioning rules, or several example families.

## Excluded content

Even Full should move these out of README when substantial:

- generated API reference;
- every prop/event signature;
- complete CSS token reference;
- exhaustive framework recipes;
- benchmark history;
- release automation internals;
- complete migration manuals;
- application deployment instructions.
