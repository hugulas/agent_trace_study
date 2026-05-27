# SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching

## Source

- Raw note: `raw/notes/semsharekv_note.md`
- Metadata: not available in note

## Compiled Summary

随着大语言模型持续规模化，推理阶段键值缓存的内存占用已成为显著瓶颈。

## Evidence Notes

- 现有方法主要聚焦于在单个提示词内部压缩 KV 缓存，或复用跨提示词的共享前缀及高频文本片段。
- 大语言模型推理阶段的 KV 缓存内存占用随序列长度呈二次增长，已成为部署瓶颈。
- 现有 KV 缓存优化可分为三类：
- **单提示词压缩**：如量化、剪枝、动态淘汰（H2O、PyramidKV）
- **前缀共享**：复用完全相同的前缀文本片段
- **查询级复用**：基于相似度搜索复用整个查询的 KV 缓存（GPTCache 等）
上述方法均无法有效处理一种常见场景：两个提示词语义相近但用词不同，例如同一主题的多文档摘要请求或对话中的换表述追问。
- ### 核心概念
SemShareKV 围绕三种缓存组件设计：
- **Key Cache（K）**：编码序列中词元间的结构关系
- **Value Cache（V）**：经注意力权重聚合的实际内容表示
- **Embedding Cache（E）**：上下文嵌入，捕捉基本语义和句法关系，作为 Transformer 处理前的词元基础表示
### 系统架构
SemShareKV 基于三个关键洞察设计：
- **洞察 1**：高偏差词元（与复用缓存差异大的词元）在各层之间保持一致
- **洞察 2**：深层注意力恢复的词元数更少，即深层只关注少数关键词元
- **洞察 3**：深层包含更多冗余信息，可更大程度压缩
基于以上洞察，框架采
- **参考提示词检索（输入：目标提示词的 E 缓存；输出：最相似的参考提示词及其 KV 缓存）**
SemShareKV 将接收到的提示词及其上下文 E 缓存存储于处理器内存。

## Wiki Connections

- Concepts: [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
