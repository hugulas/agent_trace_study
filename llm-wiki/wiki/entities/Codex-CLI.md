# Codex CLI

## Role in This Wiki

`Codex CLI` appears as a recurring entity in the local notes corpus. This page is intentionally lightweight: it anchors wikilinks and points to the source summaries where the entity is discussed.

## Linked Source Notes

- [Systematic debugging for AI agents: Introducing the AgentRx framework](summaries/a-003-Systematic-debugging-for-AI-agents-Intro.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Opik Claude Code Plugin: Auto-Configure Agent Observability](summaries/a-010-Announcing-the-Opik-Claude-Code-Plugin.md) (n.d., evidence: medium) — Indexed as relevant by title and metadata.
- [Advanced Configuration — Codex (Observability and telemetry)](summaries/a-013-Advanced-Configuration-Codex-Observabil.md) (n.d., evidence: high（官方一手文档，直接描述产品能力）) — Indexed as relevant by title and metadata.
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Reverse engineering Codex CLI rollout traces - DEV Community](summaries/a-015-Reverse-engineering-Codex-CLI-rollout-tr.md) (n.d., evidence: high) — Indexed as relevant by title and metadata.
- [GitHub — openai/swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration](summaries/a-019-GitHub-openaiswarm.md) (n.d., evidence: medium) — Indexed as relevant by title and metadata.
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](summaries/featurebench-note.md) (n.d., evidence: unknown) — 论文评估了7种框架与模型的组合配置。模型侧覆盖 DeepSeek-V3.2、Claude Opus 4.5 等闭源与开源前沿模型；框架侧包括 OpenHands、Claude Code 等代表性智能体脚手架。
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) (2026, evidence: unknown) — 作为一篇综述，本文的主要"结果"体现为对领域现状的系统刻画和未来方向的清晰预判：
- **记忆架构的四阶段演进**：当前系统已从单调上下文演进至自适应记忆系统，核心转变是从被动存储到主动控制策略。
- [View-oriented Conversation Compiler for Agent Trace Analysis](summaries/p-015-View-oriented-Conversation-Compiler-for.md) (2026, evidence: high) — Table 1 汇总了三种模型配置在 AppWorld 上的主要结果（来自 LaTeX 源码 `vcc_arxiv.tex`）。
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) (n.d., evidence: high) — ### 实验设置
评估覆盖十种框架配置，分为两种设置：
- **共享框架设置**：不同模型在相同 OpenClaw 框架下运行，以控制框架层面差异；
- **厂商原生设置**：使用模型供应商提供的生产级框架（Claude Code、Codex）。
- [Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation](summaries/retrievaltopo-note.md) (n.d., evidence: unknown) — - 路由精度：在 150 例测试集上，规则型路由器将误路由率从基于正则的基线 30.1%（95% 置信区间 [26.4, 34.1]）降至 8.2%（[6.1, 10.9]），绝对降低 21.9 个百分点，相对降低 73%。配对检验的统计量为 $\chi^2 = 43.6$，$p < 10^{-6}$。收益主要来自正则基线被关键词误导，而本文方法通过复杂度向量识别出实际范围有限的场景。

## Related Concepts

- [Agent Observability Landscape](concepts/agent-observability-landscape.md)
- [Trace Schema and Telemetry Standards](concepts/trace-schema-and-telemetry-standards.md)
- [Observability Products and Market Map](concepts/observability-products-and-market-map.md)
