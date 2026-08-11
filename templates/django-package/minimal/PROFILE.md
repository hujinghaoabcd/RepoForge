# Minimal Django Package Profile

Use this profile for a small, focused reusable Django component whose adoption can be explained without a configuration catalogue.

## Required public questions

A Minimal README should answer:

1. What does the package add to a Django project?
2. How do I install it?
3. Which short setup steps are required?
4. What is the smallest representative usage?
5. What compatibility promise should I check?
6. What license applies?

## Required sections

```text
Project identity
Installation
Setup
Quick Start
Compatibility
License
```

`Setup` may contain one or several small named steps such as:

- `INSTALLED_APPS`;
- middleware;
- a migration command;
- one URL include;
- one backend setting.

Do not add broad feature catalogues, settings tables, public API inventories, upgrade policy, or security sections unless the project has grown beyond Minimal.

## Target

Prefer roughly **40–80 rendered lines** for normal examples. The point is the shortest complete adoption path.
