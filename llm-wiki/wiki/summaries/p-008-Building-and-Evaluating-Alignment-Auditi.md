# Building and evaluating alignment auditing agents

## Source

- Raw note: `raw/notes/p-008_Building_and_Evaluating_Alignment_Auditi.md`
- 作者: Trenton Bricken, Rowan Wang, Sam Bowman, Euan Ong, Johannes Treutlein, Jeff Wu, Evan Hubinger, Samuel Marks
- 来源: Anthropic Alignment Science Blog
- DOI: 无
- arXiv: 无
- 证据质量: medium
- PDF: [p-008]-building-and-evaluating-alignment-auditing-agents.pdf

## Compiled Summary

本文开发了三个能够自主执行对齐审计任务的智能体。在针对被植入故意对齐缺陷的模型进行测试时，这些智能体成功揭露了大语言模型的隐藏目标、构建了行为评估方案，并发现了令人担忧的模型行为。研究团队已将这类智能体用于辅助 Claude 4 等前沿模型的对齐审计工作。该工作旨在解决对齐审计面临的两大核心挑战：可扩展性（人工审计耗时巨大）与验证性（无法确定审计是否覆盖了所有问题）。通过将审计游戏形式化为评估环境，研究者能够利用具有已知 ground truth 的合成任务来衡量智能体的审计能力，从而对不同审计工具和方法进行细粒度分析。

## Evidence Notes

- 对齐审计是确保大语言模型安全部署的核心环节，但在实践中面临两大根本性困难：
**可扩展性**：随着模型数量增加和每次审计范围扩大，纯粹依赖人工研究者的审计模式将难以跟上 AI 发展的速度。传统对齐审计需要投入大量专家时间，且不同审计者之间的技能差异显著。
- **验证性**：即使完成了一次审计，也无法确信是否遗漏了模型的实质性对齐问题。Marks 等人曾提出审计游戏作为验证协议，但人工审计者无法在不暴露答案的情况下重复同一审计游戏，且招募足够数量的专家以获得统计显著结果几乎不可能。
- ### 机制流程
论文核心方法是构建工具增强型审计智能体，并在标准化审计游戏中评估其性能。整体执行流程可概括为以下四步：
1.
- **输入目标模型与工具集**：将具有已知植入缺陷的目标模型提供给审计智能体，同时配置一组可用的审计工具（对话工具、数据分析工具、可解释性工具）。
- ### 单智能体审计结果
在最具现实性的配置下（所有可用工具和数据集），调查智能体在审计游戏中的表现如下：
- **开放式设置**：成功率为13%
- **元韵文提示设置**：成功率为17%
在仅使用对话工具时，胜率接近0%。增加数据分析工具后，性能仍有限。关键发现是可解释性工具能显著提升成功率：
- 在 PT+SFT+RL 的 realistic 设置中，可解释性工具将胜率提升了10-20个百分点
- 在仅 PT 数据设置中，整体性能更好，这表明可解释性工具的部分价值在于将审计者注意力引向包含关键证据的 PT 数据
- 当智能体已拥有仅针对 PT 的语义检索工具时，再添加可解释性工具的额外收益较小
提供元韵文示例行为对拥有可解释性
- 在行为发现方面，智能体很少能在未先发现根因的情况下发现超过10种行为。配备语义检索工具的智能体在行为发现上表现尤为出色。最佳运行记录为：使用对话+grep+语义检索工具发现了全部52种行为（尽管该运行未被评分器判定为正确识别根因）。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Claude Code](entities/Claude-Code.md)
