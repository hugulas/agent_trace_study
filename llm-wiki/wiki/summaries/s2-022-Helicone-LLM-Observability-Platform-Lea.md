# Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化

## Source

- Raw note: `raw/notes/s2-022_Helicone_LLM_Observability_Platform__Lea.md`
- Metadata: not available in note

## Compiled Summary

Helicone 的评测让我对"Proxy 模式 versus SDK 插桩模式"的架构之争
有了更具体、更工程化的理解。

## Evidence Notes

- Helicone 选择 Proxy 路线背后有清晰的产品逻辑和用户画像支撑：
它的核心目标用户不是那些需要深度追踪复杂 Agent 执行轨迹、
分析多步骤推理链路的系统架构师，
而是希望在现有 LLM API 调用之上快速叠加日志、监控和成本优化能力的工程团队。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [LangSmith](entities/LangSmith.md), [Langfuse](entities/Langfuse.md), [Arize Phoenix](entities/Arize-Phoenix.md), [Helicone](entities/Helicone.md)
