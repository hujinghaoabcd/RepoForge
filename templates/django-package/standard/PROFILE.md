# Standard Django Package Profile

Use this profile for the majority of maintained reusable Django packages.

## Required public questions

A Standard README should answer:

1. Why does this package exist?
2. What are its key capabilities?
3. How is it installed?
4. Which Django integration steps are required?
5. Which settings materially affect common use?
6. What is the first useful code path?
7. What representative secondary usage should users see?
8. Which Django/Python combinations are supported?
9. Where are the full docs and contribution instructions?

## Required sections

```text
Why?
Features
Installation
Configuration
Quick Start
Usage Examples
Compatibility
Documentation
Contributing
License
```

`Configuration` is intentionally a list of named integration steps rather than a hard-coded assumption that all Django packages use only `INSTALLED_APPS`.

## Keep out

Move these to Full or docs when they become substantial:

- models/migrations contract;
- admin integration contract;
- public API stability table;
- frontend/static integration;
- security boundaries;
- compatibility matrices beyond Django/Python;
- upgrade/deprecation procedure.

## Target

Prefer roughly **90–150 rendered lines** for a normal maintained package.
