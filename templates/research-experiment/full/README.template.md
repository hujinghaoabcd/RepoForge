{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(460) }}">
</p>

{% endif %}{% if figure_path %}<p align="center">
  <img src="{{ figure_path }}" alt="{{ project_name }} overview" width="{{ figure_width | default(860) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}{% if paper_link %}Paper: {{ paper_link }}

{% endif %}## Highlights

{% for highlight in highlights %}- {{ highlight }}
{% endfor %}

## Model Overview

{{ model_text }}

## Datasets and Data Identity

| Dataset | Role | Expected path | Identity / preprocessing |
| --- | --- | --- | --- |
{% for dataset in datasets %}| **{{ dataset.name }}** | {{ dataset.role }} | `{{ dataset.path }}` | {{ dataset.identity }} |
{% endfor %}

## Environment and Hardware

{{ environment_text }}

```bash
{{ environment_command }}
```

{{ hardware_text }}

## Fastest Start

```bash
{{ fastest_start }}
```

{{ fastest_start_result }}

## Available Models and Baselines

| Model | Role | Config | Tuning policy |
| --- | --- | --- | --- |
{% for model in models %}| **{{ model.name }}** | {{ model.role }} | `{{ model.config }}` | {{ model.tuning }} |
{% endfor %}

## Experiment Protocol

- **Input / horizon:** {{ protocol.window }}
- **Split:** {{ protocol.split }}
- **Preprocessing:** {{ protocol.preprocessing }}
- **Seeds:** {{ protocol.seeds }}
- **Metrics:** {{ protocol.metrics }}
- **Model selection:** {{ protocol.model_selection }}
- **Baseline tuning:** {{ protocol.baseline_tuning }}
- **Gradient / training controls:** {{ protocol.training_controls }}

## Reproducing the Main Results

{% for command in main_commands %}### {{ command.name }}

{{ command.description }}

```bash
{{ command.command }}
```

{% endfor %}## Ablation and Sensitivity Studies

{% for command in analysis_commands %}### {{ command.name }}

{{ command.description }}

```bash
{{ command.command }}
```

{% endfor %}## Statistical Testing

{{ statistical_testing.text }}
{% if statistical_testing.command %}

```bash
{{ statistical_testing.command }}
```
{% endif %}

## Result and Artifact Identity

| Artifact | Stable location / rule | Purpose |
| --- | --- | --- |
{% for artifact in artifacts %}| **{{ artifact.name }}** | `{{ artifact.path }}` | {{ artifact.purpose }} |
{% endfor %}

## Published Checkpoints and Predictions

{% for item in published_artifacts %}- **{{ item.name }}:** {{ item.location }} — {{ item.description }}
{% endfor %}

## Expected Results

{{ results_intro }}

| Dataset | Model | Seeds | Metric | Summary |
| --- | --- | --- | --- | --- |
{% for result in results %}| {{ result.dataset }} | {{ result.model }} | {{ result.seeds }} | {{ result.metric }} | {{ result.summary }} |
{% endfor %}

## Documentation Map

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}## Reproducibility Boundaries

{% for boundary in boundaries %}- {{ boundary }}
{% endfor %}

## Citation

{{ citation.intro }}
{% if citation.paper %}

Paper: {{ citation.paper }}

{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## License

{{ license_text }}
