# Harness

## 定义

Harness 是模型外部可编辑的执行表面，包括系统提示、工具描述、工具实现、中间件、技能、子智能体配置和长期记忆。它决定模型如何使用环境。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 失败模式能否映射到具体 harness 组件？
- 变更是否可回滚、可归因、可证伪？
- 演化出的 harness 是否能跨模型迁移？

## 证据入口

- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) — AHE 通过三大可观测性支柱，在固定基座模型的条件下将代码智能体的 harness 转化为可自主演化的外表面。
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](summaries/p-010-Online-Adaptation-for-Self-Improving-Fou.md) — 本文提出 Continual Harness，一个无需环境重置、通过在线上下文学习持续精修自身脚手架的具身智能体框架，并进一步将 frontier model 的 harness 精修能力蒸馏给开源模型，实现模型权重与 harness 状态的协同进化。
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) — 本文以"外部化"为核心视角，将 LLM 智能体的记忆、技能、协议与 Harness 工程统一为同一套认知负担迁移框架，指出可靠智能体的关键不仅在于更强的模型，而在于更好的外部认知基础设施。
- [Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks](summaries/p-024-Lifting-Traces-to-Logic-Programmatic-Ski.md) — NSI 将 LLM 智能体的交互轨迹提升为基于一阶逻辑的程序化技能，通过显式控制流与动态变量绑定实现少样本泛化，并借助运行时反思规划持续自我演进，在具身、网页与游戏任务上显著压缩规划 horizon。
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) — HarnessAudit 首次将智能体安全评估的单元从最终输出转移到完整执行轨迹，提出三层审计框架和大规模真实基准，系统揭示了当前执行框架在边界合规、执行保真与扰动稳定方面的严重缺陷。
- [RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?](summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden.md) — 这篇 RFC 的价值不仅在于提出了 AutoGen 的合规增强方案，更在于它揭示了多智能体系统从"功能可用"走向"生产可信"时必须跨越的治理鸿沟。当前大多数可观测性方案（包括 OpenTelemetry、LangSmith、Datadog LLM Observability 等）擅长回答系统行为的"是什么"和"什么时候"，但在"是否被允许"这一策略维度上缺乏密码学级别的证明能力。日志可以告诉你某条 API 请求在 14:32 被发出，却无法证明该请求在发出前已经通过了有效的策略审查；传统数据库的写入权限可以被拥有管理员凭证的人员事后修改，而 tamper
- [Opik Claude Code Plugin: Auto-Configure Agent Observability](summaries/a-010-Announcing-the-Opik-Claude-Code-Plugin.md) — Comet 团队这篇博客的含金量在于其"自食其果"的诚意。
- [阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台](summaries/s2-001-什么是AgentLoop-云监控CMS-阿里云文档.md) — AgentLoop 的文档给我最深刻的印象是：它将"可观测性"的定义从 "看见发生了什么"推进到了"用看见的东西驱动系统进化"。这不是简单的 功能叠加，而是产品哲学层面的跃迁。传统的 APM（Application Performance Monitoring）关注的是系统健康度——CPU 是否过高、内存是否泄漏、请求是否 超时；而 AgentLoop 关注的是 Agent 的"成长度"——它是否在不断变得更好、 更稳定、更经济、更符合用户预期。这种视角转换对于整个可观测性领域都具有 启发意义，也预示着可观测性产品正在从"运维工具"向"效果优化平台"演进
- [Mind the Metrics: Patterns for Telemetry-Aware In-IDE AI Application Development using Model Context Protocol (MCP)](summaries/s3-001-Mind-the-Metrics-Patterns-for-Telemetry.md) — 这篇预印本的独特价值在于它将多个正在发生的趋势——MCP 协议的普及、IDE 的 AI 化、Prompt 工程的工业化、可观测性的前移——编织成一个连贯的范式叙事。AIDE 概念虽然尚处早期，但它精准地捕捉到了下一代开发环境的核心特征：不再区分 "写代码" 和 "调模型"，而是将两者统一在同一个遥测驱动的反馈循环中。
- [Monitoring - Claude Code Docs](summaries/a-007-Monitoring-Claude-Code-Docs.md) — Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
