# Trajectory Format | Hermes Agent

## Source

- Raw note: `raw/notes/c-013_Hermes_Agent_Trajectory_Format.md`
- 作者: Nous Research（Hermes Agent 开发团队）
- 证据质量: high
- PDF: [c-013]-hermes-agent-trajectory-format.pdf

## Compiled Summary

Hermes Agent 的轨迹格式文档是我目前见过的最详尽的训练数据工程规范之一。它的价值不仅在于定义了一种格式，更在于展示了一个完整的"从运行时到训练集"的数据流水线设计。其中最令我印象深刻的是推理内容的归一化策略——通过强制每个 gpt 轮次包含 <think> 块，即使模型未产生显式推理，也保证了训练数据在格式上的绝对一致性。这种"宁缺勿滥"的严格性对于大规模预训练或微调至关重要，因为数据格式的不一致是导致训练失败或性能退化的常见原因。在分布式训练环境中，如果不同 worker 加载的数据具有不同的字段结构或内容格式，不仅会导致训练崩溃，还可能引入难以察觉的模型行为偏差。

## Evidence Notes

- 工具调用的 XML-wrapped JSON 表示是一个值得深入分析的设计选择。与 OpenAI API 中工具调用作为独立消息对象的方案相比，Hermes 的方案将工具调用嵌入在 assistant 消息的文本内容中。这种设计的优势在于：它统一了"文本生成"和"工具调用"两种输出模式，模型始终生成文本，而工具调用只是文本中的特殊结构。这简化了训练目标的定义（统一的语言建模损失），但也可能增加了解析的复杂度——需要在文本中准确地提取 XML 块。在综述中讨论 agent 输出格式时，可以对比 Hermes 的 XML 方案、OpenAI 的 JSON schema 约束方案、以及纯 function calling API 方案各自

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [AgentTrace](entities/AgentTrace.md)
