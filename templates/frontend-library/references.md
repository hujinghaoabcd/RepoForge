# Frontend Library README References

RepoForge extracts section-level patterns from mature frontend libraries rather than copying one README wholesale.

## MapLibre GL JS

Repository: https://github.com/maplibre/maplibre-gl-js

Useful patterns:

- concise product/library positioning;
- CSS requirement is shown directly with the first runnable browser example;
- examples and API documentation are easy to discover;
- framework bindings are linked without pretending they are all maintained in the core repository;
- semantic-versioning policy is visible.

RepoForge takeaway: setup side effects such as required CSS belong next to Quick Start, not hidden in a later configuration section.

## Floating UI

Repository: https://github.com/floating-ui/floating-ui

Useful patterns:

- strong `Why` section for a technically subtle UI problem;
- distinguishes vanilla DOM, React, React DOM, React Native, Vue, and low-level core packages;
- lets consumers install only the layer they need;
- documents visual/interaction test grounds for maintainers.

RepoForge takeaway: package variants and framework adapters are first-class consumer contracts in broader libraries.

## VueUse

Repository: https://github.com/vueuse/vueuse

Useful patterns:

- advertises tree-shaking, TypeScript, SSR, CDN use, add-ons, and bundle-size information as concrete capabilities;
- starts with a short copyable usage example;
- states framework-version compatibility near installation;
- routes the huge function catalogue to interactive docs rather than putting it all in README.

RepoForge takeaway: Full should summarize distribution/runtime properties while the complete function/API catalogue belongs in docs.

## Leaflet

Repository: https://github.com/Leaflet/Leaflet

Useful patterns:

- memorable one-line positioning;
- clearly communicates size, platform reach, plugin ecosystem, API docs, tutorials, and contribution path;
- avoids turning the root README into the full mapping manual.

RepoForge takeaway: mature libraries can remain concise when the README strongly routes readers to docs, examples, and ecosystem resources.

## Section champions

| README function | Reference | RepoForge lesson |
| --- | --- | --- |
| One-line identity | Leaflet | state exactly what developers can build |
| First working example | MapLibre / VueUse | show real usage before deep API material |
| Required CSS/assets | MapLibre | keep side effects adjacent to install/usage |
| Why / problem framing | Floating UI | explain complex browser/UI problems briefly |
| Package/adapters matrix | Floating UI | distinguish packages instead of one ambiguous install command |
| Tree-shaking / SSR / types | VueUse | publish these as explicit guarantees only when true |
| Examples + docs routing | MapLibre / Leaflet | README is the entrance, not the full manual |
| Version compatibility | VueUse / MapLibre | make upgrade expectations visible |

## Anti-patterns

Avoid:

- an install command with no import/usage example;
- a demo GIF with no copyable code;
- forgetting required CSS or peer dependencies;
- claiming framework compatibility when only community adapters exist;
- putting every component/prop/event in the root README;
- describing bundle size without a reproducible measurement context;
- calling code accessible merely because it renders semantic HTML;
- adding application deployment sections to a package README.
