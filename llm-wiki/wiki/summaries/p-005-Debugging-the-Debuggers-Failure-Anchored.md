# Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents

## Source

- Raw note: `raw/notes/p-005_Debugging_the_Debuggers_Failure-Anchored.md`
- 作者: Chenyu Zhao, Shenglin Zhang, Yihang Lin, Wenwei Gu, Zhimin Chen, Yongqian Sun, Dan Pei, Chetan Bansal, Saravan Rajmohan, Minghua Ma
- DOI: 10.1145/nnnnnnn.nnnnnnn
- arXiv: 2605.08717
- 证据质量: high
- PDF: [p-005]-probe-failure-anchored-structured-recovery-for-software-engi.pdf

## Compiled Summary

软件工程智能体日益被部署在可评估的工程环境中，但失败后的恢复仍然成本高昂、依赖人工且缺乏系统性。现有系统仅暴露执行轨迹或生成后续反馈，并未将异构的运行时证据转化为有依据的、有边界的恢复指导，以供下一次尝试使用。

## Evidence Notes

- 本文提出 PROBE，一种面向软件工程智能体的失败锚定结构化恢复框架。
- 本文围绕软件工程智能体的失败后恢复提出三个核心挑战：
- **挑战一：保留恢复关键证据**。有效的恢复不仅依赖最终错误信息，还需要保留异常签名、重复工具失败、执行顺序、智能体与环境状态及评估器反馈。现有基准大多仅关注任务目标是否达成，未保留支持恢复的细粒度诊断信号。当遥测被压缩为通用摘要或未分类日志时，这些关键证据极易丢失。
- - **挑战二：构建结构化诊断**。运行时信号在来源、格式、粒度和可靠性上差异显著：指标反映进展与资源消耗，日志记录局部失败，轨迹保留时间结构，状态和环境信号提供上下文。有用框架应整合这些信号而不模糊其不同角色，并生成可追溯至证据且可用于恢复指导的结构化诊断。
- PROBE 将软件工程智能体的失败后恢复建模为从失败运行遥测到有边界恢复指导的结构化转换。核心架构包含三个耦合阶段：遥测层、诊断层和引导门。
- 形式化地，失败运行产生类型化遥测集合：
$$\mathcal{T} = \{T_{\text{metrics}}, T_{\text{logs}}, T_{\text{traces}}, T_{\text{intent}}, T_{\text{env}}, T_{\text{outcome}}\}$$
其中每个分量对应一个信号族，$T_{\text{outcome}}$ 在外部评估器信号可用时纳入。PROBE 通过结构化流水线处理遥测：
$$\mathcal{T} \to \mathcal{E} \to \mathcal{D} \to \mathcal{G}$$
其中 T 表示类型化遥测集合，E 表示结构化证据，D 表示诊断对象，G

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/cost-token-and-resource-attribution]]
- Entities: None identified
