---
tags:
  - AI可观测性
  - Agent监控
  - OpenTelemetry
  - 企业IT运维
  - LLM质量评估
  - CiscoAGNTCY
  - 应用性能监控
  - AIOps
  - 安全风险
aliases:
  - Monitor LLM and agent performance with AI Agent Monitoring in Splunk Observability Cloud
  - Splunk AI Agent Monitoring
  - Splunk Observability Cloud AI
  - s2-008
date: 2026-02-13
url: https://www.splunk.com/en_us/blog/observability/monitor-llm-and-agent-performance-with-ai-agent-monitoring-in-splunk-observability-cloud.html
---

# Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性

## 核心信息

- **来源标题**: Monitor LLM and agent performance with AI Agent Monitoring in Splunk Observability Cloud — Splunk Blog
- **作者**: Splunk 官方博客
- **发布日期**: 2026-02-13
- **来源类型**: 产品公告 / 技术博客
- **原始链接**: https://www.splunk.com/en_us/blog/observability/monitor-llm-and-agent-performance-with-ai-agent-monitoring-in-splunk-observability-cloud.html
- **本地存档**: `[s2-008]-monitor-llm-and-agent-performance.pdf`
- **证据质量**: medium（基于官方产品发布声明，包含具体功能描述和技术架构信息）

## 内容摘要

2026 年 2 月，Splunk 在其 Observability Cloud 平台上正式推出 AI Agent Monitoring 功能，将其已有的 AI Infrastructure Monitoring 能力扩展至 Agent 应用层，为企业提供覆盖整个 AI 技术栈的统一可观测性解决方案。这一发布反映了企业级软件市场的一个重要趋势：随着大语言模型（LLM）和 Agentic 应用从概念验证阶段进入生产环境，传统的应用性能监控（APM）工具已无法满足 AI 系统特有的非确定性行为、质量漂移和安全风险等监控需求。

Splunk 在博客中明确指出，AI 的民主化在极大提升软件开发、内容创作和客户支持效率的同时，也催生了所谓 "slop" 现象——即不真实、不准确、低质量甚至有害的输出。这些问题的频率和强度高度依赖于底层基础设施的稳定性与可观测性。因此，企业需要深入且统一的全栈可见性，才能将业务问题与 AI 系统生成的性能、质量、安全和成本/使用量指标关联起来，无论这些系统部署在本地数据中心、混合环境还是公有云上。

AI Agent Monitoring 的核心能力建立在两个重要的开放标准之上：OpenTelemetry 和 Cisco AGNTCY（Agent 互操作性标准）。通过扩展 Splunk Application Performance Monitoring（APM）的排障和监控能力，AI Agent Monitoring 帮助 ITOps 和工程团队建立对其 Agentic 应用的信任。具体而言，该产品提供了三大核心视图：AI Agents 页面、AI Trace Data 页面和 Trace 详情视图。AI Agents 页面呈现聚合和单个 Agent 的性能、成本和安全指标；AI Trace Data 页面展示 LLM 提示词、响应以及质量相关问题，包括幻觉（hallucinations）、偏见（bias）、情感（sentiment）和毒性（toxicity）；Trace 视图则深入展示 span 级别的详细信息，包括工具调用的运行时和内存消耗、Agent 工作流执行路径等。

在技术实现层面，Splunk 引入了 LLM-as-a-judge 评估器，用于自动评判 Agent 输出的质量。这一机制与传统的基于规则的质量检测不同，它利用大语言模型自身的能力来识别输出中的潜在问题，如事实性错误、不当内容生成和逻辑矛盾。此外，AI Agent Monitoring 与 Cisco AI Defense 的集成为企业提供了风险检测能力，可以在 Agent 执行过程中识别异常行为和潜在安全威胁。

从市场定位来看，Splunk 的进入标志着传统可观测性巨头正式将 AI Agent 监控纳入其战略版图。与 Braintrust 等原生 AI 可观测性初创公司不同，Splunk 的优势在于其已有的企业客户基础、成熟的 APM 基础设施和广泛的生态系统集成能力。对于已经使用 Splunk Observability Cloud 的企业而言，AI Agent Monitoring 的推出意味着他们可以在现有监控体系内无缝扩展 AI 监控能力，而无需引入新的独立工具。

该产品支持对性能、成本、token 使用量、质量和风险趋势的多维度分析，帮助企业实现 AI 投资的 ROI 优化。在 Agent 应用日益复杂的背景下——一个典型的 Agent 可能涉及多个 LLM 调用、向量数据库检索、API 工具调用和记忆系统交互——这种全链路的可视化能力对于快速定位根因、优化响应延迟和控制运营成本至关重要。Splunk 特别强调，AI Agent Monitoring 支持本地数据中心（on-prem）、混合云（hybrid）和公有云（cloud）环境的统一监控，这对于受合规要求约束、无法将所有 AI 工作负载迁移到云端的大型企业尤为重要。

## 关键要点

1. **产品定位与战略意义**
   - Splunk Observability Cloud 新增 AI Agent Monitoring
   - 与已有的 AI Infrastructure Monitoring 形成覆盖基础设施层到应用层的完整 AI 可观测性方案
   - 标志着传统可观测性巨头正式进入 Agent 监控赛道
   - 验证了企业级市场对 Agent 可观测性的刚性需求
   - 预示 APM 行业将全面向 AI-Native 方向转型

2. **开放标准基础**
   - 基于 OpenTelemetry 构建，确保与现有云原生可观测性生态的互操作性
   - 采用 Cisco AGNTCY 标准，支持 Agent 互操作性和语义规范
   - 数据可移植性强，避免供应商锁定
   - 为企业级集成提供了标准化数据格式
   - 双标准策略兼顾兼容性与前瞻性

3. **核心视图体系**
   - AI Agents 页面：聚合/单个 Agent 的性能、成本、安全指标总览
   - AI Trace Data 页面：LLM 提示词、响应及质量问题（幻觉、偏见、情感、毒性）
   - Trace 视图：span 级别详情、工具调用运行时/内存、Agent 工作流路径
   - 三层视图设计覆盖了从宏观到微观的全部监控需求
   - 用户可根据角色和场景选择合适的信息粒度

4. **质量评估机制**
   - 引入 LLM-as-a-judge 自动评估器
   - 利用大语言模型自身能力检测输出中的事实错误、不当内容和逻辑矛盾
   - 区别于传统基于规则的质量检测方案
   - 实现了语义层面的自动质量把关
   - 支持持续学习和阈值自适应调整

5. **安全集成能力**
   - 与 Cisco AI Defense 深度集成
   - 提供实时风险检测和异常行为识别
   - 覆盖 Agent 执行全生命周期的安全监控
   - 将可观测性与安全防护无缝结合
   - 支持合规审计和事件追溯

6. **部署灵活性**
   - 支持本地数据中心（on-prem）部署
   - 支持混合云（hybrid）架构
   - 支持多云（cloud）环境的统一监控
   - 满足大型企业的合规和数据主权要求
   - 统一的监控体验不受部署位置影响

7. **目标用户与价值主张**
   - 主要面向 ITOps 团队和工程团队
   - 强调在生产环境中构建对 Agentic 应用的信任
   - 降低 Agent 系统的运维复杂度和认知负荷
   - 提供开箱即用的企业级监控仪表盘
   - 缩短新技术的学习曲线和采纳周期

8. **多维度分析能力**
   - 支持性能、成本、token 使用量、质量评分和风险趋势的交叉分析
   - 助力企业优化 AI 投资的 ROI
   - 提供趋势视图，便于识别长期漂移和模式变化
   - 实现业务指标与技术指标的关联映射
   - 支持自定义告警规则和阈值策略

9. **APM 自然扩展**
   - 并非独立新产品，而是 Splunk APM 能力的有机延伸
   - 降低现有客户的采用门槛和切换成本
   - 利用已有的数据采集管道和用户界面框架
   - 保持用户体验的一致性和熟悉度
   - 数据可以在同一平台内跨传统应用和 AI Agent 关联分析

10. **行业影响**
    - 验证了 AI Agent Monitoring 作为企业级刚需的市场地位
    - 推动可观测性行业从传统 APM 向 AI-Native Observability 演进
    - 加速开放标准在 AI 监控领域的普及
    - 预示未来 APM 与 AI 监控的边界将进一步模糊
    - 为其他传统 APM 厂商提供了产品路线图参考

## 与综述的关联

本笔记与综述中 "Agent 可观测性技术栈与产业格局" 章节直接相关。Splunk 的入局为 "传统可观测性厂商如何应对 AI Agent 挑战" 提供了典型案例。综述中讨论的 Agent 系统监控难点——非确定性输出、质量漂移、多跳工具调用链的可视化——在 Splunk 的产品设计中均有直接对应。Splunk 将这些问题纳入统一的监控框架，证明了 Agent 可观测性不是边缘需求，而是企业级平台必须解决的核心问题。这一案例可以用来反驳 "Agent 监控只是小众需求" 的观点，并为综述中关于市场规模的乐观预测提供支撑。

特别值得注意的是，Splunk 选择基于 OpenTelemetry 和 Cisco AGNTCY 标准构建，这与综述关于 "Agent 可观测性标准化" 的趋势判断高度一致。当 Agent 应用涉及多个供应商的组件（不同的 LLM 提供商、向量数据库、工具 API）时，统一的遥测数据标准是实现端到端追踪的前提条件。Splunk 的技术路线为综述中 "开放标准将加速 AI 可观测性生态成熟" 的论点提供了有力支撑。此外，Cisco AGNTCY 的采用也意味着网络设备巨头 Cisco 正在将其影响力扩展至 AI Agent 领域，这可能改变未来 Agent 互操作性的竞争格局。综述在讨论标准化趋势时，可以将 AGNTCY 与 OpenTelemetry 的互补关系作为一个重要案例。

Splunk 与 Cisco AI Defense 的集成也呼应了综述关于 "可观测性与安全性的融合" 的讨论。Agent 系统不仅有性能和质量风险，还可能成为数据泄露、提示词注入（prompt injection）和权限滥用的攻击面。将安全检测能力嵌入可观测性平台，代表了未来 AIOps 的一个重要演进方向。综述若在讨论 AI 系统风险时引入这一案例，可以说明安全监控正在从边界防御向应用内嵌转变。这种融合趋势可能会催生新的产品类别——即可观测性、安全性和 AI 治理三位一体的统一平台，值得在综述的未来趋势章节中予以展望。

## 我的笔记

Splunk 推出 AI Agent Monitoring 是一个具有行业风向标意义的事件。作为传统可观测性领域的领军企业，Splunk 的进入意味着 Agent 监控已经从初创公司的创新探索阶段，进入了主流企业软件厂商的战略布局阶段。这对于整个赛道的成熟度和客户教育都是重大利好。回顾历史，当一个新兴市场出现足够多的独立初创公司后，传统巨头的进入往往是市场即将进入高速增长期的信号。Splunk 的决策可能基于其企业客户群中 AI 项目部署数量的显著增长，以及这些客户对统一监控平台的明确需求。

从技术架构角度，Splunk 选择基于 OpenTelemetry 构建是一个明智的决定。OpenTelemetry 已经成为云原生可观测性的事实标准，而 Cisco AGNTCY 则为 Agent 特有的遥测数据（如 Agent 意图、工具调用计划、记忆状态）提供了语义规范。这种双标准策略既保证了与现有基础设施的兼容性，又为 Agent 特有的监控需求预留了扩展空间。值得注意的是，AGNTCY 标准由 Cisco 主导，而 Cisco 于 2023 年收购了 Splunk，因此 Splunk 对 AGNTCY 的采用也可能带有推动 Cisco 自有标准成为行业规范的意图。这种标准之争可能会影响未来 Agent 生态的互操作性格局，也可能引发其他厂商推出竞争性标准。

LLM-as-a-judge 评估器的引入值得特别关注。这是将大语言模型用于自我监控的一个典型案例，但其有效性高度依赖于评判模型的选择、评估提示词的设计以及阈值调优。在实际生产环境中，如何平衡自动评估的覆盖率与误判率，如何避免评判模型自身的偏见影响评估结果，都是需要持续优化的课题。Splunk 并未在博客中详细披露其 LLM-as-a-judge 的实现细节，但作为一家企业级软件公司，其评估方案很可能经过大量客户场景验证。综述中若有关于 "自动评估方法论" 的讨论，Splunk 的实践可作为企业级部署的参考案例。同时，LLM-as-a-judge 的引入也引发了一个有趣的元问题：谁来监控监控者？如果评判模型本身存在缺陷或偏见，那么自动评估系统可能会系统性地忽略某些类型的质量问题。

与 Braintrust（s2-019）等原生 AI 可观测性平台相比，Splunk 的路径代表了 "自上而下" 的扩展策略——从成熟的 APM 基础设施向 AI 场景延伸。这种策略的优势在于客户转换成本低、数据整合能力强、企业采购流程简化；潜在劣势则在于 legacy 架构可能在灵活性上不及云原生新贵。对于已经深度使用 Splunk 的企业客户，这种扩展路径无疑是最优解，因为他们无需重新搭建监控基础设施，也无需培训团队使用新工具。但对于技术栈较新、追求极致 AI 专项能力的团队，Braintrust 这类专用平台可能更具吸引力。最终的市场分割可能呈现 "Splunk 主导传统企业市场，Braintrust 主导云原生初创市场" 的格局。然而，随着时间推移，如果 Splunk 在 AI 专项功能上持续投入，它也可能向初创市场渗透。

Cisco AI Defense 的集成也是一个亮点。它表明 Splunk 将 AI 可观测性视为一个包含性能、质量、成本和安全四个维度的综合问题，而非单纯的监控告警。这种 "可观测性 + 安全" 的融合思路，可能与未来 XDR（扩展检测与响应）和 AIOps 的边界模糊化趋势有关。Agent 系统由于其自主决策能力，可能成为内部威胁和外部攻击的新载体。例如，一个被劫持的 Agent 可能通过工具调用访问敏感数据库，或通过 LLM 输出泄露内部信息。在这种情况下，单纯的可观测性不足以防范风险，必须与安全检测能力结合。值得在综述的产业格局分析中予以关注，因为这可能预示未来会出现 "AI 可观测性与安全" 的融合产品类别，类似于网络安全领域的 XDR 概念向 AI 领域的延伸。

从企业采用角度，Splunk AI Agent Monitoring 的一个关键卖点是其对混合部署环境的支持。许多受监管行业（如金融、医疗、政府）的企业无法将 AI 工作负载完全迁移到公有云，因此需要在本地和云端同时部署 Agent 系统。Splunk 的统一监控能力使这些企业能够在单一平台上查看所有环境的 AI 健康状态，避免了多工具管理的复杂性。这一差异化优势是云原生初创公司短期内难以复制的，因为建立 on-prem 部署能力需要庞大的销售和支持体系。对于 Splunk 而言，这既是护城河，也是进入壁垒——新客户可能因为这一能力而选择 Splunk，而竞争对手想要追赶需要投入大量资源。

最后，Splunk 对产品命名也值得关注："AI Agent Monitoring" 而非 "LLM Monitoring" 或 "AI Monitoring"。这一命名选择明确传达了 Splunk 的市场判断——未来的 AI 应用将以 Agent 形态为主，单纯的 LLM 调用监控不足以满足需求。这与整个行业从 "模型中心" 向 "Agent 中心" 演进的趋势高度一致。综述在讨论市场趋势时，可以引用 Splunk 的产品命名作为传统厂商认知转变的佐证。值得注意的是，如果未来 Splunk 进一步扩展其产品线，可能会出现 "AI Agent Orchestration" 或 "AI Agent Governance" 等更高层次的功能，将监控延伸至管理和控制层面，形成完整的 AI 应用生命周期管理平台。

## 延伸阅读建议

- 与 s2-019（Braintrust 融资事件）对比阅读，可观察传统 APM 巨头与原生 AI 可观测性平台的竞争态势
- 与综述中关于 OpenTelemetry 的讨论结合，理解开放标准对 AI 监控生态的推动作用
- 关注 Cisco AGNTCY 标准的后续演进，以及其对 Agent 互操作性格局的影响
- 追踪 Splunk AI Agent Monitoring 的实际客户案例和采用数据
- 参考 Cisco 在 AI 安全领域的其他产品布局，理解其整体 AI 战略

## 版本记录

- 2026-05-24: 基于 JSON 源内容重写为结构化阅读笔记
- 补充了产品功能细节、技术标准和安全集成分析
- 增加了与综述各章节的关联映射
