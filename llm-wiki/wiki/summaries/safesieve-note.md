# SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication

## Source

- Raw note: `raw/notes/safesieve_note.md`
- Metadata: not available in note

## Compiled Summary

基于大语言模型的多智能体系统展现出强大的协作能力，但往往面临通信冗余和令牌开销过大的问题。现有方法通常通过预训练图神经网络或贪婪算法来提升效率，但这些方法往往将任务前优化与任务后优化割裂开来，缺乏统一的策略。为此，本文提出一种渐进式自适应的多智能体剪枝算法，通过新颖的双重机制动态优化智能体间的通信。

## Evidence Notes

- 该方法将基于大语言模型的语义评估与累积的性能反馈相结合，实现了从启发式初始化到经验驱动优化的平滑过渡。与现有的贪婪 Top-k 剪枝方法不同，本文方法采用零扩展聚类来保留结构一致的智能体群组，同时剔除无效的通信链路。在多个基准测试上的实验表明，该方法在达到 94.01% 平均准确率的同时，将令牌使用量降低了 12.4% 至 27.8%。
- 基于大语言模型的多智能体系统已在协作问题求解方面展现出令人印象深刻的能力，并催生出 AutoGen、ChatDev 等实用框架。然而，智能体之间密集的轮询式通信往往带来以下问题：
- **令牌开销过大**：冗余消息显著推高推理成本。
- - **注意力稀释**：过量无关信息使智能体难以聚焦关键内容，导致准确率下降。
- SafeSieve 是一种渐进式自适应的多智能体通信剪枝框架。其核心思想是将**语义兼容性**（任务前启发式）与**历史反馈贡献**（任务后经验）动态融合，逐步精炼通信拓扑。
- ### 图建模
将多智能体通信建模为时变图，节点集为智能体集合，边集表示消息通道。具体定义如下：
$$G_t = (V, E_t)$$
其中 $V$ 为智能体集合，边 $e_{ij}$ 表示从智能体 $i$ 到 $j$ 的消息。通过掩码矩阵定义候选通信链路集合：
$$\tilde{E}_t = \{e_{ij} \in E_t : M^{(t)}_{ij} = 1\}$$
### 边重要性评分
每条边的重要性由两个因素加权组合：
1.

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
