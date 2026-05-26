# Agent Frameworks and Coding Agents

## Working Definition

Connects traces and observability to concrete agent frameworks, coding agents, Claude Code, Codex, Swarm, AgentRx, and workflow systems. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [[summaries/p-025-AgentSight-System-Level-Observability-fo|AgentSight: System-Level Observability for AI Agents Using eBPF]] (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-011-Agentic-Harness-Engineering-Observabilit|Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses]] (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo|Can Dependencies Induced by LLM-Agent Workflows Be Trusted?]] (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- [[summaries/p-018-EAGER-Efficient-Failure-Management-for-M|EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation]] (n.d., evidence: unknown) — 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- [[summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc|Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering]] (2026, evidence: unknown) — 作为一篇综述，本文的主要"结果"体现为对领域现状的系统刻画和未来方向的清晰预判：
- **记忆架构的四阶段演进**：当前系统已从单调上下文演进至自适应记忆系统，核心转变是从被动存储到主动控制策略。
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-007-The-Reliability-Gap-Agent-Benchmarks-for|The Reliability Gap: Agent Benchmarks for Enterprise]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] (n.d., evidence: unknown) — 论文发现，AgentPex 能区分不同模型和领域中的行为差异，并能发现 `${\tau}^2` 结果评分没有直接暴露的规范违反。Fig.
- [[summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen|s3-006_The_Attack_and_Defense_Landscape_of_Agen]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-007-Evaluating-Chain-of-Thought-Monitorabili|评估思维链的可监控性]] (n.d., evidence: unknown) — 文章报告了几个主要观察。第一，在几乎所有研究环境中，监控思维链比只监控行为和最终输出更有效。第二，思考时间更长的模型通常更容易监控，因为更长的思维链暴露了更多中间证据。第三，在当前前沿规模下，强化学习优化没有显著降低可监控性，部分早期阶段甚至会提高可监控性。第四，小模型在较高推理强度下可能达到与大模型低推理强度相近的能力，同时更容易监控，但需要更多测试时计算。
- [[summaries/p-017-Auditing-Agent-Harness-Safety|Auditing Agent Harness Safety]] (n.d., evidence: high) — ### 实验设置
评估覆盖十种框架配置，分为两种设置：
- **共享框架设置**：不同模型在相同 OpenClaw 框架下运行，以控制框架层面差异；
- **厂商原生设置**：使用模型供应商提供的生产级框架（Claude Code、Codex）。
- [[summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability|GenAIOps on AWS: 端到端可观测性栈]] (n.d., evidence: high) — Indexed as relevant by title and metadata.
- Plus 29 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/agent-observability-landscape]]
- [[concepts/trace-schema-and-telemetry-standards]]
- [[concepts/runtime-instrumentation-and-otel]]
