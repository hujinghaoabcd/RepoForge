# RepoForge

**可复用的代码仓库文档与项目规范体系。**

RepoForge 用于把统一、可复用的 README 与仓库文档规范应用到已经生成好的软件或科研项目中。它不替代 Cookiecutter、Scientific Python Cookie、Django 模板、Vite 等脚手架，而是作为项目脚手架之后的“文档与规范层”。

[English](README.md) · **简体中文**

## 为什么需要 RepoForge？

项目脚手架擅长生成代码结构，但仓库还需要清晰的公开文档入口。RepoForge 将这两类工作分开：

1. 先用最适合技术栈的工具生成项目结构；
2. 选择 RepoForge 的项目类型和一套独立 Profile；
3. 用显式 YAML 配置渲染普通 Markdown README；
4. 把完整理论、API、实验细节和部署手册继续放在 `docs/` 中，而不是全部塞进 README。

目标不是让所有 README 完全相同，而是形成统一的家族风格，同时保留不同项目真正需要的信息。

## 当前已实现

第一套已经可以实际渲染的模板是：

```text
scientific-python
├── minimal
├── standard
└── full
```

三种 Profile 是 **三套独立模板**，不是一个大模板里的条件分支。

每个 Profile 都包含：

```text
PROFILE.md
README.template.md
README.example.md
config.example.yml
```

## 快速开始

从源码安装：

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

生成 Minimal：

```bash
repoforge render scientific-python minimal \
  --config templates/scientific-python/minimal/config.example.yml \
  --output README.generated.md
```

生成 Standard：

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

生成 Full：

```bash
repoforge render scientific-python full \
  --config templates/scientific-python/full/config.example.yml \
  --output README.generated.md
```

渲染器使用严格变量检查：模板需要但 YAML 没有声明的字段会直接报错，不会静默生成残缺 README。

## 查看生成效果

预览文件位于：

```text
tests/previews/<project-type>/<profile>.md
```

当前科研 Python 预览为：

```text
tests/previews/scientific-python/
├── minimal.md
├── standard.md
└── full.md
```

重新生成科研 Python 三档预览：

```bash
python scripts/generate_previews.py
```

## 计划支持的项目类型

RepoForge 按七类项目组织模板：

- `scientific-python` —— 可复用科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 小型到大型 Web 应用；
- `frontend-library` —— 前端库、插件与组件；
- `desktop-application` —— 桌面端与跨平台软件。

目前只有 `scientific-python` 已具备完整可执行渲染合同；其他类型目前已经拆分出独立的 Minimal / Standard / Full 视觉预览，后续逐类实现。

## Profiles

Profile 控制文档深度，但每一档都是独立模板：

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
│   └── previews/                  # 可视化预览
├── scripts/                       # 维护脚本
└── docs/                          # 架构与规范
```

详细设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 设计原则

- **README 是项目入口，不是完整说明书。**
- **Minimal、Standard、Full 必须保持独立模板。**
- **项目类型和文档深度是两个不同维度。**
- **科研软件把 Validation、Reproducibility、Limitations、Citation 作为一级需求。**
- **生成结果始终是普通可读 Markdown。**
- **配置缺失时应明确失败，而不是生成误导性的文档。**

## 测试

```bash
python -m pytest
```

GitHub Actions 会在支持的 Python 版本上运行测试，并执行 CLI 渲染 smoke test。

## 当前状态

RepoForge 处于早期开发阶段。`scientific-python` 是第一套正式实现的渲染模板，下一步将继续完善预览同步并实现其他项目类型。

## License

MIT.
