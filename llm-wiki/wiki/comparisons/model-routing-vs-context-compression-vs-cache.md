# 模型路由、上下文压缩与缓存复用对比

## 对比表

| 维度 | 对象 1 | 对象 2 | 对象 3 |
| --- | --- | --- | --- |
| 机制 | 按任务难度和预算选择模型 | 裁剪、摘要或分层保留历史上下文 | 复用 prompt、工具结果或语义相似响应 |
| 主要收益 | 降低昂贵模型调用占比 | 降低每轮输入 token 与延迟 | 减少重复计算和外部调用 |
| 主要风险 | 低估任务难度导致质量下降 | 丢失关键证据或审计上下文 | 缓存陈旧、隐私泄漏或错误复用 |
| 观测要求 | 记录路由理由、候选模型和降级结果 | 记录被裁剪内容摘要与压缩比例 | 记录命中率、失效策略和复用来源 |
| 更适合 | 任务异质性高的产品 | 长程 agent 和多轮会话 | 重复查询、稳定工具和高频工作流 |

## 读法

这个对比页用于帮助选择分析层，而不是给工具或论文排名。若要解释单条失败轨迹，优先看诊断与归因；若要比较模型和领域，优先看过程评测；若要做生产接入，先保证结构化采集和 schema 稳定。

## 证据入口

- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [[summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho|AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives]] — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [[summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod|LLM Agent Cost Attribution: Complete Production 2026 Guide]] — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [[summaries/Dive-Into-Claude-Code|Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems]] — 论文的核心研究问题可以概括为：当前主流智能体编码工具的架构是如何从人类价值观和设计原则出发演化而来的？不同系统在面对相同设计空间问题时做出了哪些不同的选择，这些选择的后果是什么？ 具体的设计空间问题包括： - 推理应该发生在何处（模型内部还是外部编排层）。
- [[summaries/s2-022-Helicone-LLM-Observability-Platform-Lea|Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化]] — Helicone 的评测让我对"Proxy 模式 versus SDK 插桩模式"的架构之争 有了更具体、更工程化的理解。
- [[summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc|Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering]] — LLM 智能体面临的根本挑战是什么？传统上，社区将智能体能力的提升等同于模型规模的扩大和训练数据的增加。然而，本文指出，仅凭更大的模型权重无法解决三类反复出现的失配： - **连续性失配**：上下文窗口有限且会话记忆薄弱，导致长程任务中的状态难以保持。
- [[summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp|(Proposal) Adding OpenTelemetry Trace Support to MCP]] — 这篇 GitHub Discussion 是我所读到的关于 MCP 可观测性最深入、最富张力的原始技术资料之一。其价值不仅在于提案本身的设计细节，更在于围绕该提案展开的多元观点碰撞，这些碰撞暴露了当前 Agent 可观测性领域许多尚未被充分讨论的深层问题。
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] — 这篇博客的最大价值在于其极强的可操作性。与多数学术论文聚焦评估指标与算法改进不同，本文给出了大量可直接运行或稍加修改即可部署的 Python 代码片段，从 Streamlit UI 到 FastAPI 端点，从 Langfuse CallbackHandler 到熔断器类实现，工程师可以按图索骥在数小时内搭建最小可行生产系统。这种「从零到一」的指导意义，使其在综述的工程实践章节中占据了独特位置。

## 相关页面

- [[terms/agent-trace|智能体轨迹]]
- [[viewpoints/observability-is-not-logging|智能体可观测性不是日志收集]]
- [[viewpoints/final-reward-is-insufficient|最终奖励不足以评估智能体]]
