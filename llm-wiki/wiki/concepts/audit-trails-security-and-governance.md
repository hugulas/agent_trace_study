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

- [AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks](summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) (n.d., evidence: unknown) — 四项实验的核心结果如下：
**实验一：迭代工作流失控预防**
| 指标 | UNCONTRACTED | CONTRACTED | 变化 | p 值 |
|------|-------------|-----------|------|------|
| 令牌消耗 | 34,606 | 3,461 | -90% | 0.0007*** |
| 方差 | 5.29B | 10.1M | 525x 降低 | — |
| 迭代次数 | 3.00 | 1.71 | -43% | <0.0001*** |
| 大模型调用次数
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AgentPrune：面向大语言模型多智能体系统的经济通信管道](summaries/agentprune-note.md) (n.d., evidence: unknown) — 在 gpt-4 五智能体设置下，AgentPrune 与各类基线的对比如下：
- **与 SOTA 拓扑的成本对比**：AgentPrune 以约 5.6 美元的成本达到与最先进拓扑相当的结果，而后者需要 43.7 美元。
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Essential Framework for AI Agent Guardrails](summaries/c-017-Essential-Framework-for-AI-Agent-Guardra.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Systematic debugging for AI agents: Introducing the AgentRx framework](summaries/a-003-Systematic-debugging-for-AI-agents-Intro.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Token Economics for LLM Agents 深度阅读笔记](summaries/s3-011-note.md) (n.d., evidence: unknown) — 由于本文是综述性质，"结果"主要表现为对已有技术方案的系统性归类与经济映射，而非新实验数据。以下是论文梳理出的核心发现：
1.
- [What Is AI Agent Observability? Why Cost Is What You're Missing](summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [s3-006_The_Attack_and_Defense_Landscape_of_Agen](summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台](summaries/s2-001-什么是AgentLoop-云监控CMS-阿里云文档.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems](summaries/c-008-AI-NativeBench-An-Open-Source-White-Box.md) (2026, evidence: high) — Indexed as relevant by title and metadata.
- [Auditing Agent Harness Safety](summaries/p-017-Auditing-Agent-Harness-Safety.md) (n.d., evidence: high) — ### 实验设置
评估覆盖十种框架配置，分为两种设置：
- **共享框架设置**：不同模型在相同 OpenClaw 框架下运行，以控制框架层面差异；
- **厂商原生设置**：使用模型供应商提供的生产级框架（Claude Code、Codex）。
- [Detecting Safety Violations Across Many Agent Traces](summaries/p-013-Detecting-Safety-Violations-Across-Many.md) (2026, evidence: high) — ### 分布式滥用检测
![Fig.
- Plus 27 additional linked summaries in [Index](index.md).

## Related Concepts

- [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md)
