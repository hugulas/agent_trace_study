# How we built our multi-agent research system — Anthropic Engineering Blog

## Source

- Raw note: `raw/notes/a-009_How_we_built_our_multi-agent_research_sy.md`
- 作者: Anthropic Engineering Team
- 来源: Anthropic 官方工程博客（Engineering at Anthropic）
- 证据质量: high
- PDF: [a-009]-how-we-built-our-multi-agent-research-system.pdf

## Compiled Summary

Anthropic 这篇文章堪称多智能体系统从原型到生产的最完整工程复盘之一，其价值不仅在于架构设计，更在于对"为什么有效"和"代价是什么"的坦诚剖析。90.2% 的性能提升令人印象深刻，但"token 消耗解释 80% 方差"这一发现更具理论意义——它暗示多智能体系统的性能提升在很大程度上是"推理容量扩展"的结果，而非某种神秘的涌现智能。这对综述的方法论有重要启示：在评估多智能体系统时，必须将 token 效率与结果质量同时纳入指标，否则可能产生误导性的结论。一个消耗 15 倍 token 却只提升 10% 准确率的系统，与一个消耗 2 倍 token 却提升 50% 准确率的系统，其工程价值是完全不同的。

## Evidence Notes

- 另一个值得深思的点是"智能体自我改进"循环——让模型自己优化提示和工具描述，实际上构建了一个元学习（meta-learning）的飞轮。这与综述中提到的自动调试、自适应 agent、self-improving systems 等前沿方向高度契合。特别值得注意的是，工具测试智能体通过重写 MCP 工具描述使后续智能体效率提升 40%，这说明在工具生态层面也存在巨大的优化空间，而这类优化往往被传统的手动文档编写所忽视。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: None identified
