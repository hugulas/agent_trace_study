# Observability for Agentic Systems: What to Log, How to Redact, How to Debug

## Source

- Raw note: `raw/notes/c-002_Observability_for_Agentic_Systems_What_t.md`
- 作者: Scott Farrell（Leverage AI）
- 证据质量: medium
- PDF: [c-002]-observability-for-agentic-systems-what-to-log-how-to-redact-.pdf

## Compiled Summary

这篇文章的最大价值在于其极强的实操导向。作者不仅告诉读者"应该记录什么"，还提供了具体的 NDJSON schema 示例、正则表达式模式、Python 插装代码片段，以及一个从告警到修复的完整调试故事。这种"手把手"的写作风格对于正在构建生产级 agent 系统的工程团队非常友好，可以直接作为内部可观测性规范制定的参考模板。

## Evidence Notes

- 从设计哲学的角度，文章隐含地倡导了一种"全面记录、安全导出"的策略：在 agent 内部尽可能完整地捕获所有决策相关的信息（七个维度），但在导出到外部系统之前进行严格的 PII 脱敏和内容裁剪。这一策略与 AgentTrace [c-011] 的双路径存储设计（JSONL 本地完整存储 + OTel spans 导出脱敏视图）有异曲同工之妙。我认为这种"内详外简"的分层架构是当前 agent 可观测性的最佳实践之一，因为它在调试能力和隐私合规之间取得了务实平衡。综述中可以将这一设计哲学命名为"分层可观测性架构"（layered observability architecture），并作为推荐模式向读者推广。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/AgentTrace|AgentTrace]], [[entities/Langfuse|Langfuse]], [[entities/AgentOps|AgentOps]], [[entities/Claude-Code|Claude Code]]
