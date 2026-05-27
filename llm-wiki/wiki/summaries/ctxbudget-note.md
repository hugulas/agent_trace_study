# ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents

## Source

- Raw note: `raw/notes/ctxbudget_note.md`
- Metadata: not available in note

## Compiled Summary

基于大语言模型的智能体在长程推理中展现出显著潜力，但其上下文规模受到部署因素的限制，例如内存、延迟和成本，形成了严格的上下文预算约束。随着交互历史的增长，在保留历史信息与控制上下文长度之间形成权衡。为应对这一挑战，本文提出预算感知上下文管理框架（Budget-Aware Context Management，BACM），将上下文管理建模为一个带上下文预算约束的序贯决策问题。该框架使智能体能够在纳入新观测之前评估可用预算，并决定何时以及压缩多少交互历史。本文进一步提出 BACM-RL，一种端到端的基于课程学习的强化学习方法，用于在不同上下文预算下学习压缩策略。在组合多目标问答和长程网页浏览基准上的实验表明，BACM-RL 在不同模型规

## Evidence Notes

- 长程交互场景中，智能体的交互历史随步数增长迅速膨胀，而部署资源（内存、推理延迟、服务成本）严格限制了最大上下文窗口。现有上下文压缩方法普遍采用"无预算"形式化，将压缩视为静态操作，不以可用上下文容量为条件进行显式决策。这种简化导致两种关键失效模式：
- **宽松预算下过度压缩**：智能体可能压缩掉任务关键证据，降低信息保真度；
- **紧缩预算下压缩不足**：智能体可能未能充分压缩，导致上下文溢出、截断或脆弱的推理失败。
- 近期虽有研究将预算意识引入智能体推理，例如限制工具调用次数或输出令牌预算，但这些方法主要通过外部控制来调节计算量或动作数量，但并未系统性地解决上下文窗口预算本身成为瓶颈时的主动历史压缩问题。
- BACM 的核心思想是将上下文管理建模为一个带预算约束的序贯决策问题，使压缩决策能够根据剩余上下文容量在推理全过程中动态调整。
- ### 问题设定
设总上下文预算为 $B$，当前上下文为 $C_t$，待加载的新观测为 $o_t$。在将 $o_t$ 加入上下文之前，智能体先观测预算状态：
$$
b_t = (s_t, r_t, |o_t|)
$$
其中 $s_t$ 为当前上下文结构信息，$r_t = B - |C_t|$ 为剩余预算，$|o_t|$ 为待加载观测的令牌长度。上下文 $C_t$ 由若干 commit 块组成：$C_t = \{c_1, c_2, \dots, c_K\}$。
- ### 主实验性能
在 BrowseComp-Plus 和多目标问答基准上的主实验结果（表 1）显示，BACM-RL 在两个骨干模型上均取得最佳平均性能，且跨越架构与参数量差异（7B 与 30B），表现出广泛的适用性。
- > [!figure] Table 1: Performance comparison across QA settings
> 建议位置：关键结果
> 放置原因：该表汇总了 BrowseComp-Plus 和多目标问答的核心数值，是验证方法有效性的首要证据
> 当前状态：占位符
**BrowseComp-Plus（8k 预算，30B 模型）**：
- BACM-RL 平均准确率 0.147，超过 128k 窗口的 235B Qwen3-Inst（0.136），在 8k 预算约束下实现了以小博大的效果。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
