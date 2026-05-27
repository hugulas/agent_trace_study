# 使用 Datadog LLM Observability 监控、排查与优化 AI Agent

## Source

- Raw note: `raw/notes/s2-006_Monitor_troubleshoot_and_improve_AI_agen.md`
- 作者: Barry Eom, Jordan Obey（Senior Technical Content Writer）
- 证据质量: medium-high（基于官方产品文档，包含具体技术方案和可视化设计说明）

## Compiled Summary

Datadog 这篇博客的技术价值在于它非常具体地描述了多 Agent 可观测性的痛点，并给出了清晰的产品化解决方案。与许多停留在概念层面的厂商文章不同，本文深入到了可视化设计的细节——为什么火焰图不行、为什么 Span 列表不行、以及基于图的视图如何解决这些问题。这种从第一性原理出发的分析方式，使文章具有很高的技术可信度，即使作为非学术来源也值得信赖。

## Evidence Notes

- 从框架适配策略来看，Datadog 选择同时支持 LangGraph、CrewAI 和 OpenAI Agent SDK 三大主流框架，这既是市场需求驱动的结果，也反映了当前 Agent 生态碎片化的现状。每个框架都有自己的状态管理、任务编排和工具调用模式，要在统一界面中呈现它们的执行流，需要相当复杂的适配逻辑。Datadog 的做法可能是在 SDK 层面对各框架进行 instrumentation hook，捕获框架内部事件并转换为标准追踪格式。这种策略的优势是用户无需修改应用代码即可获得可观测性；劣势是当框架版本升级或内部 API 变化时，适配层可能需要频繁更新。综述在讨论框架生态时，可以将这一点作为 "Agent 可观测性 v

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
