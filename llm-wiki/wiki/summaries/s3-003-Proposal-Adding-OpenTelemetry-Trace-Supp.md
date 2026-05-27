# [Proposal] Adding OpenTelemetry Trace Support to MCP

## Source

- Raw note: `raw/notes/s3-003_Proposal_Adding_OpenTelemetry_Trace_Supp.md`
- 作者: altryne（提案发起人，GitHub 社区成员）
- 证据质量: high
- PDF: [s3-003]-proposal-adding-opentelemetry-trace-support-to-mcp.pdf

## Compiled Summary

这篇 GitHub Discussion 是我所读到的关于 MCP 可观测性最深入、最富张力的原始技术资料之一。其价值不仅在于提案本身的设计细节，更在于围绕该提案展开的多元观点碰撞，这些碰撞暴露了当前 Agent 可观测性领域许多尚未被充分讨论的深层问题。

## Evidence Notes

- 我认同 altryne 对 MCP 黑箱问题的诊断：当 Agent 调用外部工具时，如果无法看到工具内部的执行细节，调试效率将大打折扣。文中以 Sarah 调试客服 Agent 调用 Notion 工具的场景为例，生动地展示了 `notion_api_request` span 如何帮助开发者将瓶颈定位到 Notion API 本身而非 MCP 服务器逻辑或网络层。这一用例具有很强的现实说服力。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [LangSmith](entities/LangSmith.md), [Arize Phoenix](entities/Arize-Phoenix.md), [Braintrust](entities/Braintrust.md)
