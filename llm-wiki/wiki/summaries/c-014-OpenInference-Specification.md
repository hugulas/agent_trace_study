# OpenInference Specification | openinference

## Source

- Raw note: `raw/notes/c-014_OpenInference_Specification.md`
- 证据质量: high（作为社区事实标准的技术规范文档）

## Compiled Summary

OpenInference 规范的最大价值在于它提供了一个"AI 原生"的追踪语义层，而不是让 AI 应用去适配传统 HTTP 服务的追踪模型。在 HTTP 服务中，一次 span 只需要
method、status_code、path 等属性就足够理解；但在 LLM 应用中，同样的"一次调用"背后是多轮对话历史、系统提示词、工具定义、温度参数、token
消耗、模型版本等数十个维度的信息。如果这些信息散落在不同的日志格式中，不仅无法聚合分析，更无法在不同框架之间进行横向比较。

## Evidence Notes

- 从工程实践角度，我认为 OpenInference 的十种 span-kind 设计非常贴近实际 Agent 系统的执行模式。特别是 AGENT 和 CHAIN
的区分——前者代表自主决策的智能体循环，后者代表确定性的编排逻辑——这种区分对于后续做根因分析和故障定位至关重要。当一次 Agent 执行失败时，通过 span-kind
可以快速判断问题出在智能体的决策逻辑（AGENT）、工具调用的参数构造（TOOL）、检索阶段返回了不相关的上下文（RETRIEVER），还是重排序模型产生了偏差（RERANKER）。这种结构化的故障分类远比在原始日志中搜索关键词高效。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/OpenInference|OpenInference]], [[entities/Arize-Phoenix|Arize Phoenix]]
