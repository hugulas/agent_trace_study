# AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories

## Source

- Raw note: `raw/notes/p-029_AgentDiagnose_An_Open_Toolkit_for_Diagno.md`
- 作者: Tianyue Ou, Wanyao Guo, Apurva Gandhi, Graham Neubig, Xiang Yue
- DOI: 10.18653/v1/2025.emnlp-demos.15

## Compiled Summary

大语言模型智能体产生的轨迹丰富且多步，交错着外部观察、内部推理与工具动作。

## Evidence Notes

- 然而，现有评估流程大多只关注任务最终是否成功，使得智能体的决策过程不透明且难以被理解。
- 当前 LLM 智能体评估范式存在两个核心盲区：
- **结果导向的评估盲区**：大多数流水线仅以任务是否成功作为评价标准，无法解释智能体在数百乃至数千步的交互中，究竟哪些决策推动了成功、哪些失误导致了失败。
- - **诊断工具的语义缺口**：现有的轨迹检查工具（如 AgentXRay、AgentOps）主要提供逐步回放与日志记录，呈现“智能体做了什么”，但缺乏对“智能体决策质量如何”的量化诊断；而需要参考轨迹的评估框架（如 AgentEval）在开放域或无标准答案场景下难以部署。
- AgentDiagnose 由两大模块构成：评估模块（Evaluation Module）与可视化模块（Visualization Module）。前者负责将轨迹的隐性能力转化为可比较的数值，后者负责将数值与文本模式转化为可交互的视觉呈现。
- > [!figure] Fig.

## Wiki Connections

- Concepts: [[concepts/trace-schema-and-telemetry-standards]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/observability-products-and-market-map]]
- Entities: [[entities/AgentOps|AgentOps]]
