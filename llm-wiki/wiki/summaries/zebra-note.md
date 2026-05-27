# ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration

## Source

- Raw note: `raw/notes/zebra_note.md`
- Metadata: not available in note

## Compiled Summary

随着自主智能体越来越多地在固定资金预算下执行端到端任务，紧迫的开放性问题已从预算是否被遵守，转变为如何有效花费预算。

## Evidence Notes

- 现有的预算感知方法通常仅在单个智能体内部逐步控制推理过程，或通过强化学习来学习资源分配策略。这些方法均未解决如何在推理时将预算分配到多智能体流水线的各个组成阶段。
- 随着自主智能体系统日趋复杂，资源浪费已成为实际部署中的突出问题。用户不仅希望智能体遵守资金、令牌数、延迟或计算量的上限，更希望这些资源被有效使用。例如，在 10 美元预算与 100 美元预算下，同一任务的最优规划深度、工具使用强度与验证力度可能截然不同。现有预算感知方法主要集中于两类：一是在单个智能体内部逐步控制推理开销，二是在训练时通过强化学习或背包探索学习资源分配策略。然而，这些方法均未解决一个关键问题：在推理时，如何将固定总预算切分到多智能体流水线的各个组成阶段，以最大化整体输出质量。
- 论文聚焦的核心问题是：给定一个固定的多阶段智能体流水线与总预算，通过估计阶段效用曲线并显式求解优化问题，是否比直接让大语言模型输出预算分配更有效？
- ### 机制流程
1.
- **输入**为任务描述、总预算 B 及 n 阶段流水线结构；**动作**为查询各阶段可用模型及其美元定价；**输出**为带定价的流水线配置，供后续曲线估计使用。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
