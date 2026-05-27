# AgentRx: Diagnosing AI Agent Failures from Execution Trajectories

## Source

- Raw note: `raw/notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories.md`
- Metadata: not available in note

## Compiled Summary

当前本地元数据没有抽取到完整摘要。根据论文正文中的问题陈述和贡献描述，本文研究如何从智能体执行轨迹中诊断失败原因，尤其是定位导致任务无法完成的第一个不可恢复关键步骤，并给出失败类别。作者构建了一个包含 115 条失败轨迹的标注数据集，覆盖结构化应用程序接口工作流、事故管理和开放式网页或文件任务，并提出 AgentRx 框架，用执行前缀、工具约束、策略约束和观测到的违规证据来做失败归因。

## Evidence Notes

- 智能体系统的调试难点不在于“失败是否发生”，而在于失败如何沿着消息、工具调用、观测和状态更新传播。传统结果评测通常只检查最终数据库状态、最终回复或任务奖励，因此无法回答开发者真正需要的问题：是哪一个动作、哪一个工具调用或哪一次决策让后续执行不可恢复。
- 论文把问题定义为失败归因和步骤定位：给定一条已经失败的执行轨迹，系统需要找出导致任务无法成功完成的关键步骤，并将失败归入可解释类别。这一设定更接近生产环境中的调试需求，因为工程师需要知道应该修复提示、工具 schema、路由逻辑、状态更新还是安全策略。
- ### 机制流程
1.
- 系统先读取执行轨迹前缀，包括用户意图、智能体消息、工具调用、工具返回和状态更新。
- 论文报告了失败归因准确率，并把评估拆成智能体级定位和步骤级定位。证据包中显示，AgentRx 在 tau-bench 和 Magentic-One 轨迹上都优于既有失败归因基线。尤其在步骤定位上，论文关注平均值和标准差，并进一步分析容忍窗口下的准确率，说明严格单步命中和邻近步骤命中都被纳入讨论。
- **Table 2 失败归因准确率，来自 LaTeX 源码 `eval.tex`。**
| Method | tau-bench Agent | tau-bench Step | Magentic Agent | Magentic Step |
|---|---:|---:|---:|---:|
| Who&When modified | 62.0 | 17.2 | 6.2 | 56.3 |
| Our Baseline | 75.9 | 32.2 | 81.2 | 56.3 |
**Table 3 平均轨迹与步骤长度，来自 LaTeX 源码 `eval.tex`。**
| Metric | tau-bench | Flash | 

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
