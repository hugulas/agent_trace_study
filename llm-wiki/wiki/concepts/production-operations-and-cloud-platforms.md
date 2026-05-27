# Production Operations and Cloud Platforms

## Working Definition

Tracks AWS, Google, Alibaba, Baidu, and enterprise deployment guidance for operating agentic systems. In this wiki, the concept is compiled from local source notes rather than general background knowledge.

## Why It Matters

Agentic systems make decisions through multi-step trajectories: prompts, model calls, tool calls, memory updates, environment observations, planner decisions, and post-hoc evaluations. Ordinary request logging is too flat for that behavior. The notes linked here treat observability as a way to recover the trajectory, explain failures, assign responsibility, and create evidence that can be reviewed after deployment.

## Synthesis

- The corpus repeatedly separates **runtime telemetry** from **evaluation evidence**. Telemetry captures what happened; evaluation and audit layers decide whether the behavior was acceptable.
- Trace quality depends on schema discipline. Useful pages in this cluster tend to name the event surface, span or step boundary, metadata context, and downstream debugging question.
- Production material emphasizes integration cost, platform coverage, dashboards, and alerting. Academic material emphasizes failure taxonomies, attribution, monitorability, and formal structure.
- A recurring gap is that many product pages promise agent observability without exposing enough schema detail to compare cognitive, operational, and contextual traces.

## Source Notes

- [AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices](summaries/c-018-AI-Agents-in-Production-Monitoring-Guard.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds](summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat.md) (n.d., evidence: unknown) — AIOpsLab 评估了四个基于大模型的智能体以及三个传统非大模型方法，在 48 个场景上共进行 288 次评估。四个智能体分别为 GPT-4-with-Shell、GPT-3.5-with-Shell、ReAct、Flash。
- [Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems](summaries/agentcontracts-note.md) (n.d., evidence: unknown) — 四项实验的核心结果如下：
**实验一：迭代工作流失控预防**
| 指标 | UNCONTRACTED | CONTRACTED | 变化 | p 值 |
|------|-------------|-----------|------|------|
| 令牌消耗 | 34,606 | 3,461 | -90% | 0.0007*** |
| 方差 | 5.29B | 10.1M | 525x 降低 | — |
| 迭代次数 | 3.00 | 1.71 | -43% | <0.0001*** |
| 大模型调用次数
- [AgentOps AI Infrastructure Platform Market Research Report 2034](summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Best LLM Cost Tracking Tools in 2026 深度阅读笔记](summaries/costtools2026-note.md) (n.d., evidence: unknown) — 文章将八款平台划分为四个能力梯队：
**第一梯队（闭环型）：Future AGI Agent Command Center。**
唯一在单一运行时内同时实现追踪级成本归因、评估闭环、网关路由与五级预算的平台。
- [Beyond the Black Box: Next-Gen AI Agent Monitoring](summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Elastic LLM与Agentic AI可观测性技术文档](summaries/s2-010-LLM-and-agentic-AI-observability-Elasti.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Essential Framework for AI Agent Guardrails](summaries/c-017-Essential-Framework-for-AI-Agent-Guardra.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide](summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Google Cloud Trace observability for ADK](summaries/s1-001-Google-Cloud-Trace-observability-for-ADK.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Google boosts Vertex AI Agent Builder with new observability and deployment tools](summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化](summaries/s2-022-Helicone-LLM-Observability-Platform-Lea.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [Helicone：开源 LLM 可观测性与 AI 网关一体化平台](summaries/s2-023-Helicone-Open-source-LLM-observability-f.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [HybridFlow: Resource-Adaptive Subtask Routing for Efficient Edge-Cloud LLM Inference](summaries/hybridflow-note.md) (n.d., evidence: unknown) — **准确率表现（Table 1）**：
- CoT（GPT-4.1）在所有非直接提示方法中取得最高平均准确率 58.99%
- HybridFlow 平均准确率为 55.34%，紧随其后，优于 SoT（52.90%）和 PASTA（45.56%）等单模型分解方法，以及协作基线 HybridLLM（38.70%）和 DoT（46.50%）
- 纯端侧 CoT（Llama3.2-3B）仅 19.59%，纯云端 Direct Prompt（GPT-4.1）为 53.33%
**效率表现（Table 2）**：
- Hyb
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/costattribution-note.md) (n.d., evidence: unknown) — 多租户实例揭示了聚合指标为何具有误导性：
| 租户分段 | 数量 | 收入 | Token 支出 | 毛利率 |
|---|---|---|---|---|
| 健康（包月 tier） | 34 | \$145,000 | \$14,600 | 90% |
| 高消耗（应升级 tier） | 4 | \$22,000 | \$11,400 | 48% |
| 失控（集成中的循环缺陷） | 2 | \$13,000 | \$8,000 | 38% |
- 聚合 81% 的毛利率真实但无意义。
- [Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点](summaries/s2-015-AI-Agent-Observability-Platform-Langfuse.md) (n.d., evidence: unknown) — Indexed as relevant by title and metadata.
- [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](summaries/masbench-note.md) (n.d., evidence: unknown) — ### 总体性能对比
在全部 139 项任务上使用预定义快捷方式知识库的实验结果（Table 2）揭示了四个关键发现：
1.
- Plus 48 additional linked summaries in [Index](index.md).

## Related Concepts

- [agent-observability-landscape](concepts/agent-observability-landscape.md)
- [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md)
- [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md)
