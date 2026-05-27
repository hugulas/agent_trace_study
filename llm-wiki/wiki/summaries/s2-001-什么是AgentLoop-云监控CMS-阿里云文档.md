# 阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台

## Source

- Raw note: `raw/notes/s2-001_什么是AgentLoop-云监控CMS__阿里云文档.md`
- 来源: 阿里云官方产品文档 · 云监控 2.0 · AI 应用可观测
- PDF: [s2-001]-什么是agentloop-云监控cms--阿里云文档.pdf

## Compiled Summary

AgentLoop 的文档给我最深刻的印象是：它将"可观测性"的定义从
"看见发生了什么"推进到了"用看见的东西驱动系统进化"。这不是简单的
功能叠加，而是产品哲学层面的跃迁。传统的 APM（Application Performance
Monitoring）关注的是系统健康度——CPU 是否过高、内存是否泄漏、请求是否
超时；而 AgentLoop 关注的是 Agent 的"成长度"——它是否在不断变得更好、
更稳定、更经济、更符合用户预期。这种视角转换对于整个可观测性领域都具有
启发意义，也预示着可观测性产品正在从"运维工具"向"效果优化平台"演进。

## Evidence Notes

- 从架构视角看，AgentLoop 的五大功能模块（可观测性、Dataset、评估、实验、
记忆）恰好对应了一个 AI 应用从"上线运行"到"持续优化"的完整生命周期。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [Arize Phoenix](entities/Arize-Phoenix.md), [AWS AgentCore](entities/AWS-AgentCore.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md)
