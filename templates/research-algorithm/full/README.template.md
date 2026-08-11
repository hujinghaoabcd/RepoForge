{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(420) }}">
</p>

{% endif %}{% if method_figure %}<p align="center">
  <img src="{{ method_figure }}" alt="{{ project_name }} method overview" width="{{ figure_width | default(820) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Scientific Problem

{{ problem_text }}

## Why Existing Approaches Are Insufficient

{{ gap_text }}

## Proposed Method

### {{ objective.title }}

{{ objective.text }}
{% if objective.equation %}

{{ objective.equation }}
{% endif %}

### Core Formulation

{{ formulation.text }}
{% if formulation.equation %}

{{ formulation.equation }}
{% endif %}

### Algorithm Outline

{% for step in algorithm_steps %}{{ loop.index }}. **{{ step.name }}** — {{ step.description }}
{% endfor %}

## Key Contributions

{% for contribution in contributions %}- {{ contribution }}
{% endfor %}

## Installation

### Stable install

```bash
{{ install_command }}
```
{% if development_install %}

### Development install

```bash
{{ development_install }}
```
{% endif %}

## Five-Minute Example

{% if quickstart_intro %}{{ quickstart_intro }}

{% endif %}```python
{{ quickstart_code }}
```

## Inputs, Outputs, and Interpretation

| Contract | Meaning | Boundary |
| --- | --- | --- |
{% for row in interpretation_contracts %}| **{{ row.name }}** | {{ row.meaning }} | {{ row.boundary }} |
{% endfor %}

## Validation

{{ validation.summary }}
{% for section in validation.sections %}

### {{ section.name }}

{{ section.text }}
{% endfor %}{% if validation.link %}

See {{ validation.link }} for complete protocols, tolerances, and archived evidence.
{% endif %}

## Computational Characteristics

{{ computational_text }}

## Reproducibility

{% for item in reproducibility %}- {{ item }}
{% endfor %}

## Limitations

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

## Citation

{{ citation.intro }}
{% if citation.paper %}

Method paper: {{ citation.paper }}
{% endif %}{% if citation.bibtex %}

```bibtex
{{ citation.bibtex }}
```
{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## Support and Contributing

{{ support_text }}
{% if contributing_link %}

Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
