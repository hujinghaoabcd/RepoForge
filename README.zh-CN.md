<p align="center">
  <img src="assets/logo.svg" alt="RepoForge" width="160">
</p>

<h1 align="center">RepoForge</h1>

<p align="center">
  <strong>可复用的 README 模板与代码仓库文档规范体系。</strong>
</p>

<p align="center">
  <a href="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/hujinghaoabcd/RepoForge/actions/workflows/tests.yml/badge.svg"></a>
  <a href="pyproject.toml"><img alt="Version" src="https://img.shields.io/badge/version-0.1.0.dev0-174D5B.svg"></a>
  <a href="#模板矩阵"><img alt="README templates" src="https://img.shields.io/badge/templates-21-139C5A.svg"></a>
  <a href="pyproject.toml"><img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-174D5B.svg"></a>
  <a href="#项目状态"><img alt="Status" src="https://img.shields.io/badge/Status-Alpha-F4B942.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-139C5A.svg"></a>
</p>

<p align="center">
  <strong>7 类项目</strong> · <strong>3 套独立 Profile</strong> · YAML + Jinja2 · Renderer Preview · Stress-tested Contracts
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#模板矩阵">模板</a> ·
  <a href="#profiles">Profiles</a> ·
  <a href="#仓库标准">仓库标准</a> ·
  <a href="#预览">预览</a> ·
  <a href="docs/ARCHITECTURE.md">架构</a> ·
  <a href="#测试与压力测试">测试</a>
</p>

---

## RepoForge 是什么

**RepoForge 是应用在“已经有代码的项目”之上的仓库文档规范层。** 它根据项目类型、独立文档 Profile、Jinja 模板和 YAML 配置，渲染面向项目访问者的 `README.md`。

它刻意**不重复做项目脚手架**。Cookiecutter、Scientific Python Cookie、Django 模板、Vite、Astro、Electron、Qt 等负责源码结构；RepoForge 放在它们之后，负责让项目对外展示的 README 与仓库文档更一致、更清晰、更容易审查。

```text
项目脚手架
Cookiecutter / Scientific Python Cookie / Django / Vite / Qt / ...
        ↓
已有代码仓库
        ↓
RepoForge 文档规范层
        ↓
README + 文档结构 + 仓库规范
```

当前可执行核心有意保持精简：**Jinja2 + YAML + 严格 Renderer + CLI**。模板缺少必要变量时直接报错，而不是悄悄生成残缺文档。

## 为什么做 RepoForge？

不同生态的项目需要不同信息，但仍然可以拥有统一、可识别的文档体系。RepoForge 把经常混在一起的三个问题拆开：

- **项目结构** —— 交给脚手架或框架；
- **项目类型** —— 决定 README 应该重点回答什么；
- **文档深度** —— 由独立的 `minimal`、`standard`、`full` 模板控制。

这样可以避免两个极端：把一个万能 README 强行套到所有项目上，或者维护一个充满条件判断、越来越难测试的巨大模板。

RepoForge 的核心规则包括：

- README 是**项目入口页**，不是完整手册；
- Minimal、Standard、Full 是**三套独立模板**；
- Full 表示**文档更深入**，不是凭空增加项目能力；
- 科研包在适用时要明确验证、复现、限制和引用；
- 实验仓库要明确数据身份、协议、种子、结果与复现命令；
- Web 与桌面项目优先回答用户如何运行、安装、部署或升级；
- 最终输出仍然是普通 Markdown，可以继续人工维护。

## 预览

<p align="center">
  <img src="assets/placeholders/screenshot.svg" alt="RepoForge 截图占位图" width="820">
</p>

<p align="center"><em>这里预留给未来真实的 RepoForge 截图；仓库中的占位图刻意不包含虚构界面或虚构输出。</em></p>

## 模板矩阵

RepoForge 已完成第一阶段完整矩阵：**7 类项目 × 3 个 Profile = 21 套 README 模板**。

| 项目类型 | 适用项目 | README 重点 |
| --- | --- | --- |
| `scientific-python` | 可复用科研 Python 包 | 科学定位、安装、最小示例、方法、验证、文档、引用 |
| `research-algorithm` | 原创方法与创新算法 | 科学问题、方法、公式/算法、验证、限制、引用 |
| `research-experiment` | 论文代码、基准实验、可复现仓库 | 数据身份、环境、协议、种子、结果、复现 |
| `django-package` | 可复用 Django App 与扩展 | 宿主项目接入、设置、兼容、迁移、安全 |
| `web-application` | 可部署 Web 产品与系统 | 产品、本地运行、配置、数据库、部署、运维 |
| `frontend-library` | 前端库、插件、组件、适配器 | 安装/import、CSS、API、事件、适配、Browser/SSR/Types/Bundle |
| `desktop-application` | Windows/macOS/Linux 桌面软件 | 截图、下载、平台、用户数据、打包、升级、故障排查 |

每个家族都有三套独立目录：

```text
templates/<project-type>/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   ├── README.example.md
│   └── config.example.yml
├── standard/
└── full/
```

每个家族另外包含 `CONTRACT.md` 与 `references.md`，说明该项目类型的边界以及参考过的真实项目。

## Profiles

| Profile | 适用情况 | 目标 |
| --- | --- | --- |
| **Minimal** | 小型、聚焦、早期、内部或单一用途项目 | 最短但完整的项目入口页 |
| **Standard** | 大多数正式维护的开源项目 | 清晰度与信息深度的默认平衡 |
| **Full** | 兼容、科研、部署、打包、安全或升级边界更复杂的成熟项目 | 更深入，但不把 README 写成完整手册 |

Full 项目并不需要支持所有平台、框架、服务、Adapter、插件系统或发布渠道。可选章节只在项目确实维护对应能力时出现。

## 快速开始

从源码安装 RepoForge：

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

先为已有项目生成统一配置：

```bash
repoforge init /path/to/project \
  --type scientific-python \
  --profile standard \
  --name MyPackage \
  --repository-url https://github.com/example/my-package
```

编辑生成的 `repoforge.yml` 后，先查看精确文本差异，再应用：

```bash
repoforge diff /path/to/project --config /path/to/project/repoforge.yml
repoforge apply /path/to/project --config /path/to/project/repoforge.yml --dry-run
repoforge apply /path/to/project --config /path/to/project/repoforge.yml
repoforge check /path/to/project
```

`init` 会把显式选择的项目类型/Profile 写入配置，不进行项目类型自动识别。详细说明见 [`docs/INIT.md`](docs/INIT.md)、[`docs/DIFF.md`](docs/DIFF.md) 和 [`docs/APPLY.md`](docs/APPLY.md)。

选择项目类型和 Profile 渲染 README：

```bash
repoforge render scientific-python standard \
  --config templates/scientific-python/standard/config.example.yml \
  --output README.generated.md
```

其他示例：

```bash
repoforge render research-experiment full \
  --config templates/research-experiment/full/config.example.yml \
  --output README.generated.md

repoforge render web-application full \
  --config templates/web-application/full/config.example.yml \
  --output README.generated.md

repoforge render desktop-application standard \
  --config templates/desktop-application/standard/config.example.yml \
  --output README.generated.md
```

输出结果就是普通 Markdown，可以用 Git 审查、继续人工修改，并把过深内容下沉到 `docs/`。

把 README 和矩阵选中的仓库标准应用到已有项目时，可以先 Dry Run：

```bash
repoforge apply /path/to/project \
  --type scientific-python \
  --profile standard \
  --config examples/apply/scientific-python-standard.yml \
  --dry-run
```

确认计划后去掉 `--dry-run` 再执行。RepoForge 默认拒绝覆盖内容不同的已有文件，只有显式使用 `--force` 才会覆盖。完整说明见 [`docs/APPLY.md`](docs/APPLY.md)。

## Renderer 如何工作

```text
config.example.yml
        +
README.template.md
        +
项目类型 / Profile
        ↓
 RepoForge Strict Renderer
        ↓
 generated README.md
```

Renderer 使用 Jinja2 `StrictUndefined`。模板需要但配置缺失的变量会直接失败，不会静默输出残缺章节。

当前 CLI 已经实现 `repoforge render`、显式配置的 `repoforge init`、用于精确审查的 `repoforge diff` 和安全优先的 `repoforge apply`。仓库标准根据显式选择的项目类型/Profile 矩阵决定；RepoForge 明确不做项目类型自动判断。

## Preview 与 Golden Output

已批准的可视 Preview 位于：

```text
tests/previews/<project-type>/<profile>.md
```

RepoForge 自己的 Preview 统一使用一个品牌源和一个中性媒体占位图：

```text
assets/logo.svg
assets/placeholders/screenshot.svg
        ↑
tests/branding.yml
```

README Logo 的统一显示宽度为 **160px**。Preview 中需要截图、方法图或 Demo 图的位置统一使用刻意留空的占位图；面向用户的 `README.example.md` 保持项目中立，可以自行提供真实 Logo、截图、方法图或 Demo 素材。

重新生成 21 个 Preview：

```bash
python scripts/generate_previews.py
```

## 测试与压力测试

运行完整测试：

```bash
python -m pytest
```

GitHub Actions 会在 Python **3.11、3.12、3.13** 上运行测试，对全部七类模板执行 CLI Render Smoke Test，并在临时仓库上真实执行完整的 `init → diff → apply → check` 流程，并验证人为制造的文档漂移必须失败。

Renderer-backed 压力测试位于：

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

这些案例专门覆盖容易让通用 README 失效的形态：极小科研包、理论很重的算法、多种子实验、没有 Models 的 Django Middleware、没有 Queue/API 的 Full Web Monolith、没有框架 Adapter/SSR 的 Vanilla Frontend Library，以及没有插件/自动更新的 Full Desktop Application。

核心不变量是：

> **Full 表示文档深度更高，不代表可以伪造项目实际不存在的能力或基础设施。**

## 仓库标准

RepoForge 现在除了 README 矩阵，还加入了第一批仓库健康标准：

- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) —— 社区参与与行为边界；
- [`CONTRIBUTING.md`](CONTRIBUTING.md) —— 贡献流程与模板修改规则；
- [`SECURITY.md`](SECURITY.md) —— 私下漏洞报告与受支持版本策略；
- [`SUPPORT.md`](SUPPORT.md) —— 使用问题、Bug、安全问题和行为问题分别应该走什么渠道。

可复用仓库标准现在分成三组：

- [`standards/community/`](standards/community/) —— Code of Conduct、贡献、安全与支持；
- [`standards/github/`](standards/github/) —— Issue Forms 与 Pull Request Template；
- [`standards/metadata/`](standards/metadata/) —— `CITATION.cff` 与 `CHANGELOG.md`。

每组都根据显式项目类型/Profile 提供策略规则。这一层明确**不做项目类型自动判断**。

## 仓库结构

```text
RepoForge
├── assets/                         # Logo 与 README 素材
├── src/repoforge/                  # Renderer 与 CLI
├── templates/                      # 7 类项目 × 3 Profiles
├── profiles/                       # 跨项目 Profile 规则
├── standards/                      # 社区、安全、支持等仓库级合同
├── partials/                       # 可复用文档组件
├── tests/
│   ├── previews/                   # 已批准渲染效果
│   └── stress/                     # 真实困难形态压力测试
├── scripts/                        # Preview 与维护脚本
└── docs/                           # 架构与规范
```

完整设计边界见 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)。

## 设计原则

- **README 是项目入口，不是完整说明书。**
- **Minimal、Standard、Full 必须保持独立模板。**
- **项目类型和文档深度是两个不同维度。**
- **首屏先建立项目身份、有效徽章和导航，再进入正文。**
- **徽章用于表达维护中的事实，而不是装饰。**
- **Full Profile 不能凭空生成项目没有的能力。**
- **Example 与 Preview 由 Renderer 生成，使视觉和结构回归可以被测试。**
- **配置不完整时应明确失败。**
- **生成结果始终保持普通、可编辑的 Markdown。**

## 现在能用到什么程度？

RepoForge **现在已经可以用于“显式配置驱动的 README 生成 + 仓库标准应用”**。从源码安装后，显式选择七种项目类型之一和对应 Profile，提供一份合并 YAML 配置，就可以只渲染 README，也可以把选中的仓库标准安全应用到已有项目。

现在已经可用：

- `repoforge render`；
- `repoforge init`，生成包含显式项目类型/Profile 的统一 `repoforge.yml`；
- `repoforge diff`，以 Unified Diff 无写入审查当前 Apply 计划的精确变化；
- `repoforge apply`，包含 `--dry-run`、冲突预检查、`--force` 和标准选择覆盖；
- `repoforge check`，用于 CI 中检查配置、漂移、CFF/Issue Form 结构以及关键占位符；
- 7 类项目 × 3 套独立 Profile；
- 社区、GitHub 协作、Citation 与 Changelog 标准；
- 严格 Jinja/YAML 配置校验；
- 完整 Example 与 Golden Preview；
- Renderer 压力测试以及 Python 3.11–3.13 CI。

还没有实现：

- 对已经人工修改过的 README 做受控局部更新或语义合并；
- 正式发布到 PyPI。

因此当前版本已经可以作为**README 与仓库标准应用工具**实际使用，而且会保持显式配置，而不是发展成零配置的项目类型猜测器。

## 项目状态

RepoForge 当前处于 **Alpha** 阶段。模板层的第一阶段已经完成：21 种项目类型/Profile 组合全部存在，Renderer 可执行，Preview 已提交，而且七个家族都有 Contract 和 Stress Coverage。

仓库标准层以及 `init`、`diff`、`apply`、`check` 工作流已经实现。下一阶段重点转向对人工维护文件的受控局部/语义更新，以及正式包发布。

当前正式支持的 CLI 命令是 `repoforge render`、`repoforge init`、`repoforge diff`、`repoforge apply` 和 `repoforge check`。

## Contributing

RepoForge 把模板变化视为“文档设计变化”。修改 Contract 或 Template 时：

1. 保持 Minimal / Standard / Full 独立；
2. 同步更新对应 Example 与 Golden Preview；
3. 如果影响项目边界，补充或修改 Stress Case；
4. 合并前运行完整测试。

只有在 README 合同确实不同的情况下才新增项目家族，不应只因为技术名称不同就复制一个新类型。

## License

RepoForge 使用 [MIT License](LICENSE)。
