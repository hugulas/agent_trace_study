# 使用 Python 与 Llama Stack 实现可观测性

## Source

- Raw note: `raw/notes/s1-011_How_to_implement_observability_with_Pyth.md`
- 作者: Michael Dawson（Red Hat，Node.js 技术指导委员会主席）
- 证据质量: medium（来自 Red Hat 官方开发者博客，作者为开源社区核心领袖，工程实践详实，但非经同行评审的学术论文）

## Compiled Summary

本文最突出的价值在于“从能跑到好用”的完整递进：第一步展示 Llama Stack 开箱即用的追踪能力，第二步指出其在真实场景下的结构性缺陷，第三步给出切实可行的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事结构，对技术写作者和综述材料组织都有很高参考价值。许多技术文档只展示成功路径，而本文敢于暴露中间状态的不足，反而大大增强了说服力，让读者理解为何需要额外的客户端插桩工作。

## Evidence Notes

- 从工程实现角度，作者选择在 Llama Stack 0.2.8 上进行实验，因为此前版本的 trace propagation 存在 bug，无法正确识别跨进程父 span。这说明 AI 基础设施的可观测性支持仍在快速迭代中，研究者在复现或落地时需密切关注版本兼容性，不能假设“装了最新版就万事大吉”。此外，作者提到 Llama Stack 自带的 `/v1/telemetry/events` API 虽可手动启停 span，但无法返回 span id，因此不能作为父 span 被后续调用引用——这一细节暴露了当前 AI 框架在可观测性 API 设计上的不成熟，也为 Llama Stack 后续版本改进指明了方向：要么开放 span 

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]]
