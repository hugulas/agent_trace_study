---
tags: [langfuse, github, open-source, llm-engineering, observability, tracing, prompt-management, evaluation, yc-w23, mit-license]
aliases: [langfuse/langfuse GitHub Repository]
date: 2026-05-24
url: https://github.com/langfuse/langfuse
---

# Langfuse: 开源 LLM 工程平台

## 核心信息

- **标题**: GitHub - langfuse/langfuse: Open source LLM engineering platform
- **来源**: GitHub 官方仓库（开源项目主页与 README）
- **类型**: 非论文 / 开源软件项目文档
- **发表时间**: 持续更新（当前版本 v3.175.0，3 天前发布）
- **证据质量**: high
- **相关图片**:
  - `![[../cited-materials/images/[s2-014]/[s2-014]-background-v2-dark.png]]`
  - `![[../cited-materials/images/[s2-014]/[s2-014]-ds-actions-prompt-banner.png]]`

## 内容摘要

Langfuse 是一个开源的大语言模型工程平台。

由 Y Combinator W23 批次孵化，采用 MIT 许可证发布。

该项目定位为帮助团队协同开发、监控、评估和调试 AI 应用的一站式基础设施。

核心能力覆盖 LLM 可观测性（observability）、指标收集（metrics）、
评估（evals）、prompt 管理（prompt management）、实验 playground 和数据集管理（datasets）。

项目深度集成 OpenTelemetry、LangChain、OpenAI SDK、LiteLLM 等主流生态组件，
并支持自托管部署。

从 GitHub 仓库的元数据可以看出 Langfuse 的社区活跃度和产业影响力。

仓库拥有接近 5 万 stars（持续增长中），
月提交量约 213 次，
已关闭 issue 超过 9700 个，
总讨论数 3380+。

Docker 拉取量达到 990 万次，
PyPI 包月下载量 2200 万次，
npm 包月下载量 540 万次。

这些数据表明 Langfuse 已经超越了单纯的实验性项目，
成为 LLM 工程领域事实上的基础设施之一。

Langfuse 的架构采用多包 monorepo 结构，
主要包含 web 前端、worker 后端、以及多个客户端 SDK。

技术栈方面，
web 层基于 Next.js，
整体使用 pnpm workspace 管理，
支持 Docker Compose 一键启动开发环境。

项目对多语言和多云部署友好，
提供了针对 Azure、OCI 等云平台的专用 docker-compose 配置示例，
以及 Redis Cluster 模式的支持。

测试框架已从前身迁移至 vitest，
pre-commit hook 和持续集成流水线构成了完整的质量保障体系。

在核心功能层面，
Langfuse 围绕 trace 构建观测体系。

通过 `@observe()` 装饰器，
Python 开发者可以在几乎不修改现有代码的情况下，
将任意 LLM 应用的调用链路接入 Langfuse。

配合 Langfuse 提供的 OpenAI drop-in 替换集成，
所有 model parameter、token 消耗、latency 等信息会被自动捕获。

对于非 OpenAI 的模型和框架，
Langfuse 也提供了丰富的文档说明和集成方案。

接入流程高度简化：
创建项目、生成 API 凭证、安装 `langfuse` 和 `openai` 包、
设置环境变量（`LANGFUSE_SECRET_KEY`、`LANGFUSE_PUBLIC_KEY`、`LANGFUSE_BASE_URL`），
即可开始追踪首个 LLM 调用。

整个接入过程通常在数分钟内完成。

Langfuse 的集成生态极为广泛。

在框架层面，
支持 LangChain、LlamaIndex、Vercel AI SDK、Haystack、
OpenAI Agents SDK、CrewAI、AutoGen、DSPy、smolagents、Pydantic AI 等
几乎所有主流 agent 和 LLM 框架。

在模型接入层面，
通过 LiteLLM 代理可以实现对任意 LLM provider 的 drop-in 替换。

特别值得关注的是 Langfuse 与 OpenTelemetry 的深度整合。

这意味着 Langfuse 采集的 trace 数据可以无缝流入企业现有的 observability 基础设施，
避免数据孤岛。

这一设计决策对于已投资搭建 Prometheus、Grafana、Jaeger 等监控体系的企业而言，
极大地降低了采纳新工具的切换成本。

项目的开源生态影响力不仅体现在自身仓库的指标上，
更体现在下游采用度。

根据 GitHub README 中展示的统计数据，
使用 Langfuse 的顶级开源 Python 项目包括
LangFlow（低代码 LLM 工作流构建器）、
OpenWebUI（自托管 LLM 聊天界面）、
Lobe Chat（开源聊天机器人平台）、
RAGFlow（RAG 引擎）、
Screenshot-to-Code（AI 截图转代码）等。

此外，
Firecrawl、LlamaIndex、Flowise、Quivr、LibreChat、Litellm、
Mastra、Promptfoo、Cognee 等知名开源项目
均将 Langfuse 作为其可观测性基础设施。

这种广泛的下游集成形成了强大的网络效应，
使得 Langfuse 成为 LLM 应用开发工具链中事实上的观测标准之一。

从工程治理角度看，
Langfuse 展现了成熟开源项目的运作特征。

项目使用 GitHub Discussions 作为支持和功能请求的主要渠道，
设立了 SECURITY.md 安全策略文档，
采用 Code of Conduct 和贡献者协议（CLA）管理社区参与。

多语言文档支持（简体中文、日语、韩语、英语）体现了项目的国际化视野。

持续集成方面，
项目使用 GitHub Actions 并在近期迁移至 Black 代码格式化工具，
pre-commit hook 和自动化测试（vitest）构成了质量保障体系。

项目还发布了详细的 CONTRIBUTING.md 和 AGENTS.md，
规范外部贡献和内部开发流程。

在商业模式上，
Langfuse 采用开源核心 + 云托管服务（Langfuse Cloud）的双轨策略。

用户可以选择完全自托管（数据完全本地，无外部依赖），
也可以使用官方托管的 Langfuse Cloud（分 EU 和 US 区域）。

这种策略在保障数据主权敏感客户的同时，
通过云服务的便利性实现商业化变现。

评测和社区反馈普遍认为 Langfuse 的自托管体验在生产环境中表现稳定，
文档完善度高，
Docker Compose 模板覆盖了从单节点到 Redis Cluster 的多种部署拓扑。

Langfuse 的功能模块设计体现了对 LLM 应用开发全生命周期的深度理解。

Tracing 模块不仅记录 LLM 调用本身，
还涵盖 retrieval、embedding、agent action 等关键逻辑步骤，
形成完整的执行图谱。

Prompt Management 提供版本控制与团队协作能力。

Datasets 模块支持评估基准的构建与版本化管理。

Evaluations 模块允许用户通过代码或配置定义评估指标，
对 LLM 输出进行自动化质量检测。

Playground 则提供了一个交互式环境，
供开发者快速实验不同模型和参数配置的效果。

这些模块之间的数据互通
（如从 trace 直接创建 dataset、在 dataset 上运行 evaluation、
将 evaluation 结果反馈至 prompt 迭代）
构成了一个完整的开发闭环。

## 关键要点

- **开源核心 + 商业云服务的双轨模式**:
  MIT 许可证下的完全开源，支持完全自托管，
  同时提供 Langfuse Cloud 托管服务。

- **极致简化的接入体验**:
  `@observe()` 装饰器 + OpenAI drop-in 替换，
  最小化代码侵入即可实现全链路追踪。

- **庞大的集成生态**:
  覆盖 20+ 主流框架和 SDK，
  通过 OpenTelemetry 与企业现有 observability 基础设施互通。

- **顶级社区指标**:
  GitHub ~50k stars，PyPI 2200 万月下载，
  Docker 990 万拉取，9700+ issue 已解决。

- **广泛的下游采用**:
  LangFlow、OpenWebUI、LlamaIndex、Flowise 等头部开源项目均深度集成 Langfuse。

- **多语言与多云就绪**:
  支持简体中文、日语、韩语文档，
  提供 Azure、OCI 等云平台专用部署配置。

- **持续活跃的开发节奏**:
  月提交 213 次，3 天前发布 v3.175.0，功能迭代速度快。

- **ClickHouse 驱动的高性能存储**:
  后端采用 ClickHouse 开源列式数据库，
  支撑大规模 trace 数据的高效写入与查询。

- **完整的开发闭环**:
  Tracing、Prompt Management、Datasets、Evaluations、Playground 五大模块数据互通。

## 与综述的关联

Langfuse GitHub 仓库是本综述理解开源 LLM 可观测性工具生态的核心一手来源。

作为与 Arize Phoenix（s2-017）、LangSmith（c-005）直接竞争的开源方案，
Langfuse 的 MIT 许可证相比 Arize 的 Elastic License 2.0
在二次商业化和社区 fork 方面更为宽松。

这一授权差异对于评估开源观测工具的可持续性具有重要参考意义。

项目中体现的 trace 数据模型
（tracking LLM calls、retrieval、embedding、agent actions）
直接对应本综述对 agent trace 结构化记录的技术定义
（c-011 AgentTrace、c-012 Agent Audit Trail）。

Langfuse 的 prompt management、dataset version control、experiment tracking 等功能模块，
也为理解当前 LLM 工程平台的功能边界提供了产业参照。

此外，
Langfuse 与 OpenTelemetry 的深度集成实践
（通过 OTLP 导出 trace 数据）
为本综述讨论的 OpenTelemetry AI Agent Observability 标准（c-003、c-015）
提供了真实落地案例。

其与 LiteLLM 的集成模式
（任意 LLM 作为 GPT 的 drop-in 替换）
也反映了当前 LLM 工程领域通过统一网关层解耦模型依赖的架构趋势。

README 中列举的下游采用项目名单，
几乎涵盖了当前开源 LLM 应用工具链的全貌，
为理解 Langfuse 在产业生态中的枢纽位置提供了直接证据。

## 我的笔记

Langfuse 是我观察到的开源 LLM 可观测性领域社区增长最为迅猛的项目之一。

从 GitHub 指标来看，
其 star 增长曲线、PyPI 下载量和下游项目采用度均呈现指数级上升态势。

这种增长速度在 B2B developer tools 中相当罕见。

Y Combinator W23 的背书为其早期获取北美开发者关注提供了重要助力。

但项目的长期竞争力更多来源于其工程质量和社区运营能力。

GitHub Discussions 中 3380+ 的讨论总量和 9700+ 的已关闭 issue 数，
说明项目团队对社区反馈的响应速度和处理效率都维持在较高水平。

从架构角度分析，
Langfuse 选择 monorepo + pnpm workspace + Next.js + ClickHouse 的技术栈组合，
体现了团队对现代全栈开发和高性能时序数据存储的深刻理解。

ClickHouse 作为面向列式存储的分析型数据库，
在处理大规模 span 数据的聚合查询和成本效率方面具有显著优势。

这是 Langfuse 能够以开源形态支撑大规模生产部署的关键技术决策。

相比许多竞品使用 Elasticsearch 或 PostgreSQL 作为底层存储，
ClickHouse 在 trace 数据的压缩率和分析查询性能上更具竞争力。

但也对团队的运维能力提出了更高要求，
特别是在集群管理和数据保留策略方面。

Langfuse 的 `@observe()` 装饰器设计哲学
与 Python 生态的现有模式
（如 OpenTelemetry 的 `@trace`、Sentry 的 `@capture`）保持了一致性。

这种遵循社区惯例的 API 设计显著降低了开发者的学习成本。

同时，
通过提供 OpenAI SDK 的 drop-in 替换
（`from langfuse.openai import openai`），
团队将接入成本降到了理论最低。

只需修改 import 语句即可自动捕获所有模型调用参数。

这种零侵入的设计理念，
对于希望在不改动现有业务逻辑的前提下引入可观测性的团队而言，
具有极大的吸引力。

与 Arize Phoenix 相比，
Langfuse 更聚焦于纯 LLM 工程场景（不包含传统 ML 模型监控），
产品边界更为清晰。

其 MIT 许可证也使其在企业内部分发和二次开发方面障碍更低。

但 Langfuse 的完全开源模式也面临可持续性问题：
如何在不损害开源社区利益的前提下实现商业收入的持续增长。

这是其与 Arize（采用 Elastic License 2.0 进行商业保护）
路径选择上的根本差异。

从当前趋势看，
Langfuse 选择通过 Langfuse Cloud 的托管服务实现商业化。

这一模式与 Supabase、PostHog 等开源基础设施公司的成功路径高度相似。

在生态位上，
Langfuse 与 LiteLLM（统一 LLM 网关）、LangChain（应用编排框架）
形成了互补关系而非竞争关系。

README 中展示的下游采用名单几乎涵盖了 LLM 应用开发的全谱系工具链。

这种广泛的生态嵌入使得 Langfuse 具备了网络效应护城河。

对于本综述而言，
Langfuse 的实践为
"agent 可观测性应当采用何种数据模型和集成方式"
这一问题提供了经过大规模生产验证的答案。

其 trace 中同时记录 LLM call、retrieval、embedding 和 agent action 的数据结构设计，
可以直接作为 agent 系统日志规范的参考实现。

值得一提的是，
Langfuse 项目近期增加了对 AWS SES 邮件传输的支持、
OCI Object Storage Native SDK 集成、
以及 full-text search（FTS）实现。

这些功能迭代反映了团队对企业级部署需求的快速响应。

项目还发布了多个本地化 README（中文、日语、韩语），
显示其正在积极拓展北美以外的开发者市场。

对于中文开发者社区而言，
简体中文 README 的存在显著降低了上手门槛。

这是评估其社区友好度时不应忽视的正面信号。

整体来看，
Langfuse 代表了当前开源 LLM 可观测性工具的最高工程水准之一。

其在社区增长、生态集成、产品完整度和自托管体验等维度上的综合表现，
使其成为研究和实践 agent 系统可观测性时不可忽视的参照标杆。
