---
tags:
  - GenAIOps
  - AWS
  - CloudWatch
  - OpenTelemetry
  - X-Ray
  - observability
  - RAG
  - ADOT
  - Bedrock
  - distributed-tracing
aliases:
  - s1-010
  - AWS GenAI 端到端可观测性栈
  - GenAIOps on AWS Part 3
date: 2025-03-31
url: https://dev.to/aws-builders/genaiops-on-aws-end-to-end-observability-stack-part-3
---

# GenAIOps on AWS: 端到端可观测性栈

## 核心信息

- **标题**: GenAIOps on AWS: End-to-End Observability Stack - Part 3
- **作者**: Shoaibali Mir
- **来源类型**: DEV Community 技术博客（系列第 3 部分，共 4 部分）
- **发布时间**: 2025 年 3 月 31 日
- **阅读时长**: 约 22–25 分钟
- **难度级别**: 中级到高级
- **核心主题**: 使用 CloudWatch GenAI Observability、X-Ray 分布式追踪和自定义指标
  构建 GenAI 系统的综合可观测性
- **本地材料**: `[s1-010]-genaiops-on-aws-end-to-end-observability-stack---part-3.pdf`
- **图片资产**: 保存在 `cited-materials/images/[s1-010]/` 目录下，
  共 20+ 张截图与架构图，
  涵盖 CloudWatch 仪表盘、X-Ray 服务地图、ADOT 架构图、RAG 埋点流程图等
- **证据质量**: high

## 内容摘要

本文是 "GenAIOps on AWS" 四部曲中的第三篇，
聚焦 GenAI 系统的端到端可观测性建设。
作者 Shoaibali Mir 以极具画面感的
"凌晨 3 点 PagerDuty 告警" 场景切入，
深刻揭示了传统微服务可观测性工具
在面对 GenAI 系统时的无力感：
所有接口都返回 200 OK，用户却在抱怨；
日志中充斥着 10000 行 JSON，
却无法判断检索是否缓慢、大模型是否产生幻觉、
成本为何飙升 5 倍、究竟调用了哪个模型、
以及检索回了什么上下文。
传统可观测性只捕获成功与失败，
而 GenAI 可观测性需要在每一步捕获质量、成本与性能。

文章首先剖析了 GenAI 系统与传统微服务的本质差异。
传统微服务请求通常是确定性的、可预测的，
输入与输出之间存在明确的一对一映射关系；
而 GenAI 系统请求即使返回 HTTP 200，
仍可能因检索到错误文档、大模型幻觉、成本激增或延迟过高
而实质上 "失败用户"。
这意味着可观测性体系必须从二元的状态码观测，
升级为对检索质量、token 消耗、模型行为、端到端 trace 的
全链路细粒度观测。
作者用一张对比表清晰展示了这一差异：
传统微服务观测 "是否到达"，
GenAI 观测 "是否正确、是否经济、是否快速"。

随后，文章详细介绍了 AWS CloudWatch GenAI Observability。
该服务于 2024 年第四季度开启预览，
2025 年 10 月正式商用（GA），
是专为 LLM 应用构建的可观测性解决方案。
其开箱即用的能力包括三大仪表盘。

Model Invocation Dashboard 自动追踪调用次数、成功率、限流次数、
输入/输出 token、按模型和请求的成本归因、
首 token 时间（Time-to-First-Token）与生成延迟、
以及模型错误/限流/超时的分类统计。

AgentCore Agent Dashboard 面向 Amazon Bedrock AgentCore 代理，
提供会话追踪（持续时间、轮次、完成状态）、
工具调用详情（调用频率、成功率）、
内存操作（读写次数、检索性能）、
网关指标（API 延迟、认证失败）
以及推理轨迹（逐步决策日志）。

OpenTelemetry Integration 则提供分布式追踪、自定义 span、
AWS SDK 自动埋点，
并与 AWS X-Ray 深度集成实现服务地图和瓶颈检测。

在架构层面，文章展示了完整的可观测性栈。
AWS Distro for OpenTelemetry（ADOT）
作为 OpenTelemetry 的 AWS 官方发行版，
预配置了对 AWS 服务
（Bedrock、OpenSearch、Lambda、API Gateway 等）的支持，
大幅降低了埋点门槛。
作者提供了从安装 ADOT Collector、基础配置到自动埋点的完整步骤，
涵盖了基于 EC2、ECS、EKS 以及 Lambda 等
多种部署环境的差异化配置方案。

文章的核心亮点是一个经过充分埋点的 RAG 应用示例代码
（`instrumented_rag_system.py`）。
该示例将 RAG 流水线拆解为六个可观测步骤，
每一步均用 OpenTelemetry 的 `start_as_current_span` 包裹，
并附加丰富的属性（attributes）与自定义指标。

第一步生成 embedding：
调用 Bedrock Titan 模型生成向量，
记录 embedding 维度（如 1024 维）、
embedding 成本（按每 1K token 定价估算）。

第二步向量搜索：
在 OpenSearch Serverless 中执行相似度检索，
记录检索文档数（documents_retrieved）、
平均相似度分数（avg_similarity_score），
并向 CloudWatch 发布 `RetrievalQuality` 自定义指标。

第三步重排序（可选但推荐）：
对检索结果进行重排序，
记录重排序后文档数与最高重排序分数。

第四步构建 prompt 与 token 计数：
将检索结果组装为 prompt，估算输入 token，
记录上下文文档数、prompt 字符长度，
并显式检查输入 token 是否超过模型上下文窗口
（如 Claude Sonnet 4 的 200K 限制），
若超限则提前标记而非等到运行时失败。

第五步生成响应：
调用 Claude 模型生成答案，
提取输入/输出 token、计算生成成本
（按模型输入/输出单价分别计算）、
记录停止原因（stop_reason），
并向 CloudWatch 发布 InputTokens、OutputTokens、GenerationCost 等指标。

第六步提取答案：
完成最终输出，
并将总成本、总 token、答案长度等汇总信息附加到根 span。

这套方案的核心价值在于
将 GenAI 系统的 "黑盒" 拆解为
可度量、可追踪、可告警的细粒度组件。
无论是运营团队需要监控成本与延迟，
还是算法团队需要评估检索质量与模型行为，
都能在同一套可观测数据中各取所需。
文章还补充了告警配置的最佳实践：
针对 TTFT 超过阈值、成本突增、检索质量下降、错误率上升等场景
设置 CloudWatch Alarms，
并通过 SNS 通知到 Slack 或 PagerDuty。

## 关键要点

- **核心矛盾**: GenAI 系统可以全员返回 200 OK 但仍彻底失败用户——
  传统可观测性无法捕捉检索错误、幻觉、成本飙升、延迟弃用等
  GenAI 特有失效模式。
- **CloudWatch GenAI Observability 三大面板**:
  - Model Invocation Dashboard：调用量、token、成本、延迟、错误、限流
  - AgentCore Agent Dashboard：会话、工具调用、内存操作、网关指标、逐步推理轨迹
  - OpenTelemetry Integration：分布式追踪、自定义 span、AWS SDK 自动埋点、X-Ray 服务地图
- **ADOT 定位**: AWS 官方 OpenTelemetry 发行版，
  预配置 AWS 服务集成，
  支持 EC2/ECS/EKS/Lambda 多环境部署，降低埋点门槛。
- **RAG 六步可观测化**: Embedding 生成 → 向量检索 → 重排序 → Prompt 构建 → LLM 生成 → 答案提取，
  每一步均有独立 span、属性与指标。
- **质量指标自定义**: 检索质量（RetrievalQuality）、请求成本（RequestCost）、
  请求成功率（RequestSuccess）等通过 CloudWatch 自定义指标实时发布，
  支撑告警与仪表盘。
- **成本透明化**: 按模型、按请求、按用户维度的 token 与美元成本实时计算并上报，
  示例代码中甚至按输入/输出不同单价分别估算。
- **上下文窗口保护**: 在 prompt 构建阶段显式检查输入 token 是否超过模型上下文窗口，
  提前预警而非运行时失败，避免浪费 API 调用成本。
- **X-Ray 服务地图**: 与 OpenTelemetry 集成后，
  X-Ray 可自动生成服务依赖拓扑图，
  直观展示 RAG 流水线中各组件的调用关系与延迟瓶颈。
- **告警闭环**: 文章建议针对 TTFT 阈值突破、成本突增、检索质量下降、错误率上升等场景
  配置 CloudWatch Alarms，并通过 SNS 路由到运营通道。
- **系列定位**: 本文是 4 部曲中的第 3 篇，
  前篇涉及 RAG 评估与质量指标，
  后篇将讨论生产加固与高级模式，
  形成从评估到观测再到加固的完整闭环。
- **教学价值**: 不仅解释 "为什么需要"，
  还提供了可直接运行的 Python 代码框架，
  从理论到工程实现跨度完整。
- **云原生深度**: 与 AWS 托管服务深度集成，
  适合已入驻 AWS 生态的团队快速落地，
  但对多云策略团队需评估 vendor lock-in 风险。

## 与综述的关联

本材料与综述中 "Agent 与 LLM 系统的可观测性基础设施" 主题直接相关，
且提供了云厂商视角的工业级实践方案。
综述在讨论开源可观测工具（如 LangSmith、Phoenix、OpenInference）时，
往往侧重 Trace 与 Eval 的局部能力，
而对 Metrics 维度（特别是成本、延迟、限流等运营指标）的覆盖不足。
本文展示了云厂商如何将可观测性整合为
覆盖指标（Metrics）、日志（Logs）、追踪（Traces）三位一体的托管服务，
恰好补充了综述在运营指标方面的论述缺口。

综述中关于 "RAG 检索可观测性" 的论述
可从本文获得强有力的工程佐证。
作者给出的 instrumented RAG 示例
明确将向量检索步骤独立为 span，
并记录检索文档数、平均相似度、重排序分数等质量信号。
这与学术文献中提出的 RAG 评估维度
（如上下文相关性、答案忠实度、答案相关性）
形成了 "学术定义 → 工程实现" 的完整链条。
综述在引用本文时，
可特别强调 "相似度分数作为检索质量的代理指标" 这一实践，
与学术上的自动评估指标（如 BERTScore、BLEU）进行对比讨论。

此外，本文与 s1-014（Llama Stack 遥测指标提案）
形成了极为有趣的互补关系。
两者都关注 token、延迟、成本、错误四大维度，
但 AWS 方案提供了托管仪表盘与自动埋点能力，
而 Llama Stack 提案偏向开源框架的底层指标定义。
综述可将二者并置，
论证一个正在发生的产业趋势：
无论云厂商还是开源社区，
GenAI 可观测性的指标语义正在快速收敛，
但真正的差距在于 "从定义到落地" 的自动化程度——
AWS 通过 ADOT 和 CloudWatch 大幅降低了埋点成本，
而开源方案仍需开发者手动 instrument 或等待社区贡献。
这一对比可作为综述中 "可观测性落地障碍" 章节的核心论点。

本文对综述中 "生产环境 Agent 运营" 章节亦有重要贡献。
CloudWatch 的 AgentCore Dashboard
专门追踪 Agent 会话、工具调用、内存操作等 Agent 特有运行时数据，
这些数据在开源工具链中往往分散在不同系统
（LangChain 的 callback、自定义日志、外部向量数据库监控、独立的安全审计日志）中
难以统一。
AWS 的整合方案为综述讨论 "Agent 可观测性平台化" 提供了工业参照，
同时也暗示了 vendor lock-in 的风险——
深度依赖 AWS 生态的团队在迁移至其他云厂商时，
可能面临可观测数据模型的重建成本。

从标准化角度，
本文中 OpenTelemetry 的使用
与综述引用的 OpenInference 规范（c-014、c-015）存在协同空间。
ADOT 作为 OpenTelemetry 的 AWS 发行版，
天然支持 OTLP 协议，
如果 OpenInference 的语义约定能被 ADOT 识别和增强，
将极大提升跨云、跨框架的可观测数据互操作性。
综述可在讨论标准化进展时，
将本文作为 "云厂商拥抱开放标准" 的正面案例。

## 我的笔记

这篇文章是少数能将 GenAI 可观测性的 "为什么" 和 "怎么做"
同时讲透的工业博客。
开篇的凌晨 3 点 PagerDuty 告警场景极具代入感，
它准确击中了从传统微服务转型到 GenAI 系统的工程师们的共同痛点：
我们习惯了用 HTTP 状态码判断健康，
但 GenAI 系统让这套方法论彻底失效。
200 OK 只是一个开始，而非结束。

文章的技术架构设计有几个亮点值得深入记录。
首先是 CloudWatch GenAI Observability 的 "purpose-built" 定位——
它不是简单地把现有监控指标套用到 LLM 上，
而是重新定义了 Model Invocation、AgentCore、OpenTelemetry Integration
三层专属面板。
这种分层设计意味着不同角色可以在不同抽象级别上定位问题：
SRE 在模型层看延迟和成本，
算法工程师在 Agent 层看会话和工具链，
架构师在追踪层看分布式调用链路。
这种 "角色适配" 的设计理念在单一开源工具中很难见到。

其次是 RAG 六步 instrument 示例的工程价值。
作者没有停留在理论层面，
而是给出了可直接运行的 Python 代码框架，
展示了如何用 OpenTelemetry 将 RAG 流水线转化为可追溯的结构化数据。
其中几个细节尤为精妙：
在 embedding 阶段同时记录维度与估算成本，
使得向量化的开销可观测；
在向量搜索阶段发布 `RetrievalQuality` 自定义指标，
将检索效果从隐性变为显性；
在 prompt 构建阶段做上下文窗口超限检查，
这是生产环境中从 "能跑" 到 "可运营" 的关键分水岭——
很多团队在上下文溢出时才后知后觉，
而此处的提前检查避免了无效的 API 调用浪费。

不过，方案也存在可讨论的现实局限。
其一，CloudWatch GenAI Observability 目前深度绑定 AWS 生态
（Bedrock、AgentCore、ADOT），
对于混合云或多云部署的团队而言，
数据孤岛与 vendor lock-in 风险不可忽视。
如果团队同时使用 Azure OpenAI 和 AWS Bedrock，
则需要在两个云平台分别维护可观测体系，
难以形成统一视图。
其二，文中提到的成本计算基于 "按 1K token 定价" 的静态估算，
实际生产中的计费模型可能更复杂
（如 provisioned throughput、缓存命中折扣、批量推理折扣等），
需要额外的校准逻辑才能精确到账单级别。
其三，自定义质量指标（如 RetrievalQuality）的具体计算方式
在文中并未充分展开——
平均相似度分数是否足够代表检索质量？
当向量数据库中的文档分布不均匀时，
相似度分数可能存在系统性偏差。
这需要结合综述中 RAG 评估的学术研究成果
（如 RAGAS、Arize 的评估框架）来完善。

从代码质量角度看，
示例中的 instrument 模式值得推广。
将每个 RAG 步骤封装为独立 span，
不仅服务于可观测性，
还自然地文档化了数据流：
embedding → search → rerank → prompt → generate → extract。
这种 "可观测性即文档" 的副作用
对新成员理解系统架构极有帮助。
建议在实际项目中将其作为 RAG 实现的模板。

从综述写作角度，
本文是 "工业实践" 证据池中的高价值来源。
它不仅提供了 AWS 这一主流云厂商的产品设计思路，
还附带了一个完整的 RAG instrument 代码范例，
以及从安装、配置、埋点到告警的端到端流程。
建议在综述的 "可观测性技术栈对比" 表格中
将其与 LangSmith、Phoenix、Weights & Biases 等工具并列，
重点标注其 "云原生集成深度"、"Agent 专属面板"、"成本透明化"
三个差异化优势。
同时，文中提出的 "200 OK 但业务失败" 概念
可作为综述引入可观测性章节的经典论断，
比纯学术表述更具传播力和说服力。

图片资产方面，
原文包含大量架构图与仪表盘截图，
已存档于本地 `cited-materials/images/[s1-010]/` 目录。
其中涉及 CloudWatch 仪表盘
（展示 Model Invocation 的调用量与 token 分布）、
X-Ray 服务地图（展示 RAG 各组件的调用拓扑）、
ADOT 架构图（展示 Collector 与后端服务的交互关系）、
以及 RAG 埋点流程图等可视化内容。
若综述需要展示 AWS 可观测性体系的全貌
或对比云厂商与开源方案的界面差异，
可直接引用这些本地图片并标注原始出处。

最后，值得一提的是本文在四部曲中的承上启下位置。
第 2 部分讨论 RAG 评估与质量指标（解决 "评什么"），
第 3 部分讨论可观测性栈（解决 "怎么看"），
第 4 部分将讨论生产加固（解决 "怎么保"）。
这种从评估到观测再到加固的递进结构，
本身就是一个完整的 GenAI 系统成熟度提升路径，
综述在组织 "生产化" 章节时可借鉴这一叙事逻辑。
