{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(280) }}">
</p>

{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(900) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Overview

{{ overview_text }}

{% if demo_url %}Demo: {{ demo_url }}

{% endif %}## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Tech Stack

| Layer | Technology | Role |
| --- | --- | --- |
{% for item in tech_stack %}| **{{ item.layer }}** | {{ item.technology }} | {{ item.role }} |
{% endfor %}

## Local Development

### Requirements

{% for item in requirements %}- {{ item }}
{% endfor %}

### Start the application

```bash
{{ local_command }}
```

{% if local_urls %}### Local access

{% for item in local_urls %}- **{{ item.name }}:** {{ item.url }}
{% endfor %}

{% endif %}## Environment Variables

| Variable | Required | Purpose | Example |
| --- | --- | --- | --- |
{% for item in environment %}| `{{ item.name }}` | {{ item.required }} | {{ item.purpose }} | `{{ item.example }}` |
{% endfor %}

{% if database_text %}## Database and Migrations

{{ database_text }}

{% if migration_command %}```bash
{{ migration_command }}
```

{% endif %}{% endif %}## Deployment

{{ deployment_text }}

```bash
{{ deployment_command }}
```

{% if project_structure %}## Project Structure

```text
{{ project_structure }}
```

{% endif %}## Testing

{{ testing_text }}

```bash
{{ test_command }}
```

{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## License

{{ license_text }}
