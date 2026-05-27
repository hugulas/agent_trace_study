# Agent psychometrics: 智能体代码基准的任务级性能预测

## Source

- Raw note: `raw/notes/taskpredict_note.md`
- Metadata: not available in note

## Compiled Summary

随着基于大语言模型的代码生成从静态单步生成转向与工具和环境进行多步智能体交互，理解哪些任务会对智能体构成挑战以及原因变得愈发困难。当前实践进一步加剧了这一问题：智能体性能通常以基准测试上的聚合通过率来衡量，但单一数字指标掩盖了基准内部任务的多样性。本文提出了一套面向智能体代码评测场景的个体任务成功或失败预测框架。我们的方法用从任务中提取的丰富特征来增强项目反应理论，这些特征包括问题陈述、仓库上下文、解决方案和测试用例，并引入了一种将智能体能力分解为大语言模型能力与脚手架能力的新参数化方式。这种参数化使我们能够聚合来自异构排行榜的评估数据，并准确预测未见基准上的任务级性能，以及未见过的大语言模型与脚手架组合的性能。我们的方法对基准设计

## Evidence Notes

- 智能体代码评测正从静态单步生成转向多步交互式评估。这种转变带来三个核心挑战：
- **环境交互的复杂性**。测试用例往往检验问题陈述中未提及的代码库属性，或允许未充分指定的提交通过，导致任务存在多条有效解决路径和难以预料的边缘情况。
- - **任务异质性**。同一基准内的不同任务可能因不同原因导致智能体失败，而当前常见的单一聚合通过率指标无法捕捉这种差异。
- ### 核心思想
本文扩展标准项目反应理论，使其能够利用任务特征和智能体特征进行任务级性能预测，而不是将智能体和任务视为无结构的离散编号。
- 标准项目反应理论的 logistic 模型为：
$$P(y_{ij} = 1 \mid \theta_i, \beta_j) = \sigma(\theta_i - \beta_j)$$
其中 $\theta_i$ 是被试（此处为智能体）的能力参数，$\beta_j$ 是试题（此处为任务）的难度参数，$y_{ij}$ 是二元正确性指标。
- > [!figure] Table 1: Experimental settings
> 建议位置：关键结果
> 放置原因：总结四种实验设置的配置细节，是理解后续所有结果表的前提
> 当前状态：占位符
### 新任务上的难度预测
在新任务设置下，论文比较了三种任务特征向量在四个基准上的 AUC-ROC：
> [!figure] Table 2: AUC-ROC on held-out tasks for each of the four benchmarks
> 建议位置：关键结果
> 放置原因：核心结果表，展示各特征方法相对基线和 Oracle 的绝对性能位置
> 当前状态：占位符
具体数值如下：
| 基准 | 基线方法 | 嵌入
- ### 特征源消融
评判者特征源的消融实验显示，逐步加入问题陈述之外的智能体任务产物能够持续提升预测性能。这说明仅依赖问题陈述不足以刻画智能体代码任务的难度。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
