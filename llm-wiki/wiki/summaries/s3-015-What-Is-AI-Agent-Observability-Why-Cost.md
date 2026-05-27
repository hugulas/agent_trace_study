# What Is AI Agent Observability? Why Cost Is What You're Missing

## Source

- Raw note: `raw/notes/s3-015_What_Is_AI_Agent_Observability_Why_Cost_.md`
- 作者: Keith MacKenzie
- PDF: [s3-015]-what-is-ai-agent-observability-why-cost-is-the-signal-youre-.pdf

## Compiled Summary

这篇文章的价值在于它把「成本」从可观测性的附属指标提升为核心信号。

## Evidence Notes

- 在学术语境中，我们往往关注 trace 的完整性、span 的层级结构、诊断的准确率，却很少将「这次故障追踪花了多少美元」作为一级优化目标。本文提醒我们：在生产环境中，如果无法回答「服务这个客户请求从头到尾花了多少钱」，那么再精美的追踪图也无法说服 CFO 继续投入。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
