# 运行时插桩

## 定义

运行时插桩是在模型调用、工具调用、MCP server、环境事件和业务状态变更处记录结构化遥测，为实时监控和离线诊断提供数据。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些边界应产生 span？
- 插桩开销和隐私风险如何控制？
- 被动 eBPF 与应用级 SDK 各适合什么场景？

## 证据入口

- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [[summaries/s3-002-Distributed-tracing-for-agentic-workflow|Distributed tracing for agentic workflows with OpenTelemetry]] — - 这篇博客是智能体可观测性领域中少有的从企业级生产环境出发的实操指南， 与学术论文偏重理论框架和实验评估的风格形成了良好互补。
- [[summaries/s1-011-How-to-implement-observability-with-Pyth|使用 Python 与 Llama Stack 实现可观测性]] — 本文最突出的价值在于“从能跑到好用”的完整递进：第一步展示 Llama Stack 开箱即用的追踪能力，第二步指出其在真实场景下的结构性缺陷，第三步给出切实可行的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事结构，对技术写作者和综述材料组织都有很高参考价值。许多技术文档只展示成功路径，而本文敢于暴露中间状态的不足，反而大大增强了说服力，让读者理解为何需要额外的客户端插桩工作。
- [[summaries/s1-012-How-to-implement-observability-with-Node|使用 Node.js 与 Llama Stack 实现可观测性]] — 本文的最大亮点在于其层层递进的教学结构：先展示 Llama Stack 服务端“零代码”追踪的便捷性，再揭示其在真实场景下的结构性不足，最后给出完整可复现的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事方式，对技术文档写作和综述材料组织都有很高参考价值，尤其适合向非可观测性背景的 AI 开发者传达追踪的重要性。许多技术教程倾向于只展示最终完美状态，而本文敢于暴露中间探索过程中的挫折（如 /v1/telemetry/events API 的局限），反而增强了内容的真实感与可信度，让读者更容易理解每个设计决策背后的动机。
- [[summaries/c-003-OpenTelemetry-AI-Agent-Observability-Sta|AI Agent Observability - Evolving Standards and Best Practices - OpenTelemetry]] — OpenTelemetry 这篇博客的价值在于它从标准制定者的视角，将 Agent 可观测性从单纯的技术工具提升到了生态基础设施的高度。
- [[summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp|(Proposal) Adding OpenTelemetry Trace Support to MCP]] — 这篇 GitHub Discussion 是我所读到的关于 MCP 可观测性最深入、最富张力的原始技术资料之一。其价值不仅在于提案本身的设计细节，更在于围绕该提案展开的多元观点碰撞，这些碰撞暴露了当前 Agent 可观测性领域许多尚未被充分讨论的深层问题。
- [[summaries/c-004-OpenInference-OpenTelemetry-Instrumentat|GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability]] — OpenInference 的价值不仅在于提供了多少 instrumentation 包，更在于它成功地将 AI 领域的大量专有概念（如 retrieval、tool call、prompt template）映射到了 OpenTelemetry 的通用追踪模型上。
- [[summaries/s3-005-How-to-Instrument-MCP-Servers-with-OpenT|OneUptime：MCP 服务器 OpenTelemetry 仪器化指南（原文已失效）]] — 这篇来源是我所处理的资料中最为特殊的一份——它的"缺席"本身成为了最重要的"在场"。当我最初看到 JSON 中的元数据（Tyler Easterbrook、2022 年、M/C Journal、DOI）时，我以为这是一篇媒体研究论文被错误归类到了技术来源中；但当我读取 section_texts 和 PDF 内容时，发现它实际上是 OneUptime 网站的一个 404 页面。这种元数据与内容的双重错配，本身就是数字时代信息管理的典型案例。
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] — 这篇文章的价值在于它清晰地界定了"agent 可观测性"的问题边界，避免了业界将 LLM 可观测性工具简单套用到多智能体系统的常见误区。作者用"研究-写作-审阅"三 agent 流水线的具象案例，展示了传统工具在跨 agent 归因上的结构性失明，这种叙事方式对于向技术团队传达 agent 可观测性的必要性非常有效。相比学术论文的抽象定义，这种来自产业界一线的技术指南更容易被工程团队理解和接受。
- [[summaries/s1-008-Part-3-AgentCore-Runtime-Observability|Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability]] — 这篇教程的价值在于它提供了一个从"零配置"到"全链路可观测"的完整闭环实践。与大多数停留在概念层面的文档不同，作者每一步都配有控制台截图与具体配置参数，这使得该文章具有极高的复现价值。从工程实践角度，我认为以下几点值得在综述中深入展开： 第一，ADOT 自动埋点与 Starter Toolkit 的协同设计体现了 AWS 在开发者体验上的深度思考。传统上，为 Python Agent 应用添加 OpenTelemetry 埋点需要开发者手动修改依赖、配置 exporter、初始化 tracer provider，步骤繁琐且容易出错。而 AgentCore

## 相关词条

- [[terms/agent-trace|智能体轨迹]]
- [[terms/trace-schema|轨迹 Schema]]
