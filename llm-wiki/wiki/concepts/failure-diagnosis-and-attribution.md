# Failure Diagnosis and Attribution

## Working Definition

Collects work on localizing failures across agent steps, tools, dependencies, multi-agent coordination, and harnesses. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

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
- [[summaries/p-011-Agentic-Harness-Engineering-Observabilit|Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses]] (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo|Can Dependencies Induced by LLM-Agent Workflows Be Trusted?]] (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- [[summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging|DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems]] (2025, evidence: unknown) — ### 故障翻转实验结果
来自 LaTeX 源码 `ada_arXiv_v2.tex` 中 Table 2 的数据：
| 数据集 | 干预试炼数 | 试炼成功率 | 进展增益 |
|--------|-----------|-----------|---------|
| WW-AB | 72 | 17.6% | +0% |
| WW-GAIA | 99 | 17.6% | +8.8% |
| GAIA-Level-1 | 63 | 27.5% | +15.7% |
| GSMPlus | 198 | 49.0% 
- [[summaries/p-018-EAGER-Efficient-Failure-Management-for-M|EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation]] (n.d., evidence: unknown) — 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- [[summaries/p-023-EvoCF-Multi-Agent-Collaboration-via-Agen|EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning]] (n.d., evidence: unknown) — ### 与基线方法的对比
在双智能体 MAP-THOR 场景下，EvoCF 在所有评估指标上均取得一致且显著的提升。
- [[summaries/s1-009-Operating-agentic-AI-with-Amazon-Bedrock|Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 39 additional linked summaries in [[wiki/index|Index]].

## Related Concepts

- [[concepts/cost-token-and-resource-attribution]]
