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

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/evaluation-and-benchmarking]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/OpenInference|OpenInference]], [[entities/LangSmith|LangSmith]], [[entities/Arize-Phoenix|Arize Phoenix]], [[entities/AWS-AgentCore|AWS AgentCore]]
