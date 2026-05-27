# Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios

## Source

- Raw note: `raw/notes/trouter_note.md`
- Metadata: not available in note

## Compiled Summary

大型语言模型在不同任务和查询上的性能与计算成本存在显著差异，这促使研究者构建能够根据用户特定的成本与性能权衡来选择模型的路由系统。然而，现有路由器在缺乏领域内训练数据的冷启动场景中泛化能力较差。本文通过一种多级任务画像引导的数据合成框架来解决这一局限，该框架构建层次化任务分类体系并生成多样化的问答对，以逼近测试时的查询分布。在此基础上，本文提出 TRouter，一种任务类型感知的路由方法，它通过隐式任务类型变量对查询条件下的成本与性能进行建模，并利用合成任务分类体系导出的先验进行正则化。这一设计提升了 TRouter 在冷启动与有数据场景下的路由效用。在多个基准测试上的实验表明，本文的合成框架能够缓解冷启动问题，且 TRouter 

## Evidence Notes

- 现有大语言模型路由方法大多假设能够获取领域内标注训练数据，并在此基础上评估所有候选模型以收集性能与成本指标，进而训练轻量路由器。然而，真实部署中个人用户与早期产品常面临冷启动困境，缺乏资源收集标注数据。此外，预训练路由器在部署时常因训练与测试输入之间的领域偏移而泛化不佳。实验表明，即使在跨域设定下，现有分类与回归方法的表现甚至可能弱于简单的规则基线。
- > [!figure] Fig.
- ### 问题形式化
设候选模型集合为 $M = \{m_1, \dots, m_M\}$，用户查询为 $q$。LLM 路由的目标是选择模型 $m^*$ 以最大化如下效用函数：
$$m^* = \arg\max_{m \in M} U(m,q) = \mu_r \cdot r(m,q) - \mu_c \cdot c(m,q)$$
$$\text{s.t.} \quad \mu_r + \mu_c = 1, \quad \mu_r, \mu_c \geq 0$$
其中 $r(\cdot)$ 与 $c(\cdot)$ 分别为性能函数与成本函数。$\mu_r$ 与 $\mu_c$ 反映用户对性能与成本权衡的偏好。性能评估指标随任务类型而异
- ### 机制流程
1.
- 论文在冷启动与有数据两种设定下对比了多种基线方法。主结果表格分别展示了使用传统指标与使用大模型评判估计性能的两种评估方式。在两种设定下，TRouter 在三种用户偏好场景中均取得最优或次优表现，且在有数据设定下将效用总和提升超过 0.3。相比之下，分类基线 RouterDC 与回归基线 MetricRouter 在跨域设定中表现不佳，甚至弱于简单的规则基线。
- > [!figure] Table 3: Results across three user preference settings in both cold-start and in-domain scenarios.

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
