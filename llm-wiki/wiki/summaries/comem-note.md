# CoMem 深度阅读笔记

## Source

- Raw note: `raw/notes/comem_note.md`
- Metadata: not available in note

## Compiled Summary

上下文管理通过迭代总结先前的交互历史，使智能体模型能够解决长程任务。然而，这一过程通常为额外的总结令牌带来大量的解码开销，显著影响部署时的端到端响应延迟。本文提出 CoMem，一种将记忆管理从主智能体工作流中解耦的新框架，使这些过程能够并行执行。我们提出一种 k-step-off 异步流水线，将记忆模型的总结过程与智能体的推理过程重叠，从而有效掩盖上下文处理的延迟。为确保该异步设置下的鲁棒性，我们引入一种基于奖励的训练策略，使记忆模型与智能体决策所需的充分统计量对齐。理论分析证实，与耦合架构相比，CoMem 提供了更优的效率-效果权衡。我们在 SWE-Bench-Verified 上的大量实验结果表明，CoMem 在保持大部分性能的

## Evidence Notes

- 长程智能体任务（如软件工程中的仓库级代码生成）要求模型维护跨越数千步的交互历史。随着交互历史增长，键值缓存占用线性扩张，解码阶段的内存带宽成为瓶颈，导致每输出一个令牌都需要从高带宽显存加载庞大的键值缓存。现有方案分为两类：上下文缩减策略（如滑动窗口注意力、检索增强生成）牺牲了长距离依赖的召回能力；系统级优化（如分页注意力、稀疏注意力、键值缓存量化）虽然提升了吞吐量，但未能解决根本问题——每步解码都需要重新访问大量基本静态的历史。CoMem 试图回答：**能否在不影响智能体决策质量的前提下，将长上下文处理的计算负担从解码关键路径中移除？**
> [!figure] Fig.
- 1: CoMem framework: a decoupled agent framework that offloads long-context compression to an asynchronous, lightweight memory model, significantly reducing inference latency without compromising reasoning performance.
- ### 系统架构
CoMem 的核心架构包含两个模型：
- **记忆模型**：一个参数量较小的原生长上下文模型（如 Qwen3-4B），负责将长期交互历史压缩为紧凑的状态表示。
- - **智能体模型**：一个能力更强、参数量更大的模型，基于压缩摘要和短期上下文提出动作策略。
- Table 1 展示了 CoMem 在三种不同规模主干模型上的主要实验结果。
- **DeepSWE（32B 稠密模型）**：
- 完整上下文基线解决率 40.4%，延迟 9457.78s
- GRPOAC（CoMem）解决率 41.0%，延迟 5622.33s（无 CPU 卸载，1.68x 加速）或 4400.89s（有 CPU 卸载，1.45x 加速）
- 值得注意的是，GRPOAC 解决率略高于完整上下文基线，表明对齐后的摘要能够有效过滤无关噪声
**Qwen3-Coder-Max（480B）**：
- 完整上下文基线解决率 57.2%，延迟 6291.11s
- GRPOAC 解决率 51.0%，延迟 3917.68s（1.61x）或 3594.51s（1.43x）
- 相比无摘要基线（46.6%）和监督

## Wiki Connections

- Concepts: [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Arize Phoenix](entities/Arize-Phoenix.md)
