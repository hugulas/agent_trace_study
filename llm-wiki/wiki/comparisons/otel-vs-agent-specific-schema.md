# OpenTelemetry 与 Agent-specific Schema 的边界

## 对比表

| 维度 | 结论 |
|---|---|
| OTel 擅长 | 跨服务 trace、span 传播、指标/日志生态、厂商集成 |
| Agent-specific 擅长 | 意图、计划、工具语义、记忆、推理步骤、合规规范和失败类别 |
| 连接方式 | 把模型调用、工具调用、MCP server 和环境事件映射为 span，同时保留 agent 语义属性 |
| 风险 | 只用 OTel 容易丢失认知/任务语义；只用自定义 schema 容易失去生态互通 |
| 结论 | 生产系统应采用 OTel 作为传输与关联骨架，叠加 agent-specific 字段作为诊断语义层 |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [[summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp|(Proposal) Adding OpenTelemetry Trace Support to MCP]] — 这篇 GitHub Discussion 是我所读到的关于 MCP 可观测性最深入、最富张力的原始技术资料之一。其价值不仅在于提案本身的设计细节，更在于围绕该提案展开的多元观点碰撞，这些碰撞暴露了当前 Agent 可观测性领域许多尚未被充分讨论的深层问题。
- [[summaries/c-014-OpenInference-Specification|OpenInference Specification - openinference]] — OpenInference 规范的最大价值在于它提供了一个"AI 原生"的追踪语义层，而不是让 AI 应用去适配传统 HTTP 服务的追踪模型。在 HTTP 服务中，一次 span 只需要 method、status_code、path 等属性就足够理解；但在 LLM 应用中，同样的"一次调用"背后是多轮对话历史、系统提示词、工具定义、温度参数、token 消耗、模型版本等数十个维度的信息。如果这些信息散落在不同的日志格式中，不仅无法聚合分析，更无法在不同框架之间进行横向比较。
- [[summaries/s3-002-Distributed-tracing-for-agentic-workflow|Distributed tracing for agentic workflows with OpenTelemetry]] — - 这篇博客是智能体可观测性领域中少有的从企业级生产环境出发的实操指南， 与学术论文偏重理论框架和实验评估的风格形成了良好互补。
- [[summaries/c-004-OpenInference-OpenTelemetry-Instrumentat|GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability]] — OpenInference 的价值不仅在于提供了多少 instrumentation 包，更在于它成功地将 AI 领域的大量专有概念（如 retrieval、tool call、prompt template）映射到了 OpenTelemetry 的通用追踪模型上。
- [[summaries/c-015-OpenInference-OpenTelemetry-for-LLM-Apps|What is OpenInference? OTel for LLM 2026]] — 这篇博客虽然由 FutureAGI 发布，带有一定的产品视角，但它对 OpenInference 生态的描述是准确且全面的。特别有价值的是它对"为什么需要 OpenInference"的三力分析——LLM 追踪形状不同、框架插桩碎片化、OTel GenAI 标准尚未成型——这三点恰好解释了为什么一个独立于 OTel 核心项目的 AI 语义约定是必要的，而不是等待 OTel 官方来解决。如果当时没有 OpenInference 填补空白，2023-2024 年的 LLM 应用开发者将面临要么各自为战编写追踪逻辑、要么完全缺乏可观测性的困境。
- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 通过零侵入运行时插桩与三层面统一 Schema，把 LLM 智能体的操作执行、认知推理与环境交互转化为结构化、可内省且与 OpenTelemetry 兼容的日志流，为智能体安全、问责与评估提供了基础设施级的可观测性支撑。
- [[summaries/s1-011-How-to-implement-observability-with-Pyth|使用 Python 与 Llama Stack 实现可观测性]] — 本文最突出的价值在于“从能跑到好用”的完整递进：第一步展示 Llama Stack 开箱即用的追踪能力，第二步指出其在真实场景下的结构性缺陷，第三步给出切实可行的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事结构，对技术写作者和综述材料组织都有很高参考价值。许多技术文档只展示成功路径，而本文敢于暴露中间状态的不足，反而大大增强了说服力，让读者理解为何需要额外的客户端插桩工作。

## 相关页面

- [[terms/agent-trace|智能体轨迹]]
- [[viewpoints/observability-is-not-logging|智能体可观测性不是日志收集]]
- [[viewpoints/final-reward-is-insufficient|最终奖励不足以评估智能体]]
