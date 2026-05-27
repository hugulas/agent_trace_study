# DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems

## Source

- Raw note: `raw/notes/p-003_DoVer_Intervention-Driven_Auto_Debugging.md`
- 作者: Ming Ma, Jue Zhang, Fangkai Yang, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- 年份: 2025
- 来源: arXiv preprint
- DOI: 10.48550/arXiv.2512.06749

## Compiled Summary

基于大语言模型的多智能体系统难以调试，因为故障往往产生于漫长且分支交错的交互轨迹中。

## Evidence Notes

- 当前的主流做法是利用大语言模型分析日志以定位故障，将错误归因到具体的智能体和步骤。
- 当前基于大语言模型的多智能体系统在开发和部署过程中频繁出现非崩溃型故障：系统执行未中断，但输出结果不正确或不符合预期。现有主流做法是让大语言模型分析执行日志，将故障归因到特定智能体或特定步骤。然而，作者通过复现研究指出这一范式面临以下根本性问题。
- **日志分析假说无法验证**：仅通过日志推断的故障原因只是未经测试的推测，无法确认修改该步骤后任务能否成功。即便最强的模型也只能给出概率性的归因判断，缺乏执行层面的因果验证。
- DoVer 的核心思想是将故障调试从看日志猜原因转变为改日志验结果。整个流水线分为四个阶段：试炼分段、故障归因、干预生成、干预执行与评估。
- ### 机制流程
![Figure 2 DoVer 调试流水线](p-003_DoVer_Intervention-Driven_Auto_Debugging/images/fig2_pipeline.png)
1.

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
