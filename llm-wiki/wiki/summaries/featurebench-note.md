# FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

## Source

- Raw note: `raw/notes/featurebench_note.md`
- Metadata: not available in note

## Compiled Summary

由大语言模型驱动的智能体正越来越多地被软件行业所采用，以协作者甚至自主开发者的身份贡献代码。随着它们的普及，评估当前编码能力边界的重要性日益凸显。然而，现有的智能体编码基准测试覆盖的任务范围有限，例如仅限于单个拉取请求内的错误修复，并且往往依赖不可执行的评估方式，或缺乏持续更新评估覆盖范围的自动化方法。为解决这些问题，我们提出了 FeatureBench，一个旨在评估端到端、面向功能的软件开发中智能体编码性能的基准测试。FeatureBench 采用基于执行的评估协议和可扩展的测试驱动方法，能够以最少的人工工作量自动从代码仓库中派生任务。通过从单元测试出发沿依赖图进行追踪，我们的方法可以识别出横跨开发时间线上分散的多个提交和拉取请求

## Evidence Notes

- 随着大语言模型在软件开发中的应用日益深入，智能体编码系统正从辅助补全走向自主完成复杂任务。Claude Code、Qwen Code 等工具的出现标志着需求驱动型智能体能够自主规划、执行并与编译器等外部工具交互，将人类角色推向监督层面。然而，现有评估这一范式转变的基准存在明显局限：
- **任务范围狭窄**：SWE-bench 等主流基准主要关注单个拉取请求内的错误修复，缺乏对功能开发场景的覆盖。
- - **评估方式受限**：部分基准依赖非可执行的评估，难以准确判定实现是否满足功能要求。
- FeatureBench 的核心是一套从开源仓库自动生成功能级评估实例的管道。该管道围绕单元测试和依赖图展开，确保生成的任务既反映真实开发场景，又具备可执行验证能力。
- ### 机制流程
**步骤1：环境初始化与测试选取**
- **输入**：一个 GitHub 代码仓库及其单元测试套件。
- 论文评估了7种框架与模型的组合配置。模型侧覆盖 DeepSeek-V3.2、Claude Opus 4.5 等闭源与开源前沿模型；框架侧包括 OpenHands、Claude Code 等代表性智能体脚手架。
- **主要实验结果**
- **Claude Code (routing) + Claude Opus 4.5**：在 Lite 子集上取得最高解决率 20.0%，但在完整测试集上仅为 11.0%。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Claude Code](entities/Claude-Code.md), [Codex CLI](entities/Codex-CLI.md)
