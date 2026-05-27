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

- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
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
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) (n.d., evidence: unknown) — 四项实验的核心结果如下：
**实验一：迭代工作流失控预防**
| 指标 | UNCONTRACTED | CONTRACTED | 变化 | p 值 |
|------|-------------|-----------|------|------|
| 令牌消耗 | 34,606 | 3,461 | -90% | 0.0007*** |
| 方差 | 5.29B | 10.1M | 525x 降低 | — |
| 迭代次数 | 3.00 | 1.71 | -43% | <0.0001*** |
| 大模型调用次数
- [AgentDropout 深度阅读笔记](summaries/agentdropout-note.md) (n.d., evidence: unknown) — ### 性能对比
AgentDropout在全部六个基准和三种模型规模上均优于单智能体CoT和多智能体基线。以Llama3-8B为例：
| 方法 | MMLU | GSM8K | AQuA | MultiArith | SVAMP | HumanEval | 平均 |
|------|------|-------|------|------------|-------|-----------|------|
| Vanilla | 53.59 | 70.23 | 41.67 | 91.11 | 75.00 | 53
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/agenttracecausal-note.md) (n.d., evidence: unknown) — 由于 AgentTrace 定位为研究框架与概念验证，论文未在标准基准上报告曲线下面积、准确率或吞吐量等定量指标。其核心结果体现在设计贡献与下游应用潜能上：
- **结构化智能体日志的开放标准**：论文声称 AgentTrace 建立了首个跨越认知、操作和上下文痕迹的模式化结构化智能体日志开放标准，将日志从工程实用工具提升为智能体安全、可复现性和问责制的核心使能层。
- [AgentTrace: A Structured Logging Framework for Agent System Observability](summaries/p-014-AgentTrace-A-Structured-Logging-Framewor.md) (n.d., evidence: unknown) — AgentTrace 建立了首个面向智能体结构化日志的开放标准，覆盖认知、操作与上下文三类痕迹。
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [BAMAS: Structuring Budget-Aware Multi-Agent Systems](summaries/bamas-note.md) (n.d., evidence: unknown) — **成本-性能权衡**
表一和表二报告了 BAMAS 与基线方法在三个数据集上的平均成本和准确率。BAMAS 在所有数据集上均展现出优于现有方法的成本-性能权衡。
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) (n.d., evidence: unknown) — 文章将八款平台划分为四个能力梯队：
**第一梯队（闭环型）：Future AGI Agent Command Center。**
唯一在单一运行时内同时实现追踪级成本归因、评估闭环、网关路由与五级预算的平台。
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Can Dependencies Induced by LLM-Agent Workflows Be Trusted?](summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo.md) (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- Plus 79 additional linked summaries in [Index](index.md).

## Related Concepts

- [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md)
