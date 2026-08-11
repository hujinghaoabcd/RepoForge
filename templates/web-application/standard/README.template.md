<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
{% if navigation %}{{ navigation }}
{% endif %}
</div>

---
## Overview

{{ overview_text }}

{% if demo_link %}**Demo:** {{ demo_link }}

{% endif %}## Screenshots / Demo

{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(800) }}">
</p>

{% endif %}

{{ screenshot_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
{% for item in stack %}| **{{ item.layer }}** | {{ item.technology }} | {{ item.role }} |
{% endfor %}

## Local Development

### Requirements

{% for item in requirements %}- {{ item }}
{% endfor %}

### Start

```bash
{{ local_command }}
```

{{ local_result }}

## Environment Variables

{{ environment_intro }}

| Variable | Required | Purpose |
| --- | --- | --- |
{% for item in environment %}| `{{ item.name }}` | {{ item.required }} | {{ item.purpose }} |
{% endfor %}

## Database

{{ database_text }}

```bash
{{ migration_command }}
```

{% if seed_command %}```bash
{{ seed_command }}
```

{% endif %}## Deployment

{{ deployment_text }}

```bash
{{ deployment_command }}
```

{% if deployment_note %}{{ deployment_note }}

{% endif %}## Project Structure

```text
{{ project_tree }}
```

## Testing

```bash
{{ test_command }}
```

{{ testing_text }}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}## License

{{ license_text }}
