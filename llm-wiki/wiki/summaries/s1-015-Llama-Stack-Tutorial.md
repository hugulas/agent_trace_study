# Llama Stack Tutorial

## Source

- Raw note: `raw/notes/s1-015_Llama_Stack_Tutorial.md`
- 来源: Red Hat AI Services Business Unit（rh-aiservices-bu）
- 证据质量: medium（官方教程，实践导向，内容覆盖较广但深度有限）

## Compiled Summary

该教程虽然内容篇幅不长，但作为 Red Hat 官方背书的学习材料，其技术选型与内容编排具有显著的参考价值。从工程实践角度，我认为 Llama Stack 的架构设计体现了当前开源大模型应用框架的几个关键趋势：
第一，统一接口层的重要性日益凸显。随着模型部署方式的多样化（本地 Ollama、自托管 vLLM、云 Bedrock 等），开发者越来越需要一个与后端解耦的抽象层。Llama Stack 的统一接口不仅简化了代码维护，也为 A/B 测试不同模型提供了便利——开发者可以在不修改业务逻辑的情况下切换后端模型，仅需调整配置即可。

## Evidence Notes

- 第二，内置遥测是框架竞争力的核心维度之一。本教程将可观测性明确纳入中级必修内容，说明社区已经认识到：一个缺乏观测能力的框架难以进入生产环境。Llama Stack 选择将 OpenTelemetry 作为内置遥测方案，而非自建专用协议，这一决策符合云原生生态的标准化趋势，也降低了与企业现有监控体系的集成成本。然而，需要注意的是，当前 Llama Stack 的内置遥测在 Agent 语义层面的覆盖仍有不足。根据社区讨论，现有版本主要提供 `llama_stack_prompt_tokens_total`、`llama_stack_completion_tokens_total` 与 `llama_stack_tokens_total

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [LangSmith](entities/LangSmith.md), [AWS AgentCore](entities/AWS-AgentCore.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md)
