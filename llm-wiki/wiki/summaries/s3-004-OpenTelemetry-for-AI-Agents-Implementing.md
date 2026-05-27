# OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows

## Source

- Raw note: `raw/notes/s3-004_OpenTelemetry_for_AI_Agents_Implementing.md`
- 作者: MintMCP 团队
- 证据质量: low
- PDF: [s3-004]-opentelemetry-for-ai-agents-implementing-observability-in-mc.pdf

## Compiled Summary

这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。

## Evidence Notes

- 文章开头引用的 2.2x 可靠性数据是一个有力的锚点，但我对其方法论细节存疑：Galileo 作为可观测性工具厂商，其调查样本可能存在自选择偏差（使用可观测性工具的团队本身就更注重工程质量）。综述引用这一数据时应注明其来源局限性。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
