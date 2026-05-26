# 智能体轨迹

## 定义

智能体轨迹是按时间记录的用户输入、模型消息、工具调用、工具返回、状态更新、环境观测和评测结果。它是失败诊断、合规评测、审计和成本归因的共同证据层。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 这条轨迹是否足以复现失败？
- 轨迹中是否保留了工具参数、观测和状态变化？
- 哪些字段应进入审计而不是普通日志？

## 证据入口

- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] — 这篇文章的价值在于它清晰地界定了"agent 可观测性"的问题边界，避免了业界将 LLM 可观测性工具简单套用到多智能体系统的常见误区。作者用"研究-写作-审阅"三 agent 流水线的具象案例，展示了传统工具在跨 agent 归因上的结构性失明，这种叙事方式对于向技术团队传达 agent 可观测性的必要性非常有效。相比学术论文的抽象定义，这种来自产业界一线的技术指南更容易被工程团队理解和接受。
- [[summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] — 本文构建了一个支持多种执行轨迹表示的通用框架，通过大规模实验发现现有代码语义信息对 Code LLMs 的监督微调和测试时扩展几乎没有显著帮助，为未来设计更适配模型处理方式的语义表示提供了新的基线。
- [[summaries/p-013-Detecting-Safety-Violations-Across-Many|Detecting Safety Violations Across Many Agent Traces]] — Meerkat 通过聚类组织轨迹仓库并驱动智能体进行结构化搜索，能够在海量智能体轨迹中发现仅靠单条轨迹无法识别的分布式安全违规，并在合成基准和真实评估中均显著超越现有基线。
- [[summaries/a-007-Monitoring-Claude-Code-Docs|Monitoring - Claude Code Docs]] — Claude Code 的监控文档是目前公开资料中最完整、最系统化的企业级 agent 遥测实现方案。与社区驱动的实验性项目（如 Codex CLI 的 rollout trace 或各类开源 agent 框架的日志系统）不同，Anthropic 的设计体现了生产环境所需的完整性、安全性、可管理性和可扩展性。
- [[summaries/c-013-Hermes-Agent-Trajectory-Format|Trajectory Format - Hermes Agent]] — Hermes Agent 的轨迹格式文档是我目前见过的最详尽的训练数据工程规范之一。它的价值不仅在于定义了一种格式，更在于展示了一个完整的"从运行时到训练集"的数据流水线设计。其中最令我印象深刻的是推理内容的归一化策略——通过强制每个 gpt 轮次包含 <think> 块，即使模型未产生显式推理，也保证了训练数据在格式上的绝对一致性。这种"宁缺勿滥"的严格性对于大规模预训练或微调至关重要，因为数据格式的不一致是导致训练失败或性能退化的常见原因。在分布式训练环境中，如果不同 worker 加载的数据具有不同的字段结构或内容格式，不仅会导致训练崩溃，还可能引
- [[summaries/p-030-Teaching-Text-Agents-to-Learn-Sequential|Teaching Text Agents to Learn Sequential Decision Making from Failure]] — 本文提出了一种失败动作感知的目标函数和基于成功-失败轨迹对的扰动增强方法，使文本智能体能够在不依赖外部大模型标注的情况下，从含有中间失败动作的自收集轨迹中更有效地学习序列决策策略。
- [[summaries/s2-003-Appbuilder-Trace跟踪功能基本用法-百度千帆文档|千帆AppBuilder Trace跟踪功能基本用法]] — 千帆AppBuilder的Trace功能设计走的是典型的"轻量SDK插桩 + 借力成熟开源可视化"路线。
- [[summaries/s1-011-How-to-implement-observability-with-Pyth|使用 Python 与 Llama Stack 实现可观测性]] — 本文最突出的价值在于“从能跑到好用”的完整递进：第一步展示 Llama Stack 开箱即用的追踪能力，第二步指出其在真实场景下的结构性缺陷，第三步给出切实可行的客户端插桩方案。这种“先给甜头、再揭痛点、最后根治”的叙事结构，对技术写作者和综述材料组织都有很高参考价值。许多技术文档只展示成功路径，而本文敢于暴露中间状态的不足，反而大大增强了说服力，让读者理解为何需要额外的客户端插桩工作。
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] — Google 将 Cloud Trace 与 ADK 深度集成的策略非常清晰： 本地用 Web UI 做开发调试，云端用 Cloud Trace 做生产观测， 两者形成完整的开发生命周期闭环。
- [[summaries/s3-002-Distributed-tracing-for-agentic-workflow|Distributed tracing for agentic workflows with OpenTelemetry]] — - 这篇博客是智能体可观测性领域中少有的从企业级生产环境出发的实操指南， 与学术论文偏重理论框架和实验评估的风格形成了良好互补。

## 相关词条

- [[terms/runtime-instrumentation|运行时插桩]]
