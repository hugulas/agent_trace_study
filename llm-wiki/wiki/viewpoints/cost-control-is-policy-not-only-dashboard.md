# 成本控制不是只做 dashboard

## 观点

成本可见性只能说明钱花在哪里，真正的成本控制还需要预算策略、模型路由、缓存复用、上下文裁剪和超预算降级等运行时政策。

## 为什么成立

- [Amazon Bedrock AgentCore Production Operations Guide - Observability, Cost Optimization, and Disaster Recovery](summaries/s1-007-Amazon-Bedrock-AgentCore-Production-Oper.md) — 这篇指南最突出的价值在于它的「实战导向」写作风格。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化](summaries/s2-022-Helicone-LLM-Observability-Platform-Lea.md) — Helicone 的评测让我对"Proxy 模式 versus SDK 插桩模式"的架构之争 有了更具体、更工程化的理解。
- [使用 Datadog LLM Observability 监控、排查与优化 AI Agent](summaries/s2-006-Monitor-troubleshoot-and-improve-AI-agen.md) — Datadog 这篇博客的技术价值在于它非常具体地描述了多 Agent 可观测性的痛点，并给出了清晰的产品化解决方案。与许多停留在概念层面的厂商文章不同，本文深入到了可视化设计的细节——为什么火焰图不行、为什么 Span 列表不行、以及基于图的视图如何解决这些问题。这种从第一性原理出发的分析方式，使文章具有很高的技术可信度，即使作为非学术来源也值得信赖。
- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [Helicone：开源 LLM 可观测性与 AI 网关一体化平台](summaries/s2-023-Helicone-Open-source-LLM-observability-f.md) — Helicone 的产品档案让我对"AI Gateway + Observability"的融合趋势有了更清晰的认知。
- [OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows](summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing.md) — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。

## 工程含义

- trace schema 应记录预算决策和降级动作。
- 告警之后必须能定位到可执行的优化旋钮。
- 平台应把成本策略作为生产 guardrail，而不是财务报表。

## 反例与边界

这个观点不是说相邻层不重要，而是说单独依赖该层会留下诊断或治理缺口。 对于低风险 demo，轻量日志可能足够；对于生产智能体、长程任务、多智能体协作或合规场景，必须把 trace、评测、审计和成本信号组织成可追溯证据。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
- [失败归因](terms/failure-attribution.md)
- [轨迹 Schema](terms/trace-schema.md)
