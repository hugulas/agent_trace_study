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

- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks](summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds](summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat.md) (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) (n.d., evidence: unknown) — 四项实验的核心结果如下：
**实验一：迭代工作流失控预防**
| 指标 | UNCONTRACTED | CONTRACTED | 变化 | p 值 |
|------|-------------|-----------|------|------|
| 令牌消耗 | 34,606 | 3,461 | -90% | 0.0007*** |
| 方差 | 5.29B | 10.1M | 525x 降低 | — |
| 迭代次数 | 3.00 | 1.71 | -43% | <0.0001*** |
| 大模型调用次数
- [AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno.md) (n.d., evidence: unknown) — ### 人机一致性验证
在 30 条人工标注轨迹上，自动评估指标与人类评分的相关性如 Table 1 所示：
| Dimension | $r$ | $\rho$ | $\tau$ |
|:---|:---:|:---:|:---:|
| backtrack & explore | 0.39 | 0.43 | 0.36 |
| task decomposition | 0.78 | 0.86 | 0.76 |
| observation reading | 0.62 | 0.63 | 0.60 |
| self-v
- [AgentDropout 深度阅读笔记](summaries/agentdropout-note.md) (n.d., evidence: unknown) — ### 性能对比
AgentDropout在全部六个基准和三种模型规模上均优于单智能体CoT和多智能体基线。以Llama3-8B为例：
| 方法 | MMLU | GSM8K | AQuA | MultiArith | SVAMP | HumanEval | 平均 |
|------|------|-------|------|------------|-------|-----------|------|
| Vanilla | 53.59 | 70.23 | 41.67 | 91.11 | 75.00 | 53
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AgentPrune：面向大语言模型多智能体系统的经济通信管道](summaries/agentprune-note.md) (n.d., evidence: unknown) — 在 gpt-4 五智能体设置下，AgentPrune 与各类基线的对比如下：
- **与 SOTA 拓扑的成本对比**：AgentPrune 以约 5.6 美元的成本达到与最先进拓扑相当的结果，而后者需要 43.7 美元。
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [BAMAS: Structuring Budget-Aware Multi-Agent Systems](summaries/bamas-note.md) (n.d., evidence: unknown) — **成本-性能权衡**
表一和表二报告了 BAMAS 与基线方法在三个数据集上的平均成本和准确率。BAMAS 在所有数据集上均展现出优于现有方法的成本-性能权衡。
- [Beyond the Black Box: Next-Gen AI Agent Monitoring](summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Can Dependencies Induced by LLM-Agent Workflows Be Trusted?](summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo.md) (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging.md) (2025, evidence: unknown) — ### 故障翻转实验结果
来自 LaTeX 源码 `ada_arXiv_v2.tex` 中 Table 2 的数据：
| 数据集 | 干预试炼数 | 试炼成功率 | 进展增益 |
|--------|-----------|-----------|---------|
| WW-AB | 72 | 17.6% | +0% |
| WW-GAIA | 99 | 17.6% | +8.8% |
| GAIA-Level-1 | 63 | 27.5% | +15.7% |
| GSMPlus | 198 | 49.0% 
- Plus 54 additional linked summaries in [Index](index.md).

## Related Concepts

- [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
