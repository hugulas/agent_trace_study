# 使用 Node.js 与 Llama Stack 实现可观测性

## Source

- Raw note: `raw/notes/s1-012_How_to_implement_observability_with_Node.md`
- 作者: Michael Dawson（Red Hat，Node.js 技术指导委员会主席）
- 证据质量: medium（来自 Red Hat 官方开发者博客，作者为 Node.js 社区核心领袖，工程实践详实，但非经同行评审的学术论文）

## Compiled Summary

本文的最大亮点在于其层层递进的教学结构：先展示 Llama Stack 服务端“零代码”追踪的便捷性，再揭示其在真实场景下的结构性不足，最后给出完整可复现的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事方式，对技术文档写作和综述材料组织都有很高参考价值，尤其适合向非可观测性背景的 AI 开发者传达追踪的重要性。许多技术教程倾向于只展示最终完美状态，而本文敢于暴露中间探索过程中的挫折（如 `/v1/telemetry/events` API 的局限），反而增强了内容的真实感与可信度，让读者更容易理解每个设计决策背后的动机。

## Evidence Notes

- 从工程细节来看，作者特别提醒 Llama Stack 0.2.8 版本的重要性——早期版本在 trace propagation 上存在 bug，会导致服务端无法正确识别跨进程父 span。这一版本依赖细节在实际落地中极易被忽视，却直接影响端到端追踪的成败。建议在团队内部的技术规范中，将框架版本兼容性检查列为可观测性落地的前置条件。此外，Node.js 示例中 `fetch: fetch` 的显式配置虽只是一行代码，背后反映的却是自动插桩与库内部实现之间的微妙耦合：如果 Llama Stack 客户端使用了自己的 HTTP 客户端而非全局 fetch，UndiciInstrumentation 将无法捕获其请求，整个追踪链就会在客户

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md)
