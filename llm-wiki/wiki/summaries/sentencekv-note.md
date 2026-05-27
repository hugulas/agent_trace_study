# SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching

## Source

- Raw note: `raw/notes/sentencekv_note.md`
- Metadata: not available in note

## Compiled Summary

大语言模型在处理长上下文时面临显著的计算与内存挑战。在推理阶段，高效管理键值缓存——即存储自回归生成过程中中间激活的状态——对于降低内存开销和提升计算效率至关重要。

## Evidence Notes

- 传统的词元级高效键值缓存方法忽略了语义信息，将每个词元独立处理而不考虑它们之间的语义关联。与此同时，现有的语义保持型键值缓存管理方案往往伴随巨大的内存占用和较高的首词元延迟。为应对这些局限，本文提出 SentenceKV，一种新颖的句子级语义键值缓存方法，旨在提升推理效率的同时保持语义连贯性。
- 大语言模型的 Transformer 架构使得键值缓存的内存占用随序列长度线性增长。以 Llama-3.1-8B 为例，在 float16 精度下处理 32K 词元的解码阶段提示词约需 16 GB 图形处理器内存，且注意力计算的二次复杂度导致计算开销随长度急剧增加。现有解决方案主要分为两类，但各有明显缺陷：
- **词元级淘汰策略**（如 H2O、SnapKV）依据注意力权重或固定模式永久丢弃部分词元，无法适应解码过程中词元重要性的动态变化，在需要复杂推理和长程依赖的任务上性能下降显著。
- - **动态分块检索策略**（如 Quest、InfLLM）将输入切分为固定大小的块并选择性加载，但任意分块会破坏自然的语义边界，导致叙事连贯性和主题一致性受损。
- SentenceKV 的核心思想是将键值缓存的管理单元从单个词元提升到自然句，使缓存压缩和动态检索都以语义连贯的句子为单位进行。整个框架分为预填充（prefilling）和解码（decoding）两个阶段。
- 在预填充阶段，输入提示词按标点符号切分为若干句子。对每个句子内的词元，计算其重要性分数，仅保留最重要的部分词元的键值对并卸载至中央处理器，其余词元被丢弃。同时，每个句子被压缩为一个紧凑的语义向量，该向量直接驻留在图形处理器显存中。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
