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
{% if paper_link %}Paper: {{ paper_link }}

{% endif %}## Overview

{{ overview_text }}

## Model Overview

{{ model_text }}

## Datasets

| Dataset | Role | Expected path | Notes |
| --- | --- | --- | --- |
{% for dataset in datasets %}| **{{ dataset.name }}** | {{ dataset.role }} | `{{ dataset.path }}` | {{ dataset.notes }} |
{% endfor %}

## Environment

{{ environment_text }}

```bash
{{ environment_command }}
```
{% if hardware_note %}

Hardware note: {{ hardware_note }}
{% endif %}

## Quick Reproduction

{% for command in commands %}### {{ command.name }}

{{ command.description }}

```bash
{{ command.command }}
```

{% endfor %}## Experiment Protocol

- **Split:** {{ protocol.split }}
- **Preprocessing:** {{ protocol.preprocessing }}
- **Seeds:** {{ protocol.seeds }}
- **Metrics:** {{ protocol.metrics }}
- **Model selection:** {{ protocol.model_selection }}

## Main Results

{{ results_intro }}

| Setting | Metric | Value |
| --- | --- | ---: |
{% for result in results %}| {{ result.setting }} | {{ result.metric }} | {{ result.value }} |
{% endfor %}

## Outputs

{{ output_text }}

## Repository Structure

```text
{{ structure_text }}
```

## Citation

{{ citation.intro }}
{% if citation.paper %}

Paper: {{ citation.paper }}
{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## License

{{ license_text }}
