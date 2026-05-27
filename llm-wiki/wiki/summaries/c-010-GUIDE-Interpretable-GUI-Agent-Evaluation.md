# GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis

## Source

- Raw note: `raw/notes/c-010_GUIDE_Interpretable_GUI_Agent_Evaluation.md`
- 作者: Yuwen Zhai, Runze Li, Liang Wang, Nian Shi, Liwu Xu, Wei Zhang, Ran Lin, Bo Xu, Benlei Cui
- 年份: 2026
- 来源: arXiv (Cornell University)
- DOI: 10.48550/arXiv.2604.04399
- 证据质量: medium
- PDF: [c-010]-guide-interpretable-gui-agent-evaluation-via-hierarchical-di.pdf

## Compiled Summary

GUIDE 的核心贡献在于重新界定了 "好的 Agent 评估器" 的标准：不仅要准，还要能被开发者读懂并利用。

## Evidence Notes

- 当前 LLM-as-judge 的评估范式虽然在很多任务上达到了可接受的准确率，但其黑盒式的整体打分对 Agent 开发者而言几乎是不可用的——知道 Agent 得了 70 分，却不知道失分的 30 分丢在哪里，这种信息熵的浪费在工程实践中不可接受。

## Wiki Connections

- Concepts: [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md)
- Entities: None identified
