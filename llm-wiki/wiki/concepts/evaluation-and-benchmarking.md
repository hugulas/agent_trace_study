# Evaluation and Benchmarking

## Working Definition

Organizes benchmark, white-box evaluation, monitorability, alignment auditing, and long-horizon task evaluation notes. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

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
- [[summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat|AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds]] (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
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
- [[summaries/p-025-AgentSight-System-Level-Observability-fo|AgentSight: System-Level Observability for AI Agents Using eBPF]] (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [[summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (2025, evidence: unknown) — ### 全参数微调结果
来自 LaTeX 源码 `results.tex` 的 Table 2 展示了三种基座模型在全参数微调后的性能：
**Table 2 全参数微调性能对比（Pass@1，贪心解码）**
| 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O |
|---------|---------|---------|------|--------|------|-
- [[summaries/s2-015-AI-Agent-Observability-Platform-Langfuse|Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/c-007-The-Reliability-Gap-Agent-Benchmarks-for|The Reliability Gap: Agent Benchmarks for Enterprise]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] (n.d., evidence: unknown) — 论文发现，AgentPex 能区分不同模型和领域中的行为差异，并能发现 `${\tau}^2` 结果评分没有直接暴露的规范违反。Fig.
- [[summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen|s3-006_The_Attack_and_Defense_Landscape_of_Agen]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/s2-005-目前主流的智能体可观测性和智能体评测相关的产品调研-Coze-Loop详细介绍|目前主流的智能体可观测性和智能体评测相关的产品调研]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-007-Evaluating-Chain-of-Thought-Monitorabili|评估思维链的可监控性]] (n.d., evidence: unknown) — 文章报告了几个主要观察。第一，在几乎所有研究环境中，监控思维链比只监控行为和最终输出更有效。第二，思考时间更长的模型通常更容易监控，因为更长的思维链暴露了更多中间证据。第三，在当前前沿规模下，强化学习优化没有显著降低可监控性，部分早期阶段甚至会提高可监控性。第四，小模型在较高推理强度下可能达到与大模型低推理强度相近的能力，同时更容易监控，但需要更多测试时计算。
- Plus 41 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/audit-trails-security-and-governance]]
