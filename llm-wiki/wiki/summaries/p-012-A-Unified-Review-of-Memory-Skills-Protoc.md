# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

## Source

- Raw note: `raw/notes/p-012_A_Unified_Review_of_Memory_Skills_Protoc.md`
- 作者: Chenyu Zhou, Huacan Chai, Wenteng Chen, Zihan Guo, Rong Shan, Yuanyi Song, Tianyi Xu, Yingxuan Yang, Aofan Yu, Weiming Zhang, Congmin Zheng, Jiachen Zhu, Zeyu Zheng, Zhuosheng Zhang, Xingyu Lou, Changwang Zhang, Zhihui Fu, Jun Wang, Weiwen Liu, Jianghao Lin, Weinan Zhang
- 年份: 2026
- 来源: arXiv
- DOI: 10.48550/arXiv.2604.08224

## Compiled Summary

大语言模型智能体的构建方式正日益从修改模型权重，转向围绕模型重新组织运行时环境。早期系统期望模型在内部恢复的能力，如今被外部化为记忆存储、可复用技能、交互协议以及使这些模块在实际中稳定运行的Harness层。本文借助认知人工制品（cognitive artifacts）的视角回顾这一转变，指出智能体基础设施之所以重要，并非仅仅因为它增加了辅助组件，而是因为它将原本困难的认知负担转化为模型能够更可靠处理的形式。在此视角下，记忆外化了跨时间的状态，技能外化了程序性专业知识，协议外化了交互结构，而Harness工程则是将它们协调为受控执行的统一层。本文追溯了从权重到上下文再到Harness的历史演进，分析了记忆、技能和协议作为三种不同但耦

## Evidence Notes

- LLM 智能体面临的根本挑战是什么？传统上，社区将智能体能力的提升等同于模型规模的扩大和训练数据的增加。然而，本文指出，仅凭更大的模型权重无法解决三类反复出现的失配：
- **连续性失配**：上下文窗口有限且会话记忆薄弱，导致长程任务中的状态难以保持。
- - **方差失配**：多步复杂流程每次都需要重新推导，导致执行不稳定、遗漏步骤或提前终止。
- 本文采用**概念综述与系统框架构建**的研究方法，核心方法论特点如下：
- **理论锚定**：以 Norman 的认知人工制品理论和 Kirsh 的互补策略理论为分析基石，将工程设计选择与认知科学中的外部化概念对接。
- - **历史追踪**：通过"Weights → Context → Harness"三层模型，梳理社区研究重心从参数能力到提示工程再到基础设施的迁移轨迹。
- 作为一篇综述，本文的主要"结果"体现为对领域现状的系统刻画和未来方向的清晰预判：
- **记忆架构的四阶段演进**：当前系统已从单调上下文演进至自适应记忆系统，核心转变是从被动存储到主动控制策略。
- - **技能系统的三层演进**：社区经历了从原子执行原语到大规模原语选择，再到封装化技能单元的跃迁，关键转变是将能力视为可加载、可复用的程序性知识包。

## Wiki Connections

- Concepts: [[concepts/runtime-instrumentation-and-otel]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/Claude-Code|Claude Code]], [[entities/Codex-CLI|Codex CLI]]
