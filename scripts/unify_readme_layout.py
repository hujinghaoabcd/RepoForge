from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from repoforge.renderer import (
    SUPPORTED_PROFILES,
    SUPPORTED_TYPES,
    load_config,
    render_readme,
)

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def generic_header(head: str) -> str:
    has_language = "language_switch" in head
    has_navigation = "navigation" in head

    parts = [
        '<div align="center">',
        "",
        '{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">',
        '{% endif %}{{ "\\n" }}# {{ project_name }}',
        "",
        "**{{ tagline }}**",
        "",
        '{% if badges %}{{ badges }}',
        '{% endif %}{{ "\\n" }}',
    ]
    if has_language:
        parts.extend(
            [
                '{% if language_switch %}{{ language_switch }}',
                '{% endif %}{{ "\\n" }}',
            ]
        )
    if has_navigation:
        parts.extend(
            [
                '{% if navigation %}{{ navigation }}',
                "{% endif %}",
            ]
        )
    parts.extend(["</div>", "", "---", ""])
    return "\n".join(parts)


def desktop_header() -> str:
    return """<div align=\"center\">\n\n{% if logo_path %}<img src=\"{{ logo_path }}\" alt=\"{{ project_name }}\" width=\"{{ logo_width | default(160) }}\">\n{% endif %}{{ \"\\n\" }}# {{ project_name }}\n\n**{{ tagline }}**\n\n{% if badges %}{% for badge in badges %}<a href=\"{{ badge.link }}\"><img src=\"{{ badge.image }}\" alt=\"{{ badge.alt }}\"></a>{% if not loop.last %} {% endif %}{% endfor %}\n{% endif %}{{ \"\\n\" }}{% if navigation %}{% for item in navigation %}<a href=\"{{ item.link }}\">{{ item.label }}</a>{% if not loop.last %} · {% endif %}{% endfor %}\n{% endif %}</div>\n\n---\n\n"""


def media_block(variable: str, width_variable: str, default_width: int, alt: str) -> str:
    return (
        f'{{% if {variable} %}}<p align="center">\n'
        f'  <img src="{{{{ {variable} }}}}" alt="{{{{ project_name }}}} {alt}" '
        f'width="{{{{ {width_variable} | default({default_width}) }}}}">\n'
        f'</p>\n\n{{% endif %}}'
    )


def insert_before_any(body: str, headings: list[str], block: str) -> str:
    if block.strip() in body:
        return body
    for heading in headings:
        idx = body.find(heading)
        if idx >= 0:
            return body[:idx] + block.rstrip() + "\n\n" + body[idx:]

    matches = list(re.finditer(r"(?m)^## ", body))
    if len(matches) >= 2:
        idx = matches[1].start()
        return body[:idx] + block.rstrip() + "\n\n" + body[idx:]
    return body.rstrip() + "\n\n" + block.rstrip() + "\n"


def insert_after_heading(body: str, heading: str, block: str) -> str:
    if block.strip() in body:
        return body
    marker = heading + "\n\n"
    if marker in body:
        return body.replace(marker, marker + block.rstrip() + "\n\n", 1)
    return insert_before_any(body, ["## Features", "## Installation"], "## Preview\n\n" + block)


def reposition_media(project_type: str, head: str, body: str) -> str:
    if project_type == "research-algorithm" and "method_figure" in head:
        block = media_block("method_figure", "figure_width", 760, "method overview")
        return insert_before_any(
            body,
            ["## Key Contributions", "## Installation", "## Quick Start"],
            block,
        )

    if project_type == "research-experiment" and "figure_path" in head:
        block = media_block("figure_path", "figure_width", 800, "experiment overview")
        return insert_before_any(
            body,
            [
                "## Datasets and Data Identity",
                "## Datasets",
                "## Environment and Hardware",
                "## Environment",
                "## Quick Reproduction",
            ],
            block,
        )

    if project_type == "django-package" and "screenshot_path" in head:
        block = "## Preview\n\n" + media_block(
            "screenshot_path", "screenshot_width", 800, "screenshot"
        )
        return insert_before_any(body, ["## Installation"], block)

    if project_type == "web-application" and "screenshot_path" in head:
        block = media_block("screenshot_path", "screenshot_width", 800, "screenshot")
        if "## Screenshots / Demo" in body:
            return insert_after_heading(body, "## Screenshots / Demo", block)
        return insert_before_any(body, ["## Features"], "## Preview\n\n" + block)

    if project_type == "frontend-library" and "demo_image" in head:
        block = "## Preview\n\n" + media_block(
            "demo_image", "demo_width", 800, "demo"
        )
        return insert_before_any(
            body,
            ["## Packages and Installation", "## Installation"],
            block,
        )

    if project_type == "desktop-application" and "screenshot_path" in head:
        block = "## Preview\n\n" + media_block(
            "screenshot_path", "screenshot_width", 800, "screenshot"
        )
        return insert_before_any(
            body,
            [
                "## Downloads and Release Channels",
                "## Downloads",
                "## Installation",
                "## Platform Compatibility",
            ],
            block,
        )

    return body


def unify_template(path: Path, project_type: str) -> bool:
    text = path.read_text(encoding="utf-8")
    body_at = text.find("## ")
    if body_at < 0:
        raise RuntimeError(f"Could not find first body heading in {path}")

    head = text[:body_at]
    body = text[body_at:]
    body = reposition_media(project_type, head, body)

    header = desktop_header() if project_type == "desktop-application" else generic_header(head)
    if project_type == "research-experiment" and "paper_link" in head:
        header += "{% if paper_link %}Paper: {{ paper_link }}\n\n{% endif %}"

    updated = header + body.lstrip()
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def replace_readme_section(path: Path, start: str, end: str, replacement: str) -> bool:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(start) + r".*?(?=" + re.escape(end) + r")", re.DOTALL)
    updated, count = pattern.subn(replacement.rstrip() + "\n\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"Could not replace {start!r} section in {path}")
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def insert_usability_section(path: Path, marker: str, section: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if section.splitlines()[0] in text:
        return False
    if marker not in text:
        raise RuntimeError(f"Could not locate {marker!r} in {path}")
    updated = text.replace(marker, section.rstrip() + "\n\n" + marker, 1)
    path.write_text(updated, encoding="utf-8")
    return True


def regenerate_examples() -> int:
    written = 0
    for project_type in sorted(SUPPORTED_TYPES):
        for profile in ("minimal", "standard", "full"):
            if profile not in SUPPORTED_PROFILES:
                continue
            profile_dir = TEMPLATES / project_type / profile
            config_path = profile_dir / "config.example.yml"
            if not config_path.is_file():
                continue
            rendered = render_readme(
                project_type,
                profile,
                load_config(config_path),
                template_root=TEMPLATES,
            )
            example = profile_dir / "README.example.md"
            example.write_text(rendered, encoding="utf-8")
            written += 1
    return written


def main() -> int:
    changed = 0
    for project_type in sorted(SUPPORTED_TYPES):
        for profile in ("minimal", "standard", "full"):
            path = TEMPLATES / project_type / profile / "README.template.md"
            if path.is_file():
                changed += int(unify_template(path, project_type))

    english_preview = """## Preview\n\n<p align=\"center\">\n  <img src=\"assets/placeholders/screenshot.svg\" alt=\"RepoForge preview placeholder\" width=\"820\">\n</p>\n\n<p align=\"center\"><em>Reserved for real RepoForge screenshots. The committed placeholder intentionally contains no mock interface or fabricated product output.</em></p>\n"""
    chinese_preview = """## 预览\n\n<p align=\"center\">\n  <img src=\"assets/placeholders/screenshot.svg\" alt=\"RepoForge 截图占位图\" width=\"820\">\n</p>\n\n<p align=\"center\"><em>这里预留给未来真实的 RepoForge 截图；仓库中的占位图刻意不包含虚构界面或虚构输出。</em></p>\n"""

    changed += int(
        replace_readme_section(
            ROOT / "README.md",
            "## Preview gallery\n",
            "## Template matrix",
            english_preview,
        )
    )
    changed += int(
        replace_readme_section(
            ROOT / "README.zh-CN.md",
            "## 预览图库\n",
            "## 模板矩阵",
            chinese_preview,
        )
    )

    english_usability = """## Usability today\n\nRepoForge is **usable now for explicit, configuration-driven README rendering**. From a source checkout you can select any of the seven project types, choose `minimal`, `standard`, or `full`, provide YAML configuration, and render a Markdown README with the strict CLI.\n\nAvailable now:\n\n- `repoforge render`;\n- 7 project types × 3 independent profiles;\n- strict Jinja/YAML validation;\n- committed examples and golden previews;\n- renderer-backed stress tests and Python 3.11–3.13 CI.\n\nNot implemented yet:\n\n- automatic project detection;\n- `init`, `apply`, `diff`, and `check` repository workflows;\n- managed partial updates to an existing hand-edited README;\n- a published PyPI release.\n\nSo the current release is already useful as a **template renderer and standards reference**, but it is not yet the final zero-configuration repository automation tool.\n"""
    chinese_usability = """## 现在能用到什么程度？\n\nRepoForge **现在已经可以用于“显式配置驱动的 README 生成”**。从源码安装后，可以选择七种项目类型中的任意一种，再选择 `minimal`、`standard` 或 `full`，提供 YAML 配置，通过严格 CLI 生成普通 Markdown README。\n\n现在已经可用：\n\n- `repoforge render`；\n- 7 类项目 × 3 套独立 Profile；\n- 严格 Jinja/YAML 配置校验；\n- 完整 Example 与 Golden Preview；\n- Renderer 压力测试以及 Python 3.11–3.13 CI。\n\n还没有实现：\n\n- 自动识别项目类型；\n- `init`、`apply`、`diff`、`check` 等仓库工作流；\n- 对已经人工修改过的 README 做受控局部更新；\n- 正式发布到 PyPI。\n\n因此当前版本已经可以作为**模板生成器与仓库文档规范参考**实际使用，但还不是最终的“零配置自动整理整个仓库”工具。\n"""

    changed += int(insert_usability_section(ROOT / "README.md", "## Project status", english_usability))
    changed += int(insert_usability_section(ROOT / "README.zh-CN.md", "## 项目状态", chinese_usability))

    examples = regenerate_examples()
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_previews.py")],
        cwd=ROOT,
        check=True,
    )

    print(f"unified {changed} source files; regenerated {examples} examples and all previews")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
