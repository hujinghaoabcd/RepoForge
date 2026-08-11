{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(280) }}">
</p>

{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(900) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{{ intro_text }}

## Features

{% for feature in features %}- {{ feature }}
{% endfor %}

## Run Locally

{{ run_intro }}

```bash
{{ run_command }}
```

{% if local_url %}Open: {{ local_url }}

{% endif %}## Configuration

{% for item in configuration %}- **`{{ item.name }}`** — {{ item.description }}{% if item.example %} Example: `{{ item.example }}`.{% endif %}
{% endfor %}

## Deploy

{{ deploy_text }}

{% if deploy_command %}```bash
{{ deploy_command }}
```

{% endif %}## License

{{ license_text }}
