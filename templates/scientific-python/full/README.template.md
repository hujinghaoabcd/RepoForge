{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(460) }}">
</p>
{% endif %}

# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}
{% if language_switch %}{{ language_switch }}
{% endif %}
{% if navigation %}{{ navigation }}
{% endif %}

## What {{ project_name }} Is

{{ overview_text }}

## Why Use It?

{{ why_text }}

## Scientific Scope

{{ scope_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

### Stable release

```bash
{{ install_command }}
```

{% if optional_install_commands %}### Optional features

{% for item in optional_install_commands %}```bash
{{ item.command }}  # {{ item.description }}
```
{% endfor %}
{% endif %}

{% if development_install %}### Development install

```bash
{{ development_install }}
```
{% endif %}

## Five-Minute Example

{{ quickstart_intro }}

```python
{{ quickstart_code }}
```

{% if methods %}## Method Catalogue

| Method / area | Purpose | New-data operation | Notes |
| --- | --- | --- | --- |
{% for method in methods %}| `{{ method.name }}` | {{ method.purpose }} | {{ method.operation }} | {{ method.notes }} |
{% endfor %}

{% endif %}
{% if method_selection %}## Choosing a Method

{{ method_selection }}

{% endif %}
{% if data_contracts %}## Data Contracts and Conventions

{% for item in data_contracts %}- {{ item }}
{% endfor %}

{% endif %}
{% if representative_example %}## Representative Workflow

{{ representative_example.intro }}

```python
{{ representative_example.code }}
```

{% endif %}
{% if validation %}## Validation and Reproducibility

{{ validation.summary }}

{% for item in validation.items %}- {{ item }}
{% endfor %}

{% endif %}
{% if examples %}## Examples

{% for example in examples %}- **{{ example.name }}:** {{ example.link }}{% if example.description %} — {{ example.description }}{% endif %}
{% endfor %}

{% endif %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

{% if project_status %}## Project Status and API Stability

{{ project_status }}

{% endif %}
{% if limitations %}## Limitations

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

{% endif %}
{% if citation %}## Citation

{{ citation.intro }}

{% if citation.bibtex %}```bibtex
{{ citation.bibtex }}
```
{% endif %}
{% if citation.cff %}Citation metadata is available in [`CITATION.cff`]({{ citation.cff }}).
{% endif %}
{% if citation.doi %}DOI: {{ citation.doi }}
{% endif %}

{% endif %}## Support and Contributing

{{ support_text }}
{% if contributing_link %}
Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
