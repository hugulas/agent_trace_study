# SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing

## Source

- Raw note: `raw/notes/sage_note.md`
- Metadata: not available in note

## Compiled Summary

具备长上下文窗口的大语言模型可以直接从完整的学术、技术和政策文档中回答复杂问题，但传递整篇文档往往成本高昂、速度缓慢，还可能降低回答质量并增加不必要的数据泄露风险。

## Evidence Notes

- 本文针对一个常见场景：对单篇或多篇长文档回答大量异构问题。在这一场景中，固定位置启发式方法和标准检索增强生成（RAG）可能因文档结构多变以及查询与分块之间的语义相似度较弱而失效，而后者通常需要针对任务和领域对嵌入检索器进行专门调优。
- 本文聚焦于长文档问答中的**预算约束上下文缩减**问题。具体而言，给定一篇长文档和多个异构查询，如何在用户指定的词元预算内，提取出最能保留答案质量的文本子集，从而避免将整篇文档传递给下游生成模型。
- 作者指出，现有方法存在三类明显局限：
- **固定位置启发式方法**（如假设答案总在摘要或结论段）只在粗略统计意义上成立。实际上，不同问题类型的证据分布差异极大。例如作者相关信息集中在论文开头，而主要贡献的证据则分散在全文中。
- SAGE 的设计目标是在严格遵循用户指定词元预算的前提下，从长文档中提取最具信息量的文本跨度，并确保生成大语言模型获得高质量且连续的上下文。
- 整体流水线包含四个主要阶段，由轻量级本地大语言模型驱动：
1.

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
