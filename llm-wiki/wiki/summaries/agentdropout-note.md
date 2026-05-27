# AgentDropout 深度阅读笔记

## Source

- Raw note: `raw/notes/agentdropout_note.md`
- Metadata: not available in note

## Compiled Summary

基于大型语言模型的多智能体系统在协作问题解决中展现了显著潜力。然而，它们仍面临通信效率低下和任务性能不佳的重大挑战，这使得对智能体通信拓扑的精心设计尤为重要。受高效团队中角色常被动态调整这一管理理论启发，我们提出了AgentDropout，该方法通过优化通信图的邻接矩阵来识别不同通信轮次中的冗余智能体和冗余通信，并将其消除，以同时提升token效率和任务性能。与现有最优方法相比，AgentDropout平均减少了21.6%的提示词token消耗和18.4%的补全token消耗，同时任务性能提升了1.14。此外，扩展实验表明AgentDropout具有显著的领域迁移能力和结构鲁棒性，证明了其可靠性与有效性。我们在以下地址公开了代码：h

## Evidence Notes

- 当前基于大语言模型的多智能体系统虽然在数学推理、代码生成等任务上展现了超越单智能体的潜力，但普遍存在两个核心问题：
- **通信效率低下**：多轮对话中智能体频繁生成消息并互相传递，导致prompt token和completion token开销巨大，实际部署成本高昂。
- - **静态角色约束**：现有方法如AgentPrune虽然通过可训练的图掩码剪除了部分冗余边，但参与每一轮讨论的智能体角色集合固定不变，只能应用跨轮次的统一剪枝策略，限制了系统在效率和性能上的进一步提升。
- AgentDropout的核心思想是将多智能体通信建模为图，并通过可学习的邻接矩阵权重识别冗余节点和边，在推理阶段执行动态淘汰。整个流程分为拓扑学习与推理执行两个阶段。
- ### 图形式化
将多智能体系统表示为通信图：
$$G = (V, E, F)$$
其中节点集合 $V$ 包含全部智能体，边集合 $E$ 包含轮内通信边与轮间通信边，映射集合 $F$ 描述各智能体的推理函数。
- ### 性能对比
AgentDropout在全部六个基准和三种模型规模上均优于单智能体CoT和多智能体基线。以Llama3-8B为例：
| 方法 | MMLU | GSM8K | AQuA | MultiArith | SVAMP | HumanEval | 平均 |
|------|------|-------|------|------------|-------|-----------|------|
| Vanilla | 53.59 | 70.23 | 41.67 | 91.11 | 75.00 | 53.33 | 64.16 |
| CoT | 56.86 | 70.47 | 43.75 | 92.25 | 76.17 
- - 在Qwen2.5-72B上，平均准确率91.58，较AgentPrune提升0.77。

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
