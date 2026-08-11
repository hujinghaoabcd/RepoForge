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

RepoForge 目前已有六套可执行模板家族：

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

web-application
├── minimal
├── standard
└── full

frontend-library
├── minimal
├── standard
└── full
```

三种 Profile 都是**独立模板**，不是一个大模板里的条件分支。

- `scientific-python` —— 可复用科研 Python 软件包；
- `research-algorithm` —— 原创科学/技术方法与创新算法；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django App、扩展、中间件、认证/权限后端与 Admin 集成；
- `web-application` —— 完整、可运行和可部署的 Web 产品；
- `frontend-library` —— 安装进其他前端项目中的库、插件、组件、Hook 以及框架/地图引擎适配器。

每个已实现家族都具有 Contract、真实案例分析、独立 Profile 规则、Jinja 模板、YAML 示例配置、生成示例、带统一 Logo 的 Preview、renderer 测试以及压力测试。

## 快速开始

安装：

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

例如生成前端库 Standard README：

```bash
repoforge render frontend-library standard \
  --config templates/frontend-library/standard/config.example.yml \
  --output README.generated.md
```

渲染器使用严格的 Jinja 变量检查：模板需要但 YAML 未声明的字段会直接报错，不会静默生成残缺 README。

## 预览与 Logo

预览文件位于：

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge 自己的 Preview 统一使用：

```text
assets/logo.svg
```

**Markdown 中统一显示宽度为 280px**，只控制 `<img width="280">`，不修改 SVG 原文件。用户项目的 `README.example.md` 不强制使用 RepoForge Logo，可自由提供自己的 `logo_path` 和尺寸。

## 压力测试

Renderer-backed 压力测试位于：

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
├── django-package/
├── web-application/
└── frontend-library/
```

Frontend Library 压力测试覆盖：极小 DOM 工具、CSS 重型组件、框架适配插件、多包 UI 工具集，以及**没有 React/Vue Adapter、也不声明 SSR 支持的 Full Vanilla TypeScript 库**。

最后一个案例继续保护 RepoForge 的核心规则：**Full 表示文档深度更高，而不是凭空为项目增加生态能力。**

## 七类项目类型

- `scientific-python` —— 可复用科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 小型到大型、可部署的 Web 应用；
- `frontend-library` —— 前端库、插件与组件；
- `desktop-application` —— 桌面端与跨平台软件。

现在只剩最后一类 `desktop-application` 尚未实现。

## Profiles

- **Minimal** —— 小型、聚焦项目，最短但完整；
- **Standard** —— 大多数正式维护开源项目的默认选择；
- **Full** —— 面向集成面、兼容性、安全、部署、运行时边界或升级规则更复杂的成熟项目。

对于 Frontend Library，Profile 深度与生态宽度是两个不同维度：Full Vanilla 库仍然可以不提供 React/Vue 适配器、不支持 SSR，也不需要拆成多个 npm package。

## Frontend Library 的边界

`frontend-library` 面向安装进其他前端项目中的可复用代码，因此 README 的核心路径是：

```text
解决什么前端问题
  ↓
安装哪个包
  ↓
CSS / Peer Dependencies 等必要设置
  ↓
最短可复制示例
  ↓
API / Events / Lifecycle
  ↓
Styling / Framework Adapters
  ↓
Browser / TypeScript / SSR / Bundle / Accessibility
  ↓
完整文档与版本策略
```

完整网站和 SaaS 属于 `web-application`，而不是 `frontend-library`。

## 设计原则

- **README 是项目入口，不是完整说明书。**
- **Minimal、Standard、Full 必须保持独立模板。**
- **项目类型和文档深度是两个不同维度。**
- **科学软件必须明确验证、复现、限制和引用。**
- **实验仓库必须明确数据身份、协议、种子、结果身份和复现命令。**
- **Django 包必须明确宿主项目接入、兼容性、迁移、安全和升级边界。**
- **Web 应用必须区分产品、本地开发、配置、持久化数据、部署、运维与安全。**
- **前端库必须在真实适用时明确安装/CSS/Peer Dependency、API/Event、Adapter、Browser、TypeScript、SSR、Tree-shaking、Accessibility 和版本兼容合同。**
- **Full Profile 不能凭空生成项目实际不存在的能力。**
- **生成结果始终是普通可读 Markdown。**

## 测试

```bash
python -m pytest
```

GitHub Actions 会在 Python 3.11、3.12、3.13 上运行测试，并对每个已实现模板家族执行 CLI render smoke test。

## 当前状态

RepoForge 目前已有六套可执行模板家族：`scientific-python`、`research-algorithm`、`research-experiment`、`django-package`、`web-application` 和 `frontend-library`。最后计划实现 `desktop-application`。

## License

MIT.
