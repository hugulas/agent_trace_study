# Willful Disobedience: Automatically Detecting Failures in Agentic Traces

## Source

- Raw note: `raw/notes/p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces.md`
- Metadata: not available in note

## Compiled Summary

人工智能智能体正越来越多地嵌入真实软件系统中，通过多轮对话、工具调用和中间决策执行多步骤工作流。这些很长的执行历史被称为智能体轨迹，它们让验证变得困难。只看结果的基准可能漏掉关键过程性失败，例如错误的工作流路由、不安全的工具使用，或违反提示中指定的规则。本文提出 AgentPex，这是一个由人工智能驱动的工具，旨在系统评估智能体轨迹。AgentPex 从智能体提示和系统指令中抽取行为规则，然后用这些规范自动评估轨迹是否合规。作者在来自 `${\tau}^2$-bench` 的 424 条轨迹上评估 AgentPex，覆盖电信、零售和航空客户服务中的多个模型。结果表明，AgentPex 能区分不同模型的智能体行为，并发现只看结果评分无

## Evidence Notes

- 结果型 benchmark 的问题是视野太窄。一个智能体可能最终碰巧得到正确数据库状态，但过程中调用了错误工具、暴露了不该暴露的信息，或者违反了系统提示中的操作顺序。相反，一个任务也可能最终失败，但开发者仍然需要知道失败来自参数错误、路由错误、计划偏离还是输出格式不合规。
- AgentPex 针对的是这种“轨迹合规性”问题：给定系统提示、工具 schema 和完整消息日志，自动抽取可检查规范，并对轨迹进行多维度评分。它不是替代最终奖励，而是补足最终奖励无法解释过程错误的缺口。
- ### 机制流程
![Fig.
- 1 AgentPex 轨迹违规示例](p-004_Willful_Disobedience_Automatically_Detecting_Failures_in_Agentic_Traces/images/fig1_agentpex_example.png)
*论文原图编号：Fig.
- 论文发现，AgentPex 能区分不同模型和领域中的行为差异，并能发现 `${\tau}^2` 结果评分没有直接暴露的规范违反。Fig.
- 5 显示，当轨迹按 AgentPex 聚合分数排序时，低 `${\tau}^2` 轨迹集中在低 AgentPex 分数区域，说明过程合规性与最终任务结果存在一致性。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: None identified
