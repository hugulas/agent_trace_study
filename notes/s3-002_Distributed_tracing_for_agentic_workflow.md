---
tags:
  - agentic-workflow
  - distributed-tracing
  - opentelemetry
  - observability
  - mcp
  - llama-stack
  - red-hat
  - auto-instrumentation
  - context-propagation
  - production
aliases:
  - "s3-002"
  - "Red Hat OpenTelemetry Agent Tracing"
  - "OpenTelemetry Agentic Workflow 分布式追踪"
date: 2026-04-06
url: https://developers.redhat.com/articles/2026/04/06/distributed-tracing-agentic-workflows-opentelemetry
---

# Distributed tracing for agentic workflows with OpenTelemetry

## 核心信息

- **标题**: Distributed tracing for agentic workflows with OpenTelemetry
- **作者**: Fabio Massimo Ercoli
- **发布日期**: 2026 年 4 月 6 日
- **来源**: Red Hat Developer 官方博客
- **关联项目**: it-self-service-agent AI quickstart
- **PDF**: `[s3-002]-distributed-tracing-for-agentic-workflows-with-opentelemetry.pdf`
- **技术栈**: OpenTelemetry, Python, FastAPI, HTTPx, MCP, Llama Stack, Red Hat OpenShift
- **证据质量**: medium

## 内容摘要

这篇由 Red Hat 工程师 Fabio Massimo Ercoli 撰写的技术博客，
系统性地介绍了如何在多智能体 AI 系统中实现生产级的分布式追踪（distributed tracing）。
文章基于 it-self-service-agent AI quickstart 项目的真实开发经验，
详细阐述了利用 OpenTelemetry 为智能体工作流提供端到端可见性的完整工程方案。
该 quickstart 项目是 Red Hat AI 快速入门目录中的一员，
旨在展示如何在可靠的开源基础设施上运行行业特定的 AI 用例。

现代智能体应用通常涉及路由智能体（routing agents）、
专业智能体（specialist agents）、知识库、
Model Context Protocol（MCP）服务器以及外部系统之间的复杂交互。
这种高度分布式的架构使得生产环境中的故障排查变得异常困难——
当一次用户请求流经多个服务、触发多次模型调用、访问多个外部工具时，
缺乏清晰的可见性意味着工程师往往需要花费大量时间才能定位问题的根因。
分布式追踪通过为每个请求生成完整的调用链（trace），
提供了跨组件的因果关联视图，
从而将原本黑盒式的交互过程转化为可观测、可分析的执行图谱。
正如文中所述，agentic 应用各组件之间的交互复杂性，
使得没有清晰可见性的生产调试几乎不可能完成。

文章的核心方法论围绕 OpenTelemetry 的自动仪表化（auto-instrumentation）
与手动仪表化（manual instrumentation）相结合展开。
对于基于 REST API 的组件间通信，
作者明确推荐优先使用自动仪表化库，
具体而言是 OpenTelemetry HTTPx Instrumentation 和 OpenTelemetry FastAPI Instrumentation。
这些库的最大优势在于能够在不修改业务代码的情况下，
为所有 HTTP 请求和响应自动生成 span，
并且自动处理上下文传播（context propagation），
开发者无需手动将父调用上下文逐层传递给子调用。
在 it-self-service-agent quickstart 项目中，
作者团队将这些仪表化库添加到所有使用对应框架的模块中，
同时引入 OpenTelemetry API、SDK 和 exporter 的基础库，
构建了一套完整的遥测基础设施。
这种"优先自动、辅以手动"的策略，
是本文最具实践指导意义的核心主张之一。

然而，自动仪表化并不能覆盖所有场景。
在 MCP 服务器和 Llama Stack 的集成中，
由于这些组件可能不具备开箱即用的 OpenTelemetry 支持，
开发者需要手动注入追踪头以维持 trace context propagation。
文章展示了具体的代码实现：
通过 `opentelemetry.propagate.inject()` 方法
将 `traceparent` 和 `tracestate` 等 W3C 标准头部信息
注入到 MCP 服务器配置中，再传递给 Responses API。
这种机制确保了手动创建的 span 能够正确识别其父 span，
而下游的子操作——例如自动仪表化捕获的 HTTP 调用——
能够无缝地延续当前的 trace，
从而在整条链路上保持因果一致性。
具体实现中，作者在 agent-service 的 responses_agent.py 中引入了上述注入逻辑，
并在 MCP 服务器配置中添加了 `TELEMETRY_SINKS` 环境变量
以支持 console、sqlite 和 otel_trace 三种遥测输出。
这种多目标输出的设计充分考虑了不同部署环境下的差异化需求。

此外，文章还提供了 Llama Stack 的追踪配置示例，
展示了如何通过 Python 装饰器模式自动追踪 MCP 工具调用。
具体做法是为每个工具调用创建命名 span，
并附加 `mcp.tool.name`、`mcp.server.name` 等语义化属性，
使得追踪数据不仅包含时序信息，还携带了丰富的业务上下文。
装饰器内部通过 `get_request_headers()` 提取请求头部，
构建 carrier，再使用 `extract(carrier)` 恢复父上下文，
最终通过 `tracer.start_as_current_span()` 在正确的上下文中启动新 span。
作者特别提出了一个性能方面的最佳实践：
应避免在 span 属性中设置需要昂贵计算的值，
如果必须记录这类信息，应当尽可能采用惰性求值（lazy evaluation）策略，
以免追踪本身成为系统瓶颈。
另一个重要的最佳实践是关于异常处理的——
在发生异常时，应将堆栈跟踪和异常元数据附加到 span 上，
以便在 trace 视图中直接看到错误发生的精确位置和原因。
这些细节体现了作者在生产环境中摸爬滚打的真实经验。

文章的最后部分展示了一个来自 Red Hat OpenShift Distributed Tracing 的真实 trace 树示例。
这个示例清晰呈现了从 request-manager 到 agent-service、llamastack 乃至 snow-mcp-server 的完整调用链路，
每个节点的耗时一目了然。
读者可以从中直观看到一次请求如何在约 3.75 秒内流经多个服务：
request-manager 发出 POST 请求后，
调用链依次经过 mock-eventing-service、agent-service（处理 CloudEvents）、
llamastack（模型推理和向量存储查询）以及 snow-mcp-server（工具调用）。
其中模型推理调用（Llama Stack 的 `/v1/openai/v1/responses` 
及内部的 `InferenceRouter.openai_chat_completion` 和 `stream_tokens_openai_chat`）
占据了绝大部分请求耗时，
而外部工具调用（`mcp.tool.open_laptop_refresh_ticket`）仅需约 11.93 毫秒。
这个实例充分证明了分布式追踪在复杂智能体系统中定位性能瓶颈、
理解组件交互模式方面的实际工程价值。
对于正在调试类似系统的工程师而言，
这样的 trace 树能够在几秒钟内指出延迟的主要来源，
而不需要逐个组件地排查日志。

从工程实践的角度来看，
这篇文章的价值不仅在于提供了可复现的代码片段，
更在于它展示了一个真实企业级项目从零开始构建可观测性的完整决策路径：
何时使用自动仪表化、何时必须手动干预、
如何在异构组件之间保持追踪上下文、
以及如何为业务操作附加有意义的语义属性。
这些经验对于任何正在将智能体系统从原型推向生产的工程团队都具有直接的指导意义。
文章虽然是博客形式，但其技术深度和实操细节并不逊色于技术白皮书，
堪称社区中难得的工程宝藏。

## 关键要点

1. **自动仪表化优先原则**
   对于 REST API 通信，优先使用 OpenTelemetry HTTPx 和 FastAPI Instrumentation 库，
   实现零侵入式的请求追踪。
   自动仪表化库还能自动处理上下文传播，
   免除手动传递 parent context 的负担。

2. **上下文传播是核心挑战**
   跨组件的 trace 连续性依赖于正确的 context propagation。
   在异构系统或尚不支持 OpenTelemetry 的组件（如 MCP 服务器）中，
   需通过 `opentelemetry.propagate.inject()` 手动注入 W3C trace 头部
   （`traceparent`、`tracestate`）。

3. **MCP 工具追踪的装饰器模式**
   利用 Python 装饰器为每个 MCP 工具调用生成带语义属性的 span，
   通过 `extract()` 恢复父上下文、
   通过 `start_as_current_span()` 在正确上下文中启动新 span，
   实现工具层级的精细化观测。

4. **性能与最佳实践**
   避免在 span 属性中进行昂贵计算，推荐惰性求值；
   发生异常时应将堆栈跟踪和异常元数据附加到 span，
   以便在 trace 视图中直接定位错误。

5. **多组件全覆盖**
   完整的追踪方案需同时覆盖应用工作负载（agent-service）、
   消息中间件（mock-eventing-service）、
   模型服务层（Llama Stack）和外部工具层（MCP 服务器）。

6. **企业级验证**
   Red Hat OpenShift Distributed Tracing 提供了从请求入口到外部工具调用的完整 trace 树，
   展示了 3.75 秒请求中各阶段的精确耗时分布，
   验证了方案在生产环境中的可行性。

7. **遥测输出的灵活性**
   通过 `TELEMETRY_SINKS` 环境变量可配置多种遥测输出目标
   （console、sqlite、otel_trace），
   便于开发调试和生产监控的差异化需求。

8. **系列文章的系统积累**
   本文是 it-self-service-agent AI quickstart 系列博文的第六篇，
   该系列从 IT 流程自动化、Slack 与 ServiceNow 集成、
   提示工程到可观测性，形成了一个完整的知识积累体系。

## 与综述的关联

- 本文与综述中智能体系统可观测性（observability）章节直接相关，
  提供了来自 Red Hat 这一企业级开源社区的一线工程实践，
  填补了学术文献中生产落地细节不足的空白。

- 与 c-003（OpenTelemetry AI Agent Observability）和 
  c-015（OpenInference OpenTelemetry for LLM Apps）形成规范定义与落地实践的对照关系：
  c-003 和 c-015 定义了应该如何对 AI 智能体进行仪表化，
  而本文展示了在真实的 Red Hat AI quickstart 项目中如何一步步实现这些规范。

- MCP 服务器的追踪头注入模式，
  与综述中讨论的工具调用可追踪性（tool-call traceability）需求高度契合。
  本文可作为 c-012（Agent Audit Trail: A Standard Logging Format）中工具行为记录要求的具体实现参照。

- 文中展示的完整 trace 树示例，
  为综述中"可观测性基础设施"小节提供了具体的企业级案例。
  这个示例可与 LangSmith 的 run tree、AgentTrace 的日志结构进行可视化层面的横向比较，
  分析不同方案在信息密度、呈现方式和查询能力上的差异。

- 自动仪表化与手动仪表化的分层策略，
  可作为综述讨论智能体系统遥测架构设计时的关键维度。
  网络层通信交给自动仪表化，
  业务逻辑和跨协议边界（如 MCP）则辅以手动 span，
  这种分层思路对于设计可扩展的遥测架构非常有益。

- 本文与 a-007（Monitoring Claude Code Docs）和 
  a-013（Advanced Configuration Codex Observability）共同构成了业界对 AI 编程助手和智能体系统可观测性实践的完整图景，
  可在综述的行业实践部分并列引用。

- 关于 Llama Stack 的追踪配置经验，
  与综述中讨论的开源模型服务层可观测性相关，
  可与 vLLM、TGI 等推理服务的监控方案进行对比。

- 本文的实践案例来自 IT 自助服务场景，
  这种企业 IT 自动化场景与综述中讨论的企业级智能体部署需求高度吻合，
  可作为"智能体在企业环境中落地"的典型案例。

## 我的笔记

- 这篇博客是智能体可观测性领域中少有的从企业级生产环境出发的实操指南，
  与学术论文偏重理论框架和实验评估的风格形成了良好互补。
  Red Hat 工程师基于真实 quickstart 项目总结的经验，
  对于计划将智能体系统投入生产的团队具有很强的参考价值。
  尤其是文中提到的"为组件添加仪表化库"的决策过程，
  能够帮助读者理解在实际项目中引入 OpenTelemetry 的优先级排序。

- 自动仪表化与手动仪表化的分层策略值得在综述中专门讨论。
  网络层通信交给自动仪表化（HTTPx、FastAPI），
  业务逻辑和跨协议边界（如 MCP、自定义工具调用）则辅以手动 span，
  这种分层思路对于设计可扩展的遥测架构非常有益。
  综述可将此总结为"渐进式仪表化"策略，
  建议团队从自动仪表化入手，逐步对关键业务路径补充手动 span。

- 通过 `traceparent` 头部注入 MCP 服务器的模式，
  对于理解跨协议上下文传播机制很有启发。
  MCP 作为新兴的上下文协议，其可观测性支持尚不成熟，
  本文提供了一种可行的过渡方案。
  在综述中可将此归类为"协议桥接式传播"（protocol-bridging propagation），
  并与其他跨协议追踪方案（如 gRPC-HTTP 桥接、消息队列上下文传递）进行比较。

- 文中提到的"避免在 span 属性中设置昂贵计算值"这一建议，
  在实际工程中常被忽视，但对于高频调用的智能体系统而言至关重要。
  综述中可在最佳实践部分引用此观点，并进一步扩展：
  对于需要记录大量结构化信息的场景，
  可考虑使用 span 事件（events）或关联日志（correlated logs）而非属性，
  以平衡信息丰富度和性能开销。

- 从 trace 树示例中可以观察到，
  模型推理调用（`/v1/openai/v1/responses`）占据了绝大部分请求耗时（约 3.54 秒），
  而外部工具调用（`mcp.tool.open_laptop_refresh_ticket`）仅需约 11.93 毫秒。
  这一数据有助于综述讨论智能体系统的性能瓶颈分布，
  说明在大多数智能体工作流中，
  模型推理延迟仍然是端到端延迟的主导因素，
  工具调用的优化空间相对有限。

- `TELEMETRY_SINKS` 的多目标输出设计很有启发。
  console 输出便于本地开发调试，
  sqlite 便于离线分析和小规模部署，
  otel_trace 则用于对接企业级可观测性平台。
  这种分层输出策略降低了开发者在不同环境中切换的成本，
  综述可在讨论"开发-生产遥测一致性"时引用。

- 建议将本文的 OpenTelemetry trace 树与 LangSmith 的 run tree、
  AgentTrace 的结构化日志、以及 c-011（AgentTrace）中定义的轨迹格式
  进行语义层面的对比分析。
  OpenTelemetry 的 span 模型更偏向通用分布式系统的请求追踪，
  而 LangSmith 和 AgentTrace 的模型更面向 LLM 特定的概念
  （如 token 用量、提示模板版本、模型参数）。
  综述可分析这两种建模思路各自的适用场景和互补性。

- 本文的一个潜在局限是案例相对单一——主要围绕 IT 自助服务场景。
  综述在引用时应指出，虽然技术方案具有通用性，
  但在更复杂的编排模式（如多智能体协作、竞争性智能体、长时间运行的智能体工作流）中，
  trace 的规模和结构复杂度可能会显著增加，
  需要额外的采样、聚合和归档策略。
  此外，本文未深入讨论分布式追踪数据的存储成本、
  保留期限和隐私合规等问题，
  这些也是生产部署中不可忽视的维度。
