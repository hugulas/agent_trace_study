# 轨迹 Schema

## 定义

轨迹 Schema 是把智能体事件结构化的字段约定，决定跨平台日志能否被诊断器、评测器、审计器和成本分析器复用。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些字段是跨平台最小集合？
- OTel span 与智能体认知事件如何映射？
- schema 是否保留足够上下文用于事后取证？

## 证据入口

- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 通过零侵入运行时插桩与三层面统一 Schema，把 LLM 智能体的操作执行、认知推理与环境交互转化为结构化、可内省且与 OpenTelemetry 兼容的日志流，为智能体安全、问责与评估提供了基础设施级的可观测性支撑。
- [[summaries/c-004-OpenInference-OpenTelemetry-Instrumentat|GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability]] — OpenInference 的价值不仅在于提供了多少 instrumentation 包，更在于它成功地将 AI 领域的大量专有概念（如 retrieval、tool call、prompt template）映射到了 OpenTelemetry 的通用追踪模型上。
- [[summaries/c-013-Hermes-Agent-Trajectory-Format|Trajectory Format - Hermes Agent]] — Hermes Agent 的轨迹格式文档是我目前见过的最详尽的训练数据工程规范之一。它的价值不仅在于定义了一种格式，更在于展示了一个完整的"从运行时到训练集"的数据流水线设计。其中最令我印象深刻的是推理内容的归一化策略——通过强制每个 gpt 轮次包含 <think> 块，即使模型未产生显式推理，也保证了训练数据在格式上的绝对一致性。这种"宁缺勿滥"的严格性对于大规模预训练或微调至关重要，因为数据格式的不一致是导致训练失败或性能退化的常见原因。在分布式训练环境中，如果不同 worker 加载的数据具有不同的字段结构或内容格式，不仅会导致训练崩溃，还可能引
- [[summaries/c-015-OpenInference-OpenTelemetry-for-LLM-Apps|What is OpenInference? OTel for LLM 2026]] — 这篇博客虽然由 FutureAGI 发布，带有一定的产品视角，但它对 OpenInference 生态的描述是准确且全面的。特别有价值的是它对"为什么需要 OpenInference"的三力分析——LLM 追踪形状不同、框架插桩碎片化、OTel GenAI 标准尚未成型——这三点恰好解释了为什么一个独立于 OTel 核心项目的 AI 语义约定是必要的，而不是等待 OTel 官方来解决。如果当时没有 OpenInference 填补空白，2023-2024 年的 LLM 应用开发者将面临要么各自为战编写追踪逻辑、要么完全缺乏可观测性的困境。
- [[summaries/c-014-OpenInference-Specification|OpenInference Specification - openinference]] — OpenInference 规范的最大价值在于它提供了一个"AI 原生"的追踪语义层，而不是让 AI 应用去适配传统 HTTP 服务的追踪模型。在 HTTP 服务中，一次 span 只需要 method、status_code、path 等属性就足够理解；但在 LLM 应用中，同样的"一次调用"背后是多轮对话历史、系统提示词、工具定义、温度参数、token 消耗、模型版本等数十个维度的信息。如果这些信息散落在不同的日志格式中，不仅无法聚合分析，更无法在不同框架之间进行横向比较。
- [[summaries/c-011-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 的最大贡献在于将智能体可观测性问题从传统的"事后调试工具" 提升到了"运行时安全基础设施"的战略高度。
- [[summaries/c-003-OpenTelemetry-AI-Agent-Observability-Sta|AI Agent Observability - Evolving Standards and Best Practices - OpenTelemetry]] — OpenTelemetry 这篇博客的价值在于它从标准制定者的视角，将 Agent 可观测性从单纯的技术工具提升到了生态基础设施的高度。
- [[summaries/s3-002-Distributed-tracing-for-agentic-workflow|Distributed tracing for agentic workflows with OpenTelemetry]] — - 这篇博客是智能体可观测性领域中少有的从企业级生产环境出发的实操指南， 与学术论文偏重理论框架和实验评估的风格形成了良好互补。
- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — 这篇博客的价值在于它将 OpenTelemetry 的通用可观测性框架与 MCP 这一特定协议场景进行了深度对接，提供了一套从概念到实践的完整实施路径。与许多停留在理念层面的可观测性文章不同，本文给出了具体的集成模式、采样策略配置建议和敏感数据处理方案，具有较强的工程参考价值。
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] — 这份 IETF 草案的出现在时机上极具战略意义：2026 年 3 月发布，恰好赶在欧盟 AI 法案 8 月生效之前，为高风险 AI 系统的日志合规提供了急需的标准化框架。作者 Raza Sharif 来自 CyberSecAI Ltd，这一背景也解释了为何文档对 SOC 2、PCI DSS 等企业合规框架有如此细致的映射。从标准演进角度看，AAT 目前仍处于 Individual 提交的 Internet-Draft 阶段，尚未被 IETF 正式背书，这意味着其在未来六个月内可能经历大幅修订，甚至被其他草案取代。在综述中引用时需注意其"work in p

## 相关词条

- [[terms/runtime-instrumentation|运行时插桩]]
