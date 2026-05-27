# Willful Disobedience: Automatically Detecting Failures in Agentic Traces

## Source

- Raw note: `raw/notes/AgentPex_Willful_Disobedience.md`
- 作者: Reshabh K Sharma, Shraddha Barke, Benjamin Zorn
- 年份: 2026
- DOI: 10.1145/3786335.3813153
- arXiv: 2603.23806
- 证据质量: medium（bundle 中 method/mechanism 部分提取不完整）
- PDF: [a-004]-agentpex-auditing-agent-trajectories-via-specification-guide.pdf

## Compiled Summary

人工智能智能体日益嵌入真实软件系统，通过多轮对话、工具调用和中间决策执行多步骤工作流。这些漫长的执行历史（称为智能体轨迹）使验证变得困难。仅基于结果的基准测试可能遗漏关键的过程性失败，例如错误的工作流路由、不安全的工具使用或违反提示指定规则的情况。本文提出 AgentPex，一种用于系统性评估智能体轨迹的人工智能驱动工具。AgentPex 从智能体提示和系统指令中提取行为规则，然后利用这些规范自动评估轨迹的合规性。作者在四百二十四条来自 tau-squared-bench 的轨迹上评估 AgentPex，涵盖电信、零售和航空客服领域的多个模型。结果表明，AgentPex 能够区分不同模型的行为，并发现仅基于结果的评分无法捕获的规范违

## Evidence Notes

- 论文明确提出了四个核心研究问题，对应智能体评估中的关键空白：
1.
- **RQ1**: 基于大语言模型的评估能否补充人工编写的真值标准？
2.
- AgentPex 的流水线分为三个主要阶段。
- ### 第一阶段：轨迹归一化
将来自异构来源的轨迹导入并归一化为格式无关的表示，包含：
- 系统提示
- 工具模式
- 顺序消息日志（用户、助手、工具消息）
- 可选的任务元数据
### 第二阶段：规范提取
从系统提示和工具模式中自动提取行为规范。提取的规范类型包括：
- **输出规范**：要求引用来源、不透露内部推理、返回符合指定 JSON 模式的输出
- **参数规范**：工具调用的参数约束
- **计划遵从**：预期执行步骤
- **最终状态预测**：预期最终数据库状态
### 第三阶段：合规评估
运行一组大语言模型作为裁判的评估器，每条规范维度上给出零到一百的合规分数。聚合公式为：
$$\text{final} = \min
- ### RQ1：大语言模型评估与真值标准的关系
- 输出规范评估器对 tau-squared 失败轨迹给出系统性的更低分数（均值五十六点九 vs 通过轨迹的八十四点一）
- 作为 tau-squared 失败的二元分类器，输出规范评估器达到 **ROC-AUC 零点六八零**
- 阈值低于六十五时，能标记 **百分之四十八的 tau-squared 失败轨迹**
### RQ2：仅结果评估遗漏的违反
- **百分之八十三的 Claude 三点五 Sonnet 轨迹** 即使在 tau-squared reward 等于一（完美结果）的情况下仍包含至少一个程序性违反
- 这表明仅结果评估严重低估了实际失败率
### RQ3：跨模型泛化

## Wiki Connections

- Concepts: [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: None identified
