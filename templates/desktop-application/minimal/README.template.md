<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{% for badge in badges %}<a href="{{ badge.link }}"><img src="{{ badge.image }}" alt="{{ badge.alt }}"></a>{% if not loop.last %} {% endif %}{% endfor %}
{% endif %}{{ "\n" }}{% if navigation %}{% for item in navigation %}<a href="{{ item.link }}">{{ item.label }}</a>{% if not loop.last %} · {% endif %}{% endfor %}
{% endif %}</div>

---

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Preview

{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(800) }}">
</p>

{% endif %}

## Download and Install

{{ download_text }}

{% if download_options %}| Platform | Package | Link |
| --- | --- | --- |
{% for item in download_options %}| {{ item.platform }} | {{ item.package }} | {{ item.link }} |
{% endfor %}

{% endif %}## Supported Platforms

{% for item in platforms %}- **{{ item.name }}:** {{ item.support }}
{% endfor %}

{% if run_from_source %}## Run from Source

```bash
{{ run_from_source }}
```

{% endif %}## License

{{ license_text }}
