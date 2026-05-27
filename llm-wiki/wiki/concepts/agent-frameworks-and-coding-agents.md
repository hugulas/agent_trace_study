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
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) (n.d., evidence: unknown) — 四项实验的核心结果如下：
**实验一：迭代工作流失控预防**
| 指标 | UNCONTRACTED | CONTRACTED | 变化 | p 值 |
|------|-------------|-----------|------|------|
| 令牌消耗 | 34,606 | 3,461 | -90% | 0.0007*** |
| 方差 | 5.29B | 10.1M | 525x 降低 | — |
| 迭代次数 | 3.00 | 1.71 | -43% | <0.0001*** |
| 大模型调用次数
- [Agent psychometrics: 智能体代码基准的任务级性能预测](summaries/taskpredict-note.md) (n.d., evidence: unknown) — > [!figure] Table 1: Experimental settings
> 建议位置：关键结果
> 放置原因：总结四种实验设置的配置细节，是理解后续所有结果表的前提
> 当前状态：占位符
### 新任务上的难度预测
在新任务设置下，论文比较了三种任务特征向量在四个基准上的 AUC-ROC：
> [!figure] Table 2: AUC-ROC on held-out tasks for each of the four benchmarks
> 建议位置：关键结果
> 放置原因：核心结果表，展示各
- [AgentPrune：面向大语言模型多智能体系统的经济通信管道](summaries/agentprune-note.md) (n.d., evidence: unknown) — 在 gpt-4 五智能体设置下，AgentPrune 与各类基线的对比如下：
- **与 SOTA 拓扑的成本对比**：AgentPrune 以约 5.6 美元的成本达到与最先进拓扑相当的结果，而后者需要 43.7 美元。
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories.md) (n.d., evidence: unknown) — 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- [AgentSight: System-Level Observability for AI Agents Using eBPF](summaries/p-025-AgentSight-System-Level-Observability-fo.md) (n.d., evidence: unknown) — ### 性能开销
来自 LaTeX 源码 `eval-conclusion.tex`：
**Table 1.
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](summaries/p-011-Agentic-Harness-Engineering-Observabilit.md) (n.d., evidence: unknown) — ### RQ1：主结果
在 Terminal-Bench 2 上运行十轮 AHE 迭代（从仅含命令行的 NexAU$_0$ 种子出发，耗时约 32 小时），最佳配置记为 AHE。
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Can Dependencies Induced by LLM-Agent Workflows Be Trusted?](summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo.md) (n.d., evidence: unknown) — ### 主实验结果
Table 1 展示了 SeqCV 与基线在七个任务上的平均表现。SeqCV 在三项指标上均取得最高分，平均总分达到 88%，显著优于所有对比方法。
- [CoMem 深度阅读笔记](summaries/comem-note.md) (n.d., evidence: unknown) — Table 1 展示了 CoMem 在三种不同规模主干模型上的主要实验结果。
- [CompactPrompt 深度阅读笔记](summaries/compactprompt-note.md) (n.d., evidence: unknown) — ### 词元削减效果
在配置 G=2、T=3（即保留前三个最高频的二元组）时，TAT-QA 的提示词长度实现约 2.35 倍压缩，相当于减少 58% 的词元；FinQA 实现约 2.12 倍压缩，相当于减少 53% 的词元。整体而言，系统在两个基准上最高可降低 60% 的总词元使用量与推理成本。
- [EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation](summaries/p-018-EAGER-Efficient-Failure-Management-for-M.md) (n.d., evidence: unknown) — 作者在三个开源多智能体系统上开展了初步评估，核心实验结果分为异常检测与故障诊断性能、检测延迟以及任务性能提升三个维度。
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) (2026, evidence: unknown) — 作为一篇综述，本文的主要"结果"体现为对领域现状的系统刻画和未来方向的清晰预判：
- **记忆架构的四阶段演进**：当前系统已从单调上下文演进至自适应记忆系统，核心转变是从被动存储到主动控制策略。
- [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](summaries/featurebench-note.md) (n.d., evidence: unknown) — 论文评估了7种框架与模型的组合配置。模型侧覆盖 DeepSeek-V3.2、Claude Opus 4.5 等闭源与开源前沿模型；框架侧包括 OpenHands、Claude Code 等代表性智能体脚手架。
- [Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide](summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- Plus 49 additional linked summaries in [Index](index.md).

## Related Concepts

- [agent-observability-landscape](concepts/agent-observability-landscape.md)
- [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md)
- [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md)
