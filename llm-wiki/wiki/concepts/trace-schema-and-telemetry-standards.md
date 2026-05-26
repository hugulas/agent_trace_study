# Trace Schema and Telemetry Standards

## Working Definition

Compares structured agent trace schemas, OpenTelemetry alignment, OpenInference, Hermes-style trajectories, and audit-trail formats. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S|AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno|AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories]] (n.d., evidence: unknown) — ### 人机一致性验证
在 30 条人工标注轨迹上，自动评估指标与人类评分的相关性如 Table 1 所示：
| Dimension | $r$ | $\rho$ | $\tau$ |
|:---|:---:|:---:|:---:|
| backtrack & explore | 0.39 | 0.43 | 0.36 |
| task decomposition | 0.78 | 0.86 | 0.76 |
| observation reading | 0.62 | 0.63 | 0.60 |
| self-v
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-028-FLARE-Faithful-Logic-Aided-Reasoning-and|FLARE: Faithful Logic-Aided Reasoning and Exploration]] (n.d., evidence: unknown) — **Table 1** 各模型在不同数据集上的准确率（%）。来自 LaTeX 源码 `results.tex`。
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi|Google boosts Vertex AI Agent Builder with new observability and deployment tools]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-023-Helicone-Open-source-LLM-observability-f|Helicone：开源 LLM 可观测性与 AI 网关一体化平台]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-015-AI-Agent-Observability-Platform-Langfuse|Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 54 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/runtime-instrumentation-and-otel]]
