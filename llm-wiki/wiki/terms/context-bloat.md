# 上下文膨胀

## 定义

上下文膨胀指长程智能体在累积消息、工具返回、检索片段、记忆和多智能体通信时不断扩大 prompt，导致成本、延迟和错误传播同步上升。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些历史信息真正影响下一步决策？
- 上下文压缩会损失哪些可监控和审计信号？
- 长上下文成本应如何与失败风险一起评估？

## 证据入口

- [Token Economics for LLM Agents: A Dual-View Study from Computing and Economics](summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi.md) — 在 agentic trace 分析的研究中，我们通常关注功能正确性和执行效率，但往往忽视了经济维度。
- [A Guide to AI Agent Cost Optimization With Observability](summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi.md) — 这篇指南的最大价值在于它将「可观测性」从「事后排查工具」重新定位为「成本工程的基础设施」。
- [AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives](summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho.md) — 这篇技术文章的实践价值极高，因为它揭示了一个被学术界和工业界同时忽视的问题：agent 系统的真实运行成本与其设计时的成本预估之间存在数量级的差距。
- [LLM Agent Cost Attribution: Complete Production 2026 Guide](summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod.md) — 这篇指南的价值在于它将成本归因从一个财务部门的报表需求，重新定义为工程团队的基础设施责任。
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc.md) — LLM 智能体面临的根本挑战是什么？传统上，社区将智能体能力的提升等同于模型规模的扩大和训练数据的增加。然而，本文指出，仅凭更大的模型权重无法解决三类反复出现的失配： - **连续性失配**：上下文窗口有限且会话记忆薄弱，导致长程任务中的状态难以保持。
- [Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems](summaries/Dive-Into-Claude-Code.md) — 论文的核心研究问题可以概括为：当前主流智能体编码工具的架构是如何从人类价值观和设计原则出发演化而来的？不同系统在面对相同设计空间问题时做出了哪些不同的选择，这些选择的后果是什么？ 具体的设计空间问题包括： - 推理应该发生在何处（模型内部还是外部编排层）。
- [(Proposal) Adding OpenTelemetry Trace Support to MCP](summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp.md) — 这篇 GitHub Discussion 是我所读到的关于 MCP 可观测性最深入、最富张力的原始技术资料之一。其价值不仅在于提案本身的设计细节，更在于围绕该提案展开的多元观点碰撞，这些碰撞暴露了当前 Agent 可观测性领域许多尚未被充分讨论的深层问题。
- [Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践](summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践.md) — 腾讯云这篇实践文章的价值在于其「从实践中来」的视角。
- [GenAIOps on AWS: 端到端可观测性栈](summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability.md) — 这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做" 同时讲透的工业博客。
- [How we built our multi-agent research system — Anthropic Engineering Blog](summaries/a-009-How-we-built-our-multi-agent-research-sy.md) — Anthropic 这篇文章堪称多智能体系统从原型到生产的最完整工程复盘之一，其价值不仅在于架构设计，更在于对"为什么有效"和"代价是什么"的坦诚剖析。90.2% 的性能提升令人印象深刻，但"token 消耗解释 80% 方差"这一发现更具理论意义——它暗示多智能体系统的性能提升在很大程度上是"推理容量扩展"的结果，而非某种神秘的涌现智能。这对综述的方法论有重要启示：在评估多智能体系统时，必须将 token 效率与结果质量同时纳入指标，否则可能产生误导性的结论。一个消耗 15 倍 token 却只提升 10% 准确率的系统，与一个消耗 2 倍 token

## 相关词条

- [成本归因](terms/cost-attribution.md)
- [Token 经济学](terms/token-economics.md)
- [Token 预算](terms/token-budget.md)
