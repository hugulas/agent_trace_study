# GenAIOps on AWS: 端到端可观测性栈

## Source

- Raw note: `raw/notes/s1-010_GenAIOps_on_AWS_End-to-End_Observability.md`
- 作者: Shoaibali Mir
- 证据质量: high

## Compiled Summary

这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做"
同时讲透的工业博客。

## Evidence Notes

- 开篇的凌晨 3 点 PagerDuty 告警场景极具代入感，
它准确击中了从传统微服务转型到 GenAI 系统的工程师们的共同痛点：
我们习惯了用 HTTP 状态码判断健康，
但 GenAI 系统让这套方法论彻底失效。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [OpenInference](entities/OpenInference.md), [LangSmith](entities/LangSmith.md), [Arize Phoenix](entities/Arize-Phoenix.md), [AWS AgentCore](entities/AWS-AgentCore.md)
