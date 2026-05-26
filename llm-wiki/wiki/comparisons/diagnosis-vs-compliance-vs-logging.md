# 失败诊断、过程合规与结构化日志的分工

## 对比表

| 维度 | 对象 1 | 对象 2 | 对象 3 |
| --- | --- | --- | --- |
| 核心问题 | 哪里失败、为什么失败 | 是否按规范行动 | 发生了什么、如何复现 |
| 典型输入 | 失败轨迹、工具约束、人工标注 | 系统提示、工具 schema、完整轨迹 | 消息、工具调用、状态、span |
| 典型输出 | 关键失败步骤、失败类别、责任主体 | 多维合规评分、违规类型 | 结构化事件、可查询 trace |
| 适用阶段 | 失败后调试与 benchmark 分析 | 持续评测与模型/领域对比 | 运行时采集与离线分析基底 |
| 代表来源 | AgentRx, Who&When, GUIDE | AgentPex, monitorability work | AgentTrace, OpenInference, OTel material |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 通过零侵入运行时插桩与三层面统一 Schema，把 LLM 智能体的操作执行、认知推理与环境交互转化为结构化、可内省且与 OpenTelemetry 兼容的日志流，为智能体安全、问责与评估提供了基础设施级的可观测性支撑。
- [[summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] — AgentPex 是一个从提示和工具规范中抽取行为规则、再自动检查智能体轨迹是否违反这些规则的过程性评测工具。
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] — AgentRx 博客的价值不仅在于技术本身，更在于它清晰地展示了一个从学术研究到开源工具的完整叙事。
- [[summaries/a-002-GitHub-microsoftAgentRx|GitHub — microsoft/AgentRx]] — AgentRx 的设计哲学值得在综述中重点展开：它将"诊断"视为一个独立于"执行"的工程环节，通过引入 Trajectory IR 和约束合成，把原本需要人工逐行阅读日志的调试工作自动化。这种分层思想——采集层（原始日志）→ 表示层（IR）→ 规则层（不变量）→ 证据层（检查器）→ 判断层（Judge）→ 应用层（报告）——为 agent 可观测性提供了一个完整的方法论闭环。
- [[summaries/c-011-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — AgentTrace 的最大贡献在于将智能体可观测性问题从传统的"事后调试工具" 提升到了"运行时安全基础设施"的战略高度。
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] — AgentRx 是一个面向智能体执行轨迹的失败诊断框架，核心目标是在长轨迹中定位第一个关键失败步骤，并用约束违反证据解释失败类别。
- [[summaries/AgentPex-Willful-Disobedience|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] — AgentPex 通过从提示自动提取行为规范并以大语言模型作为裁判逐条评估轨迹合规性，弥补了仅结果评估无法发现的过程性失败，在四百二十四条 tau-squared-bench 轨迹上揭示了模型特有的故意不服从模式。
- [[summaries/c-013-Hermes-Agent-Trajectory-Format|Trajectory Format - Hermes Agent]] — Hermes Agent 的轨迹格式文档是我目前见过的最详尽的训练数据工程规范之一。它的价值不仅在于定义了一种格式，更在于展示了一个完整的"从运行时到训练集"的数据流水线设计。其中最令我印象深刻的是推理内容的归一化策略——通过强制每个 gpt 轮次包含 <think> 块，即使模型未产生显式推理，也保证了训练数据在格式上的绝对一致性。这种"宁缺勿滥"的严格性对于大规模预训练或微调至关重要，因为数据格式的不一致是导致训练失败或性能退化的常见原因。在分布式训练环境中，如果不同 worker 加载的数据具有不同的字段结构或内容格式，不仅会导致训练崩溃，还可能引

## 相关页面

- [[terms/agent-trace|智能体轨迹]]
- [[viewpoints/observability-is-not-logging|智能体可观测性不是日志收集]]
- [[viewpoints/final-reward-is-insufficient|最终奖励不足以评估智能体]]
