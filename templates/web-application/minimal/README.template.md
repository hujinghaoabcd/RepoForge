<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
</div>

---
## Preview

{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(800) }}">
</p>

{% endif %}

## Features

{% for feature in features %}- {{ feature }}
{% endfor %}

## Run Locally

{{ local_intro }}

```bash
{{ local_command }}
```

{{ local_result }}

## Configuration

| Variable | Required | Purpose |
| --- | --- | --- |
{% for item in environment %}| `{{ item.name }}` | {{ item.required }} | {{ item.purpose }} |
{% endfor %}

## Deploy

{{ deploy_text }}

```bash
{{ deploy_command }}
```

{% if deploy_note %}{{ deploy_note }}

{% endif %}## License

{{ license_text }}
