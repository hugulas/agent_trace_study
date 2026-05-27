# Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems

## Source

- Raw note: `raw/notes/supervisoragent_note.md`
- Metadata: not available in note

## Compiled Summary

尽管多智能体系统在复杂任务中表现优异，但随着运行复杂度的提升，其自主性的增长往往导致严重的效率低下，例如过度的令牌消耗以及由错误信息引发的失败。现有方法主要聚焦于事后失败归因，缺乏能够主动、实时提升系统鲁棒性与效率的干预手段。为此，本文提出 SupervisorAgent，一种轻量且模块化的运行时自适应监督框架，该框架无需修改底层智能体的架构即可工作。在无需大语言模型参与的自适应过滤器触发下，SupervisorAgent 在关键节点进行干预，主动纠正错误、引导低效行为并净化观察信息。在具有挑战性的 GAIA 基准测试上，SupervisorAgent 将 Smolagent 框架的令牌消耗平均降低 29.68%，同时不损害其成功率

## Evidence Notes

- 本文解决的核心矛盾可概括为：多智能体系统的能力与复杂度持续提升，但其运行鲁棒性与经济性却在下降。具体而言，本文识别出两大效率瓶颈来源：
- **观察信息过载**：智能体在处理冗长的网页内容或工具输出时，上下文窗口被大量无关信息淹没，不仅推高了令牌成本，还可能掩盖关键信息，导致智能体偏离任务目标。
- - **策略性低效**：智能体可能陷入重复的行动循环，或选择过于复杂的求解路径，造成计算资源的浪费。
- ### 形式化定义
本文将受监督的多智能体系统（Supervised Multi-Agent System, SMAS）形式化如下。对于每个智能体，定义其工作单元为：
$$W = (N, Q_g, Q_l, T_l, S)$$
其中 $N$ 为被监督智能体的名称，$Q_g$ 和 $Q_l$ 分别为全局与局部查询，$T_l$ 为局部轨迹，$S$ 为当前状态。扩展工作单元进一步纳入全局交互轨迹：
$$W_{\text{ext}} = W \cup \{T_g\}$$
其中 $T_g$ 记录所有智能体交互的全局轨迹。
- ### 监督目标：三大高风险交互点
SupervisorAgent 的监督目标聚焦于三类高风险交互通道：
1.
- ### GAIA 主实验
在 GAIA 验证集上，以 Smolagent 为基线的实验结果显示，SupervisorAgent（SMAS）在保持竞争力的 pass@k 成功率的同时，显著降低了平均令牌成本。具体而言：
- pass@1 准确率从基线的 34.62% 提升至 **38.46%**（提升 3.84%）。
- - 平均令牌消耗从基线的 611.90K 降至 **427.72K**（降低 30.10%）。

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
