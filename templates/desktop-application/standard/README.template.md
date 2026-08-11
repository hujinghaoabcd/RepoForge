{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(180) }}">
</p>
{% endif %}<h1 align="center">{{ project_name }}</h1>
<p align="center"><strong>{{ tagline }}</strong></p>
{% if badges %}<p align="center">
{% for badge in badges %}  <a href="{{ badge.link }}"><img src="{{ badge.image }}" alt="{{ badge.alt }}"></a>{% if not loop.last %} {% endif %}
{% endfor %}</p>
{% endif %}{% if navigation %}<p align="center">
{% for item in navigation %}  <a href="{{ item.link }}">{{ item.label }}</a>{% if not loop.last %} · {% endif %}
{% endfor %}</p>
{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(900) }}">
</p>
{% endif %}
## Overview

{{ overview_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Download and Install

| Platform | Recommended package | Notes | Link |
| --- | --- | --- | --- |
{% for item in download_options %}| **{{ item.platform }}** | {{ item.package }} | {{ item.notes }} | {{ item.link }} |
{% endfor %}

{% if first_launch %}## First Launch

{{ first_launch }}

{% endif %}## Platform Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
{% for item in compatibility %}| **{{ item.target }}** | {{ item.range }} | {{ item.notes }} |
{% endfor %}

{% if data_locations %}## User Data and Configuration

| Data | Location / rule | Purpose |
| --- | --- | --- |
{% for item in data_locations %}| **{{ item.name }}** | {{ item.location }} | {{ item.purpose }} |
{% endfor %}

{% endif %}## Build from Source

{{ build_text }}

```bash
{{ build_command }}
```

## Development and Testing

```bash
{{ development_command }}
```

```bash
{{ test_command }}
```

{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## Contributing

{{ contributing_text }}

## License

{{ license_text }}
