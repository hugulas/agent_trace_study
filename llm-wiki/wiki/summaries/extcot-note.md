# Towards Efficient Large Language Reasoning Models via Extreme-Ratio Chain-of-Thought Compression

## Source

- Raw note: `raw/notes/extcot_note.md`
- Metadata: not available in note

## Compiled Summary

思维链（Chain-of-Thought, CoT）推理有效提升了大语言模型的推理能力，但也带来了巨大的推理计算开销。现有的 CoT 压缩方法在高压缩比下往往会遭遇逻辑保真度的严重损失，导致性能显著下降。为了实现高保真、快速的推理，我们提出了一种全新的极端比例思维链压缩框架，称为 Extra-CoT，该框架在大幅降低词元预算的同时保持答案准确率。为了生成可靠的高保真监督信号，我们首先在一个带有细粒度标注的数学 CoT 数据上训练一个专用的语义保持压缩器。随后，一个大语言模型在这些压缩后的样本对上通过混合比例监督微调进行微调，使其学会遵循一系列压缩预算，并为强化学习提供稳定的初始化。我们进一步提出了约束分层比例策略优化，通过分层奖励机

## Evidence Notes

- 大语言推理模型如 OpenAI o1 和 DeepSeek-R1 通过生成逐步思维链在复杂逻辑推理任务上取得了优异表现。然而，这种性能以消耗大量词元为代价，模型容易产生过度思考，即使面对简单查询也会生成冗余的推理路径。这导致推理阶段的计算开销极高，限制了在资源受限场景下的部署。
- 现有可控思维链压缩方法通常依赖通用重要性估计器，在低至中等压缩比下表现尚可，但在高压缩比下性能会灾难性下降。其核心原因在于极端压缩下关键推理步骤稀疏且难以识别，通用压缩器无法保持语义完整性和逻辑保真度。而推理链的完整性与一致性直接影响最终解题能力。因此，如何在极端压缩比下实现语义保持的高效推理，是该论文要解决的核心问题。
- Extra-CoT 的整体框架是一个三阶段紧密耦合的训练流水线，目标是在极端压缩比下保持思维链的语义完整性和解题准确率。
- ### 机制流程
1.
- > [!figure] Fig.
- 1: Comparison between accuracy and actual compression ratio of CoT tokens
> 建议位置：关键结果
> 放置原因：该图直观展示了不同方法在三个基准上的准确率与压缩比权衡，是论文核心结论的可视化
> 当前状态：占位符
### 主实验：Qwen3-1.7B 上的匹配比例对比
在 Qwen3-1.7B 骨干上，Extra-CoT 与 TokenSkip 和 Thinkless* 在相同目标比例下进行对比：
在 MATH-500 上，Extra-CoT 在目标比例 0.2 时实现超过 73% 的词元压缩，同时准确率相比 Base Model 提升 0.6%。相比之下，T

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
