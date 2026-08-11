# Desktop Application README references

RepoForge uses mature desktop repositories as design references rather than copying one project literally.

## QGIS

Repository: `qgis/QGIS`

Useful patterns:

- product identity appears before implementation details;
- platform and build/test badges are visible near the top;
- installation points users to precompiled binaries rather than forcing source builds;
- screenshots and visual examples matter for a GUI product;
- rich functionality is summarized in README while manuals and APIs route to dedicated documentation;
- release channels and supported platforms are explicit.

RepoForge takeaway: desktop README flow should prioritize **product → visual proof → download → platform support** before developer internals.

## KeePassXC

Repository: `keepassxreboot/keepassxc`

Useful patterns:

- release, build, security-practice, and coverage badges are visible immediately;
- the README names Windows, macOS, and Linux directly;
- Quick Start sends normal users to pre-built downloads and user docs;
- feature scope is concrete;
- build instructions are separated from normal installation.

RepoForge takeaway: distinguish **using the product** from **building the product** and keep meaningful release/build badges prominent.

## Joplin

Repository: `laurent22/joplin`

Useful patterns:

- desktop product behavior is explained in user language;
- a large screenshot establishes what the application is;
- desktop/mobile availability is explicit;
- plugin/theme extensibility is described as a product feature;
- deeper developer instructions are routed elsewhere.

RepoForge takeaway: screenshots and extensibility deserve first-class treatment when they are actually important to the product.

## Visual Studio Code / Code - OSS

Repository: `microsoft/vscode`

Useful patterns:

- repository/source identity is distinguished from the distributed desktop product;
- a centered screenshot provides visual orientation;
- download links target user-facing builds;
- contribution/build documentation is separate from product onboarding;
- extension ecosystem and development workflow are documented without pretending the README is the whole manual.

RepoForge takeaway: a source repository may need to state clearly whether it builds the official product, a community distribution, or only the upstream source base.

## Section champions

- **Product + download boundary:** KeePassXC
- **Visual product proof:** Joplin / VS Code
- **Large cross-platform technical application:** QGIS
- **Source-product distinction:** VS Code
- **Release/build badges:** KeePassXC / QGIS

## Anti-patterns

Avoid:

- opening with compiler prerequisites before explaining the application;
- hiding official downloads below build-from-source instructions;
- listing Windows/macOS/Linux without stating which builds are actually supported;
- inventing package-manager channels;
- claiming auto-update, plugin APIs, portable mode, telemetry, signing, or cloud sync because the profile is Full;
- leaving the title centered while badges and navigation remain left-aligned;
- filling the README with exhaustive packaging and code-signing runbooks.
