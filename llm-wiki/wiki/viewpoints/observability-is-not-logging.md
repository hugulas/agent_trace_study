# 智能体可观测性不是日志收集

## 观点

单纯存下消息和工具调用并不能回答为什么失败；可观测性必须把轨迹转化为可诊断、可评测、可审计的证据。

## 为什么成立

- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 通过零侵入运行时插桩与三层面统一 Schema，把 LLM 智能体的操作执行、认知推理与环境交互转化为结构化、可内省且与 OpenTelemetry 兼容的日志流，为智能体安全、问责与评估提供了基础设施级的可观测性支撑。
- [[summaries/c-011-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 的最大贡献在于将智能体可观测性问题从传统的"事后调试工具" 提升到了"运行时安全基础设施"的战略高度。
- [[summaries/s2-003-Appbuilder-Trace跟踪功能基本用法-百度千帆文档|千帆AppBuilder Trace跟踪功能基本用法]] — 千帆AppBuilder的Trace功能设计走的是典型的"轻量SDK插桩 + 借力成熟开源可视化"路线。
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] — 这篇文章的价值在于它清晰地界定了"agent 可观测性"的问题边界，避免了业界将 LLM 可观测性工具简单套用到多智能体系统的常见误区。作者用"研究-写作-审阅"三 agent 流水线的具象案例，展示了传统工具在跨 agent 归因上的结构性失明，这种叙事方式对于向技术团队传达 agent 可观测性的必要性非常有效。相比学术论文的抽象定义，这种来自产业界一线的技术指南更容易被工程团队理解和接受。
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] — AgentRx 博客的价值不仅在于技术本身，更在于它清晰地展示了一个从学术研究到开源工具的完整叙事。
- [[summaries/a-007-Monitoring-Claude-Code-Docs|Monitoring - Claude Code Docs]] — Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] — Google 将 Cloud Trace 与 ADK 深度集成的策略非常清晰： 本地用 Web UI 做开发调试，云端用 Cloud Trace 做生产观测， 两者形成完整的开发生命周期闭环。
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] — AgentRx 是一个面向智能体执行轨迹的失败诊断框架，核心目标是在长轨迹中定位第一个关键失败步骤，并用约束违反证据解释失败类别。
- [[summaries/a-015-Reverse-engineering-Codex-CLI-rollout-tr|Reverse engineering Codex CLI rollout traces - DEV Community]] — 这篇技术博客的最大价值在于它提供了一个“从假设到验证”的完整案例研究。作者没有停留在理论分析或文档阅读，而是通过构建 proxy、生成真实数据、对比源码预期与实际格式，最终产出可工作的开源解析器。这种“逆向工程”方法论对任何试图解析闭源或半开源 agent 工具的开发者都具有高度借鉴意义。

## 工程含义

- 日志平台需要上接诊断器、评测器和审计器。
- 字段设计要从问题反推，而不是只记录容易拿到的数据。
- 轨迹质量比轨迹体量更重要。

## 反例与边界

这个观点不是说相邻层不重要，而是说单独依赖该层会留下诊断或治理缺口。 对于低风险 demo，轻量日志可能足够；对于生产智能体、长程任务、多智能体协作或合规场景，必须把 trace、评测、审计和成本信号组织成可追溯证据。

## 相关词条

- [[terms/agent-trace|智能体轨迹]]
- [[terms/failure-attribution|失败归因]]
- [[terms/trace-schema|轨迹 Schema]]
