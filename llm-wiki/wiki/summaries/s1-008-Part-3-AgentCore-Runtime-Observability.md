# Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability

## Source

- Raw note: `raw/notes/s1-008_Part_3_AgentCore_Runtime_Observability.md`
- 作者: Vadym Kazulkin（AWS Hero）
- 来源: DEV Community 技术博客
- 证据质量: high（AWS Hero 撰写的官方生态实践指南，包含大量控制台截图与配置步骤）

## Compiled Summary

这篇教程的价值在于它提供了一个从"零配置"到"全链路可观测"的完整闭环实践。与大多数停留在概念层面的文档不同，作者每一步都配有控制台截图与具体配置参数，这使得该文章具有极高的复现价值。从工程实践角度，我认为以下几点值得在综述中深入展开：
第一，ADOT 自动埋点与 Starter Toolkit 的协同设计体现了 AWS 在开发者体验上的深度思考。传统上，为 Python Agent 应用添加 OpenTelemetry 埋点需要开发者手动修改依赖、配置 exporter、初始化 tracer provider，步骤繁琐且容易出错。而 AgentCore Runtime Starter Toolkit 通过 `agentcore c

## Evidence Notes

- 第二，CloudWatch GenAI Observability 的专属面板设计值得重点关注。与通用云监控产品不同，该面板针对 LLM Agent 的工作特性提供了 Model Invocations、Trajectory View、Session 级追踪等专属视图，这些功能并非通用监控平台的简单扩展，而是深入理解了 Agent 执行范式后的针对性设计。特别是 Trajectory View 将 span 链以决策流的方式呈现，使开发者能够直观理解 Agent 的"思考过程"——模型何时决定调用工具、工具返回后模型如何重新规划下一步行动。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [LangSmith](entities/LangSmith.md), [Langfuse](entities/Langfuse.md), [AWS AgentCore](entities/AWS-AgentCore.md)
