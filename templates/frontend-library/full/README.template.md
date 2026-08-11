{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(280) }}">
</p>

{% endif %}{% if demo_image %}<p align="center">
  <img src="{{ demo_image }}" alt="{{ project_name }} demo" width="{{ demo_width | default(900) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Why {{ display_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

{% if demo_url %}## Live Demo

{{ demo_url }}

{% endif %}## Packages and Installation

| Package | Use when | Install |
| --- | --- | --- |
{% for item in packages %}| `{{ item.name }}` | {{ item.purpose }} | `{{ item.install }}` |
{% endfor %}

{% if setup_text %}{{ setup_text }}

{% endif %}## Quick Start

```{{ quickstart_language }}
{{ quickstart_code }}
```

## API Overview

| API family | Purpose | Stability |
| --- | --- | --- |
{% for item in api_items %}| `{{ item.name }}` | {{ item.purpose }} | {{ item.stability }} |
{% endfor %}

{% if events %}## Events and Lifecycle

| Event / hook | When it fires | Typical use |
| --- | --- | --- |
{% for item in events %}| `{{ item.name }}` | {{ item.when }} | {{ item.use }} |
{% endfor %}

{% endif %}{% if styling_text %}## Styling, Themes, and CSS Contract

{{ styling_text }}

{% endif %}{% if adapters %}## Framework Adapters

| Adapter | Package / status | Notes |
| --- | --- | --- |
{% for item in adapters %}| **{{ item.name }}** | {{ item.package }} | {{ item.notes }} |
{% endfor %}

{% endif %}{% if typescript_text %}## TypeScript Support

{{ typescript_text }}

{% endif %}{% if bundle_text %}## Bundle and Tree-Shaking

{{ bundle_text }}

{% endif %}{% if ssr_text %}## SSR and Non-Browser Environments

{{ ssr_text }}

{% endif %}## Browser Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
{% for item in compatibility %}| **{{ item.target }}** | {{ item.range }} | {{ item.notes }} |
{% endfor %}

{% if accessibility_text %}## Accessibility

{{ accessibility_text }}

{% endif %}## Examples

{% for item in examples %}- **{{ item.name }}:** {{ item.link }} — {{ item.description }}
{% endfor %}

## Development and Testing

{{ development_text }}

```bash
{{ development_command }}
```

```bash
{{ test_command }}
```

## Release and Versioning Policy

{{ versioning_text }}

{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## Contributing

{{ contributing_text }}

## License

{{ license_text }}
