---
tags:
  - OpenInference
  - OpenTelemetry
  - semantic-convention
  - LLM-observability
  - distributed-tracing
  - agent-telemetry
  - span-kind
  - attribute-schema
  - AI-observability-standard
aliases:
  - OpenInference Specification
  - OpenInference 语义规范
  - OpenInference 技术规范文档
date: 2026-05-24
url: https://arize-ai.github.io/openinference/spec/
---

# OpenInference Specification | openinference

## 核心信息

- **来源编号**: c-014
- **标题**: OpenInference Specification
- **发布方**: Arize AI
- **文档类型**: 技术规范（technical spec）
- **状态**: ongoing（持续更新）
- **URL**: https://arize-ai.github.io/openinference/spec/
- **证据质量**: high（作为社区事实标准的技术规范文档）
- **相关标准**: OpenTelemetry OTLP、RFC 2119
- **覆盖范围**: LLM 调用、智能体推理、工具调用、检索操作、嵌入生成、护栏检查、评估打分

## 内容摘要

OpenInference 是一套面向 AI 应用可观测性的语义约定规范，它直接构建在 OpenTelemetry 之上，专门为 LLM 调用、智能体推理步骤、工具调用、检索操作等 AI
特定工作负载定义了分布式追踪的标准化表示方式。

OpenTelemetry 本身定义了通用的分布式追踪 wire format 和 SDK 模型，但其属性模型是刻意保持通用性的。然而，AI
应用呈现出一系列通用约定无法覆盖的独特可观测性需求。首先，LLM 调用携带的是结构化的多轮消息数组，包含系统提示词、工具定义以及多模态内容，单一的字符串型 `input.value`
远远不够。其次，Token 经济学是 AI 应用运维的核心指标，提示词 token 数、完成 token 数、缓存 token 数以及推理 token
数的细粒度拆分必须成为一等公民，而非事后补充。第三，现代 AI 系统的控制流具有显著的智能体特征，它们通过推理循环进行路由，将任务委派给子智能体，调用工具，查询检索系统，每一次跳转都需要一致的标识和
span-kind 分类法，否则追踪数据将无法解读。第四，隐私敏感性要求提示词和完成内容中经常包含个人身份信息，必须在导出前具备按字段粒度进行脱敏和掩码的能力。第五，LLM
输出具有随机性，追踪必须携带足够的上下文信息，以便复现或至少解释某一次特定的执行过程。

OpenInference 通过在 OpenTelemetry span 之上定义具体的属性模式和 span-kind 分类法来解决这些问题。每一条 OpenInference 追踪都是一条有效的
OTLP 追踪，这些语义约定赋予了通用属性名称以 AI 特定的含义。这意味着任何已经支持 OpenTelemetry 的后端系统，无需修改底层协议即可消费 OpenInference
数据，只需在展示层理解这些 AI 特定的属性语义即可。

在追踪结构中，trace 记录了一个请求的完整执行路径，从用户的初始输入开始，经过每一次 LLM 调用、工具调用和检索步骤，直到最终响应。追踪是由父子关系连接的 span 树。根 span
通常代表一次智能体回合或流水线调用，子 span 则代表其中的各个独立操作。这种树状结构对于理解复杂 Agent
系统的执行流程至关重要，因为一个高层任务通常会分解为多个子任务，每个子任务又可能触发进一步的 LLM 调用或工具执行。

Span 是工作的原子单位：一次 LLM 调用、一次工具执行、一次检索查询、一次嵌入向量生成。每个 span 都携带描述信息（人类可读的操作名称，如
ChatCompletion）、起止时间戳（纳秒精度的墙钟时间）、`openinference.span.kind`（该操作在流水线中的角色）以及类型化的键值对（捕获输入、输出、配置和成本）。这些属性不仅用于事后分析，也是实时监控和告警的数据基础。

`openinference.span.kind` 属性对操作进行分类，使可观测性平台能够以 AI 感知的方式渲染追踪和聚合数据。规范中定义了十种 span kind，包括：LLM（语言模型 API
调用，携带输入消息、模型参数、输出消息和 token 计数）、AGENT（自主智能体的推理步骤，可能产生工具调用、检索或嵌套 LLM 调用的子
span）、CHAIN（确定性操作序列，如提示词格式化、后处理或编排逻辑）、TOOL（语言模型调用的函数或外部
API）、RETRIEVER（向量存储、搜索引擎或知识库的查询）、RERANKER（按相关性重新排序文档候选集的模型）、EMBEDDING（文本或其他内容的向量嵌入生成）、GUARDRAIL（输入或输出的合规性检查）、EVALUATOR（模型响应的自动化评估，如
LLM-as-judge）、PROMPT（命名提示词模板的调用）。

属性是附加到 span 上的类型化键值对，遵循结构化的命名约定。它们是 OpenInference
的主要载荷，携带提示词、响应、模型名称、检索到的文档、工具参数以及理解和复现给定执行所需的一切信息。属性名称使用点分隔的命名空间，例如 `llm.input_messages` 和
`llm.token_count.prompt`。列表值属性采用基于零的整数索引扁平化形式，例如 `llm.input_messages.0.message.role`。这种扁平化设计既保持了与
OTel 属性模型的兼容性，又能够表达复杂的嵌套结构。规范文档中对这些属性名称、类型和含义有完整的权威定义。

规范还涵盖了追踪结构、span 层次结构和上下文传播，语言模型调用、嵌入生成、工具调用、多模态属性的完整属性参考，以及环境变量、隐私控制和数据掩码的配置选项。在合规性方面，规范明确使用了 RFC
2119 中的关键词（MUST、MUST NOT、REQUIRED、SHALL、SHALL NOT、SHOULD、SHOULD NOT、RECOMMENDED、NOT
RECOMMENDED、MAY、OPTIONAL），并以全大写形式出现。满足所有 MUST、MUST NOT、REQUIRED、SHALL 和 SHALL NOT
要求的实现才是合规的。不满足任何此类要求的实现即视为不合规。项目的官方名称为 "OpenInference"（Open 和 Inference 之间没有空格）。

## 关键要点

1. **OpenTelemetry 之上的 AI 语义层**：OpenInference 不是重新发明追踪协议，而是在 OTLP 之上定义 AI 专用的属性模式和 span-kind
分类法，确保与现有 OTel 生态完全兼容，任何 OTel 后端都可以直接消费。

2. **十种 span kind 覆盖 AI 全链路**：从 LLM
调用、嵌入生成、检索查询、重排序、工具调用到智能体推理、编排链、护栏检查和评估打分，每种操作都有明确的语义分类，使追踪数据具备自解释性。

3. **结构化输入输出支持**：突破了传统 `input.value` / `output.value`
字符串的限制，支持多轮消息数组、工具定义、多模态内容等复杂结构的精确描述，通过扁平化索引语法表达嵌套结构。

4. **Token 经济的一等公民地位**：规范将提示词 token、完成 token、缓存 token、推理 token 的计数定义为关键属性，使其成为成本归因、预算控制和性能优化的核心数据。

5. **隐私保护的字段级掩码**：规范支持在导出前对敏感字段进行按字段粒度的掩码处理，满足 GDPR、CCPA 等数据保护法规的要求，同时保留非敏感字段的完整追踪价值。

6. **RFC 2119 合规性要求**：规范以严格的 IETF 标准语言编写，区分了必须满足的要求和推荐做法，为不同实现之间的互操作性提供了明确的合规基准。

7. **项目命名规范**：官方项目名称为 "OpenInference"，中间无空格，在引用、集成和文档编写时应注意保持命名一致性。

8. **与 OTel GenAI 的互补关系**：OpenInference 早于 OTel GenAI 语义约定出现，两者当前处于互补和逐步融合的状态，共同推动 AI 可观测性标准的成熟。

9. **多模态与工具调用支持**：规范对图像、音频等混合内容消息以及函数/工具调用和结果表示都有专门的属性定义，适应了现代多模态 Agent 系统的需求。

10. **持续演进的规范文档**：作为 ongoing 状态的技术规范，OpenInference Specification 会随着 AI 应用形态的演化而持续更新，保持对新兴框架和用例的覆盖。

11. **属性命名空间的层次化设计**：通过点分隔的层次化命名空间，属性名称本身就携带了语义信息，便于查询、过滤和聚合，也为后端系统的自动解析和展示提供了便利。

12. **上下文传播的标准化**：规范对 trace 之间的上下文传播进行了定义，确保在复杂的分布式 Agent 系统中，跨服务边界的追踪能够正确地关联和拼接。

## 与综述的关联

本规范是理解整个 AI Agent 可观测性技术栈的基础性文档。在综述中，OpenInference 作为连接 OpenTelemetry 通用追踪框架与 AI
特定可观测性需求之间的关键桥梁，其语义约定直接支撑了以下讨论主题：

- **追踪数据结构标准化**：综述中关于 Agent 执行轨迹的统一表示、跨框架追踪互操作性的讨论，直接依赖于 OpenInference 定义的 span-kind 和属性命名空间。没有这样的标准，来自 LangChain、LlamaIndex、CrewAI 等不同框架的追踪数据将无法在同一后端中进行统一查询和分析。

- **成本归因与 Token 经济**：综述中关于 Agent 系统运行成本分析和预算控制的内容，需要依赖 OpenInference 规范中对 token 计数、调用参数、模型名称等属性的标准化定义。这些属性是进行细粒度成本分摊和异常检测的前提。

- **隐私与安全合规**：综述中关于 Agent 系统审计日志和数据隐私保护的讨论，可以引用 OpenInference 的字段级掩码机制作为技术实现参考。特别是在处理包含个人身份信息的用户输入时，按字段掩码比全量删除更符合运维需求。

- **与 OpenTelemetry GenAI 语义约定的关系**：综述需要说明 OpenInference 与 OTel 原生 GenAI 约定之间的互补和融合趋势，这是当前可观测性领域的重要演进方向。理解两者之间的历史渊源和技术差异，有助于读者把握标准的未来走向。

- **Agent 系统的根因分析**：综述中关于 Agent 执行失败诊断的内容，可以借助 OpenInference 的 span-kind 分类法进行快速定位。通过区分 AGENT（决策问题）、TOOL（调用问题）、RETRIEVER（上下文问题）等类别，可以显著缩短故障排查时间。

- **评估指标与追踪的关联**：规范中定义的 EVALUATOR span kind 为将 LLM-as-judge 等评估机制融入追踪流水线提供了标准化的语义基础，这与综述中"观测驱动评估"的主题紧密相关。

- **多模态 Agent 的可观测性**：随着视觉-语言模型和音频理解模型在 Agent 系统中的应用越来越广泛，OpenInference 的 Multimodal Attributes 部分为这些场景提供了标准化的描述方式，综述在讨论多模态 Agent 时应引用此规范。

## 我的笔记

OpenInference 规范的最大价值在于它提供了一个"AI 原生"的追踪语义层，而不是让 AI 应用去适配传统 HTTP 服务的追踪模型。在 HTTP 服务中，一次 span 只需要
method、status_code、path 等属性就足够理解；但在 LLM 应用中，同样的"一次调用"背后是多轮对话历史、系统提示词、工具定义、温度参数、token
消耗、模型版本等数十个维度的信息。如果这些信息散落在不同的日志格式中，不仅无法聚合分析，更无法在不同框架之间进行横向比较。

从工程实践角度，我认为 OpenInference 的十种 span-kind 设计非常贴近实际 Agent 系统的执行模式。特别是 AGENT 和 CHAIN
的区分——前者代表自主决策的智能体循环，后者代表确定性的编排逻辑——这种区分对于后续做根因分析和故障定位至关重要。当一次 Agent 执行失败时，通过 span-kind
可以快速判断问题出在智能体的决策逻辑（AGENT）、工具调用的参数构造（TOOL）、检索阶段返回了不相关的上下文（RETRIEVER），还是重排序模型产生了偏差（RERANKER）。这种结构化的故障分类远比在原始日志中搜索关键词高效。

隐私保护方面，字段级掩码的支持是一个务实的设计。在生产环境中，完全禁止记录提示词和响应会导致调试困难，而全量明文记录又违反数据保护法规。OpenInference
的按字段掩码机制允许在保留结构化信息的同时对敏感内容脱敏，这种"结构化匿名化"的思路值得在 Agent
审计日志设计时借鉴。例如，可以保留消息的角色（system/user/assistant）和时间戳，但掩码消息中的邮箱地址、电话号码等 PII 内容。

规范采用 RFC 2119 语言编写，说明 Arize 有意将其定位为社区标准而非仅仅是内部文档。这对于推动整个行业采用统一的 AI 可观测性语义至关重要。未来在综述写作中，可以将
OpenInference 的合规性要求作为评估其他可观测性工具（如 Langfuse、OpenLIT、OpenLLMetry）兼容性的基准。一个声称支持 AI 可观测性的工具，如果不能正确理解和消费
OpenInference 定义的属性命名空间，其互操作性就存在根本缺陷。

此外，规范对多模态内容的属性定义也值得关注。随着视觉-语言模型和音频理解模型在 Agent
系统中的应用越来越广泛，追踪数据需要能够描述图像、音频等非文本输入的内容类型、编码格式和引用关系。OpenInference 的 Multimodal Attributes
部分为这些场景提供了标准化的描述方式，这是传统文本日志无法做到的。

最后，规范的 ongoing 状态意味着它是一个活文档，会随着技术发展而持续更新。在综述中引用规范时，应注意标注版本或时间点，避免因规范演进导致引用内容过时。同时，这种持续迭代也表明 AI
可观测性领域仍处于快速发展阶段，标准尚未完全固化，存在参与和影响标准走向的机会窗口。对于正在构建 Agent 可观测性基础设施的团队来说，密切跟踪 OpenInference
规范的更新动态，可以帮助及时调整自身的追踪数据模型，确保与未来生态的兼容性。

在实际落地层面，建议团队在引入 OpenInference

13. **分层规范的模块化组织**：规范将内容划分为 Trace Specifications、Semantic Conventions、Configuration、LLM Spans、Embedding Spans、Tool Calling、Multimodal Attributes 等独立模块，便于读者按需查阅和实现者分阶段支持。

14. **向后兼容与版本演进策略**：规范作为 ongoing 文档，在更新时注重向后兼容性，确保已有的插桩实现和消费端不会因规范升级而立即失效。
