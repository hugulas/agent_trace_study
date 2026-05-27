# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

## Source

- Raw note: `raw/notes/p-011_Agentic_Harness_Engineering_Observabilit.md`
- Metadata: not available in note

## Compiled Summary

Harness 指模型外部可编辑的工程组件集合，已成为决定代码智能体性能的核心因素，它中介了模型与工具及执行环境之间的交互方式。

## Evidence Notes

- 然而 harness 工程至今仍是一项手工技艺，因为自动化面临三大障碍：可编辑组件之间的异构动作空间、海量轨迹中可行动信号被淹没、以及编辑效果难以归因。
- 代码智能体在长程软件工程任务上的进步不仅依赖于底层语言模型，同样依赖于周边工程组件。
- 这些周边工程组件包括塑造工作风格的系统提示、暴露文件系统与命令行接口的工具、以及控制上下文与执行的中间件。
- AHE 将 harness 优化转化为由另一个智能体驱动的闭环，基座模型保持固定，仅显式编辑 harness。
- 设计原则是循环的每个阶段都必须可观测。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Codex CLI](entities/Codex-CLI.md)
