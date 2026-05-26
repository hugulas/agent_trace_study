# Runtime Instrumentation and OpenTelemetry

## Working Definition

Covers implementation patterns for instrumenting agents, MCP servers, tool calls, model calls, and distributed workflows. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S|AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat|AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds]] (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo|Can Dependencies Induced by LLM-Agent Workflows Be Trusted?]] (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- [[summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (2025, evidence: unknown) — ### 全参数微调结果
来自 LaTeX 源码 `results.tex` 的 Table 2 展示了三种基座模型在全参数微调后的性能：
**Table 2 全参数微调性能对比（Pass@1，贪心解码）**
| 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O |
|---------|---------|---------|------|--------|------|-
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc|Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering]] (2026, evidence: unknown) — 作为一篇综述，本文的主要"结果"体现为对领域现状的系统刻画和未来方向的清晰预判：
- **记忆架构的四阶段演进**：当前系统已从单调上下文演进至自适应记忆系统，核心转变是从被动存储到主动控制策略。
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 65 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/trace-schema-and-telemetry-standards]]
