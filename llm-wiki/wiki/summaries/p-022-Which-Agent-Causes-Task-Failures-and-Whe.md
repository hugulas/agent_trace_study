# Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems

## Source

- Raw note: `raw/notes/p-022_Which_Agent_Causes_Task_Failures_and_Whe.md`
- 作者: Shaokun Zhang, Ming Yin, Jieyu Zhang, Jiale Liu, Zhiguang Han, Jingyang Zhang, Beibin Li, Chi Wang, Huazheng Wang, Yiran Chen, Qingyun Wu
- DOI: 10.48550/arXiv.2505.00212
- arXiv: 2505.00212
- 证据质量: high

## Compiled Summary

在大语言模型多智能体系统中，故障归因——即识别导致任务失败的智能体和具体步骤——为系统调试提供了关键线索。但该领域尚未得到充分探索，且高度依赖人工劳动。本文提出并形式化了一个新研究方向：面向 LLM 多智能体系统的自动化故障归因。为支持该研究，作者构建了 Who-When 数据集，包含来自 127 个 LLM 多智能体系统的详细失败日志，并附有细粒度标注，将失败与特定智能体及决定性错误步骤关联起来。基于 Who-When，作者开发并评估了三种自动化故障归因方法，总结了各自的优势与局限。最优方法在识别故障责任智能体上的准确率为 53.5%，但在定位故障步骤上的准确率仅为 14.2%，部分方法甚至低于随机水平。即便使用 OpenAI-o

## Evidence Notes

- 随着 LLM 多智能体系统（如 AutoGen、CAMEL、MetaGPT 等）在编码、科学发现、复杂现实世界问题求解等领域展现出巨大潜力，系统开发通常遵循一个迭代循环：在基准上评估系统表现，然后手动进行故障归因，最后针对性地改进系统。然而，故障归因——即识别直接导致任务失败的系统组件——目前几乎完全依赖人工完成。开发人员需要分析复杂的历史执行日志，理解每个智能体的行为逻辑，并判断哪些动作是正确的、哪些动作误导了整个求解过程。随着系统复杂度增加，组件数量增多，手动故障归因变得愈发困难且耗时。
- 现有研究主要通过构建更细粒度的基准（如 DevAI）来辅助故障归因，但这本质上仍只是提供更多参考指标，未能从根本上解决"评估结果如何映射到具体故障组件"的问题。因此，本文提出一个核心问题：**能否利用 LLM 的能力自动识别多智能体系统中导致任务失败的智能体（哪个）和具体步骤（何时）？**
![Figure 1 研究动机与自动化故障归因概览](p-022_Which_Agent_Causes_Task_Failures_and_Whe/images/fig1_overview.png)
- 本文提出并评估了三种自动化故障归因方法，分别对应不同的信息接收策略。所有方法均基于以 LLM 为裁判的范式，由判断模型对失败日志进行分析。
- ### 机制流程
三种方法的执行流程可概括如下：
1.
- ### 总体性能对比（Table 1）
Table 1 展示了三种方法在 Who-When 数据集上的总体表现（使用 GPT-4o）。以下表格来自 LaTeX 源码 `_exp.tex`：
| Agentic Systems Types | Setting | Random Agent-Level | Random Step-Level | All-at-Once Agent-Level | All-at-Once Step-Level | Step-by-Step Agent-Level | Step-by-Step Step-Level | Binary Search Agent-Level | Binary Search St
- - **步骤准确率依赖细粒度处理**：逐步法在步骤准确率上表现最好（最高 25.51%），因为它逐步处理上下文，能更聚焦地定位错误步骤。全局法在步骤准确率上表现最差，部分设置甚至低于随机基线，这体现了"大海捞针"问题——LLM 难以从长上下文中精确定位特定信息。

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
