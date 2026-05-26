# Monitoring Monitorability

## Source

- Raw note: `raw/notes/p-006_Monitoring_Monitorability.md`
- 作者: Melody Y. Guan, Miles Wang, Micah Carroll, Zehao Dou, Annie Y. Wei, Marcus Williams, Benjamin Arnav, Joost Huizinga, Ian Kivlichan, Mia Glaese, Jakub Pachocki, Bowen Baker
- DOI: 10.48550/arXiv.2512.18311
- arXiv: 2512.18311
- 证据质量: medium
- PDF: [p-006]-monitoring-monitorability.pdf

## Compiled Summary

现代 AI 系统的决策过程需要具备可观测性，才能安全地部署能力越来越强的智能体。

## Evidence Notes

- 对当前推理模型的思维链（chain-of-thought）进行监控，已被证明在检测模型不良行为方面十分有效。
- 随着前沿模型能力不断提升，其造成潜在危害的能力也在增长。确保模型安全部署的两大方向是对齐与控制。尽管对齐研究取得了进展，模型仍偶尔出现不良行为，因此深度防御至关重要。控制协议通常包含某种形式的不良行为分类器，它们可以访问智能体的部分观测信息，例如输入提示、智能体行为、最终输出或内部神经激活。
- 现代推理模型的出现提供了一个独特的监控机会：它们在被训练用人类语言思考后才给出输出或行动，这使得我们可以监控其思维链。已有研究表明，思维链监控在检测奖励篡改等不当行为方面具有实用价值。然而，思维链可监控性尚未被充分理解，学界普遍担忧它在不同训练流程或持续扩展下可能十分脆弱。
- ### 指标设计
为了在不同模型和监控器之间进行公平比较，需要一种对类别不平衡不敏感的指标。标准的 F1 和准确率会随基线行为率变化，无法区分真实可监控性的变化与行为分布的变化。
- 本文选择灵敏度（TPR）与特异度（TNR）的几何均值：
$$\text{g-mean} = \sqrt{\mathrm{TPR} \cdot \mathrm{TNR}}$$
并进一步将其平方得到 g-mean²，以更严厉地惩罚失败：
$$\text{g-mean}^2 = \mathrm{TPR} \times \mathrm{TNR}$$
在实践中，监控器的 TNR 通常接近 1，因此 g-mean² 很大程度上追踪 TPR，直观反映监控器在目标属性出现时的检测频率。随机监控器的 g-mean² 期望值为 0.25。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/evaluation-and-benchmarking]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: None identified
