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

- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [A Guide to AI Agent Cost Optimization With Observability — 深度阅读笔记](summaries/galileocost-note.md) (n.d., evidence: unknown) — 由于本文是实践指南而非受控实验报告，以下结果为作者基于生产观察提出的定量声明，应结合具体场景审慎采纳：
- **上下文膨胀**：五轮对话的上下文窗口可达 8k token，其中为重复历史上下文支付的费用超过新增推理成本。
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds](summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat.md) (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno.md) (n.d., evidence: unknown) — ### 人机一致性验证
在 30 条人工标注轨迹上，自动评估指标与人类评分的相关性如 Table 1 所示：
| Dimension | $r$ | $\rho$ | $\tau$ |
|:---|:---:|:---:|:---:|
| backtrack & explore | 0.39 | 0.43 | 0.36 |
| task decomposition | 0.78 | 0.86 | 0.76 |
| observation reading | 0.62 | 0.63 | 0.60 |
| self-v
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/agenttracecausal-note.md) (n.d., evidence: unknown) — 由于 AgentTrace 定位为研究框架与概念验证，论文未在标准基准上报告曲线下面积、准确率或吞吐量等定量指标。其核心结果体现在设计贡献与下游应用潜能上：
- **结构化智能体日志的开放标准**：论文声称 AgentTrace 建立了首个跨越认知、操作和上下文痕迹的模式化结构化智能体日志开放标准，将日志从工程实用工具提升为智能体安全、可复现性和问责制的核心使能层。
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/p-014-AgentTrace-A-Structured-Logging-Framewor.md) (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) (n.d., evidence: unknown) — 文章将八款平台划分为四个能力梯队：
**第一梯队（闭环型）：Future AGI Agent Command Center。**
唯一在单一运行时内同时实现追踪级成本归因、评估闭环、网关路由与五级预算的平台。
- [Beyond the Black Box: Next-Gen AI Agent Monitoring](summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [CoMem 深度阅读笔记](summaries/comem-note.md) (n.d., evidence: unknown) — Table 1 展示了 CoMem 在三种不同规模主干模型上的主要实验结果。
- [EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation](summaries/p-018-EAGER-Efficient-Failure-Management-for-M.md) (n.d., evidence: unknown) — 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide](summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 56 additional linked summaries in [Index](index.md).

## Related Concepts

- [agent-observability-landscape](concepts/agent-observability-landscape.md)
- [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md)
- [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md)
