<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="280">
</p>

<h1 align="center">RepoForge</h1>

<p align="center"><strong>可复用的代码仓库文档与项目规范体系。</strong></p>

<p align="center">
  <a href="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml"><img src="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="#当前已实现的模板类型"><img src="https://img.shields.io/badge/templates-7%20families-blue" alt="7 template families"></a>
  <a href="#测试"><img src="https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue" alt="Python 3.11–3.13"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

RepoForge 用于把统一、可复用的 README 与仓库文档规范应用到已经生成好的软件或科研项目中。它不替代 Cookiecutter、Scientific Python Cookie、Django 模板、Vite 等脚手架，而是作为项目脚手架之后的“文档与规范层”。

## 为什么需要 RepoForge？

项目脚手架负责代码结构，RepoForge 负责仓库对外呈现和文档规范：

1. 先用最合适的脚手架生成项目；
2. 选择 RepoForge 项目类型和独立 Profile；
3. 用显式 YAML 配置渲染普通 Markdown README；
4. 详细理论、API、实验、部署与运维手册继续下沉到 `docs/`。

目标不是让所有 README 完全相同，而是形成统一家族风格，同时保留不同项目真正需要的信息。

## 当前已实现的模板类型

RepoForge 的初始七类项目现在已经全部可执行，每类都有独立的 `minimal`、`standard`、`full`：

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

desktop-application
├── minimal
├── standard
└── full
```

三种 Profile 都是**独立模板**，不是一个大模板中的条件分支。

- `scientific-python` —— 可复用科研 Python 软件包；
- `research-algorithm` —— 原创科学/技术方法与创新算法；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django App 与扩展；
- `web-application` —— 完整、可运行和可部署的 Web 产品；
- `frontend-library` —— 安装进其他前端项目的库、插件、组件、Hook 与适配器；
- `desktop-application` —— Windows、macOS、Linux 或明确限定平台的可安装桌面软件。

每个家族都包含 Contract、真实案例分析、独立 Profile、Jinja 模板、YAML 示例配置、生成示例、Preview、renderer 测试以及压力测试。

## 快速开始

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

按项目类型和 Profile 生成 README，例如：

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render frontend-library standard \
  --config templates/frontend-library/standard/config.example.yml \
  --output README.generated.md
```

```bash
repoforge render desktop-application standard \
  --config templates/desktop-application/standard/config.example.yml \
  --output README.generated.md
```

渲染器使用严格的 Jinja 变量检查：模板需要但 YAML 未声明的字段会直接报错，不会静默生成残缺 README。

## 预览与 Logo

预览文件位于：

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge 自己的 Preview 统一使用 `assets/logo.svg`，Markdown 显示宽度为 **280px**。这里只控制 `<img width="280">`，不修改 SVG 原文件。用户项目可自由提供自己的 Logo 和尺寸。

## 压力测试

七类项目都具有 renderer-backed 压力测试：

```text
tests/stress/
├── scientific-python/
├── research-algorithm/
├── research-experiment/
├── django-package/
├── web-application/
├── frontend-library/
└── desktop-application/
```

这些测试故意覆盖容易让“万能 README 模板”失效的形态，例如：没有 API/队列的 Full Web 单体应用、没有 React/Vue/SSR 的 Full Vanilla 前端库，以及**只有 Windows、没有插件、没有自动更新、没有 Portable Mode、没有 Telemetry 的 Full 桌面应用**。

它们共同保护一条核心规则：**Full 表示文档深度更高，而不是凭空制造功能。**

## 七类项目类型

- `scientific-python` —— 可复用科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 小型到大型、可部署的 Web 应用；
- `frontend-library` —— 前端库、插件与组件；
- `desktop-application` —— 可安装桌面软件与跨平台应用。

## Profiles

- **Minimal** —— 小型、聚焦项目，最短但完整；
- **Standard** —— 大多数正式维护开源项目的默认选择；
- **Full** —— 面向兼容性、集成、安全、发布、打包或升级边界更复杂的成熟项目。

Profile 深度与项目能力宽度是两个维度。Full 不意味着必须支持所有平台、框架、服务、插件系统或分发渠道。

## Desktop Application 的头部规范

桌面软件首先要让用户识别“这是什么软件、去哪下载、支持什么平台”，因此头部统一居中：

```text
Logo / 应用图标
项目名
一句话定位
Release / Platform / Build / License 等核心徽章
Download / Docs / Issues 导航
有条件时展示 Screenshot
```

Full 再根据真实能力加入项目格式、插件、更新渠道、Portable Mode、隐私/Telemetry、签名、迁移和故障排查；项目没有的能力就不生成对应章节。

## 设计原则

- **README 是项目入口，不是完整说明书。**
- **Minimal、Standard、Full 必须保持独立模板。**
- **项目类型和文档深度是两个不同维度。**
- **有决策价值的徽章集中放在项目身份区，不散落到 README 各处。**
- **科学软件明确 Validation、Reproducibility、Limitations、Citation。**
- **实验仓库明确数据身份、协议、种子、结果身份和复现命令。**
- **Django 包明确宿主项目接入、兼容性、迁移、安全和升级边界。**
- **Web 应用区分产品、本地开发、配置、持久化数据、部署、运维与安全。**
- **前端库明确安装/CSS/Peer Dependency、API/Event、Adapter、Browser、TypeScript、SSR、Bundle 与 Accessibility 合同。**
- **桌面应用优先明确下载、平台、产品视觉、用户数据位置、打包和发布兼容性。**
- **Full Profile 不能凭空生成实际不存在的能力。**
- **生成结果始终是普通可读 Markdown。**

## 测试

```bash
python -m pytest
```

GitHub Actions 会在 Python 3.11、3.12、3.13 上运行测试，并对全部七类模板执行 CLI render smoke test。

## 当前状态

RepoForge 的初始 **7 类项目 × 3 个 Profile = 21 个模板组合**已经全部进入可执行体系。下一阶段重点将转向项目自动识别、配置体验、`apply/diff/check` 工作流，以及七类模板的统一视觉细化。

## License

MIT.
