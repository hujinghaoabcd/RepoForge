{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
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
{% endif %}{{ "\n" }}## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

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
