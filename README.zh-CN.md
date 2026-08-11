<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="280">
</p>

# RepoForge

**可复用的代码仓库文档与项目规范体系。**

RepoForge 用于把统一、可复用的 README 与仓库文档规范应用到已经生成好的软件或科研项目中。它不替代 Cookiecutter、Scientific Python Cookie、Django 模板、Vite 等脚手架，而是作为项目脚手架之后的“文档与规范层”。

[English](README.md) · **简体中文**

## 为什么需要 RepoForge？

项目脚手架负责代码结构，RepoForge 负责仓库对外呈现和文档规范：

1. 先用最合适的脚手架生成项目；
2. 选择 RepoForge 项目类型和一个独立 Profile；
3. 用显式 YAML 配置渲染普通 Markdown README；
4. 详细理论、API、实验和部署手册继续下沉到 `docs/`。

目标不是让所有 README 完全相同，而是形成统一家族风格，同时保留不同项目真正需要的信息。

## 当前已实现的模板类型

RepoForge 目前已有四套可执行模板家族：

```text
scientific-python
├── minimal
├── standard
└── full

research-algorithm
├── minimal
├── standard
└── full

research-experiment
├── minimal
├── standard
└── full

django-package
├── minimal
├── standard
└── full
```

三种 Profile 都是**独立模板**，不是一个大模板里的条件分支。

- `scientific-python` —— 可复用科研 Python 软件包；
- `research-algorithm` —— 原创科学/技术方法与创新算法；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django App、扩展、中间件、认证/权限后端与 Admin 集成。

每个已实现家族都具有 Contract、真实案例分析、独立 Profile 规则、Jinja 模板、YAML 示例配置、生成示例、带统一 Logo 的 Preview、renderer 测试以及压力测试。

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

生成论文实验 Full README：

```bash
repoforge render research-experiment full \
  --config templates/research-experiment/full/config.example.yml \
  --output README.generated.md
```

生成 Django 可复用包 Standard README：

```bash
repoforge render django-package standard \
  --config templates/django-package/standard/config.example.yml \
  --output README.generated.md
```

渲染器使用严格的 Jinja 变量检查：模板需要但 YAML 未声明的字段会直接报错，不会静默生成残缺 README。

## 预览

预览文件位于：

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge 自己的 Preview 统一使用唯一品牌源：

```text
assets/logo.svg
```

重新生成已实现模板类型的预览：

```bash
python scripts/generate_previews.py
```

用户项目的 `README.example.md` 不强制使用 RepoForge Logo，真正生成项目时仍可自由提供自己的 `logo_path`。

## 压力测试

Renderer-backed 压力测试位于：

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
└── django-package/
```

Django 压力测试故意覆盖差异很大的可复用包形态：极小 Template Tag App、中间件顺序约束、权限 Backend、复杂 Admin 扩展，以及**没有 Models/Admin 的 Full 中间件包**。因此 Full 表示“文档深度更高”，而不是强行让项目拥有所有功能。

## 七类项目类型

- `scientific-python` —— 可复用科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 小型到大型 Web 应用；
- `frontend-library` —— 前端库、插件与组件；
- `desktop-application` —— 桌面端与跨平台软件。

剩余三类将继续按照同一套 Contract、独立 Profile、Preview 和压力测试规则逐类实现。

## Profiles

- **Minimal** —— 小型、聚焦项目，最短但完整；
- **Standard** —— 大多数正式维护开源项目的默认选择；
- **Full** —— 面向集成面、兼容性、验证、复现、安全或升级边界更复杂的成熟项目。

## Django Package 的边界

`django-package` 面向“安装到另一个 Django 项目中的可复用组件”，因此重点是：

```text
包是什么
  ↓
如何安装
  ↓
需要哪些 Django 接入点
  ↓
最短可运行用法
  ↓
公开 API / Admin / Middleware / Backend 等实际能力
  ↓
兼容性、安全与升级边界
```

完整 Django 网站、SaaS、后台系统等不属于这一类，它们后续进入 `web-application`。

## 仓库结构

```text
RepoForge
├── assets/                         # RepoForge 品牌资产
├── src/repoforge/                  # renderer 与 CLI
├── templates/                      # 项目类型 / Profile 模板
├── profiles/                       # 跨项目 Profile 规则
├── partials/                       # 可复用文档模块
├── tests/
│   ├── previews/                   # 可视化生成效果
│   └── stress/                     # 极端真实形态压力测试
├── scripts/                        # 维护脚本
└── docs/                           # 架构与规范
```

详细设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 设计原则

- **README 是项目入口，不是完整说明书。**
- **Minimal、Standard、Full 必须保持独立模板。**
- **项目类型和文档深度是两个不同维度。**
- **科研软件把 Validation、Reproducibility、Limitations、Citation 作为一级需求。**
- **实验仓库必须明确数据身份、实验协议、随机种子、结果身份和复现命令。**
- **Django 包必须明确宿主项目接入点、兼容性、迁移、安全和升级边界。**
- **Full Profile 不能凭空生成项目实际不存在的能力。**
- **生成结果始终是普通可读 Markdown。**
- **配置缺失时应明确失败，而不是生成误导性的文档。**

## 测试

```bash
python -m pytest
```

GitHub Actions 会在 Python 3.11、3.12、3.13 上运行测试，并对每个已实现模板家族执行 CLI render smoke test。

## 当前状态

RepoForge 目前已有四套可执行模板家族：`scientific-python`、`research-algorithm`、`research-experiment` 和 `django-package`。下一类开始实现 `web-application`。

## License

MIT.
