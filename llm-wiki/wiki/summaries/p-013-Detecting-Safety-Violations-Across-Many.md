# Detecting Safety Violations Across Many Agent Traces

## Source

- Raw note: `raw/notes/p-013_Detecting_Safety_Violations_Across_Many_.md`
- 作者: Adam Stein, Davis Brown, Hamed Hassani, Mayur Naik, Eric Wong
- 年份: 2026
- 来源: arXiv (Cornell University)
- DOI: 10.48550/arXiv.2604.11806
- 证据质量: high
- PDF: [p-013]-meerkat-detecting-safety-violations-across-many-agent-traces.pdf

## Compiled Summary

为了识别安全违规，审计人员经常需要在大量智能体轨迹中进行搜索。这类搜索非常困难，因为失败往往是稀少的、复杂的，有时甚至是被对抗性地隐藏起来的，只有在多条轨迹被共同分析时才能被发现。这些挑战出现在多种场景中，例如滥用活动、隐蔽破坏、奖励篡改和提示注入。现有方法在这类问题上表现不佳，原因有多个：逐轨迹评判器会遗漏那些只有在跨轨迹视角下才可见的失败；朴素的智能体审计无法扩展到大规模轨迹集合；而固定监控器对未预见到的行为非常脆弱。我们引入了 Meerkat，它结合聚类与智能体搜索，以发现由自然语言描述的安全违规。通过结构化搜索和对有前景区域的自适应调查，Meerkat 能够在不依赖种子场景、固定工作流或穷举枚举的情况下发现稀疏的失败。在滥用

## Evidence Notes

- 当前 AI 安全监控研究大多聚焦于逐轨迹的异常检测，即判断单条智能体交互记录是否包含破坏、隐藏目标或其他不安全行为。然而在实际部署中，安全违规的证据往往分散在大量轨迹之中，单看任何一条轨迹都可能是无害的。例如 Anthropic 曾发现的大规模网络间谍活动，正是通过多条看似正常的查询组合在一起才构成了完整攻击，只有事后仔细的跨轨迹监控才能揭露。
- 这种仓库级审计面临三个核心困难：
- **分布式证据**：违规的证明存在于多条轨迹的联合见证 $W$ 中，且 $|W| > 1$，单条轨迹无法定责。
- Meerkat 的整体思路是：先用聚类将海量轨迹组织成层次结构，使相关轨迹可以被集中比较、良性区域被快速降级；再构建包含安全属性、仓库内容和聚类结构的提示与环境，交给通用智能体进行推理、假设见证并给出判决。
- ### 机制流程
Meerkat 的核心流程如 Algorithm 1 所示，输入为轨迹仓库与自然语言安全属性，输出为离散判决、仓库级分数、逐轨迹分数序列以及候选见证集合。整体可分为四个阶段：
1.
- ### 分布式滥用检测
![Fig.
- 2 分布式滥用检测的 precision-recall 曲线](p-013_Detecting_Safety_Violations_Across_Many_/images/fig2_dm_pr_curves.png)
Figure 2 展示了网络与生物两个分布式滥用领域上的精确率-召回率曲线。Meerkat 在两种设定下均显著优于所有基线。特别地，当单轨迹监控器在生物领域背景比例为 100 倍时几乎完全失效（平均精确率接近 0），Meerkat 配合 Qwen3.5 仍能达到 0.142 的平均精确率。这是因为分布式滥用属性只能由多条轨迹联合满足，单轨迹分类器本质上无法检测此类违规，而 Meerkat 通过同时推理多条轨迹实现了突破

## Wiki Connections

- Concepts: [[concepts/audit-trails-security-and-governance]]
- Entities: None identified
