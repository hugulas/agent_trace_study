# Token-Budget-Aware LLM Reasoning

## Source

- Raw note: `raw/notes/tale_note.md`
- Metadata: not available in note

## Compiled Summary

推理对于大语言模型在广泛任务中取得优异表现至关重要。虽然思维链等推理方法通过将问题分解为中间步骤来提升大语言模型的性能，但它们也带来了显著的词元使用开销，导致成本上升。我们发现当前大语言模型的推理过程存在不必要的长度冗余，可以通过在提示中加入合理的词元预算来压缩，但词元预算的选择对实际压缩效果起着关键作用。基于此，我们提出了一种词元预算感知的大语言模型推理框架，该框架根据每个问题的推理复杂度动态调整推理词元的数量。实验表明，我们的方法在思维链推理中有效降低了词元成本，同时仅带来轻微的性能下降，为平衡大语言模型推理的效率与准确性提供了实用的解决方案。

## Evidence Notes

- 大语言模型在采用思维链推理时性能显著提升，但伴随而生的是输出词元数量的急剧膨胀，这直接转化为更高的推理延迟、计算资源消耗和调用费用。一个自然的问题是：当前大语言模型的推理过程是否存在可压缩的冗余词元？如果存在，如何为不同复杂度的问题确定合适的压缩程度，才能在削减成本的同时尽量不牺牲答案正确性？
作者在实验中观察到，以 GPT-4o-mini 解决一道数学应用题为例，直接回答仅需 15 个输出词元，而思维链推理消耗了 258 个词元。更关键的是，如果在提示中加入"使用少于 50 个词元"的约束，模型仅用了 86 个词元就得出了正确答案；但如果约束过紧（如少于 10 个词元），实际输出反而膨胀到 157 个词元。这说明预算的选择至关重要
- > [!figure] Fig.
- TALE 框架包含两条实现路径：**TALE-EP**（估计与提示，零样本、无需训练）和 **TALE-PT**（后训练，通过监督微调或直接偏好优化将预算感知内化到模型参数中）。
- ### 机制流程
TALE 的核心执行链路围绕"最优预算搜索—预算感知推理"展开，具体流程如下：
1.
- **TALE-EP 在 GPT-4o-mini 上的主实验**
表 3 对比了直接回答、原始思维链和 TALE-EP 在六个数据集上的表现。TALE-EP 平均准确率为 81.03%，相较原始思维链的 83.75% 仅下降 2.72 个百分点；但输出词元从平均 461.25 降至 148.72，降幅达 67.75%；费用从 289.78 降至 118.46，降幅达 59.12%。
- | 数据集 | 原始 CoT 准确率 | TALE-EP 准确率 | 原始 CoT 词元 | TALE-EP 词元 |
|---|---|---|---|---|
| GSM8K | 81.35% | 84.46% | 318.10 | 77.26 |
| GSM8K-Zero | 99.50% | 98.72% | 252.96 | 22.67 |
| MathBench-Arithmetic | 75.00% | 73.67% | 313.51 | 39.60 |
| MathBench-Middle | 84.67% | 79.33% | 553.93 | 238.14 |
| MathBench-High | 84.00% 

## Wiki Connections

- Concepts: [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
