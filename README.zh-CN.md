<p align="center">
  <img src="assets/repoforge-logo.png" alt="RepoForge" width="520">
</p>

# RepoForge

**可复用的代码仓库文档与项目规范体系。**

RepoForge 用于把统一、可复用的 README 与仓库文档规范应用到已经生成好的软件或科研项目中。它不替代 Cookiecutter、Scientific Python Cookie、Django 模板、Vite 等脚手架，而是作为项目脚手架之后的“文档与规范层”。

[English](README.md) · **简体中文**

## 为什么需要 RepoForge？

项目脚手架负责代码结构，RepoForge 负责仓库对外呈现和文档规范：

1. 先用最合适的脚手架生成项目；
2. 选择 RepoForge 项目类型和独立 Profile；
3. 用 YAML 配置渲染普通 Markdown README；
4. 详细理论、API、实验和部署内容继续下沉到 `docs/`。

目标不是让所有 README 完全相同，而是形成统一家族风格，同时保留不同项目真正需要的信息。

## 当前已实现的模板类型

```text
scientific-python
├── minimal
├── standard
└── full

research-algorithm
├── minimal
├── standard
└── full
```

三种 Profile 都是**独立模板**，不是一个大模板里的条件分支。

`scientific-python` 目前更成熟，已经包含 Profile 合同、Jinja 模板、YAML 示例、预览和专门压力测试；`research-algorithm` 已建立第一版合同、参考分析、三档独立模板、配置和 renderer 测试。

## 快速开始

安装：

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

生成科研 Python Standard README：

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

生成原创算法 Standard README：

```bash
repoforge render research-algorithm standard \
  --config templates/research-algorithm/standard/config.example.yml \
  --output README.generated.md
```

渲染器使用严格变量检查：模板需要但 YAML 没有声明的字段会直接报错，不会静默生成残缺 README。

## 预览

```text
tests/previews/<project-type>/<profile>.md
```

重新生成已实现模板类型的预览：

```bash
python scripts/generate_previews.py
```

## 科研 Python 压力测试

```text
tests/stress/scientific-python/
├── README.md
├── manifest.yml
└── cases/
    ├── tiny-numerical-utility.yml
    ├── multi-method-geospatial.yml
    ├── broad-model-library.yml
    ├── theory-heavy-statistics.yml
    └── pre1-experimental-package.yml
```

这 5 个案例不是手写展示 README，而是实际输入 renderer 的配置，用来检查不同 Profile 在真实极端形态下会不会过度膨胀、缺失关键内容或选错结构。

## 七类项目类型

- `scientific-python` —— 可复用科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 小型到大型 Web 应用；
- `frontend-library` —— 前端库、插件与组件；
- `desktop-application` —— 桌面端与跨平台软件。

其余类型目前保留三档视觉预览，后续逐类升级为可执行模板。

## Profiles

- **Minimal** —— 小型、聚焦项目，最短但完整；
- **Standard** —— 大多数正式维护开源项目的默认选择；
- **Full** —— 方法较多、科学边界复杂或成熟度较高的项目。

## 仓库结构

```text
RepoForge
├── src/repoforge/                 # renderer 与 CLI
├── templates/                     # 项目类型 / Profile 模板
├── profiles/                      # 跨项目 Profile 规则
├── partials/                      # 可复用文档模块
├── tests/
│   ├── previews/                  # 可视化预览
│   └── stress/                    # 压力测试配置
├── scripts/                       # 维护脚本
└── docs/                          # 架构与规范
```

详细设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 测试

```bash
python -m pytest
```

GitHub Actions 会在支持的 Python 版本上运行测试，并执行 CLI 渲染 smoke test。

## 当前状态

RepoForge 处于早期开发阶段。`scientific-python` 是第一套较成熟模板；`research-algorithm` 已成为第二套可执行模板，下一步将继续补充真实案例、预览与压力测试。

## License

MIT.
