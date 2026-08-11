# Changelog

All notable changes to {{ project_name }} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/).
{{ versioning_statement }}

## [Unreleased]

{% set categories = ['Added', 'Changed', 'Deprecated', 'Removed', 'Fixed', 'Security'] %}{% for category in categories %}{% if unreleased[category] %}### {{ category }}

{% for entry in unreleased[category] %}- {{ entry }}
{% endfor %}
{% endif %}{% endfor %}{% if not (unreleased['Added'] or unreleased['Changed'] or unreleased['Deprecated'] or unreleased['Removed'] or unreleased['Fixed'] or unreleased['Security']) %}<!-- Add only non-empty change sections: Added, Changed, Deprecated, Removed, Fixed, or Security. -->
{% endif %}{% if latest_version %}
[Unreleased]: {{ repository_url }}/compare/v{{ latest_version }}...HEAD
{% endif %}