---
tags:
  - observability
  - OpenTelemetry
  - LlamaStack
  - Node.js
  - JavaScript
  - distributed-tracing
  - AI-infrastructure
  - RedHat
  - Jaeger
  - OTLP
  - Undici
  - W3C-Trace-Context
  - RAG
  - production-observability
aliases:
  - "s1-012 Node.js与Llama Stack可观测性实践"
  - "Red Hat Node.js Llama Stack 分布式追踪"
  - "Node.js AI应用 OpenTelemetry 插桩指南"
date: 2025-06-12
url: https://developers.redhat.com/articles/2025/06/12/how-implement-observability-nodejs-and-llama-stack
---

# 使用 Node.js 与 Llama Stack 实现可观测性

## 核心信息

- **标题**: How to implement observability with Node.js and Llama Stack
- **作者**: Michael Dawson（Red Hat，Node.js 技术指导委员会主席）
- **发布日期**: 2025-06-12
- **来源类型**: 技术博客/实战教程
- **发布平台**: Red Hat Developer
- **系列定位**: Node.js + Llama Stack 系列第四篇（最终篇）
- **关联技术栈**: Node.js, JavaScript, Llama Stack, OpenTelemetry, Jaeger, Undici, Ollama, Podman
- **本地材料**: `[s1-012]-how-to-implement-observability-with-nodejs-and-llama-stack.pdf`
- **证据质量**: medium（来自 Red Hat 官方开发者博客，作者为 Node.js 社区核心领袖，工程实践详实，但非经同行评审的学术论文）

## 内容摘要

这篇技术博客由 Red Hat 的 Michael Dawson 撰写，详尽演示了如何在基于 Node.js 的 AI 应用中，结合 Llama Stack 与 OpenTelemetry 构建分布式追踪能力。文章属于该作者探索 Llama Stack 与 Node.js 生态融合使用的系列第四篇，前三篇分别涵盖了 Llama Stack 入门、检索增强生成（RAG）以及 AI 安全护栏的实现。本文将焦点放在可观测性上，尤其深入探讨了分布式追踪的完整落地路径，从概念阐释、工具选型、服务端配置到客户端插桩，形成了一套可直接复现的工程指南，为 Node.js AI 开发者提供了权威参考。

文章开篇界定了可观测性的三大基石：日志记录（logging）、指标采集（metrics）与分布式追踪（distributed tracing），并指出在 Node.js 生产应用中，Node.js Reference Architecture 已对这三类组件的集成给出了官方推荐。随后引入 OpenTelemetry，强调其正迅速成为可观测性领域的事实标准，且对 JavaScript/Node.js 提供完善支持。OpenTelemetry 的核心价值在于既能通过 API 进行手动插桩，也能借助预置包对现有库实现自动插桩，让开发者在不大幅修改业务代码的前提下获得追踪能力。需要注意的是，OpenTelemetry 仅负责生成和导出追踪数据，后续接收、存储与可视化需要额外工具；作者选用 Jaeger 承担这一角色，并给出了基于 Podman 的容器启动命令，将 Jaeger UI 暴露于 16686 端口、OTLP 接收端点暴露于 4318 端口。

在服务端的搭建上，作者沿用 Ollama 作为模型推理后端，通过 Llama Stack 的容器化发行版快速部署。关键步骤包括升级至 Llama Stack 0.2.8（该版本修复了此前影响追踪传播的关键缺陷），设置环境变量 `OTEL_SERVICE_NAME=LlamaStack` 与 `TELEMETRY_SINKS=otel_trace,otel_metric`，并在从容器内提取的 `run.yaml` 模板中配置 `otel_metric_endpoint` 和 `otel_trace_endpoint`，使其指向 Jaeger 的 OTLP HTTP 端点。完成这些配置后，无需触碰任何应用代码，Llama Stack 服务端即可自动为每一次 API 调用生成 span 并上报至 Jaeger。作者以先前系列中开发的 RAG 智能体应用 `llama-stack-agent-rag.mjs` 为例，在 Jaeger 中成功观察到向量数据库创建、文档检索、模型推理等每一步 API 调用对应的独立 span，并展示了展开 span 后可见的端点路径与请求参数等丰富细节。

然而，作者很快揭示了这种“服务端单点追踪”模式的根本短板：所有 API 调用产生的 span 彼此割裂，缺少能够代表一次完整业务请求的顶层父 span。在单请求串行场景下这或许无伤大雅，但在真实生产环境中，多个客户端应用可能并发访问 Llama Stack，导致 Jaeger 中充斥着大量无法归属的离散 span，排查问题时犹如大海捞针。作者曾尝试利用 Llama Stack 内置的 `/v1/telemetry/events` API 手动创建父 span，但实验发现该 API 不返回 span id，无法被后续调用引用为父节点，因此不得不转向在客户端应用中直接集成 OpenTelemetry SDK。

客户端插桩是本文的技术重头戏。作者使用 `@opentelemetry/sdk-node` 构建 `NodeSDK` 实例，配置 `OTLPTraceExporter` 将追踪数据发送至 Jaeger，并引入 `@opentelemetry/instrumentation-undici` 对 Node.js 底层提供全局 `fetch` 的 Undici 库进行自动插桩，从而捕获 Llama Stack 客户端发出的所有 HTTP 请求。为了确保 Llama Stack 客户端真正使用 Node.js 全局 `fetch` 而非内部自定义实现，作者在实例化客户端时显式传入 `fetch: fetch` 参数。更为关键的是配置 `W3CTraceContextPropagator` 作为传播器，这是实现跨进程链路串联的核心机制。在应用代码层面，作者使用 `trace.getTracer` 获取 tracer 实例，并通过 `startActiveSpan` 将整个 RAG 工作流包裹在一个以 `Node.js LlamaStack request - ${randomUUID()}` 命名的顶层 span 中。此外，为应对 Node.js 进程可能在 span 处理器默认 30 秒刷新间隔前退出的问题，作者添加了 40 秒的延迟等待，确保所有 span 都能完整送达 Jaeger。

当插桩后的应用再次运行时，Jaeger 中出现了名为 `NodeAgentRAG` 的新服务。展开其顶层 span 后，可以清晰看到三层嵌套结构：最上层是应用代码中手动创建的 `NodeAgentRAG` 父 span；其下是由 Undici 自动插桩生成的 outgoing GET 请求 span；最底层则是 Llama Stack 服务端处理该请求时产生的子 span。这种端到端的统一追踪视图，不仅使并发请求拥有了明确的归属边界，还能直观呈现完整请求耗时与各阶段细粒度耗时，为性能分析与故障定位提供了强有力的可视化手段。文章最后提醒读者，更复杂的应用还可对数据库访问等额外组件进行插桩，并务必审查 span 中是否包含敏感信息，严控 Jaeger UI 的访问权限。

## 关键要点

1. **可观测性三大支柱**: 日志、指标、分布式追踪构成了现代云原生应用可观测性的核心。本文深入实践分布式追踪，并指出 Node.js Reference Architecture 已对相关组件选型给出官方建议，Red Hat 企业级用户可直接参考该架构进行落地。对于 AI 智能体系统，这三者的结合尤为重要：日志捕获离散事件，指标量化资源消耗，分布式追踪还原端到端调用链路。

2. **OpenTelemetry 与 Jaeger 的分工协作**: OpenTelemetry 负责生成和导出追踪数据，Jaeger 负责接收、存储与可视化；两者通过 OTLP HTTP 协议对接。这种职责分离符合云原生可观测性架构的设计原则，也让开发者可以灵活替换后端（例如将 Jaeger 替换为 Tempo 或 AWS X-Ray），避免供应商锁定，保持架构的开放性与灵活性。

3. **Llama Stack 服务端开箱即用追踪**: 通过环境变量与 `run.yaml` 配置 OTLP 端点，Llama Stack 0.2.8 可自动上报服务端 span，无需修改业务代码。这降低了可观测性的初始接入门槛，让团队可以快速获得 API 级别的性能数据，实现“先看到、再优化”的渐进式改进策略。

4. **版本兼容性至关重要**: 必须升级至 Llama Stack 0.2.8 以上版本，早期版本的 trace propagation 存在缺陷，会导致跨进程父 span 识别失败，追踪链在服务端断裂。版本依赖是实际落地中极易被忽视却直接影响成败的细节，建议在技术选型文档中明确标注最低版本要求，并在 CI/CD 流程中加入版本检查。

5. **服务端追踪的结构性缺陷**: 仅有服务端 span 时，各 API 调用彼此孤立，缺少业务级父 span，无法应对多并发场景下的链路归属与性能分析需求。作者以“大海捞针”形容在 Jaeger 中排查无父 span 的离散追踪数据，形象说明了这一痛点。这也解释了为何许多团队虽然“装了监控”却依然排障困难，根源在于缺乏业务语义的链路聚合。

6. **Node.js 客户端插桩五要素**:
   - `NodeSDK` + `OTLPTraceExporter` 构建数据上报链路，指向 Jaeger 的 OTLP 端点；
   - `UndiciInstrumentation` 自动捕获 Llama Stack 客户端通过 Node.js 全局 `fetch` 发出的 HTTP 请求；
   - 显式设置 `fetch: fetch` 确保 Llama Stack 客户端实例使用 Node.js 全局 fetch，从而被 Undici 插桩覆盖；
   - `W3CTraceContextPropagator` 将 W3C Trace Context 标准格式注入 HTTP 请求头，实现跨进程传播；
   - 应用层使用 `startActiveSpan` 创建顶层父 span，聚合离散调用为完整业务链路，使并发请求在 Jaeger 中拥有清晰归属。

7. **跨进程传播的标准化机制**: 客户端通过 `traceparent` HTTP 头（格式为 `version-traceid-spanid-sampled`）将追踪上下文传递至 Llama Stack 服务端。服务端识别该头部后，将其设为本地新生成 span 的父节点，从而实现端到端关联。这一机制遵循 W3C Trace Context 国际标准，保证了与任何兼容该标准的中间件或服务的互操作性。

8. **进程退出与数据刷新问题**: Node.js 默认 span 处理器每 30 秒批量刷新一次，若进程提前退出可能导致数据丢失。示例中通过 40 秒 `setTimeout` 延迟等待规避此问题，但作者也坦承这并非生产最佳实践。生产环境应使用更优雅的关闭钩子（shutdown hook），在收到 SIGTERM/SIGINT 信号时主动调用 SDK 的 flush 与 shutdown 方法，确保数据完整性。

9. **安全与隐私风险**: 追踪数据中可能包含向量数据库配置、请求参数乃至提示词内容。作者在示例中展示了 `vector_db_id`、`embedding_model`、`embedding_dimension` 等字段以明文形式进入 span。在涉及企业数据或个人信息（PII）的场景下，这直接关联到合规风险，必须配套字段级脱敏、采样过滤与访问控制机制。

10. **微服务与复杂系统的扩展性**: 对于更复杂的智能体应用，可进一步对数据库访问、缓存读写、外部 API 调用等组件进行插桩，或创建额外的 subspan 以获取更细粒度的性能信息。这说明 OpenTelemetry 插桩是一个可渐进增强的过程，团队可以根据实际需求逐步扩展追踪覆盖范围，而不必一次性追求全量覆盖，降低了采用门槛。

11. **自动插桩的边界与限制**: `UndiciInstrumentation` 只能覆盖使用 Node.js 全局 fetch 的请求，若库内部使用自定义 HTTP 客户端则无法捕获。这提示开发者在使用自动插桩时必须验证其覆盖范围，必要时结合手动插桩补足盲区。`fetch: fetch` 的显式配置就是一个典型的验证步骤。

12. **RAG 工作流作为追踪示例**: 本文以 RAG 智能体为具体案例，展示了向量数据库创建、文档检索、模型推理等步骤在分布式追踪中的可视化效果。这为理解 AI 工作流的可观测性需求提供了具象参考，也说明复杂 AI 链路天然需要分布式追踪来还原其时序与依赖关系。每一个步骤的性能波动都可能影响最终用户体验，追踪数据是识别瓶颈的关键依据。

13. **randomUUID 与请求标识**: 作者在顶层 span 命名中使用 `randomUUID()` 为每次请求生成唯一标识，这种做法在并发场景下尤为重要，因为它确保了每个业务请求在 Jaeger 中都有独立的追踪入口，避免了不同请求的 span 相互混淆，是生产级追踪的基本实践。

14. **run.yaml 配置分离**: 将 OTLP 端点配置放在 `run.yaml` 而非硬编码在代码中，符合十二要素应用（Twelve-Factor App）的配置管理原则，使得同一容器镜像可以在不同环境中灵活切换可观测性后端，无需重新构建。

15. **Node.js Reference Architecture 的指导价值**: 文章提到 Node.js Reference Architecture 已对可观测性组件选型给出官方建议，这为企业级 Node.js 应用的可观测性建设提供了权威参考，减少了技术选型的不确定性。

## 与综述的关联

本文是 Red Hat 官方出品的 Node.js + Llama Stack 可观测性权威实践，对于综述中讨论 AI 智能体系统的工程化部署、生产级可观测性架构以及跨语言追踪标准化等主题，具有直接的材料支撑价值：

- **智能体框架的可观测性原生集成**: Llama Stack 通过内置 telemetry provider 与 OpenTelemetry 无缝对接，表明现代 AI 基础设施正在将可观测性视为核心能力而非附加功能。这一趋势与综述中“智能体系统需要系统化追踪支持”的论点形成呼应，也说明业界正在从 demo 级原型向生产级系统演进。对于综述中关于“AI 框架可观测性成熟度”的讨论，本文提供了来自工业界第一线的证据。

- **端到端追踪的实践必要性**: 文章用对比方式清晰展示了“仅服务端追踪”与“客户端+服务端联合追踪”的差异。前者虽零代码实现，但在并发场景下完全失效；后者通过应用层插桩与 W3C 标准传播，才能真正还原完整业务链路。这为综述中关于“智能体-模型-工具多层调用链需要完整链路追踪”的论述提供了来自工业界的实证，也为“为何服务端日志不足以支撑复杂 AI 系统排障”提供了论据。

- **跨语言生态的一致性**: 本文与 s1-011（Python 版本）构成了同一主题的跨语言双篇。两者在架构设计、OpenTelemetry 语义约定、W3C Trace Context 传播机制上完全一致，仅在具体 SDK 与自动插桩库（Node.js 用 `UndiciInstrumentation`，Python 用 `HTTPXClientInstrumentor`）上因语言生态而异。这种一致性为综述讨论多语言智能体系统的统一可观测性标准提供了有力证据，也说明 OpenTelemetry 的标准化价值已穿透语言边界，成为异构系统的共同底座。

- **云原生可观测性栈的成熟**: 文章采用 OpenTelemetry + Jaeger + W3C Trace Context 的组合，完全遵循云原生计算基金会（CNCF）生态标准。这说明 AI 应用的可观测性正在快速融入现有云原生监控体系，而非另起炉灶。对于综述中关于“智能体监控应与现有 DevOps 基础设施兼容”的观点，本文提供了具体的技术路径和配置范例。

- **工程化落地的版本与细节陷阱**: 作者强调 Llama Stack 0.2.8 版本修复了 trace propagation 的关键 bug，以及 `fetch: fetch` 显式配置的必要性，说明即使有了标准化工具链，实际落地时仍需关注框架版本、库内部实现细节等工程化陷阱。这为综述中关于“智能体系统可观测性落地需要综合考虑版本兼容性、库实现与配置细节”的论述提供了第一手经验。

- **渐进式可观测性建设路径**: 从服务端自动追踪到客户端手动插桩的渐进过程，为综述中讨论“智能体系统可观测性落地策略”提供了方法论参考。团队不必一次性完成所有插桩工作，而是可以随着系统复杂度增长逐步扩展追踪覆盖范围，这种务实策略在企业落地中更具可操作性。

## 我的笔记

本文的最大亮点在于其层层递进的教学结构：先展示 Llama Stack 服务端“零代码”追踪的便捷性，再揭示其在真实场景下的结构性不足，最后给出完整可复现的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事方式，对技术文档写作和综述材料组织都有很高参考价值，尤其适合向非可观测性背景的 AI 开发者传达追踪的重要性。许多技术教程倾向于只展示最终完美状态，而本文敢于暴露中间探索过程中的挫折（如 `/v1/telemetry/events` API 的局限），反而增强了内容的真实感与可信度，让读者更容易理解每个设计决策背后的动机。

从工程细节来看，作者特别提醒 Llama Stack 0.2.8 版本的重要性——早期版本在 trace propagation 上存在 bug，会导致服务端无法正确识别跨进程父 span。这一版本依赖细节在实际落地中极易被忽视，却直接影响端到端追踪的成败。建议在团队内部的技术规范中，将框架版本兼容性检查列为可观测性落地的前置条件。此外，Node.js 示例中 `fetch: fetch` 的显式配置虽只是一行代码，背后反映的却是自动插桩与库内部实现之间的微妙耦合：如果 Llama Stack 客户端使用了自己的 HTTP 客户端而非全局 fetch，UndiciInstrumentation 将无法捕获其请求，整个追踪链就会在客户端侧断裂。这提示我们在为智能体框架设计可观测性方案时，必须深入了解其底层网络库选型，不能假设“自动插桩就能覆盖一切”。

关于进程退出时的数据刷新问题，作者采用的 40 秒 `setTimeout` 方案虽在实验环境中可行，但在生产微服务或 serverless 场景下显然不够优雅。更合理的做法是在进程关闭信号（SIGTERM/SIGINT）触发时主动调用 SDK 的 shutdown 与 flush 方法。这一点在综述中讨论智能体系统的生产级部署时应当加以强调：可观测性不是“装上就行”，还需要考虑生命周期管理、优雅关闭与数据完整性保障。对于 serverless 场景，由于函数执行时间受限，可能需要配置更短的批量导出间隔或使用同步导出器。

在架构层面，`W3CTraceContextPropagator` 的使用是一个关键细节。W3C Trace Context 作为国际标准，意味着 Llama Stack 可以与任何遵循同一标准的上下游服务共享追踪上下文——无论是 API 网关、服务网格（如 Istio）、负载均衡器，还是企业自研的微服务。这为构建大规模、异构的智能体流水线（agent pipeline）奠定了可观测性基础。综述在讨论多智能体协作、多步骤工作流或智能体与现有微服务生态集成时，可将此作为“标准化传播协议降低集成复杂度”的实证案例。

作者对敏感数据风险的提醒非常务实。在示例 span 中，向量数据库的端点参数（如 `vector_db_id`、`embedding_model`、`embedding_dimension`）以明文形式被记录；若业务代码未加过滤，用户输入的提示词或检索返回的文档片段也可能进入追踪系统。在涉及企业数据或个人信息（PII）的场景下，这直接关联到 GDPR、HIPAA 等合规风险。因此，可观测性方案的设计必须包含字段级脱敏、正则过滤或采样策略，并辅以严格的 Jaeger 访问控制与数据保留策略，而不能仅仅关注技术集成本身。这一安全维度在当前 AI 可观测性的技术讨论中往往被忽视，综述将其纳入分析可显著提升研究的完整性与现实指导意义。

最后，本文与 s1-011 的 Python 版本形成良好互补。两者在技术路线上高度一致，仅在语言运行时与具体插桩包上有所差异，这种跨语言复现能力恰恰印证了 OpenTelemetry 作为统一标准的价值。对于综述而言，将这两篇并列引用，可有效说明“无论智能体应用采用何种语言实现，都可借助标准化工具链获得一致的可观测性体验”，从而为异构智能体生态的监控统一性提供论据。这种跨语言的一致性证据，对于说服技术决策者采纳标准化方案而非各自为政的私有实现，具有特殊的说服力。

从更长远的视角看，Red Hat 作为企业级开源解决方案提供商，其官方技术博客的选题方向本身就反映了市场需求的演变。当 Red Hat 开始系统性产出 Llama Stack + OpenTelemetry 的实战内容时，说明企业客户对 AI 应用的可观测性需求已经从“nice-to-have”变为“must-have”。综述在讨论行业趋势时，可将 Red Hat 的这一内容系列作为风向标，说明 AI 可观测性正在从社区探索走向企业刚需，相关研究和工具建设将迎来加速发展期。对于研究者而言，这意味着可观测性不再只是运维团队的专属话题，而是 AI 系统设计与评估中不可忽视的核心维度。

另一个值得关注的细节是作者在服务端配置中使用 `run.yaml` 模板来指定 OTLP 端点，而非硬编码在应用代码中。这种配置与代码分离的做法符合十二要素应用（Twelve-Factor App）的方法论，使得同一套代码可以在不同环境（开发、测试、生产）中灵活切换可观测性后端，而无需重新构建镜像。综述在讨论智能体系统的生产级部署最佳实践时，可将此作为配置管理的正面案例加以引用。

在实际复现本文方案时，建议读者特别注意环境变量的传递方式。由于 Llama Stack 以容器方式运行，环境变量需要在容器启动时正确注入，而非仅在宿主机 shell 中设置。此外，从容器内提取 `run.yaml` 模板后进行修改再挂载回去的做法，虽然适合学习和实验，但在生产环境中应考虑使用 ConfigMap 或类似机制进行配置管理，以确保配置变更的可追溯性和版本控制。

16. **OTLP 协议的优势**: OpenTelemetry Protocol（OTLP）作为统一的传输协议，支持 gRPC 和 HTTP 两种传输方式。
本文使用 HTTP 方式与 Jaeger 对接，这种灵活性使得不同后端系统的集成变得更加简单。
OTLP 的标准化数据模型包括 traces、metrics 和 logs 三大类信号，为未来的统一可观测性平台奠定了基础。

17. **Podman 与 Docker 的选择**: 作者在示例中选用 Podman 作为容器运行时，这反映了 Red Hat 生态对 rootless 容器的偏好。
Podman 的无守护进程架构在安全性上具有优势，特别适合企业级部署场景。
无论使用 Podman 还是 Docker，Jaeger 的容器化部署方式都大大降低了分布式追踪后端的运维成本。

18. **火焰图与性能分析**: Jaeger 提供的火焰图视图可以直观展示每个 span 的耗时分布，
帮助开发者快速识别性能瓶颈所在的具体阶段。
在 AI 应用中，模型推理通常是耗时最长的环节，但向量检索和文档预处理也可能成为意想不到的瓶颈点。
分布式追踪的可视化能力使得这些问题的定位变得前所未有的高效。

19. **配置即代码的理念**: 将 `run.yaml` 纳入版本控制系统，可以追踪可观测性配置的变更历史，
并在出现问题时快速回滚到已知良好的配置状态。
这种配置即代码（Configuration as Code）的做法是现代 DevOps 实践的重要组成部分，
也是保障生产环境稳定性的关键措施。

20. **学习曲线与团队培训**: 虽然 OpenTelemetry 的自动插桩降低了入门门槛，
但团队仍然需要理解 distributed tracing 的基本概念才能有效利用追踪数据。
建议企业在引入可观测性工具链的同时，配套开展相关培训，
确保开发和运维团队都能正确解读 span、trace 和 context propagation 等核心概念。

21. **Node.js 生态的可观测性成熟度**: Node.js Reference Architecture 对可观测性组件的官方推荐，
说明 Node.js 生态在企业级可观测性方面已经形成了较为成熟的指导意见。
这与 Python 生态相比具有一定的先发优势，也为 Node.js AI 应用的观测能力建设提供了更明确的路线图。

22. **未来演进方向**: 随着 OpenTelemetry 生态的不断成熟，
AI 专用语义约定（semantic conventions）正在逐步完善。
这将为 LLM 调用、嵌入向量操作、RAG 检索等 AI 特有操作提供标准化的属性命名规范，
使得不同 AI 框架和工具链之间的追踪数据具有更高的可比性和互操作性。

23. **成本与采样策略**: 在高吞吐生产环境中，全量追踪可能带来显著的性能开销和存储成本。
OpenTelemetry 支持基于概率的头部采样（head-based sampling）和尾部采样（tail-based sampling），
团队应根据业务敏感度和成本预算选择合适的采样策略，
在数据完整性和系统开销之间取得平衡。
