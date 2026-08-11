# Desktop Application README Contract

`desktop-application` is for complete installable desktop products: Qt applications, Electron/Tauri apps, native utilities, creative tools, scientific workstations, GIS software, editors, and other Windows/macOS/Linux applications.

It is **not** for reusable libraries, browser applications, command-line-only tools, or plugins whose primary job is to be installed into another host application.

## First-screen contract

A desktop README must make the product immediately recognizable before asking the reader to understand the source tree.

The top block is intentionally stricter than other RepoForge families:

1. Logo or application icon when available;
2. project name;
3. one-line product description;
4. **release / platform / build / license badges as appropriate**;
5. short navigation such as Download · Docs · Issues;
6. screenshot or product preview when available.

**The entire identity block must be centered.** Templates must not leave the title centered while badges or navigation fall back to left alignment.

## Questions a desktop README should answer

A first-time visitor should quickly learn:

1. What does the application do?
2. What does it look like?
3. Which operating systems are supported?
4. Where can I download an official build?
5. Which installer/package should I choose?
6. Where does the application keep user data, configuration, and cache?
7. Can I build it from source?
8. Does it support plugins, extensions, updates, portable mode, or telemetry?
9. How are releases packaged and signed?
10. Where are user documentation, support, and issue reporting?

## Profile boundaries

### Minimal

For a focused desktop utility or early but usable application. Keep the product identity, essential badges, one screenshot if available, features, download/install route, platform support, optional source-run command, and license.

### Standard

For most maintained desktop applications. Add installer/package choices, first-run guidance, user data/config locations, compatibility, build-from-source instructions, testing, documentation, and contribution links.

### Full

For mature or operationally complex applications. Add deeper architecture and only the capabilities that really exist: project/file formats, plugins, update channels, portable mode, security/privacy, telemetry, signing/notarization, backup/migration, troubleshooting, release engineering, and upgrade compatibility.

## Capability honesty

Full does not mean Electron + auto-update + plugins + telemetry + cloud sync.

A mature Qt utility with no plugin system and no telemetry is still a valid Full project. Optional sections must disappear when the project does not provide the capability.

## Badge policy

Badges belong in the centered header, not scattered through the README. Prefer badges that help a user or contributor make a decision:

- latest release/version;
- supported platform/build status;
- CI/tests;
- package/distribution availability when maintained by the project;
- license;
- documentation or download status when useful.

Do not add decorative badges that duplicate prose or imply unsupported distribution channels.

## README vs documentation

README should route users to the application and its official downloads. Long user manuals, exhaustive keyboard shortcuts, complete plugin APIs, detailed packaging recipes, code-signing runbooks, and platform-specific troubleshooting belong in `docs/`.
