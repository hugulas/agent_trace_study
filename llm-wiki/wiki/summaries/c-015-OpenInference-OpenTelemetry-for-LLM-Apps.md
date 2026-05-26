# What is OpenInference? OTel for LLM 2026

## Source

- Raw note: `raw/notes/c-015_OpenInference_OpenTelemetry_for_LLM_Apps.md`
- 证据质量: medium（作为生态概述和对比分析，时效性强，但带有 FutureAGI 自身产品视角）

## Compiled Summary

这篇博客虽然由 FutureAGI 发布，带有一定的产品视角，但它对 OpenInference 生态的描述是准确且全面的。特别有价值的是它对"为什么需要
OpenInference"的三力分析——LLM 追踪形状不同、框架插桩碎片化、OTel GenAI 标准尚未成型——这三点恰好解释了为什么一个独立于 OTel 核心项目的 AI
语义约定是必要的，而不是等待 OTel 官方来解决。如果当时没有 OpenInference 填补空白，2023-2024 年的 LLM
应用开发者将面临要么各自为战编写追踪逻辑、要么完全缺乏可观测性的困境。

## Evidence Notes

- 从工程落地角度，我认为 OpenInference 最大的隐性优势在于它的"monkey-patch 插桩"策略。与需要修改业务代码的显式追踪 API 不同，OpenInference 的
instrumentor 在运行时动态替换框架内部方法，这意味着开发者可以在完全不改动现有代码的情况下获得完整的追踪数据。这种零侵入性对于已经在生产环境运行的 Legacy Agent
系统尤其重要——它们往往缺乏测试覆盖，任何代码修改都伴随着 regression 风险，而运行时插桩规避了这一问题。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/OpenInference|OpenInference]], [[entities/Arize-Phoenix|Arize Phoenix]], [[entities/AWS-AgentCore|AWS AgentCore]], [[entities/Google-ADK-and-Vertex-AI|Google ADK and Vertex AI]]
