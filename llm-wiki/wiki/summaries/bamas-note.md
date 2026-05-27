# BAMAS: Structuring Budget-Aware Multi-Agent Systems

## Source

- Raw note: `raw/notes/bamas_note.md`
- Metadata: not available in note

## Compiled Summary

基于大语言模型的多智能体系统已成为使自主智能体解决复杂任务的重要范式。随着这些系统在复杂度上不断扩展，成本成为实际部署中必须考虑的重要因素。然而，现有工作很少探讨如何在显式预算约束下构建多智能体系统。本文提出 BAMAS，一种构建具有预算意识的多智能体系统的新方法。BAMAS 首先通过将大语言模型选择问题建模为整数线性规划问题来选取最优模型集合，从而在性能和成本之间取得平衡。随后，它利用基于强化学习的方法确定这些模型应如何协作，以选择交互拓扑结构。最后，系统基于所选智能体及其协作拓扑进行实例化并执行。我们在三个代表性任务上评估了 BAMAS，并与最先进的智能体构建方法进行比较。结果表明，BAMAS 在取得可比性能的同时，最多可将成本

## Evidence Notes

- 论文针对的核心问题是：给定任务描述、可用大语言模型池和成本预算，如何构建一个多智能体系统，使其在严格满足预算约束的前提下实现最优的性能-成本权衡。具体而言，需要同时确定两个互相关联的决策变量：
- 选择哪些大语言模型作为系统内的智能体，即模型配备问题；
- 这些智能体之间应采用何种交互拓扑结构，即协作模式问题。
- 这一问题的动机来源于当前多智能体系统在实际部署中的成本困境。单次任务可能涉及数十次大语言模型调用，而成本随协作拓扑和推理深度不可预测地增长。现有框架通常以最大化性能为首要目标，对成本缺乏前置控制，导致系统难以在真实业务场景中可靠扩展。
- BAMAS 的整体架构包含三个串行组件：预算约束下的大语言模型配备、智能体协作拓扑选择、以及系统实例化与执行。
- ### 预算约束下的大语言模型配备
该组件从可用模型池中选出子集，使得总成本不超过预算。作者基于以下观察采用性能优先策略：对于复杂推理任务，单个高性能模型通常优于多个弱模型的简单组合。因此，优化目标是在预算内最大化所选模型的总体性能权重。
- **成本-性能权衡**
表一和表二报告了 BAMAS 与基线方法在三个数据集上的平均成本和准确率。BAMAS 在所有数据集上均展现出优于现有方法的成本-性能权衡。
- - **GSM8K**（预算 1625）：BAMAS 达到 95.3% 的准确率，几乎追平 AutoGen 配合 DeepSeek-V3 的 95.4%，但平均成本仅为 542.9，相比基线的 1425.3 降低 62%。

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
