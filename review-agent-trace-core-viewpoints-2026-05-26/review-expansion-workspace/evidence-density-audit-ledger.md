# 证据密度审查账本

> 目的：按“是否有具体学术机制、是否有互联网/云厂商或产品实例、是否只是点名未展开、是否需要修改”审查各章节。审查对象以 `chapters/*.md` 为源，修改后再重建 `rebuilt.md` 与根目录 `report.md`。

| 范围 | 审查结论 | 是否修改 | 处理说明 |
| --- | --- | --- | --- |
| 2.1 智能体轨迹 | 原文只有 Datadog/Langfuse/Arize/AgentOps 工具列表，缺少互联网/云厂商如何落地 trace 的具体场景。 | 已修改 | 增加 Google ADK/Cloud Trace、AWS CloudWatch/AgentCore Runtime、阿里云 AgentLoop、百炼、百度千帆 AppBuilder Trace、Coze Loop，并补 R032-R038。 |
| 2.2 失败归因 | 原文只说明 replay/drill-down，缺少生产事故排查式归因示例。 | 已修改 | 增加 Google/AWS 云链路排查与阿里云/百炼/千帆/Coze 应用平台 bad case 回流例子，并明确“产业平台提供归因入口，学术方法提供根因验证”。 |
| 2.3 过程合规性 | 原文点名 AgentPex、Monitoring Monitorability、HarnessAudit，但未展开差异。 | 已修改 | 增加三篇论文的方法差异解释和对比表。 |
| 2.4 Harness | 原文有 AHE、Lifting Traces to Logic 和平台闭环，但没有拆开两篇论文的机制差异，也没有说明厂商产品中 harness 如何分布在 runtime、prompt、插件、知识库、eval 和发布流程中。 | 已修改 | 增加 AHE/Lifting 方法差异表；补 AWS AgentCore/Runtime、Google ADK/Vertex、百炼、百度千帆、Coze Loop 中 harness 的产品化对象。 |
| 2.5 审计轨迹、成本归因与 Token 经济学 | 原文证据覆盖面够，但审计、成本归因和 token 经济学三者边界混在一起，产业落地也偏概括。 | 已修改 | 增加审计轨迹/成本归因/token 经济学三方向对比表；补 AWS/GenAIOps、Helicone/AgentOps、百炼/千帆/Coze 的落地差异。 |
| 3 五层架构 | 各层均有学术机制、产业平台和图表；3.1/3.3 的互联网厂商细节在 2.1/2.2 已补，3.5 已有 AWS 成本图。 | 不修改 | 第 3 章定位为架构总览，过多厂商例子会和第 2、5、8 章重复。 |
| 4 七个核心观点 | 每个观点已有学术论文、产业平台和图表支撑。 | 不修改 | 作为观点压缩章，维持“判断-机制-证据-工程含义”的密度。 |
| 5 关键对比 | 已有多张对比表，覆盖诊断/合规/日志、学术/产品、OTel/schema、单/多智能体、运行时/离线、token 架构路线。 | 不修改 | 对比章已满足“不同做法、不同架构”的要求。 |
| 6 方法谱系 | 已按 capture-diagnosis-governance-platform-cost 管线展开，产业例子集中在平台和 token 控制路线。 | 不修改 | 方法谱系章节不宜再堆具体厂商案例。 |
| 7.1 跨格式语义映射 | 已有 AgentTrace、Hermes、AAT、OpenInference、Datadog、Phoenix、AWS。 | 不修改 | 缺口聚焦 schema mapping，证据充分。 |
| 7.2 失败分类法碎片化 | 原文有论文和 Datadog/AgentOps，但缺少互联网/云厂商分类体系与学术 taxonomy 不可 join 的说明。 | 已修改 | 增加 Google/AWS 云链路分类与阿里云/百炼/千帆/Coze 应用平台分类的差异，说明产品侧分类难映射到学术失败机制。 |
| 7.3 长轨迹与多智能体因果推断 | 原文有 DoVer/Who&When 与 replay，但未说明厂商平台为何仍只能给“入口”而非“因果边”。 | 已修改 | 增加 Google/AWS 外部依赖排查、百炼/千帆/Coze bad case 回流例子，并指出缺少反事实验证和责任模型。 |
| 7.4-7.8 其他研究缺口 | 已分别覆盖规范质量、隐私/诊断、成本/质量、预算策略、自动修复，且引用和图表明确。 | 不修改 | 证据目标是指出缺口，不要求每节都列厂商全集。 |
| 8.1 trace schema 契约 | 已有 AgentTrace/Hermes/OpenInference/Datadog/Phoenix/AWS。 | 不修改 | 设计建议已足够具体。 |
| 8.2 OTel + agent-specific 语义 | 原文只有概念和学术/AgentSight，缺少厂商架构实例。 | 已修改 | 增加 Google Cloud Trace、AWS CloudWatch/AgentCore、阿里云/百炼/千帆/Coze，明确“传播骨架 + 任务语义 + 应用迭代对象”。 |
| 8.3 长轨迹/多智能体依赖边 | 原文只给字段建议，缺少平台字段落地场景。 | 已修改 | 增加云 trace 字段与 agent id/role/handoff/message edge/shared memory/tool owner 等字段差异，说明为什么线性 timeline 不够。 |
| 8.4 结果、规范、安全和审计证据关联 | 原文有审计材料，但缺少厂商治理对象差异。 | 已修改 | 增加 AWS/IAM/runtime 与阿里云/百炼/千帆/Coze 应用/插件/知识库/版本治理差异。 |
| 8.5-8.7 其他设计建议 | 已覆盖 harness 数据飞轮、token 预算、平台选型，且产业例子充分。 | 不修改 | 保持现状。 |
| 9 结论 | 已有总分总收束和参考文献索引。 | 不修改 | 结论不再堆例子，只收束主要判断。 |
