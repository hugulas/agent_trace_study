# Langfuse

## Role in This Wiki

`Langfuse` appears as a recurring entity in the local notes corpus. This page is intentionally lightweight: it anchors wikilinks and points to the source summaries where the entity is discussed.

## Linked Source Notes

- [Advanced Configuration — Codex (Observability and telemetry)](summaries/a-013-Advanced-Configuration-Codex-Observabil.md) (n.d., evidence: high（官方一手文档，直接描述产品能力）) — Indexed as relevant by title and metadata.
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Agent Observability: Tracing, Debugging, and the OpenTelemetry Standard](summaries/c-001-AI-Agent-Observability-Tracing-Debugging.md) (n.d., evidence: medium) — Indexed as relevant by title and metadata.
- [Observability for Agentic Systems: What to Log, How to Redact, How to Debug](summaries/c-002-Observability-for-Agentic-Systems-What-t.md) (n.d., evidence: medium) — Indexed as relevant by title and metadata.
- [LangSmith: AI Agent & LLM Observability Platform](summaries/c-005-LangSmith-AI-Agent-LLM-Observability-Pl.md) (n.d., evidence: medium) — Indexed as relevant by title and metadata.
- [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](summaries/c-006-MASPrism-Lightweight-Failure-Attribution.md) (2026, evidence: medium) — Indexed as relevant by title and metadata.
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [claude-devtools: Open-Source DevTools for Claude Code](summaries/claudedevtools-note.md) (n.d., evidence: unknown) — 作为开源工具项目，claude-devtools 不提供传统学术论文中的基准测试或实验对比。其结果体现在功能完整性和架构设计决策上：
- **七维归因覆盖**: 工具实现了对 Claude Code 上下文窗口的完整分类归因，涵盖从全局配置到用户输入的全部七个类别，填补了原生三段进度条的信息空白。
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/cloudzerocost-note.md) (n.d., evidence: unknown) — 文章的核心“结果”体现为行业调研统计与成本爆炸案例，而非受控实验数据：
- **成本方差可达 50 倍**。一个原本单次大语言模型调用成本为 0.03 美元的功能，在由智能体处理后可能达到 2.40 美元/请求，最佳与最差情况之间的方差可达 50 倍。
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) (n.d., evidence: unknown) — 文章将八款平台划分为四个能力梯队：
**第一梯队（闭环型）：Future AGI Agent Command Center。**
唯一在单一运行时内同时实现追踪级成本归因、评估闭环、网关路由与五级预算的平台。
- [bq-agent-app：基于 Google ADK 与 BigQuery 的多智能体数据分析系统](summaries/s1-003-bq-agent-app-Observability-with-Agent-En.md) (n.d., evidence: medium（开源代码仓库，README 与配置文档详尽，但未经同行评审）) — Indexed as relevant by title and metadata.

## Related Concepts

- [Agent Observability Landscape](concepts/agent-observability-landscape.md)
- [Trace Schema and Telemetry Standards](concepts/trace-schema-and-telemetry-standards.md)
- [Observability Products and Market Map](concepts/observability-products-and-market-map.md)
