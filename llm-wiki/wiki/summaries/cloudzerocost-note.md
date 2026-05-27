# What Is AI Agent Observability? Why Cost Is What You're Missing

## Source

- Raw note: `raw/notes/cloudzerocost_note.md`
- Metadata: not available in note

## Compiled Summary

人工智能智能体可观测性是对自主智能体在生产环境中执行的多步骤工作流进行追踪、评估与成本核算的实践。与单次调用的大语言模型可观测性不同，它需要跨链式模型调用、工具调用与检索步骤进行分层追踪，并支持按任务、按用户、按功能进行复合成本归因。

## Evidence Notes

- 当前的大语言模型可观测性栈已经能够较好地处理单个模型调用：延迟、词元数量、错误率，甚至评估分数。但智能体让情况变得复杂。一个用户请求会产生指数级效应：触发一次规划步骤、三次工具调用、两次推理遍历、一次检索查询和最终响应。这相当于单次点击背后有七次模型调用和四次外部接口调用。观测工具会展示 11 个独立的追踪跨度，但没有一个能汇总到任务级成本，也无法说明是哪个客户触发了调用链、哪个工具静默失败，或者为什么人工智能账单在周四暴涨了 40%。这就是智能体可观测性问题——它是大语言模型可观测性的困难模式，而大多数团队只有在收到愤怒账单后才会意识到这一点。
- 随着智能体从实验走向生产，工程团队面临的核心问题是：**现有的观测基础设施无法覆盖智能体工作流的完整生命周期**。具体而言，研究动机包含以下三个层面：
- **成本归因缺失**。单次大语言模型调用的成本是可预测的——已知模型、已知词元数即可估算账单。但智能体任务的成本在运行时动态复合：智能体自主决定调用多少次、调用哪些工具、是否对失败步骤重试十二次才放弃。没有任务级成本汇总，就无法知道哪些工作流昂贵、哪些用户驱动了最高支出、哪些工具集成在重试上浪费资金。
- - **失败模式不可见**。当工具返回错误数据时，智能体不会停止，而是基于错误数据进行推理，可能再次调用同一工具，形成越来越昂贵的错误决策级联。传统的错误率监控在 HTTP 层面捕捉不到这种失败，因为每一次单独调用都是成功的。
- 文章提出的智能体可观测性框架建立在大语言模型可观测性之上，但针对智能体特有的运行时非确定性进行了能力扩展。框架核心包含以下五个技术维度：
- **分层追踪**。单个智能体任务产生的是跨度树而非扁平列表。需要通过父跨度（完整任务）关联子跨度（每个步骤），从而识别决策树中哪条分支驱动了成本、延迟或失败。
- - **复合成本归因**。关注任务的总美元成本，而非单次调用的成本。需要将成本标记到用户、租户、功能和工作流维度。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [Langfuse](entities/Langfuse.md), [Arize Phoenix](entities/Arize-Phoenix.md)
