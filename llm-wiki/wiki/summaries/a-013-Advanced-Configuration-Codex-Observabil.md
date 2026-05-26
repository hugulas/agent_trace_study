# Advanced Configuration — Codex (Observability and telemetry)

## Source

- Raw note: `raw/notes/a-013_Advanced_Configuration__Codex_Observabil.md`
- 来源: OpenAI 官方开发者文档
- 证据质量: high（官方一手文档，直接描述产品能力）

## Compiled Summary

Codex CLI 的高级配置文档虽然篇幅不长，但信息密度很高。它揭示了一个重要趋势：AI 编码工具的可观测性正在从"平台侧"（如 LangSmith、Langfuse 等第三方服务）向"客户端侧"（CLI 本身）下沉。这意味着开发者无需额外的 SDK 集成或代码插桩，只需修改配置文件即可获取生产级的 trace 与 metrics 数据。

## Evidence Notes

- 从架构设计角度看，opt-in 策略是一个精明的权衡。一方面，默认关闭 OTel 导出避免了不必要的性能开销和网络流量，尤其对在资源受限环境或敏感网络中使用的开发者更为友好；另一方面，一旦启用，`[otel]` 节提供的丰富事件类型和指标维度，足以支撑大多数调试与监控场景。这种"按需启用、深度可用"的设计，值得其他 agent 框架借鉴。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/LangSmith|LangSmith]], [[entities/Langfuse|Langfuse]], [[entities/Claude-Code|Claude Code]], [[entities/Codex-CLI|Codex CLI]]
