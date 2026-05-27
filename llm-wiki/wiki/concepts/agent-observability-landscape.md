# Agent Observability Landscape

## Working Definition

Frames agent observability as traces, evaluations, governance, and production operations rather than ordinary LLM logging. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

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
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AgentPro: Enhancing LLM Agents with Automated Process Supervision](summaries/p-026-AgentPro-Enhancing-LLM-Agents-with-Autom.md) (n.d., evidence: unknown) — ### 主实验结果
在 LLaMA-3.1-8B-Instruct 上的主实验表明，AgentPro 在四个数据集上均稳定超越所有基线：
- **FEVER**：相比最优基线 ExpeL（51.87%）提升 3.59%，达到 55.46%（按文中 Fig.
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/agenttracecausal-note.md) (n.d., evidence: unknown) — 由于 AgentTrace 定位为研究框架与概念验证，论文未在标准基准上报告曲线下面积、准确率或吞吐量等定量指标。其核心结果体现在设计贡献与下游应用潜能上：
- **结构化智能体日志的开放标准**：论文声称 AgentTrace 建立了首个跨越认知、操作和上下文痕迹的模式化结构化智能体日志开放标准，将日志从工程实用工具提升为智能体安全、可复现性和问责制的核心使能层。
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/p-014-AgentTrace-A-Structured-Logging-Framewor.md) (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) (n.d., evidence: unknown) — 文章将八款平台划分为四个能力梯队：
**第一梯队（闭环型）：Future AGI Agent Command Center。**
唯一在单一运行时内同时实现追踪级成本归因、评估闭环、网关路由与五级预算的平台。
- [Beyond the Black Box: Next-Gen AI Agent Monitoring](summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 84 additional linked summaries in [Index](index.md).

## Related Concepts

- [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md)
- [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md)
- [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md)
