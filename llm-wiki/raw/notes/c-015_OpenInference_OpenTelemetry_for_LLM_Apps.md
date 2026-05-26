---
tags:
  - OpenInference
  - OpenTelemetry
  - LLM-observability
  - auto-instrumentation
  - Arize
  - Phoenix
  - FutureAGI
  - traceAI
  - OpenLLMetry
  - OpenLIT
  - LangChain
  - LlamaIndex
date: 2026-04-18
url: https://futureagi.com/blog/what-is-openinference-2026/
aliases:
  - OpenInference OTel for LLM 2026
  - What is OpenInference
  - OpenInference 生态概述 2026
---

# What is OpenInference? OTel for LLM 2026

## 核心信息

- **来源编号**: c-015
- **标题**: What is OpenInference? OTel for LLM Apps in 2026
- **发布方**: FutureAGI（基于 Arize OpenInference 生态的技术博客）
- **文档类型**: 技术博客（technical blog）
- **发布日期**: 2026-04-18
- **URL**: https://futureagi.com/blog/what-is-openinference-2026/
- **证据质量**: medium（作为生态概述和对比分析，时效性强，但带有 FutureAGI 自身产品视角）
- **对比对象**: traceAI、OpenLLMetry、OpenLIT
- **核心后端**: Phoenix（Arize 参考实现）、FutureAGI、Datadog、Grafana、Jaeger

## 内容摘要

本文是一篇面向 LLM 应用开发者的 OpenInference 生态全景介绍，写作时间为 2026 年 4 月。文章以团队为 LangChain RAG
流水线添加追踪的场景切入，指出传统的打印日志方式（输出提示词、模型名称、响应和延迟）在 hello-world 规模下可用，但在生产规模下完全不可行。生产环境需要的是完整的 span
树：哪个检索查询执行了、哪个嵌入模型返回了什么、哪个 LLM 调用发起了哪个工具调用、评估得分是多少、成本是多少。团队可以选择自己编写所有这些追踪逻辑并在每次框架升级时重写，或者安装一个包、注册一个
instrumentor，让所有 LangChain 调用自动发出与 OTel 对齐的、具有正确属性名称的 span。这个包就是 OpenInference。

OpenInference 是由 Arize 维护的、与 OpenTelemetry 对齐的语义约定和自动插桩框架，专为 LLM 应用设计。它定义了一套以 `openinference.*`
为命名空间的属性名称，用于描述 LLM span，并提供了跨多个 LLM 提供商、智能体框架和 RAG 库的即插即用自动插桩包。这些插桩包以 Apache 2.0 许可证发布在
Arize-ai/openinference 仓库中，发出 OTLP 格式的 span，任何 OTel 后端都可以消费。Arize 的参考开源后端是
Phoenix；FutureAGI、Datadog、Grafana、Jaeger 以及任何其他兼容 OTel 的系统也都可以使用。语言覆盖方面，Python 的覆盖率最广，同时也提供了
JavaScript / TypeScript 和 Java（LangChain4j、Spring AI 及核心库）的包。OpenInference 早于 OTel GenAI
语义约定出现，目前两者保持互补关系；部分插桩包会同时发出两个命名空间的属性，但双发行为是逐包实现的，使用前需要验证。

OpenInference 诞生的背后有三股驱动力。第一，LLM 应用产生的追踪形状与 HTTP 服务截然不同。HTTP span 携带 `http.method` 和
`http.status_code`，而 LLM span 需要提示词、完成内容、模型名称、token 计数、温度参数、工具定义、检索查询、嵌入向量等信息，2023 年 LLM
应用开始上线时还没有这些属性的标准。第二，每个框架都有自己的插桩模式。LangChain 提供 callbacks，LlamaIndex 提供 event handlers，CrewAI 提供
step listener，模式不同、属性名称不同、span 无法互操作。来自 LangChain 的追踪无法与来自 LlamaIndex
的追踪直接合并，需要大量胶水代码进行转换。第三，OpenTelemetry 的 GenAI 语义约定当时还不存在，OTel 项目在 2024 年启动该命名空间，2025
年发布初始版本；OpenInference 从 2023 年起就以并行命名空间和插桩包填补了这一空白。到 2026 年，两个命名空间正在收敛，OpenInference
插桩包同时发出两套属性以保持向后兼容。

OpenInference 的架构分为三层。最上层是框架和提供商，即应用直接调用的组件：OpenAI、Anthropic、LangChain、LlamaIndex、CrewAI、DSPy 等。中间层是
OpenInference 插桩包，通过 monkey-patch 框架或提供商客户端来发出 span，通常只需一次 pip install 加上一行
`Instrumentor().instrument()` 调用。最下层是 OTLP 传输层，将 span 携带到任何 OTel 后端。插桩包与后端完全解耦，后端可以是
Phoenix、FutureAGI、Datadog、Grafana、Tempo、Jaeger 或任何支持 OTLP
的系统。这种解耦设计意味着团队可以在不更换插桩的情况下切换后端，也可以同时使用多个后端消费同一套追踪数据。

在语义约定方面，每个 OpenInference span 都携带 `openinference.span.kind` 属性，定义了操作类型：LLM（聊天或补全端点调用）、CHAIN（多步编排单元，如
LangChain chain 或 LlamaIndex query engine）、RETRIEVER（向量搜索或 BM25
检索器）、EMBEDDING（嵌入生成调用）、TOOL（函数或工具调用）、AGENT（智能体运行，智能体循环的顶层）、RERANKER（对检索到的分块进行重排序）、GUARDRAIL（前置或后置护栏检查）、EVAL（在线评估得分）。常用的
LLM 特定属性包括
`llm.model_name`、`llm.provider`、`llm.input_messages`、`llm.output_messages`、`llm.token_count.prompt`、`llm.token_count.completion`、`llm.token_count.total`、`llm.temperature`、`llm.max_tokens`、`llm.invocation_parameters`、`llm.system_prompt`。检索特定属性包括
`retrieval.documents`（带内容和得分的检索文档列表）、`retrieval.query`（搜索查询）。嵌入属性包括 `embedding.embeddings` 和
`embedding.model_name`。通用输入输出属性包括
`input.value`、`input.mime_type`、`output.value`、`output.mime_type`。这些约定与 OTel GenAI 命名空间有重叠，近期的
OpenInference 插桩包会同时发出两套属性。

Python 插桩包的覆盖范围包括：LLM 提供商（OpenAI、Anthropic、Bedrock、Groq、MistralAI、VertexAI/Gemini、LiteLLM、OpenAI
Agents）、智能体框架（LangChain、LlamaIndex 及 Workflows、CrewAI、Agno、AutoGen 含
AgentChat、PydanticAI、Smolagents、BeeAI、Google ADK）、RAG 库（Haystack、LlamaIndex retrievers）、DSL
框架（DSPy）。JavaScript / TypeScript 端覆盖 OpenAI、Anthropic、Vertex、Bedrock、LangChain JS、LlamaIndex JS
及核心库。Java 端覆盖 LangChain4j 和 Spring AI。每个包的集成模式基本一致：导入对应 instrumentor，调用 `instrument()` 方法，然后正常使用框架
API 即可。这种一致性降低了开发者在多技术栈环境中采用可观测性的认知负担。

文章还将 OpenInference 与 2026 年的同类工具进行了对比。traceAI 提供面向 35+ 框架的自动插桩，覆盖范围最广；OpenLLMetry 是 Traceloop 推出的与
OpenTelemetry 对齐的 LLM 可观测性方案，在企业级特性方面有优势；OpenLIT 是另一个开源的 OTel 原生 LLM 可观测性框架，以简洁易用著称。FutureAGI
的定位则是一个围绕"闭环可靠性"构建的生产级后端，它整合了 span 附加评估（50+ first-party 指标，支持 BYOK 让任意 LLM 担任 judge，turing_flash 以
50–70ms p95 运行相同评分规则）、基于 persona 的模拟场景测试、以及 Agent Command Center 网关和护栏（前端对接 20+ 提供商，18+
运行时护栏）。FutureAGI 的差异化在于它不只是消费追踪数据，而是将评估和防护能力也纳入同一个平面。

![OpenInference RAG 实践]([c-015]-mastering-agentic-rag.png)

![OpenInference 架构示意]([c-015]-H79dDz26C43qaosXsOb3m0PcU.jpg)

![OpenInference 评估体系]([c-015]-uhlqH65m7DcIanSa6EsyB63kC4.jpg)

![AI Agent 评估]([c-015]-mastering-ai-agent-evaluation.png)

## 关键要点

1. **生产级追踪不能靠打印日志**：LLM 应用需要的不是零散日志，而是包含检索、嵌入、LLM 调用、工具调用、评估得分的完整 span 树，OpenInference
通过一行代码即可实现自动采集，避免团队自行维护脆弱的追踪逻辑。

2. **三层解耦架构**：框架/提供商层 → OpenInference 插桩层 → OTLP 传输层，插桩包与后端完全解耦，支持
Phoenix、FutureAGI、Datadog、Grafana、Jaeger 等任意 OTel 后端，团队可自由切换或同时使用多个后端。

3. **九种 span kind 精确描述 AI 操作**：从 LLM
调用到智能体推理、从检索查询到护栏检查、从重排序到在线评估，每种操作都有标准化的语义分类，使追踪数据在任意后端中都能被正确理解和展示。

4. **30+ Python 框架的即插即用覆盖**：涵盖主流 LLM 提供商（OpenAI、Anthropic、Bedrock
等）、智能体框架（LangChain、LlamaIndex、CrewAI、AutoGen 等）、RAG 库和 DSL 框架，JS/TS 和 Java 生态也有相应支持。

5. **与 OTel GenAI 语义约定的双发兼容**：OpenInference 早于 OTel GenAI 约定出现，当前正通过同时发出 `openinference.*` 和
`gen_ai.*` 两套属性实现向后兼容和生态融合，过渡期需注意逐包验证双发行为。

6. **2026 年生态竞争格局**：OpenInference 与 traceAI（35+ 框架自动插桩）、OpenLLMetry（Traceloop 方案）、OpenLIT（OTel
原生框架）共同构成 LLM 可观测性工具矩阵，各有侧重，选择时应考虑语言支持、后端兼容性和企业级特性需求。

7. **FutureAGI 的闭环可靠性理念**：除了作为消费后端，FutureAGI 还提供 span 附加评估（50+ 指标）、模拟测试、网关路由（20+ 提供商）和运行时护栏（18+
规则），形成从采集到评估到防护的完整闭环。

8. **monkey-patch 插桩的零侵入优势**：运行时动态替换框架内部方法，无需修改业务代码即可获取完整追踪，对已在生产环境运行的 Legacy Agent 系统尤其重要。

9. **跨语言生态差异**：Python 插桩覆盖最完整（30+ 包），JS/TS 和 Java 处于追赶状态，选择工具时应匹配团队的技术栈分布。

10. **Apache 2.0 开源许可**：OpenInference 插桩包采用宽松的 Apache 2.0 许可证，降低了企业采用顾虑，有利于社区贡献和生态扩展。

## 与综述的关联

本文是理解 OpenInference 生态现状和竞争格局的重要一手资料，与综述的以下主题直接相关：

- **Agent 可观测性技术栈架构**：综述中对观测层、评估层、防护层三层架构的论述，可以引用本文描述的三层解耦模型（框架 → 插桩 → OTLP 后端）作为技术实现参考。FutureAGI 进一步将评估和护栏整合到同一平面，展示了从"可观测"到"可控"的演进路径。

- **自动插桩与开发者体验**：综述讨论如何让 Agent 开发者以最小成本接入可观测性时，OpenInference 的 `pip install + instrument()` 模式是一个极具说服力的案例。这种零侵入的 monkey-patch 方式显著降低了生产环境接入追踪的门槛。

- **跨框架追踪互操作性**：综述中关于不同 Agent 框架之间追踪数据如何打通的问题，OpenInference 通过统一属性命名空间和标准化插桩机制提供了实践层面的解决方案。当团队同时使用 LangChain 和 LlamaIndex 构建不同模块时，统一的追踪语义使全链路分析成为可能。

- **评估与追踪的结合**：FutureAGI 提出的"span-attached evals"概念（将 50+ 评估指标作为 span 属性附加）是综述中"观测驱动评估"主题的典型实现，代表了从被动监控到主动评估的演进方向。BYOK 和 turing_flash 的 50–70ms p95 延迟也说明评估不再是离线批处理的专利。

- **Token 成本与性能归因**：综述中关于 Agent 系统运行成本分析的内容，可以直接引用 OpenInference 对 `llm.token_count.*` 和调用参数的标准化定义。这些属性是实现细粒度成本分摊和异常检测的基础设施。

- **OTel 生态在 AI 领域的演进**：本文对 OpenInference 与 OTel GenAI 语义约定之间互补与融合趋势的描述，为综述提供了关于行业标准演进的一手判断。双发属性的过渡期策略反映了标准制定中的务实考量。

- **可观测性工具的选型框架**：综述中如果需要指导读者如何选择 LLM 可观测性工具，可以基于本文提供的对比维度（覆盖框架数量、语言支持、后端兼容性、企业特性）构建选型决策树。

## 我的笔记

这篇博客虽然由 FutureAGI 发布，带有一定的产品视角，但它对 OpenInference 生态的描述是准确且全面的。特别有价值的是它对"为什么需要
OpenInference"的三力分析——LLM 追踪形状不同、框架插桩碎片化、OTel GenAI 标准尚未成型——这三点恰好解释了为什么一个独立于 OTel 核心项目的 AI
语义约定是必要的，而不是等待 OTel 官方来解决。如果当时没有 OpenInference 填补空白，2023-2024 年的 LLM
应用开发者将面临要么各自为战编写追踪逻辑、要么完全缺乏可观测性的困境。

从工程落地角度，我认为 OpenInference 最大的隐性优势在于它的"monkey-patch 插桩"策略。与需要修改业务代码的显式追踪 API 不同，OpenInference 的
instrumentor 在运行时动态替换框架内部方法，这意味着开发者可以在完全不改动现有代码的情况下获得完整的追踪数据。这种零侵入性对于已经在生产环境运行的 Legacy Agent
系统尤其重要——它们往往缺乏测试覆盖，任何代码修改都伴随着 regression 风险，而运行时插桩规避了这一问题。

关于双发属性（同时发出 `openinference.*` 和 `gen_ai.*`），我认为这是 2026
年生态过渡期的一个务实策略，但长期来看可能会带来数据冗余和存储成本问题。如果后端同时消费两套属性，如何确保一致性、如何避免重复计算，这些在生产环境中都需要仔细处理。综述中可以提及这一点作为当前生态的不完善之处，并建议团队在后端消费时明确选择一套主属性集进行索引和聚合。

FutureAGI 提到的"闭环可靠性"理念值得关注。传统的可观测性工具通常是"采集-存储-查询"的被动模式，而 FutureAGI
将评估（evals）和护栏（guardrails）也纳入同一个平面，形成了"采集-评估-防护"的主动闭环。这种设计思路与综述中讨论的"从可观测性到可控性"的演进方向高度一致。当评估发现某个 Agent
路径的幻觉率持续升高时，系统可以直接触发护栏规则进行拦截或降级，而不需要人工介入。

最后，文章中提到的语言覆盖情况也值得注意：Python 生态最完整，JS/TS 和 Java 处于追赶状态。这反映了当前 Agent 开发以 Python 为主流的现状，但随着企业级 Java
后端越来越多地集成 LLM 能力，Java 端的插桩覆盖将变得越来越重要。综述在讨论可观测性工具选型时，应考虑目标技术栈的语言支持情况。对于多语言微服务架构的团队，可能需要组合使用
OpenInference（Python）、OpenLLMetry（多语言）和 Jaeger（通用 OTel）等多种工具来满足全链路追踪需求。
