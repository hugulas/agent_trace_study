# Google Cloud Trace observability for ADK

## Source

- Raw note: `raw/notes/s1-001_Google_Cloud_Trace_observability_for_ADK.md`
- Metadata: not available in note

## Compiled Summary

Google 将 Cloud Trace 与 ADK 深度集成的策略非常清晰：
本地用 Web UI 做开发调试，云端用 Cloud Trace 做生产观测，
两者形成完整的开发生命周期闭环。

## Evidence Notes

- 这种分层可观测性设计避免了开发者在不同阶段切换工具链的认知负担，
从工程体验角度来说是极为出色的设计。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [AWS AgentCore](entities/AWS-AgentCore.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md)
