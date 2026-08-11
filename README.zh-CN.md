# RepoForge

**可复用的代码仓库文档与项目规范体系。**

RepoForge 用于把统一、可复用的文档与仓库规范应用到已经生成好的软件或科研项目中。它并不替代 Cookiecutter、Scientific Python Cookie、Vite、Django 模板等项目脚手架，而是作为脚手架之后的“规范层”。

[English](README.md) · **简体中文**

## 为什么需要 RepoForge？

项目脚手架擅长生成代码结构，但一个真正可维护、可发布、可复现的仓库，还需要清晰的 README、文档入口以及贡献、引用、测试、部署等规范。RepoForge 将这两类工作分开：

1. **先用最适合技术栈的脚手架生成项目**；
2. **再用 RepoForge 套用统一的 README 与仓库文档结构**；
3. **最后补充项目特有内容**，例如算法、截图、实验、部署、API 和论文信息。

RepoForge 的目标不是让所有 README 长得完全一样，而是让不同类型的项目保持统一的家族风格，同时保留各自真正需要的信息。

## 首批项目类型

RepoForge 计划首先支持七类模板：

- `scientific-python` —— 科研 Python 包；
- `research-algorithm` —— 原创方法与创新算法实现；
- `research-experiment` —— 论文代码、基准实验与可复现实验仓库；
- `django-package` —— 可复用 Django 应用与扩展；
- `web-application` —— 从小型网站到大型 Web 应用；
- `frontend-library` —— 前端库、插件和组件；
- `desktop-application` —— 桌面端与跨平台软件。

## 文档深度 Profiles

每一种项目类型再区分三种文档深度：

- **minimal** —— Demo、小工具、原型、小型插件；
- **standard** —— 大多数正式维护的开源项目，默认推荐；
- **full** —— 成熟科研软件、大型应用、复杂可复现实验。

项目类型与项目规模是两个不同维度。例如，小型网站和大型网站都属于 `web-application`，只是使用不同 profile，而不需要维护两套完全独立的模板。

## 架构

RepoForge 初始结构由三个可复用层组成：

```text
RepoForge
├── templates/   # 按项目类型组织的 README 结构
├── profiles/    # minimal / standard / full 深度规则
├── partials/    # badges、citation、testing、deployment 等可复用模块
└── docs/        # 设计规范与编写规则
```

未来计划提供如下命令：

```bash
repoforge apply .
repoforge apply . --type scientific-python --profile standard
repoforge check .
```

RepoForge 应尽可能自动识别 `pyproject.toml`、`package.json`、Django 项目文件、测试、文档与 CI 配置，只询问无法安全推断的信息。

初始设计见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 设计原则

- **README 是项目入口，不是完整说明书。** 理论、API、部署手册和开发说明过长时应下沉到 `docs/`。
- **项目类型和项目规模分开建模。** 不因为项目更大就复制一套新模板。
- **通用模块尽量复用。** 安装、徽章、引用、测试、安全、部署、贡献说明不应在每个模板中重新发明。
- **科研软件拥有科研专属需求。** Validation、Reproducibility、Limitations、Citation 在适用时是一级内容。
- **生成结果必须仍是普通可读 Markdown。** 不依赖专有格式才能维护项目。

## 当前状态

RepoForge 处于初始设计与模板调研阶段。第一阶段先完成 `scientific-python`，以成熟 Scientific Python 项目和现有科研包作为参考案例。

## License

首个公开版本发布前再确定项目许可证。
