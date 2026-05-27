# Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning

## Source

- Raw note: `raw/notes/cotprune_note.md`
- Metadata: not available in note

## Compiled Summary

长链思维（Long-CoT）推理能够提升大语言模型的准确率，但其冗长且自我反思的风格常常阻碍其向小语言模型（SLM）的有效蒸馏。本文从能力对齐的视角重新审视长链思维压缩，并提出问题：剪枝能否提升推理能力？作者提出了 Prune-on-Logic，一种结构感知的框架，将长链思维转化为逻辑图，并在自验证约束下有选择地剪除低效用推理步骤。通过对三种剪枝策略的系统分析，即针对完整推理链、核心推理和验证阶段的剪枝，研究发现验证阶段剪枝在降低token使用量的同时持续提升准确率，而推理步骤剪枝或不加区分的剪枝则会损害性能。该研究表明，有效的剪枝是将监督信号与模型容量对齐，而非仅仅缩短输入长度。这种收益在不同任务、模型规模和链思维能力上均成立，规

## Evidence Notes

- 大语言模型如 OpenAI-O1 和 DeepSeek-R1 借助长链思维（Long-CoT）推理在数学解题和逻辑推理等复杂任务上取得了显著进展。然而，长链思维的冗长推理链带来了巨大的计算开销：推理延迟增加、键值缓存占用大量内存、注意力计算的二次复杂度急剧上升。这些限制严重制约了LLM在实际复杂推理任务中的部署效率。
- 更关键的是，将长链思维蒸馏到小语言模型时面临根本挑战：SLM由于容量有限，难以有效习得长上下文推理能力。现有压缩方法（如基于困惑度的token级压缩、提示策略、步骤级压缩、RLHF长度协调数据集等）本质上都属于有损压缩，存在丢弃关键推理信息的风险，从而损害模型在复杂任务上的性能。
- 本文提出 Prune-on-Logic 框架，核心思想是将长链思维推理痕迹转化为逻辑图，通过结构感知的方式识别并剪除低效用步骤，从而在保证语义等价的前提下实现压缩与性能提升的双重目标。
- ### 逻辑图构建
给定长链思维序列 $S = \{s_1, s_2, \ldots, s_n\}$，框架首先通过大语言模型和分类提示 $P_{\text{logic}}$ 将每个句子划分为两个互不相交的子集：
- $N$：表达推理或验证步骤的原始句子，如符号运算、数值推导或包含推理的结论
- $C$：起修辞连接作用的原始句子，如填充语、过渡句或元认知短语
这一分类产生结构化标注，将每个句子标记为推理节点或连接词并保留原始位置。
- ### 主实验结果
表2展示了在 DeepSeek-R1-Distill-Llama-8B 和 DeepSeek-R1-Distill-Qwen-7B 上三种剪枝策略的完整结果。
- **DeepSeek-R1-Distill-Llama-8B（基线 57.7%，4555.9 tokens）**：
- 全链剪枝（Cut All）：准确率暴跌至 10.4%（下降 47.3 个百分点），token 降至 475.4（减少 89.6%）
- 仅推理剪枝（Cut All）：准确率降至 38.1%（下降 19.6 个百分点），token 降至 1681.5（减少 63.1%）
- 仅验证剪枝（Cut All）：准确率提升至 62.9%（提升 5.2 个百分点），token 降至 4295.2（减少 5.72%）
**DeepSeek-R1-Distill-Qwen-7B（基线 57.0%，4344.3 tokens）**：

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
