# Agent Contracts: A Formal Framework for Resource-Bounded Autonomous AI Systems

## Source

- Raw note: `raw/notes/agentcontracts_note.md`
- Metadata: not available in note

## Compiled Summary

Contract Net Protocol（1980）首次通过合约机制实现了多智能体系统中的协调。

## Evidence Notes

- 现代智能体协议标准化了连接性与互操作性，但均未能提供形式化的资源治理规范机制，以限制智能体可以消耗多少资源或可以运行多长时间。
- 2025年末，一个工程团队部署了包含四个专业智能体的多智能体研究系统，其中两个智能体陷入递归澄清循环，在未被检测的情况下持续运行十一天，最终产生47000美元的 API 账单。
- 该系统没有任何停止条件、预算限制或实时成本监控。
- Agent Contracts 的核心是一个形式化合约规范，其元组表示为
$$C = (I, O, S, R, T, \Phi, \Psi)$$
该设计将资源治理、时间治理和质量治理统一为单一机制。
- ### 合约七元组
- **输入规范**：元组表示为 $I = (\sigma_I, \mathcal{V}_I, \mathcal{P}_I)$，
其中 $\sigma_I$ 为输入模式，$\mathcal{V}_I$ 为验证规则，$\mathcal{P}_I$ 为预处理变换
- **输出规范 $O$**：定义输出格式、质量阈值 $Q_{min}$ 和后置条件
- **成功准则 $S$**：判定任务完成的条件，可以是逻辑谓词（如 all_items_processed）、质量指标（如 accuracy > 0.95）或业务规则
- **资源约束 $R$**：多维资源预算，包括令牌数、API 调用次数、工具调用次数、计算时间和成本


## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [AWS AgentCore](entities/AWS-AgentCore.md), [Google ADK and Vertex AI](entities/Google-ADK-and-Vertex-AI.md)
