# Observability Products and Market Map

## Working Definition

Maps product-level agent observability tools such as LangSmith, Langfuse, Arize Phoenix, Braintrust, AgentOps, Datadog, Elastic, New Relic, Splunk, Helicone, and Opik. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat|AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds]] (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [[summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno|AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories]] (n.d., evidence: unknown) — ### 人机一致性验证
在 30 条人工标注轨迹上，自动评估指标与人类评分的相关性如 Table 1 所示：
| Dimension | $r$ | $\rho$ | $\tau$ |
|:---|:---:|:---:|:---:|
| backtrack & explore | 0.39 | 0.43 | 0.36 |
| task decomposition | 0.78 | 0.86 | 0.76 |
| observation reading | 0.62 | 0.63 | 0.60 |
| self-v
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-025-AgentSight-System-Level-Observability-fo|AgentSight: System-Level Observability for AI Agents Using eBPF]] (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-018-EAGER-Efficient-Failure-Management-for-M|EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation]] (n.d., evidence: unknown) — 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi|Google boosts Vertex AI Agent Builder with new observability and deployment tools]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-022-Helicone-LLM-Observability-Platform-Lea|Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-023-Helicone-Open-source-LLM-observability-f|Helicone：开源 LLM 可观测性与 AI 网关一体化平台]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-015-AI-Agent-Observability-Platform-Langfuse|Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 48 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/agent-observability-landscape]]
- [[concepts/trace-schema-and-telemetry-standards]]
- [[concepts/runtime-instrumentation-and-otel]]
