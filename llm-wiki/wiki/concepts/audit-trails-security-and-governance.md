# Audit Trails, Security, and Governance

## Working Definition

Synthesizes tamper-evident audit trails, guardrails, safety violations, agent vulnerabilities, and governance evidence. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

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
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [[summaries/p-025-AgentSight-System-Level-Observability-fo|AgentSight: System-Level Observability for AI Agents Using eBPF]] (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen|s3-006_The_Attack_and_Defense_Landscape_of_Agen]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-001-什么是AgentLoop-云监控CMS-阿里云文档|阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-008-AI-NativeBench-An-Open-Source-White-Box|AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems]] (2026, evidence: high) — Indexed as relevant by title and metadata.
- [[summaries/p-017-Auditing-Agent-Harness-Safety|Auditing Agent Harness Safety]] (n.d., evidence: high) — ### 实验设置
评估覆盖十种框架配置，分为两种设置：
- **共享框架设置**：不同模型在相同 OpenClaw 框架下运行，以控制框架层面差异；
- **厂商原生设置**：使用模型供应商提供的生产级框架（Claude Code、Codex）。
- [[summaries/p-013-Detecting-Safety-Violations-Across-Many|Detecting Safety Violations Across Many Agent Traces]] (2026, evidence: high) — ### 分布式滥用检测
![Fig.
- [[summaries/s2-014-langfuselangfuse-GitHub|Langfuse: 开源 LLM 工程平台]] (n.d., evidence: high) — Indexed as relevant by title and metadata.
- [[summaries/a-007-Monitoring-Claude-Code-Docs|Monitoring - Claude Code Docs]] (n.d., evidence: high) — Indexed as relevant by title and metadata.
- [[summaries/a-020-Multi-Agent-Portfolio-Collaboration-with|Multi-Agent Portfolio Collaboration with OpenAI Agents SDK]] (n.d., evidence: high) — Indexed as relevant by title and metadata.
- Plus 24 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/evaluation-and-benchmarking]]
