{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(180) }}">
</p>
{% endif %}<h1 align="center">{{ project_name }}</h1>
<p align="center"><strong>{{ tagline }}</strong></p>
{% if badges %}<p align="center">
{% for badge in badges %}  <a href="{{ badge.link }}"><img src="{{ badge.image }}" alt="{{ badge.alt }}"></a>
{% endfor %}</p>
{% endif %}{% if navigation %}<p align="center">
{% for item in navigation %}  <a href="{{ item.link }}">{{ item.label }}</a>{% if not loop.last %} ·{% endif %}
{% endfor %}</p>
{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(900) }}">
</p>

{% endif %}{{ "\n" }}## Why {{ display_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Downloads and Release Channels

| Platform / channel | Package | Support level | Link |
| --- | --- | --- | --- |
{% for item in download_options %}| **{{ item.platform }}** | {{ item.package }} | {{ item.support }} | {{ item.link }} |
{% endfor %}

## Platform Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
{% for item in compatibility %}| **{{ item.target }}** | {{ item.range }} | {{ item.notes }} |
{% endfor %}

{% if architecture %}## Architecture

{{ architecture_intro }}

| Component | Technology | Responsibility |
| --- | --- | --- |
{% for item in architecture %}| **{{ item.component }}** | {{ item.technology }} | {{ item.responsibility }} |
{% endfor %}

{% endif %}{% if data_locations %}## User Data, Configuration, and Cache

| Data | Location / rule | Purpose / backup status |
| --- | --- | --- |
{% for item in data_locations %}| **{{ item.name }}** | {{ item.location }} | {{ item.purpose }} |
{% endfor %}

{% endif %}{% if file_formats %}## Project and File Formats

{% for item in file_formats %}- **{{ item.name }}:** {{ item.description }}{% if item.compatibility %} — {{ item.compatibility }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}{% if extensions_text %}## Plugins and Extensions

{{ extensions_text }}

{% endif %}{% if update_text %}## Updates and Release Compatibility

{{ update_text }}

{% endif %}{% if portable_text %}## Portable Mode

{{ portable_text }}

{% endif %}{% if privacy_text %}## Privacy and Network Behavior

{{ privacy_text }}

{% endif %}{% if telemetry_text %}## Telemetry

{{ telemetry_text }}

{% endif %}{% if security_notes %}## Security

{% for note in security_notes %}- {{ note }}
{% endfor %}

{% endif %}## Build from Source

{{ build_text }}

```bash
{{ build_command }}
```

## Packaging and Release Engineering

{{ packaging_text }}

{% for item in packaging_steps %}
### {{ item.name }}

{{ item.description }}

{% if item.command %}```bash
{{ item.command }}
```

{% endif %}{% endfor %}## Development and Testing

{{ development_text }}

```bash
{{ development_command }}
```

```bash
{{ test_command }}
```

{% if backup_text %}## Backup and Migration

{{ backup_text }}

{% endif %}{% if troubleshooting %}## Troubleshooting and Diagnostics

{% for item in troubleshooting %}- **{{ item.problem }}:** {{ item.guidance }}
{% endfor %}

{% endif %}{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## Contributing

{{ contributing_text }}

## License

{{ license_text }}
