# 阿里云百炼应用观测 — 大模型应用端到端可观测实践

## Source

- Raw note: `raw/notes/s2-002_应用观测-大模型服务平台百炼Model_Studio__阿里云文档.md`
- 来源: 阿里云官方产品文档 · 大模型服务平台百炼 · 用量监控与性能分析
- PDF: [s2-002]-应用观测-大模型服务平台百炼model-studio--阿里云文档.pdf

## Compiled Summary

百炼应用观测文档的价值在于展示了一种"平台原生可观测性"的落地形态。与
独立的可观测性产品（如 Langfuse、AgentLoop、Datadog）不同，百炼将观测
能力直接嵌入到大模型应用开发和运行的核心路径中，用户在无需额外接入任何
第三方 SDK 的情况下即可获得基础的 Trace 和 Metric 能力。这种"开箱即用"
的体验对于降低 AI 应用可观测性的 adoption 门槛具有重要意义，尤其是在中国
市场大量企业开发者尚未建立系统化的 AI 运维体系的背景下。对于许多初次接触
大模型应用的企业而言，百炼的这种内置方案可能是他们接触 Agent 可观测性的
第一入口。

## Evidence Notes

- 文档中提到的三个初始化步骤（授权、开通、初始化 LogStore）揭示了一个重要
事实：即使是平台原生的观测能力，在云环境中仍然需要跨产品的权限和资源配置。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [LangSmith](entities/LangSmith.md), [Langfuse](entities/Langfuse.md), [Arize Phoenix](entities/Arize-Phoenix.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md)
