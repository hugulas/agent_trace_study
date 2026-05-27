# AgentPrune：面向大语言模型多智能体系统的经济通信管道

## Source

- Raw note: `raw/notes/agentprune_note.md`
- Metadata: not available in note

## Compiled Summary

近期大语言模型驱动的智能体研究表明，集体智能可以显著超越个体能力，这在很大程度上归功于精心设计的智能体间通信拓扑。尽管性能令人印象深刻，但现有的多智能体流水线本质上引入了大量的令牌开销以及更高的经济成本，这对其大规模部署构成了挑战。为应对这一挑战，我们提出了一种经济、简洁且鲁棒的多智能体通信框架，称为 AgentPrune，它可以无缝集成到主流多智能体系统中，并剪除冗余甚至恶意的通信消息。从技术层面看，AgentPrune 首次识别并形式化定义了当前基于大语言模型的多智能体流水线中存在的通信冗余问题，并在时空消息传递图上执行高效的一次性剪枝，从而产生一个令牌经济且高性能的通信拓扑。在六个基准测试上的大量实验表明，AgentPrune

## Evidence Notes

- 基于大语言模型的多智能体系统通过智能体间的协作通信在推理、代码生成等复杂任务上取得了显著进展。然而，这种协作的代价是令牌消耗的急剧增加：即便最简单的通信框架也会使提示令牌量增长 2~11.8 倍，带来沉重的经济负担，并阻碍其在边缘设备上的部署。
- 论文指出，现有通信机制可分为两类：
- **对话内通信**：同一轮次中多个智能体通过合作、教学或竞争产生解决方案；
- **对话间通信**：当前对话内容通过总结、复制或过滤传递给下一轮作为参考。
- AgentPrune 将多智能体通信建模为一个时空图 $G = \{G_S, G_T\}$，其中 $G_S = (V, E_S)$ 为空间图（有向无环图，描述单轮内的智能体间消息流），$G_T = (V, E_T)$ 为时间图（描述跨轮历史传递）。每个智能体 $v_i$ 由基础模型、角色、状态与插件组成。
- ### 机制流程
给定输入查询，AgentPrune 的核心执行链路包含以下步骤：
1.
- 在 gpt-4 五智能体设置下，AgentPrune 与各类基线的对比如下：
- **与 SOTA 拓扑的成本对比**：AgentPrune 以约 5.6 美元的成本达到与最先进拓扑相当的结果，而后者需要 43.7 美元。
- - **集成到现有框架的降本效果**：与 AutoGen 和 GPTSwarm 集成后，提示令牌消耗降低 28.1%~72.8%，成本降低显著。

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
