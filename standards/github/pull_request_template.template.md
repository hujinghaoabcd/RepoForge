## Summary

Describe the change in a few sentences.

## Why this change?

Explain the problem, user need, maintenance need, or project goal this pull request addresses.

## What changed?

- 
- 

## Validation

Describe how you tested or reviewed the change. Include commands, datasets, environments, screenshots, or manual checks only when they are relevant.

{% if require_tests %}- [ ] Relevant automated tests were added or updated.
- [ ] The applicable test suite passes locally or in CI.
{% endif %}{% if require_docs %}- [ ] User-facing documentation was updated when behavior or interfaces changed.
{% endif %}{% if require_changelog %}- [ ] The changelog was updated when the change is user-visible.
{% endif %}
## Compatibility and risk

- [ ] I considered backward compatibility, migration, or upgrade impact where relevant.
- [ ] I did not include secrets, private data, credentials, or sensitive logs.
- [ ] Security-sensitive changes are described clearly enough for review without publicly disclosing an unpatched vulnerability.

## Repository standards

- [ ] This pull request is focused on one coherent change.
- [ ] Generated files, snapshots, fixtures, or examples were updated when required.
{% if contributing_link_enabled %}- [ ] I followed `CONTRIBUTING.md`.
{% endif %}{% if code_of_conduct_link_enabled %}- [ ] I followed the project's `CODE_OF_CONDUCT.md`.
{% endif %}
## Additional notes

Add reviewer guidance, follow-up work, known limitations, or intentionally deferred items here.
