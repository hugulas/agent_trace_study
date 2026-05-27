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

- [AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks](summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AI Cost Visibility 深度阅读笔记](summaries/costvisibility-note.md) (n.d., evidence: unknown) — 文章未进行传统实验，但以weather agent为例展示了以下关键数字：
**成本膨胀效应**：
- 简单天气agent（每次查询五百输入加两百输出token，GPT-4.1-mini定价，每月一万次）
- 电子表格预估：约3.60美元每月
- 生产实际：约25至40美元每月（差距约七到十一倍）
- 五工具agent上下文累积可达两千以上token
- 两成重试率导致1.2倍成本放大
- 三轮ReAct agent的成本约为基线的五到七倍
- 框架开销增加每调用两百到五百token
**效率提升**：
- 成本发
- [AI agent observability: tracing, debugging, and monitoring multi-agent systems](summaries/a-021-AI-agent-observability-tracing-debugging.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds](summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat.md) (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems](summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agent psychometrics: 智能体代码基准的任务级性能预测](summaries/taskpredict-note.md) (n.d., evidence: unknown) — > [!figure] Table 1: Experimental settings
> 建议位置：关键结果
> 放置原因：总结四种实验设置的配置细节，是理解后续所有结果表的前提
> 当前状态：占位符
### 新任务上的难度预测
在新任务设置下，论文比较了三种任务特征向量在四个基准上的 AUC-ROC：
> [!figure] Table 2: AUC-ROC on held-out tasks for each of the four benchmarks
> 建议位置：关键结果
> 放置原因：核心结果表，展示各
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
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [BEAVER: A Training-Free Hierarchical Prompt Compression Method via Structure-Aware Page Selection](summaries/beaver-note.md) (n.d., evidence: unknown) — ### 主基准性能
在 LongBench 与 ZeroSCROLLS 基准上，BEAVER 在 2,000 与 3,000 词元预算约束下整体优于 LLMLingua-2 与 LongLLMLingua。
- [C3PO：概率成本约束下的LLM级联优化](summaries/c3po-note.md) (n.d., evidence: unknown) — C3PO在三组模型级联和16个数据集上进行了系统评估，主要结果如下：
**成本效率优势**。在LLAMA级联上，C3PO在16个基准中均展现出显著优越的成本效率。达到与MPM相差不超过2%、5%和10%的准确率差距时，C3PO仅需MPM成本的不到20%。对于SVAMP和MATH-500等大型数据集，C3PO以比其他级联基线低10倍的成本获得了最高的准确率。
- [Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning](summaries/cotprune-note.md) (n.d., evidence: unknown) — ### 主实验结果
表2展示了在 DeepSeek-R1-Distill-Llama-8B 和 DeepSeek-R1-Distill-Qwen-7B 上三种剪枝策略的完整结果。
- [ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents](summaries/ctxbudget-note.md) (n.d., evidence: unknown) — ### 主实验性能
在 BrowseComp-Plus 和多目标问答基准上的主实验结果（表 1）显示，BACM-RL 在两个骨干模型上均取得最佳平均性能，且跨越架构与参数量差异（7B 与 30B），表现出广泛的适用性。
- [Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models](summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S.md) (2025, evidence: unknown) — ### 全参数微调结果
来自 LaTeX 源码 `results.tex` 的 Table 2 展示了三种基座模型在全参数微调后的性能：
**Table 2 全参数微调性能对比（Pass@1，贪心解码）**
| 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O |
|---------|---------|---------|------|--------|------|-
- Plus 69 additional linked summaries in [Index](index.md).

## Related Concepts

- [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md)
