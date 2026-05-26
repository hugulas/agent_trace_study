---
tags:
  - New-Relic
  - AI-monitoring
  - APM
  - observability
  - LLM-observability
  - OpenAI
  - Bedrock
  - DeepSeek
  - LangChain
  - vector-database
  - official-doc
aliases:
  - s2-013
  - New Relic AI Monitoring
  - New Relic AI 监控
  - New Relic LLM 可观测性
date: 2026-05-22
url: https://docs.newrelic.com/docs/ai-monitoring/intro-to-ai-monitoring/
---

# Introduction to AI monitoring | New Relic Documentation

## 核心信息

- **标题**: Introduction to AI monitoring | New Relic Documentation
- **作者**: New Relic 官方文档团队
- **来源类型**: 官方产品文档（技术参考类）
- **发布时间**: 2026 年（文档版权标注 © 2026 New Relic Inc）
- **阅读时长**: 约 5–8 分钟
- **核心主题**: New Relic AI Monitoring 的功能概述、工作原理与入门路径
- **本地材料**: `[s2-013]-introduction-to-ai-monitoring--new-relic-docs.pdf`
- **证据质量**: high

## 内容摘要

本文是 New Relic 官方文档中关于 AI Monitoring 产品的入门指南，
系统介绍了该产品的定位、核心能力、工作机制和部署路径。
作为传统 APM（Application Performance Monitoring）领域的头部厂商，
New Relic 将 AI Monitoring 定义为 "面向 AI 的 APM 解决方案"，
这标志着可观测性行业正在从通用应用监控向 AI 原生监控快速演进。

AI Monitoring 的核心价值主张是提供端到端的可见性，
覆盖 AI 驱动应用的性能、成本和输出质量三大维度。
当用户启用该功能后，
New Relic 的 APM Agent 能够自动捕获来自外部 LLM 和向量存储的指标与事件数据，
并支持 OpenAI、Amazon Bedrock 和 DeepSeek 等主流模型厂商。
团队可以通过统一平台探索用户与 AI 助手的交互模式，
深入追踪模型对特定 AI 事件的响应细节，
以及在不同应用环境之间横向比较多个模型的表现差异。
所有数据均可通过 one.newrelic.com 的 AI Monitoring > AI Responses 入口访问。

在具体工作机制上，
New Relic 延续了其传统 APM 的埋点范式：
用户首先需要使用 APM Agent 对 AI 驱动的应用进行 instrument（埋点），
随后启用 AI Monitoring 功能，
Agent 即可在 AI 助手接收 prompt 并返回 response 的过程中，
自动捕获由外部 LLM 和向量存储生成的指标与事件数据。
根据文档描述，Agent 具备三项核心能力：
一是解析 completion、prompt 和 response 的 token 信息，
实现精确的 token 级成本归因；
二是追踪流经任意支持模型的请求与响应，
覆盖多模型切换和模型版本迭代的场景；
三是关联终端用户对特定响应的正面或负面反馈，
将用户满意度信号纳入可观测数据体系。
这些能力共同构成了从底层基础设施到上层用户体验的完整观测链路。

在性能优化方面，
文档明确指出 AI Monitoring 能够帮助团队回答一系列关键运营问题：
终端用户是否在等待过长的响应时间？
近期是否出现了 token 使用量的异常激增？
某些主题周围是否存在负面用户反馈的聚集模式？
通过 AI Responses 页面，
团队可以从响应表中识别特定 prompt-response 交互中的错误，
并通过 trace-level 数据深入分析模型的具体行为。
如果团队在多个应用环境中使用了不同的模型，
还可以在部署前横向比较各模型的成本与性能表现，
为模型选型提供数据支撑。

数据合规与隐私保护也是文档强调的重点。
New Relic 提供了 drop filters 功能，
允许团队在将敏感数据发送至 New Relic 平台之前对其进行过滤或脱敏处理。
这一功能对于处理包含 PII（个人身份信息）、
财务数据或受监管内容的 AI 应用尤为重要，
体现了企业级可观测性平台在合规层面的必要考量。

在生态集成方面，
根据 reading log 中的补充信息，
New Relic AI Monitoring 支持超过 50 种集成，
涵盖了 LangChain 等主流编排框架、
Pinecone / Weaviate / Milvus 等向量数据库，
以及 PyTorch / TensorFlow 等机器学习库。
这种广泛的生态覆盖意味着团队无需大幅改造现有技术栈
即可接入 New Relic 的可观测性体系，
降低了采用门槛和迁移成本。

部署路径方面，
文档建议用户首先确认其 AI 库或框架是否在支持列表中，
如果应用已经完成了 APM 埋点，
可能只需要升级 Agent 版本并开启 AI Monitoring 配置即可。
对于新用户，
文档提供了从安装 APM Agent 到配置 AI Monitoring 的完整步骤指引，
覆盖了主流编程语言和部署环境的差异化要求。

## 关键要点

- **产品定位清晰**:
  AI Monitoring 不是独立的新产品，
  而是 New Relic 现有 APM 体系的自然延伸，
  将传统应用监控的能力模型扩展至 AI 层，
  体现了 "APM for AI" 的演进逻辑。
- **三大观测维度**:
  性能（延迟、吞吐量、错误率）、
  成本（token 消耗、按模型/环境归因）、
  质量（用户反馈、响应准确性）
  三位一体的观测体系，
  覆盖了 AI 应用运营的核心关切。
- **自动化埋点机制**:
  基于成熟的 APM Agent 架构，
  自动捕获 LLM 调用和向量存储交互的指标与事件数据，
  无需手动修改大量业务代码即可实现可观测性覆盖。
- **Token 级精细化**:
  Agent 能够解析 completion、prompt 和 response 的 token 分布，
  支持按模型、按环境、按请求的精细化成本归因，
  这是通用 APM 难以提供的 AI 专属能力。
- **用户反馈关联**:
  将终端用户的正面/负面反馈与具体请求-响应对关联，
  使得用户满意度不再是孤立的数据点，
  而是可追踪、可分析的连续信号。
- **Trace-level 诊断**:
  支持深入到单次模型调用的 trace 层级，
  帮助团队从宏观仪表盘定位到微观异常根因，
  实现从症状到病因的穿透式分析。
- **跨环境模型比较**:
  允许在 staging、production 等不同环境之间
  横向对比不同模型的成本与性能，
  为模型选型和版本升级提供数据驱动的决策依据。
- **数据合规保障**:
  内置 drop filters 功能，
  可在数据上传前过滤敏感信息，
  满足企业级数据隐私和合规要求。
- **生态集成广泛**:
  50+ 集成覆盖 LangChain、Pinecone、Weaviate、Milvus、PyTorch、TensorFlow 等主流组件，
  与现有 AI 技术栈的兼容性强，
  降低了采用摩擦。
- **部署路径成熟**:
  对于已使用 New Relic APM 的团队，
  升级 Agent 并开启配置即可；
  新用户亦有完整的安装指引，
  覆盖了多语言和多环境场景。

## 与综述的关联

本材料与综述中 "云厂商与传统 APM 厂商的 AI 可观测性布局" 主题直接相关。
New Relic 作为传统 APM 领域的代表厂商，
其 AI Monitoring 产品的推出具有强烈的行业信号意义：
它表明 AI 可观测性不再是初创公司的专属赛道，
而是正在被成熟企业软件厂商快速吸收和整合。
综述在讨论可观测性市场格局时，
可将 New Relic 与 Datadog（s2-007）、Splunk（s2-009）、Elastic（s2-010、s2-011）
并置分析，
论证传统 APM/可观测性厂商如何通过产品扩展策略进入 AI 领域。

从功能设计角度，
New Relic AI Monitoring 的 "APM Agent + AI 扩展" 架构
与 s1-010（AWS CloudWatch GenAI Observability）和 s1-006（Amazon CloudWatch）
形成了有趣的对照。
AWS 选择了 purpose-built 的新服务路径，
从零开始为 GenAI 设计仪表盘和数据模型；
而 New Relic 选择了在现有 APM 体系上叠加 AI 感知层，
利用已有的 Agent 基础设施和查询平台扩展能力。
综述可将这两种策略并置讨论：
前者优势在于设计自由度和 AI 原生语义，
后者优势在于存量客户的平滑升级和生态惯性。
这一对比可作为综述中 "AI 可观测性架构演进路径" 章节的核心素材。

文档中强调的 token 级成本归因和用户反馈关联，
与综述中 "LLM 应用运营成本管理" 和 "用户满意度可观测性" 的论述高度契合。
特别是 "将负面用户反馈与特定响应关联" 的能力，
在学术文献中较少被讨论，
但在工业实践中是闭环优化的关键——
它让运营团队不仅能够知道 "模型表现不好"，
还能精确定位 "在哪个场景下、对哪类输入、产生什么样的错误输出"。
综述可借此引入 "用户反馈作为可观测性信号源" 的概念，
补充学术视角中对 "human-in-the-loop" 讨论的操作化细节。

drop filters 的设计也值得综述关注。
在企业级部署中，
AI 应用经常需要处理包含敏感信息的用户输入
（如医疗记录、财务数据、个人身份信息），
如何在保证可观测性的同时不违反数据隐私法规，
是学术文献中讨论较少的 "工程现实"。
New Relic 的方案是在 Agent 层实现数据过滤，
属于 "源头治理" 策略；
综述可将其与 "事后脱敏"、"差分隐私"、"联邦可观测性" 等替代方案进行比较，
形成对 AI 可观测性合规维度的系统论述。

在生态集成方面，
New Relic 对 LangChain 和主流向量数据库的原生支持，
与 s2-014（Langfuse）、s2-016（Phoenix）等开源工具形成了互补与竞争关系。
开源工具通常以框架深度集成和灵活定制见长，
而 New Relic 以企业级稳定性、合规能力和托管服务见长。
综述在组织 "开源 vs 商业" 对比时，
可引用本文档作为商业方案的权威参考，
同时注意区分 "功能覆盖" 和 "落地成本" 两个维度的差异。

## 我的笔记

作为官方产品文档，
本文的信息密度和可信度较高，
但深度上自然受限于入门指南的定位——
它告诉你 "有什么" 和 "怎么用"，
但不会深入讨论 "为什么这样设计" 或 "与其他方案相比优劣如何"。
综述在引用本文时，
应将其作为 New Relic 产品能力的权威事实来源，
而非技术分析或竞品对比的依据。

New Relic 选择 "APM 扩展" 而非 "独立新产品" 的策略值得深思。
这一决策背后是对存量客户基础和迁移成本的精明考量：
对于已经深度使用 New Relic 的企业客户，
AI Monitoring 几乎是无缝升级；
Agent 基础设施、查询语言、告警体系、团队培训均可复用。
但这种路径也可能带来架构债务——
传统 APM 的数据模型是为请求-响应型微服务设计的，
AI 系统的异步推理流、多轮对话状态、工具调用链等特征
可能需要对底层数据模型进行较大幅度的扩展。
文档未透露这些底层实现细节，
但从产品描述中 "捕获 metric 和 event 数据" 的措辞来看，
New Relic 似乎仍在沿用其传统的 Metrics + Events + Logs + Traces（MELT）框架，
只是在 Events 和 Traces 中增加了 AI 特有的属性字段。

Token 级成本归因是本文档中最具 AI 原生特征的能力。
在传统 APM 中，
成本通常以基础设施资源（CPU、内存、网络）来衡量；
而在 LLM 应用中，
成本的核心驱动因素是 token 消耗量，
且输入 token 和输出 token 往往采用不同的定价策略。
New Relic Agent 能够区分 prompt token、completion token 和 response token，
这意味着团队可以精确追踪 "哪些用户查询最烧钱"、
"哪些模型在输出端更经济"、
"哪些功能模块的上下文窗口过大导致成本浪费"。
这种精细化成本管理能力，
在开源可观测性工具中往往需要大量自定义埋点才能实现，
而 New Relic 通过 Agent 自动化降低了实施门槛。

用户反馈关联功能是另一个值得记录的设计亮点。
文档中仅提到 "correlate negative or positive feedback about a response"，
未展开说明具体实现机制，
但可以合理推断有两种可能路径：
一是通过前端 SDK 在用户界面中嵌入反馈按钮，
将 thumbs-up/thumbs-down 信号与 trace ID 关联；
二是通过后端 API 接收来自客服系统或用户调研的反馈数据，
再与可观测数据进行 join。
无论采用哪种机制，
这一功能的本质是将 "定性用户体验" 转化为 "定量可观测信号"，
使得团队可以在仪表盘上直接看到 "某类查询的用户满意度趋势"，
而非依赖周期性的用户调研或偶发的投诉工单。

drop filters 的存在反映了企业级 AI 部署中的一个真实痛点：
可观测性数据与业务数据之间的边界模糊。
当 AI 应用处理用户输入时，
prompt 中可能包含敏感信息，
而这些 prompt 同时又是诊断模型行为的关键线索。
完全不上传会丢失可观测性，
完全上传会违反合规要求，
因此需要在 Agent 层实现智能过滤。
文档未详细说明 drop filters 的配置语法和匹配规则，
但从命名来看，
它可能支持基于正则表达式、关键字列表或字段路径的过滤策略。
综述在讨论 AI 可观测性的隐私与合规维度时，
可将此作为 "数据最小化原则" 的工程实践案例。

关于生态集成的 50+ 声明，
虽然 reading log 中列出了 LangChain、Pinecone、Weaviate、Milvus、PyTorch、TensorFlow 等组件，
但官方文档正文对具体集成列表的覆盖较为简略。
综述在引用这一数字时应保持审慎，
因为 "50+ 集成" 可能包含大量通用库（如 HTTP 客户端、数据库驱动），
而非全部是针对 AI 场景的深度集成。
真正有价值的判断标准是：
对于某个特定的 AI 组件，
Agent 是否能够自动识别其内部调用语义
（如区分 LangChain 的 chain 步骤、向量数据库的检索操作），
而不仅仅是记录一次外部 HTTP 调用。
前者是 "AI-aware" 集成，
后者只是 "通用网络" 集成，
两者在诊断价值上存在显著差异。

最后，文档中 "compare the performance of different models across app environments" 的描述，
暗示了 New Relic 支持多模型 A/B 测试和灰度发布的观测需求。
这对于正在从单一模型向多模型策略演进的团队尤为重要——
当 staging 环境运行 Claude 3.5、production 环境运行 GPT-4 时，
团队需要一套统一的可观测性语言来比较两者的延迟、成本和输出质量差异。
New Relic 的跨环境比较能力，
恰好为这种 "模型即服务"（Model-as-a-Service）的选型决策提供了数据基础设施。
综述在讨论 "模型治理" 和 "模型选型" 时，
可引用此能力作为工业实践的支撑证据。
