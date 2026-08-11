# Reusable Partials

`partials/` contains reusable README/documentation sections that can be shared across project types.

Planned partial families include:

```text
header
badges
navigation
installation
quickstart
features
screenshots
architecture
configuration
api
testing
validation
reproducibility
deployment
security
citation
contributing
support
roadmap
license
```

Partials are not meant to force identical wording into unrelated repositories. They define reusable structure, prompts, metadata inputs, and rendering conventions.

A partial may be:

- required by a project type;
- enabled only for a certain profile;
- activated by detected repository capabilities;
- explicitly requested by the user.

Examples:

- `citation` is important for scientific software but usually unnecessary for a small frontend plugin;
- `screenshots` is central to web and desktop applications but optional for a numerical library;
- `reproducibility` is central to experiment repositories;
- `deployment` matters for applications but normally not for reusable Python libraries.

Partials should remain small enough that project-specific content can replace or extend them naturally.
