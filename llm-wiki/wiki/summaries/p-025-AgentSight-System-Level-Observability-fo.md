# AgentSight: System-Level Observability for AI Agents Using eBPF

## Source

- Raw note: `raw/notes/p-025_AgentSight_System-Level_Observability_fo.md`
- Metadata: not available in note

## Compiled Summary

现代软件基础设施日益依赖大语言模型智能体进行开发与维护，例如 Claude Code 与 Gemini-cli。

## Evidence Notes

- 然而，这类 AI 智能体与传统确定性软件存在根本差异，给常规监控与调试带来了重大挑战。
- AI 智能体将大语言模型的推理能力与直接操作系统工具的能力耦合，使其能够生成动态代码、派生任意子进程并执行命令。这种非确定性执行路径与传统软件的可预测逻辑截然不同，导致现有可观测性工具面临根本性盲区。
- 具体而言，当前方案被困在语义鸿沟的某一侧：
- **应用层插桩**（如 LangChain、AutoGen）只能捕获智能体的高层级意图和工具选择，却无法看到 shell 子进程中的系统动作；它们依赖协作式信任模型，一条 shell 命令即可逃逸监控。
- AgentSight 的设计围绕一个核心目标：弥合智能体意图与动作之间的语义鸿沟。其方法论基础是边界追踪，通过多信号关联引擎实现。
- ### 核心挑战
**挑战一：跨越意图与动作之间的语义鸿沟**
智能体的意图以自然语言表达，经大语言模型解释后动态生成运行时源码。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/observability-products-and-market-map]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/AgentOps|AgentOps]], [[entities/Claude-Code|Claude Code]]
