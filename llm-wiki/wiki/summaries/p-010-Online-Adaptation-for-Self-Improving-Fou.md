# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

## Source

- Raw note: `raw/notes/p-010_Online_Adaptation_for_Self-Improving_Fou.md`
- 作者: Seth Karten, Joel Zhang, Tersoo Upaa, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli
- DOI: 10.48550/arXiv.2605.09998
- 证据质量: high

## Compiled Summary

业界已有成熟的编程 harness。

## Evidence Notes

- 代表产品包括 CC 与 OH。
- 具身智能体领域长期缺乏像编程 agent 那样成熟的 harness 基础设施。
- PokeAgent Challenge 的报告指出，若没有领域特定的 scaffolding，前沿视觉语言模型在 RPG 游戏中几乎无法取得进展。
- ### Harness 的四元组表示
Harness 状态被形式化为四元组：
$$
\mathcal{H} = (p, \mathcal{G}, \mathcal{K}, \mathcal{M})
$$
其中：
- $p$：系统提示词，包含指令与战略指导；
- $\mathcal{G}$：子智能体集合，可被编排器调用以处理特定任务；
- $\mathcal{K}$：技能库，既包含文本级启发式，也包含可执行代码；
- $\mathcal{M}$：持久记忆，累积事实、策略与观测。
- 此外，harness 暴露一组元工具，允许智能体与精修器就地编辑上述四组件。

## Wiki Connections

- Concepts: [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md)
- Entities: None identified
