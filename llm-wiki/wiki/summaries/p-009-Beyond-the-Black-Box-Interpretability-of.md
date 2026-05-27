# Beyond the Black Box: Interpretability of Agentic AI Tool Use

## Source

- Raw note: `raw/notes/p-009_Beyond_the_Black_Box_Interpretability_of.md`
- 作者: Hariom Tatsat, Ariye Shater
- 年份: 2026
- 来源: ArXiv.org
- DOI: 10.48550/arXiv.2605.06890
- 证据质量: high
- PDF: [p-009]-beyond-the-black-box-interpretability-of-agentic-ai-tool-use.pdf

## Compiled Summary

AI 智能体在高风险企业工作流中具有广阔前景，但可靠部署仍受限于工具使用故障难以诊断与控制。智能体可能跳过必要的工具调用、不必要地调用工具，或执行仅在事后才显现后果的操作。现有可观测性方法大多来自外部：提示词只能揭示相关性，评估只打分输出，日志仅在模型已经行动之后才到达。在长程设置中，这些故障尤其昂贵，因为早期的工具错误会改变后续整个轨迹，增加 token 消耗，并带来下游安全与风险。

## Evidence Notes

- 本文提出一种基于稀疏自编码器（SAE）和线性探针的机制可解释性工具包。该框架在每次行动前读取模型状态，推断当前是否需要工具以及下一步工具行动的可能风险等级。通过将激活分解为稀疏特征，它能够识别与工具决策最相关的内部层和特征，并通过特征消融检验其功能重要性。作者在 NVIDIA Nemotron 函数调用数据集的多步轨迹上训练探针，并将相同工作流应用于 GPT-OSS 20B 和 Gemma 3 27B 模型。
- 论文围绕四个研究问题展开：
- **RQ1**：模型激活是否编码了当前决策步骤是否需要工具？
- **RQ2**：哪些稀疏特征和层最强地编码了工具需求与工具风险信号？
- **RQ3**：内部信号能否比日志更清晰地揭示遗漏调用和不必要调用？
- **RQ4**：这些信号在重复决策点之间以及跨数据集零样本迁移时是否仍然有效？
- 本文方法的核心思想是：在模型做出工具决策前的瞬间，读取其内部激活，通过 SAE 分解为稀疏特征，再用线性探针读出两个互补信号。整个流程不依赖工具特定的输出模式，因此可跨多个工具和重复决策点复用。
- ![图 1 机制监控框架概览](p-009_Beyond_the_Black_Box_Interpretability_of/images/fig1_framework_overview.png)
### 机制流程
方法可按以下四步理解：
1.
- ### 核心测试结果
> [!figure] Table 2 主要结果
> 建议位置：关键结果
> 放置原因：该表给出两个模型在留出的 Nemotron 测试集上的核心指标对比，是论文的 headline 结果。
- > 当前状态：已根据 LaTeX 源码 `main.tex` 转写。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
