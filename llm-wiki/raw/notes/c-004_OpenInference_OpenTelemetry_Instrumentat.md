---
tags:
  - openinference
  - opentelemetry
  - arize-phoenix
  - llm-observability
  - instrumentation
  - tracing
  - semantic-conventions
  - github
  - open-source
  - python
  - typescript
  - genai-telemetry
aliases:
  - OpenInference OpenTelemetry Instrumentation
  - Arize OpenInference
  - c-004
date: 2026-05-24
url: https://github.com/Arize-ai/openinference
---

# GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability

## 核心信息

- **标题**: GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability
- **作者**: Arize AI
- **来源**: GitHub 开源仓库
- **URL**: https://github.com/Arize-ai/openinference
- **日期**: 2026-05-24（持续更新）
- **PDF**: `[c-004]-openinference-opentelemetry-instrumentation-for-ai-observabi.pdf`
- **证据质量**: medium

## 内容摘要

OpenInference 是由 Arize AI 发起并维护的一套面向 AI 应用可观测性的开源规范与工具集。

其核心定位是作为 OpenTelemetry 的补充，为 LLM 应用、Agent 系统以及机器学习流水线提供标准化的追踪语义和自动化插桩能力。

该项目不仅定义了与传输协议和文件格式无关的规范（支持 JSON、ProtoBuf、DataFrame 等多种序列化方式），还提供了覆盖主流 AI 框架的现成 instrumentation 包，使得开发者能够在不改动业务代码的前提下，快速接入分布式追踪系统。

规范层面，OpenInference 的核心关注点是 LLM 调用本身以及围绕 LLM 调用的完整应用上下文。

具体包括向量存储检索（retrieval from vector stores）、外部工具调用（如搜索引擎、API 等）、多步推理链中的中间状态，以及模型输入输出的语义化描述。

这种设计哲学与 OpenTelemetry 的 GenAI semantic conventions 高度一致。

但 OpenInference 在 AI 特有的概念（如 prompt template、token usage、embedding vector、retrieval documents、tool call 参数等）上做了更细粒度的约定，填补了通用遥测标准在生成式 AI 领域的空白。

在工程实现上，OpenInference 提供了极为丰富的多语言 instrumentation 生态。

Python 侧覆盖了当前主流的 LLM 框架与 Agent 框架，包括 OpenAI SDK、OpenAI Agents SDK、LangChain、LlamaIndex、DSPy、CrewAI、Haystack、LiteLLM、Groq、MistralAI、Anthropic、Instructor、Portkey、Guardrails、BeeAI、Google GenAI 与 Google ADK、Microsoft Autogen AgentChat、PydanticAI、smolagents、Pipecat、Agno 等。

此外，还针对 AWS Bedrock（包括 Bedrock Agent Runtime）、VertexAI、MCP（Model Context Protocol）等云平台与协议提供了专门的支持。

JavaScript/TypeScript 侧同样提供了 `@arizeai/openinference-semantic-conventions`、`@arizeai/openinference-core` 以及面向 Bedrock、BeeAI 等场景的 instrumentation 包。

这种广泛的框架覆盖意味着无论团队使用何种技术栈构建 Agent，都能找到对应的即插即用追踪方案。

除了直接的 instrumentation，OpenInference 还提供了 span processor 机制，用于归一化和转换来自其他 instrumentation 库的数据。

例如，`openinference-instrumentation-openlit` 和 `openinference-instrumentation-openllmetry` 分别将 OpenLIT 和 OpenLLMetry（Traceloop）的 trace 数据转换为符合 OpenInference 规范的格式，从而在不同观测后端之间实现数据互操作。

Arize Phoenix 是 OpenInference 的原生支持后端，但由于项目完全遵循 OpenTelemetry 标准，任何兼容 OTel 的后端（如 Jaeger、Zipkin、Grafana Tempo、Datadog、Honeycomb 等）都可以直接消费其产生的 trace 数据。

从架构复杂度来看，OpenInference 的示例覆盖了从简单（如单次 OpenAI chat completion、MistralAI SDK 调用）到中等复杂度（如 OpenAI Agents with handoffs、Autogen Team Chat、PydanticAI agent、Pipecat 应用）的多种场景。

这说明其语义约定和插桩工具已经能够支撑现实世界中的多步 Agent 协作与对话式应用。

对于正在构建 AI 可观测性基础设施的团队而言，OpenInference 不仅是一个技术实现参考，更是连接 AI 领域专用概念与通用云原生可观测性生态的重要桥梁。

## 关键要点

- OpenInference 是 Arize AI 主导的 AI 可观测性开源项目，作为 OpenTelemetry 的补充，专注于 LLM 应用和 Agent 系统的追踪语义与自动插桩。
- 规范层面对 LLM 调用、向量检索、外部工具调用等 AI 特有场景进行了细粒度语义约定，支持 JSON、ProtoBuf、DataFrame 等多种格式。
- Python instrumentation 生态极为丰富，覆盖 OpenAI、LangChain、LlamaIndex、DSPy、CrewAI、Haystack、LiteLLM、Anthropic、Google GenAI/ADK、Autogen、PydanticAI、smolagents、Pipecat、MCP 等主流框架与协议。
- JavaScript/TypeScript 生态提供语义约定核心包以及面向 Bedrock、BeeAI 等场景的插桩实现。
- 通过 span processor 支持将 OpenLIT、OpenLLMetry（Traceloop）等第三方追踪数据归一化为 OpenInference 规范，提升数据互操作性。
- 原生对接 Arize Phoenix，同时兼容所有支持 OpenTelemetry 的后端，避免供应商锁定。
- 示例覆盖从简单 SDK 调用到多 Agent handoff、团队对话、语音/视频流水线等中等复杂度场景，具备生产级参考价值。
- 语义约定涵盖 prompt template、token usage、embedding vector、retrieval documents、tool call 参数等 AI 专属遥测维度，填补了通用 OTel 在生成式 AI 领域的空白。
- 项目采用与传输协议和文件格式无关的设计，允许灵活适配不同的数据管道和存储后端。
- 作为开源社区事实标准之一，OpenInference 在 AI 可观测性工具链中扮演着连接业务框架与底层遥测基础设施的关键角色。
- 仓库中包含的 internal_docs 目录暗示项目团队有持续维护的内部文档体系，表明规范的演进具有组织保障。
- 从提交历史看，该项目活跃度较高，1,881 次提交反映出社区和厂商的持续投入，规范本身也在随 AI 生态快速迭代。
- Instrumentation 的复杂度分级（简单到中等）有助于用户根据自身场景选择合适的集成深度，降低了初次采纳的门槛。
- 语义约定包的独立发布（如 openinference-semantic-conventions）使得其他项目可以在不引入完整 instrumentation 的情况下复用其数据模型。
- Span processor 的设计体现了对异构遥测生态的包容性，承认企业环境中多工具共存是常态而非例外。
- 对 MCP 协议的早期支持表明项目团队对 Agent 生态演进方向的敏锐判断，MCP 正在成为 Agent 与工具交互的事实标准。
- 项目还包含对 Open Agent Specification 和 Strands Agents 等新兴框架的支持，显示出其对新技术的快速响应能力。
- 每个 instrumentation 包通常都附带使用示例和配置说明，降低了开发者的上手成本。
- 通过 pre-commit 配置和 cspell 等工具保证了代码质量和文档一致性。
- release-please 配置表明项目采用自动化版本发布流程，有利于依赖该库的用户及时获取更新。
- 代码贡献指南（CONTRIBUTING）和 CODE_OF_CONDUCT 的存在说明社区治理相对规范。
- 项目对 LiteLLM Proxy 的支持使得通过统一网关调用多厂商模型时的遥测变得可行。
- Pipecat 的插桩示例说明 OpenInference 的适用范围已扩展到实时语音和视频对话场景。
- 对 Google ADK 和 VertexAI 的双轨支持覆盖了 Google 生态中不同层级的 AI 开发工具。
- DSPy 的插桩使得声明式编程框架中的模块化优化过程也能被完整追踪。
- 该项目的存在大幅降低了 AI 框架开发者自行实现遥测功能的重复劳动。
- 在综述写作中，OpenInference 可作为讨论 AI 可观测性标准化进程的核心参考文献。
- 对 AWS Bedrock Agent Runtime 的支持说明项目不仅关注模型调用层，还关注 Agent 编排层的遥测需求。
- Guardrails 和 Instructor 等输入校验框架的插桩支持，使得数据验证过程也能被纳入追踪视图。

## 与综述的关联

- 与综述中讨论的 OpenTelemetry for AI Agents 主题直接相关：OpenInference 是 OTel 生态在 AI 领域最成功的实践扩展之一，为综述提供了具体的标准实现案例。
- 与 trace schema 和 telemetry standards 章节关联：OpenInference 的语义约定是构建统一 Agent 追踪格式的重要参考，可与 AgentTrace、Hermes 等结构化日志框架对比分析。
- 与 observability products and market map 关联：Arize Phoenix 作为 OpenInference 的原生后端，是市场中 LLM 可观测性平台的代表性产品，其数据模型直接影响行业实践。
- 与 runtime instrumentation and OTel 关联：项目中大量 instrumentation 包展示了如何在不同 AI 框架中植入 OTel trace，为综述的技术实现章节提供了代码级参考。
- 与 distributed tracing for agentic workflows 关联：OpenInference 支持的跨框架、跨语言追踪能力，是实现端到端 Agent 工作流可观测性的基础组件。
- 与评测和基准测试章节关联：OpenInference 提供的标准化遥测数据可作为 Agent 评测和故障归因的数据源，与 MASPrism、AgentRx 等诊断工具形成数据层面的协同。
- 与开源生态和标准化章节关联：该项目是连接商业可观测性平台与开源 AI 框架的关键纽带，其存在降低了整个生态采用统一遥测标准的门槛。
- 与成本管理章节关联：OpenInference 对 token usage 和模型调用链的标准化记录，为 Agent 成本的精细化归因提供了数据基础。
- 与工具调用安全章节关联：OpenInference 对 tool call 参数和检索文档的追踪语义，是审计 Agent 工具使用行为的前提条件。
- 与多 Agent 系统可观测性章节关联：OpenInference 对 Autogen、CrewAI 等多 Agent 框架的插桩支持，为综述提供了多 Agent 追踪的实际案例。

## 我的笔记

OpenInference 的价值不仅在于提供了多少 instrumentation 包，更在于它成功地将 AI 领域的大量专有概念（如 retrieval、tool call、prompt template）映射到了 OpenTelemetry 的通用追踪模型上。

这种映射是 AI 可观测性从“作坊式日志”走向“标准化遥测”的关键一步。

对于正在调研 Agent 可观测性技术栈的团队，我建议将 OpenInference 作为基准参考：如果某个新框架或新协议尚未被 OpenInference 覆盖，那么自行实现 instrumentation 时应当优先遵循其语义约定，以保证与未来生态的兼容性。

在实际落地层面，OpenInference 的 span processor 机制尤其值得关注。

很多团队在生产环境中并非从零开始，而是已经使用了 OpenLIT、OpenLLMetry 或 Langfuse 等工具。

OpenInference 的 processor 允许这些团队在不更换现有 instrumentation 的前提下，将数据转换为标准格式后送入统一后端，这种渐进式迁移策略对于大型企业尤为重要。

不过也需要注意到，GitHub 仓库中的内容以代码和 README 为主，缺乏对规范设计原理的系统性文档说明。

例如，为何某些属性被定义为 required 而另一些是 optional，不同框架的 instrumentation 在语义一致性上如何保证，这些信息在仓库中并未充分展开。

若综述需要深入讨论标准制定的权衡过程，可能需要额外查阅 Arize 官方博客或社区 RFC 文档。

此外，随着 MCP 和 OpenAI Agents SDK 等新兴协议的快速迭代，OpenInference 的覆盖速度能否跟上生态变化，也是值得持续观察的问题。

另一个值得思考的方向是：OpenInference 目前主要覆盖的是“追踪”维度，对于指标（metrics）和日志（logs）的语义约定相对较少。

在完整的可观测性三大支柱中，trace 固然重要，但缺乏 metrics 和 logs 的配套标准，可能导致不同后端之间的数据模型仍然割裂。

综述在讨论遥测标准时，可以指出这一缺口，并展望未来的发展方向。

最后，从社区治理角度观察，OpenInference 由 Arize AI 主导但保持开源，这种厂商-社区混合模式在 AI 可观测性领域非常典型。

它既保证了规范演进的专业性和资源投入，又通过开源协议避免了单一厂商的完全控制。

综述在讨论行业标准形成机制时，可以将 OpenInference 作为一个典型案例进行分析。
