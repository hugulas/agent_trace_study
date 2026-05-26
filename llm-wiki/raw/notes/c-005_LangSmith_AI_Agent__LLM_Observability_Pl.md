---
tags: [langsmith, langchain, llm-observability, agent-tracing, production-monitoring, smithdb]
aliases: [LangSmith: AI Agent & LLM Observability Platform]
date: 2025-06-01
url: https://smith.langchain.com
---

# LangSmith: AI Agent & LLM Observability Platform

## 核心信息

- **标题**: LangSmith: AI Agent & LLM Observability Platform
- **来源**: LangChain 官方产品页面
- **类型**: 产品文档 / 官方介绍
- **发表时间**: 2025 年（页面内容持续更新）
- **证据质量**: medium
- **相关图片**:
  - `![[../cited-materials/images/[c-005]/[c-005]-699c2eefbd7b8167be8c8f03_funnel2.png]]`
  - `![[../cited-materials/images/[c-005]/[c-005]-6995a790527adb83ca44ff63_glow.png]]`
  - `![[../cited-materials/images/[c-005]/[c-005]-6a056e362caf179dbc8ecc60_clay_logo.png]]`

## 内容摘要

LangSmith 是 LangChain 官方推出的 AI Agent 与 LLM 可观测性平台。

其核心定位是为工程团队提供对 agent 行为的完整可见性（complete visibility into agent behavior）。

平台支持通过 Python、TypeScript、Go 和 Java SDK 集成。

覆盖主流 agent 框架和 OpenTelemetry 协议。

LangSmith 的产品能力围绕四大支柱展开：Agent Tracing、Production Monitoring、自动洞察分析（Insights）、以及专用追踪数据库 SmithDB。

在 Agent Tracing 方面，LangSmith 提供逐步（step-by-step）的 agent 执行追踪。

工程团队可以精确观察 agent 在每一步做了什么决策。

快速定位影响延迟（latency）、成本（cost）和响应质量（response quality）的问题。

平台内置了对主流 agent 框架的原生追踪支持。

同时兼容 OpenTelemetry 协议。

支持多轮对话的 message threading。

这一能力对于调试复杂的 multi-turn 交互至关重要。

在 Production Monitoring 方面，LangSmith 提供实时性能视图。

团队可以及早发现问题、理解影响范围并开始分流（triage）。

监控功能包括成本追踪（cost tracking）、在线评估（online evals）。

其中 LLM-as-judge 和 code evals 是两种主要的在线评估手段。

此外还包括工具和 agent 轨迹监控（tool and agent trajectory monitoring）。

以及通过 webhook 和 PagerDuty 发送告警的能力。

自定义仪表盘可以追踪 token 使用量、延迟分布（P50、P99）、错误率、成本细目和用户反馈评分。

Insights 功能是 LangSmith 的差异化能力之一。

通过无监督主题聚类（unsupervised topic clustering）自动分析和聚类追踪数据。

检测使用模式、常见 agent 行为和故障模式。

平台提供错误分析模板（templates for error analysis）。

以及包含关键发现的执行摘要（executive summary with key findings）。

这种自动化分析对于大规模生产环境中的模式发现非常有价值。

SmithDB 是 LangSmith 专为 agent 可观测性设计的底层数据库。

Agent 追踪数据具有深度嵌套和超大载荷的特点。

单次对话可能在数十次运行和工具调用中产生数兆字节的数据。

通用数据库虽然可以存储追踪数据。

但并非为团队查询追踪数据的方式而设计。

SmithDB 针对 agent 查询模式进行了优化。

支持单条运行的随机访问、全文检索、JSON key-path 过滤和轨迹查询。

在数百万条追踪的规模下仍能保持亚秒级查询性能。

同时提供自托管选项。

可以在 VPC 内部署，确保敏感追踪数据不会离开基础设施。

部署架构由三个无状态组件组成，基于对象存储和 Postgres。

无需本地磁盘或复杂的分片机制。

在 FAQ 部分，LangSmith 澄清了多个关键问题。

首先，团队为什么需要 LLM 可观测性平台？

因为需要理解 AI 应用在生产环境中的行为。

包括 RAG 管道、agent 决策、模型性能指标（如成本和延迟）。

以及通过端到端执行追踪调试复杂故障和幻觉。

其次，LangSmith 支持哪些框架？

答案是与任何 LLM 框架兼容。

包括 OpenAI SDK、Anthropic SDK、Vercel AI SDK、LlamaIndex 和自定义实现。

不仅仅是 LangChain。

第三，LangSmith 是否支持 OpenTelemetry？

答案是肯定的。

如果团队已有基于 OTel 的可观测性基础设施，LangSmith 可以与之集成。

可以双向发送和接收追踪数据。

第四，关于数据驻留（data residency）和自托管。

LangSmith 提供托管云、自带云（BYOC）和完全自托管三种选项。

企业计划可以在 AWS、GCP 或 Azure 的 Kubernetes 集群上运行。

确保数据不会离开客户环境。

最后，关于性能影响。

LangSmith SDK 使用异步回调处理器将追踪发送至分布式采集器。

不会影响应用性能。

即使 LangSmith 发生故障，agent 也会继续正常运行。

## 关键要点

1. **LangSmith 是 LangChain 生态的旗舰可观测性产品**。
   提供从开发调试到生产监控的完整链路。
   与 LangChain 框架深度集成，但同样支持非 LangChain 应用。

2. **四大核心能力：Tracing、Monitoring、Insights、SmithDB**。
   Tracing 提供逐步执行可见性。
   Monitoring 提供实时性能视图和告警。
   Insights 通过无监督聚类自动发现模式和故障。
   SmithDB 是专为 agent 追踪设计的专用数据库。

3. **SmithDB 解决了通用数据库在 agent 追踪场景下的性能瓶颈**。
   深度嵌套的追踪数据和超大载荷对通用数据库的查询模式不友好。
   SmithDB 针对随机访问、全文检索、JSON path 过滤和轨迹查询进行了优化。
   在数百万追踪规模下保持亚秒级性能。

4. **灵活的部署选项满足企业安全合规需求**。
   托管云（数据存储在 GCP us-central-1）。
   自带云（BYOC）。
   完全自托管（VPC 内部署，三状态组件架构）。
   企业计划支持 AWS、GCP、Azure 的 Kubernetes 集群。

5. **在线评估（Online Evals）是生产监控的关键差异化功能**。
   支持 LLM-as-judge 和 code evals 两种方式。
   可以在生产流量上实时评估质量特征。
   结合自定义仪表盘和 PagerDuty/webhook 告警，形成闭环监控。

6. **OpenTelemetry 双向集成确保生态兼容性**。
   既可以将 LangSmith 的追踪数据发送到现有 OTel 基础设施。
   也可以将外部 OTel 数据导入 LangSmith。
   这降低了已有可观测性栈的企业的采纳门槛。

7. **异步非侵入式 SDK 设计保证零性能影响**。
   使用异步回调处理器发送追踪。
   即使 LangSmith 服务不可用，也不会阻塞或影响应用运行。
   这种设计对于生产环境至关重要。

8. **定价模式按追踪量 scaling，提供免费层**。
   免费层适用于开发和小规模生产。
   付费计划按追踪量计费。
   企业计划提供定制化定价和部署选项。

## 与综述的关联

LangSmith 作为 agent 可观测性领域最具影响力的商业平台之一，是综述中"商用可观测性平台对比"章节的重要案例。

它与 Langfuse、Arize Phoenix、Braintrust 等平台共同构成了当前市场的第一梯队。

本文档为综述提供了关于 LangSmith 产品架构和功能边界的权威一手信息。

在技术架构层面，SmithDB 的设计理念与综述中"agent-native 数据基础设施"的讨论高度相关。

通用时序数据库和日志系统在处理 agent 追踪数据时面临嵌套结构复杂、载荷大、查询模式特殊等挑战。

SmithDB 的出现验证了这一判断。

即 agent 可观测性需要专门的数据存储和查询引擎，而非简单复用现有基础设施。

这与 p-025（AgentSight）等研究中提出的专用追踪数据结构形成了工业实践与学术探索的呼应。

在评估方法论方面，LangSmith 的在线评估（online evals）功能，特别是 LLM-as-judge 和 code evals。

为综述中"运行时评估与离线评估的关系"提供了工业界的实践视角。

这与 p-006（Monitoring Monitorability）等论文关于监控可监控性的讨论形成了互补。

学术界关注"什么值得监控"的理论框架。

而 LangSmith 提供了"如何实施监控"的工程方案。

在标准化方面，LangSmith 对 OpenTelemetry 的双向支持。

使其成为综述讨论 OTel 生态时的重要参与者。

作为同时提供托管 SaaS 和自托管选项的平台。

LangSmith 代表了企业级 agent 可观测性的一种主流交付模式。

其数据驻留策略（data residency）和 VPC 部署能力。

为综述讨论企业采纳障碍时提供了具体案例。

此外，LangSmith 的 Insights 功能通过无监督聚类自动发现故障模式。

这与综述中"智能化故障分析"的趋势一致。

可以联系到 p-004（Willful Disobedience）等关于自动检测 agent 轨迹中异常行为的研究。

以及 p-029（AgentDiagnose）等诊断工具包。

形成"学术提出算法→工业集成到平台"的技术转移链条。

## 我的笔记

LangSmith 的产品页面透露了一个重要的行业信号：agent 可观测性正在从"开发者工具"演进为"企业基础设施"。

SmithDB 的推出尤其值得注意。

它标志着厂商开始意识到，agent 追踪数据的管理需要专门的基础设施，而非简单地复用现有日志或 APM 后端。

这种专用化趋势与数据库领域中"从通用 SQL 到专用 NoSQL/NewSQL"的演进非常相似。

从架构角度看，SmithDB 的三状态组件设计（stateless components on object storage and Postgres）是一个务实的选择。

它既保证了水平扩展性，又避免了复杂的分片管理。

不过，object storage + Postgres 的组合在超大规模场景下是否会遇到瓶颈，仍然是一个开放问题。

特别是当单条 trace 达到 MB 级别、日增量达到 TB 级别时，查询性能如何保持，需要更多实际数据来验证。

LangSmith 对 OTel 的双向支持是一个明智的策略。

对于已有成熟可观测性栈的企业（如使用 Datadog、Honeycomb 或自托管 Jaeger），这种兼容性大大降低了采纳门槛。

但它也带来一个有趣的问题：当 LangSmith 既作为 OTel 数据的消费者又作为生产者时，如何避免循环依赖和数据重复？

这在多后端并存的复杂架构中需要仔细设计。

Insights 的无监督聚类功能听起来很有吸引力。

但我对其在大规模异构工作流中的实际效果持谨慎乐观态度。

不同 agent 应用的使用模式差异巨大。

客服机器人、代码生成 agent、研究助手的行为特征几乎完全不同。

通用的无监督聚类是否能在不加领域定制的情况下产生有意义的洞察，取决于聚类算法对语义的理解深度。

如果仅仅是基于文本相似度，可能会产生大量 noise。

关于定价，LangSmith 的"按追踪量计费"模式在行业中是主流做法。

但对于高频、长轮次的 agent 应用（如自动客服），追踪成本可能迅速累积。

这与综述中 s3-014（LLM Agent Cost Attribution）讨论的成本归因问题形成了实际关联。

企业在评估可观测性平台时，不仅要考虑功能覆盖度，还要精确建模追踪量增长曲线和对应的成本曲线。

最后，LangSmith 强调"异步 SDK、零性能影响"的设计理念。

这在生产环境中是必要但非充分的条件。

同样重要的是 SDK 自身的可靠性、回溯缓冲机制、以及在网络分区情况下的优雅降级。

这些细节在产品页面中没有深入展开。

但对于大规模部署而言，其重要性不亚于功能特性本身。
