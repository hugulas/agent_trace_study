# Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving

## Source

- Raw note: `raw/notes/graphcot_note.md`
- Metadata: not available in note

## Compiled Summary

图链式思维（Graph-CoT）使大语言模型能够对图结构知识进行逐步推理，但现有流水线存在准确率低下、token 消耗过度、延迟高且吞吐量低等问题，根源在于单智能体单体提示、重复上下文重新编码以及低效的推理执行。

## Evidence Notes

- 本文提出 GLM，首个与优化大语言模型服务架构协同设计的多智能体 Graph-CoT 系统。GLM 将推理分解为分类、推理、动作生成和图检索四类专用智能体，通过分支执行与选择性上下文共享来缩短提示长度并减少推理轮次，同时保持推理质量，从而提升准确率并降低整体 token 消耗。
- 现有 Graph-CoT 系统在复杂图结构知识推理中面临三重瓶颈。
- **单智能体能力边界**：现有框架采用单智能体单体提示，每一步都需重新编码完整上下文和中间轨迹，导致长链条推理不稳定。实验显示，随着推理步数增加，Graph-CoT 的 GPTScore 从 3 步时的 0.42 跌至 9 步时的 0.17，准确率急剧衰减。
- GLM 的整体架构由两大模块组成：基于大语言模型的智能体模块和图检索增强生成（Graph RAG）检索器模块，均基于约 3,000 行 Python 代码在 vLLM（v0.8.5）之上实现。
- ### 智能体定义
每个智能体由输入空间、提示模板与输出空间三元组刻画。

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
