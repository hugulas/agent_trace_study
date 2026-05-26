# 智能体轨迹可观测性综述：从日志采集到诊断、评测与治理

> 时间边界：2023-2026  
> 语料基础：`agentic_trace_insight/notes` 中的 117 篇本地笔记，以及由这些笔记刷新得到的 `llm-wiki` 词条、观点与对比页  
> 报告性质：研究与工程综述，不是产品选型白皮书

---

## 摘要

智能体可观测性正在从“记录模型调用日志”的工程附属功能，演变为支撑智能体可靠性、安全性、合规性和成本控制的核心基础设施。117 篇本地笔记覆盖了学术论文、产品文档、工程博客、标准草案和产业材料；它们共同指向一个清晰结论：智能体系统的关键问题已经不再只是“最终答案对不对”，而是“执行过程中发生了什么、哪里首先不可恢复地出错、是否违反系统规范、证据能否被审计、成本能否被归因”。

本综述将现有材料重构为五层架构。第一层是轨迹证据层，负责将用户意图、模型消息、工具调用、工具返回、状态变化、记忆读写、环境观测和评测结果组织成可复用证据。第二层是 schema 与插桩层，围绕 OpenTelemetry、OpenInference、AgentTrace、Hermes trajectory format 和平台自定义格式展开，解决跨框架采集与语义保真问题。第三层是诊断与归因层，以 AgentRx、Who&When、DoVer、HORIZON、AgentDiagnose、MASPrism 等工作为代表，试图回答“哪个智能体、哪个步骤、哪条依赖链导致失败”。第四层是过程评测与治理层，以 AgentPex、Monitoring Monitorability、HarnessAudit、AgentPro、安全审计和防篡改 audit trail 为代表，强调最终成功率不足以覆盖过程违规、策略绕过和不可追责行为。第五层是生产平台与经济层，包括 Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、Datadog、Splunk、Elastic、New Relic、AWS、Google、阿里云、百度、Coze 等产品材料，显示可观测性正在与评估、数据集、实验、成本和合规平台合流。

全文的核心判断是：智能体可观测性的真正对象不是日志，而是“可行动证据”。日志只回答发生了什么；可行动证据还必须支持失败定位、过程合规、审计追责、成本归因和系统演化。因而，未来的智能体可观测系统不会只是 APM 的 LLM 插件，而会成为连接运行时、评测器、诊断器、安全策略、数据飞轮和 harness 工程的公共证据层。

---

## 1. 范围与材料组织

本综述的材料来自四类来源。

第一类是智能体轨迹诊断和评测论文，主要包括 AgentRx、AgentPex、AIOpsLab、DoVer、PROBE、Monitoring Monitorability、Beyond the Black Box、Continual Harness、Agentic Harness Engineering、Meerkat、AgentTrace、VCC、HORIZON、HarnessAudit、EAGER、OpsAgent、SeqCV、Why Do Multi-Agent LLM Systems Fail、Who&When、EvoCF、Lifting Traces to Logic、AgentSight、AgentPro、Do Code Semantics Help、FLARE、AgentDiagnose 和 Teaching Text Agents to Learn from Failure 等 `p-001` 到 `p-030` 条目。

第二类是 agent 可观测性、trace schema、OpenTelemetry、OpenInference、audit trail、安全护栏、MCP tracing 和产品架构相关技术材料，主要分布在 `c-*` 与 `s3-*` 条目。

第三类是云平台与商业工具材料，覆盖 Google ADK / Vertex AI、AWS Bedrock AgentCore、阿里云 AgentLoop、百炼、百度千帆、Coze Loop、Datadog、Splunk、Elastic、New Relic、LangSmith、Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone 等。

第四类是 coding agent 与 agent framework 材料，覆盖 Claude Code、Codex CLI、OpenAI Swarm / Agents SDK、Hermes Agent、OpenClaw、Llama Stack 和多智能体协作示例。

这些材料的质量并不均匀。学术论文通常给出明确任务定义、数据集和实验结果，但部署成本、权限模型和组织流程讨论不足。产品文档和产业文章更贴近生产接入和团队工作流，但常常缺少可复现实验和 schema 细节。综述因此不采用单一路线，而是把每类材料放入不同证据位置：论文用于定义问题和方法边界，产品材料用于刻画落地需求和平台能力，标准与协议材料用于判断互操作性和长期演进方向。

---

## 2. 核心词条：从 trace 到可行动证据

### 2.1 智能体轨迹

智能体轨迹是按时间记录的用户输入、模型消息、工具调用、工具返回、状态更新、环境观测和评测结果。它不是普通日志的同义词。普通日志往往服务于运行状态回放，而智能体轨迹还必须支撑语义判断：模型是否误读了工具输出，是否违反了系统提示，是否在多智能体协作中传播了错误，是否在成本上进入无效循环。

AgentTrace 将轨迹组织为系统级、认知级和环境级三类表面，使日志从“API 请求记录”变成面向 agent 行为的结构化事件流。Hermes trajectory format 则展示了训练数据视角的轨迹规范：每轮工具调用和响应都应保持一致结构，以便后续训练、重放和分析。OpenInference 进一步尝试把 LLM、agent、tool、retriever、embedding、evaluator、guardrail 等 span kind 纳入 OpenTelemetry 生态。

由此可以得到第一条原则：trace 的字段设计必须从下游问题反推。如果目标只是统计 token 和延迟，普通 span 足够；如果目标是失败归因和审计，trace 必须保留工具参数、工具返回、状态变化、策略版本、agent 身份、任务上下文和事件间依赖。

### 2.2 失败归因

失败归因关注失败由哪个智能体、哪个步骤、哪类约束违反或哪条依赖链触发。AgentRx 把问题具体化为定位“第一个不可恢复关键步骤”，并用约束违反证据解释失败类别。Who&When 把多智能体失败归因拆成“哪个 agent”和“什么时候”两个维度。DoVer 则质疑只让 LLM 阅读日志后归因的可靠性，强调干预式验证。HORIZON 从长程任务角度揭示失败机制随任务长度迁移，说明短轨迹上的诊断成功不能直接外推到长轨迹。

失败归因的核心困难在于区分根因和后果。长轨迹中后续多个步骤都可能异常，但它们往往只是早期错误传播的结果。AgentRx 用工具 schema、领域策略和执行前缀抽取约束，试图把“原因”限制在可验证违反处。MASPrism 则显示，失败归因不一定总需要 frontier LLM；在多智能体轨迹中，prefill-stage 信号和注意力/NLL 特征可以为轻量模型提供诊断线索。

### 2.3 过程合规性

过程合规性评估智能体是否按系统提示、工具 schema、业务规则和安全策略行动，而不只看最终答案是否正确。AgentPex 是这一方向的代表：它从提示和工具规范中抽取行为规则，再用 judge 对完整轨迹进行多维合规评分。其关键贡献不是替代最终奖励，而是证明最终奖励和过程规范不等价。一个任务可以最终成功，却在中途跳过必要确认、调用错误工具、泄露不该泄露的信息，或违反输出格式要求。

这一点对生产系统尤其重要。在客户服务、医疗、金融、企业自动化和受监管场景中，过程违规本身就是失败。最终数据库状态正确不能抵消不合规访问、越权工具调用或缺失审批链。因而，智能体评测应至少分成三层：最终结果、过程规范、失败诊断。只报告 pass@1 或 reward 的 benchmark 很难指导工程修复。

### 2.4 Harness

Harness 是模型外部可编辑的执行表面，包括系统提示、工具描述、工具实现、中间件、技能、子智能体配置和长期记忆。Agentic Harness Engineering 的贡献在于把 harness 从手工经验对象变成可观测、可回滚、可演化的工程对象。它提出组件可观测性、经验可观测性和决策可观测性三根支柱：组件必须文件化，轨迹经验必须被压缩成可消费证据，编辑决策必须带有可证伪预测。

这一方向改变了“失败归因”的责任边界。很多失败不应简单归咎于模型能力，而可能来自工具描述含糊、中间件缺失、技能不可发现、记忆污染或系统提示与工具行为不一致。Harness 作为可编辑表面，使智能体改进从“换更强模型”扩展到“改造模型外部工作环境”。

### 2.5 审计轨迹与成本归因

审计轨迹面向责任追踪、合规和事后取证，要求完整性、时间顺序、身份绑定、敏感信息控制和防篡改能力。Agent Audit Trail 草案、AutoGen tamper-evident audit trail RFC、OWASP agentic security 材料和多篇治理文章都指出：智能体日志如果可以被管理员事后随意修改，就难以成为合规证据。

成本归因则把 token、模型调用、工具调用、重试、缓存、失败和多智能体依赖链连接起来。Token economics 相关材料显示，智能体任务的 token 消耗可能远高于单轮调用，且不同运行间方差很大。成本因此不是财务尾项，而是运行时信号：长上下文膨胀、失败重试、工具循环和多智能体低效协作都会首先体现在成本曲线上。

---

## 3. 五层架构：智能体可观测性的系统分解

### 3.1 轨迹证据层

轨迹证据层回答“发生了什么”。它需要捕获模型输入输出、工具调用、工具返回、状态读写、环境变化、用户反馈、失败标签和评测结果。与传统日志相比，它的重点不是单条事件，而是事件序列中可复原的任务路径。

这一层的最低要求是可重放和可查询。OpenClaw 的 JSONL 本地会话日志、Hermes 的 ShareGPT-like trajectory、Claude Code 的 OTel events、Coze 的全链路调试、AgentLoop 的应用观测、Llama Stack 与 MCP 相关 tracing 实践都体现了这一点。不同系统的差异主要在于轨迹是否开放、是否标准化、是否能跨平台导出，以及是否保留足够语义。

轨迹证据层的主要风险是“记录很多，但不可诊断”。大量非结构化消息并不能自动告诉开发者哪里错了。若缺乏 agent 身份、工具 schema、状态变化、父子 span、call id、策略版本和任务上下文，后续诊断器只能做文本猜测。

### 3.2 Schema 与插桩层

Schema 与插桩层回答“如何把发生的事情标准化”。OpenTelemetry 正在成为传输和关联骨架，OpenInference 尝试补足 LLM/agent 语义，AgentTrace 给出 agent 行为三表面结构，Hermes 和 ACL/EMNLP 相关工作体现训练数据格式需求。云平台和产品工具则倾向于在 OTel 之上添加自有字段、UI 和数据存储。

这里的关键矛盾是通用性与语义保真。只用 OTel span 可以获得生态互通，但容易丢失智能体特有语义，例如意图、计划、工具语义、记忆读写、handoff、子 agent 生命周期、过程规范和失败类别。只用自定义 schema 可以保留语义，但会削弱跨平台工具复用。更合理的路径是：用 OTel 处理 trace id、span id、parent-child、上下文传播和后端生态；用 agent-specific 属性承载诊断语义。

MCP tracing 是这一矛盾的典型场景。MCP 统一了工具协议，但不自动保证 trace 上下文传播。Red Hat、MintMCP、OneUptime 和社区提案都说明，MCP server 内部执行若不向客户端回传 span 或 trace id，工具调用仍然是黑盒。未来 MCP 是否纳入标准化 telemetry 扩展，将直接影响跨工具 agent 可观测性的上限。

### 3.3 诊断与归因层

诊断与归因层回答“为什么失败，应该修哪里”。AgentRx、Who&When、DoVer、HORIZON、AgentDiagnose、MASPrism、GUIDE、EAGER、OpsAgent、SeqCV 等工作从不同角度推进这一层。

这一层至少包含四类方法。第一类是约束驱动诊断，用工具 schema、领域策略和提示规范定义可检查条件，例如 AgentRx。第二类是数据集和分类法驱动诊断，用人工标注失败轨迹训练或评估模型，例如 Who&When、HORIZON 和 AgentDiagnose。第三类是干预式诊断，通过改变步骤、替换输出或验证依赖来确认根因，例如 DoVer。第四类是信号驱动轻量诊断，用 NLL、attention、执行 trace 表征或程序语义特征降低诊断成本，例如 MASPrism 和执行轨迹语义相关工作。

该层尚未成熟的原因有三点。第一，失败分类法碎片化。AgentRx、Who&When、HORIZON、HarnessAudit、AgentDiagnose 和各类产品平台使用的失败类别并不统一。第二，长轨迹中的因果链容易断裂，LLM-as-judge 在长上下文下会混淆根因与后果。第三，多智能体失败的责任边界不清晰，错误可能跨 agent、跨工具和跨共享状态传播。

### 3.4 过程评测与治理层

过程评测与治理层回答“行为是否被允许、是否可追责、是否可验证”。AgentPex、Monitoring Monitorability、OpenAI 的 CoT monitorability blog、Anthropic alignment auditing agents、HarnessAudit、AgentPro、AgentVerify、Agent Audit Trail、OWASP ASI、AutoGen audit RFC 等材料都属于这一层。

这一层和诊断层的差别在于目标。诊断层关注失败发生后的修复；过程评测和治理层关注行为是否符合规范，即使最终任务成功也可能判为风险。AgentPex 证明，过程规范分数与最终 reward 有相关性但不等价。HarnessAudit 把安全评估单元从最终输出移动到完整执行轨迹。Monitoring Monitorability 和 alignment auditing agents 进一步说明，很多危险行为需要在过程层面观察，不能只依赖最终输出分类器。

治理层还引入防篡改、身份、时间戳、策略版本和 SIEM 集成等要求。这些要求会反过来约束 trace schema：如果日志需要作为证据，字段就不能只为调试便利而设计，还必须支持证明“谁在何时依据哪个规则允许了哪个动作”。

### 3.5 生产平台与经济层

生产平台与经济层回答“如何落地、如何运营、如何控制成本”。Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、LangSmith、Datadog、Splunk、Elastic、New Relic、AWS Bedrock AgentCore、Google ADK / Vertex AI、阿里云 AgentLoop、百炼、百度千帆和 Coze Loop 都展示了不同产品路线。

这一层的共同趋势是从 tracing 工具走向“观测 + 评估 + 数据集 + 实验 + 成本 + 治理”的平台化。Langfuse 强调开源、自托管、trace、prompt、eval、dataset 闭环。Arize Phoenix 和 OpenInference 强调开放 instrumentation 与评估。Braintrust 强调 eval、trace 查询和团队工作流。Helicone 以 proxy/gateway 进入请求、缓存和成本管理。Datadog、Splunk、Elastic、New Relic 则把 agent telemetry 接入已有 APM 和企业运维栈。中国云厂商和低代码平台更强调应用观测、节点级调试、BadCase 回流和数据飞轮。

生产平台层的风险是 dashboard 先行、schema 滞后。很多产品能展示漂亮的 trace timeline、成本曲线和错误率，但没有暴露足够语义字段支持跨平台诊断、自动归因和审计证明。评价产品成熟度时，不应只看 UI，而应看是否支持原始轨迹导出、OpenTelemetry/OpenInference 对齐、敏感字段控制、跨 agent span 传播、评测数据回流和成本 drill-down。

---

## 4. 六个核心观点

### 4.1 智能体可观测性不是日志收集

日志收集只是必要条件，不是充分条件。一个系统可以记录所有消息，却仍然无法回答为什么失败。AgentRx、AgentTrace、AgentDiagnose 和多篇工程材料共同说明，可观测性必须把轨迹转化为可诊断、可评测、可审计的证据。

这意味着可观测平台需要三个额外能力。第一，结构化：事件必须带有 agent、tool、state、span、task 和 policy 上下文。第二，解释性：系统应能把事件映射到失败类别、规范违反或成本异常。第三，闭环：诊断结果应能回流到 prompt、tool schema、harness、评测数据集或安全策略。

### 4.2 最终奖励不足以评估智能体

AgentPex 是最清晰的证据：最终任务成功可能掩盖过程违规。HarnessAudit、AgentPro、Monitoring Monitorability 和 alignment auditing materials 也指向同一问题：智能体评估不能只看最终答案，而应同时看执行路径是否合规、是否安全、是否可解释、是否可复现。

未来 benchmark 应报告至少四类指标：最终任务结果、过程规范得分、失败归因准确率和资源/成本效率。单一 pass@1 会把“偶然成功”“违规成功”和“稳健成功”混在一起。

### 4.3 Schema 决定产品边界

Schema 不是后端细节，而是产品能力边界。若 schema 只记录 prompt、completion、latency、tokens，那么产品只能做 LLM 请求监控。若 schema 能表达 agent、tool、handoff、memory、state、policy、eval、cost 和 audit chain，平台才可能支持完整 agent observability。

OpenTelemetry 与 OpenInference 的关系应被理解为骨架与语义层。OTel 提供 trace 传播和后端生态，OpenInference/AgentTrace/Hermes/AAT 等格式提供 agent-specific 语义。谁能把二者稳定结合，谁就更可能成为跨框架事实标准。

### 4.4 Harness 是可优化的工程表面

Agentic Harness Engineering 把智能体可靠性问题从“模型是否足够强”转移到“模型外部工作环境是否可改进”。系统提示、工具描述、工具实现、中间件、技能、子智能体和长期记忆都是可编辑对象。轨迹证据不仅用于诊断失败，也可用于自动演化 harness。

这一观点对工程实践很重要：当 agent 失败时，修复动作不应只有换模型和改 prompt。更常见的修复可能是收紧工具 schema、增加中间件、拆分技能、改写记忆策略、约束子 agent 或修改 evaluation harness。

### 4.5 审计能力需要防篡改证据链

审计日志和调试日志目标不同。调试日志追求信息充分；审计日志追求证据可信。受监管智能体系统需要记录身份、策略版本、动作、结果、时间戳、敏感字段处理和完整性证明。AAT、AutoGen RFC、SIEM 集成和 OWASP agentic security 材料都说明，审计能力不是在事故后整理日志，而是在动作发生时生成证据链。

这会推动可观测系统引入签名、hash chain、Merkle tree、WORM storage、OPA 策略记录和访问审计。它也会加剧隐私与诊断之间的张力：越完整的轨迹越有助于复盘，但也越可能包含敏感数据。

### 4.6 成本是可观测性信号

Token 成本、工具调用成本、重试成本和缓存命中率正在成为 agent observability 的核心指标。成本异常往往意味着系统行为异常：上下文无限膨胀、工具循环、失败重试、agent 间重复工作、检索不命中或模型路由错误。

因此，成本分析不能停留在月度账单。生产平台应支持按任务、用户、agent、工具、模型、失败类别和 trace 片段 drill down。更合理的指标不是单次调用成本，而是单次成功任务成本、单位质量成本和失败样本浪费成本。

---

## 5. 关键对比

### 5.1 失败诊断、过程合规与结构化日志

| 维度 | 失败诊断 | 过程合规 | 结构化日志 |
|---|---|---|---|
| 核心问题 | 哪里失败、为什么失败 | 是否按规范行动 | 发生了什么、如何复现 |
| 典型输入 | 失败轨迹、工具约束、人工标注 | 系统提示、工具 schema、完整轨迹 | 消息、工具调用、状态、span |
| 典型输出 | 关键失败步骤、失败类别、责任主体 | 多维合规评分、违规类型 | 结构化事件、可查询 trace |
| 适用阶段 | 失败后调试与 benchmark 分析 | 持续评测与治理审计 | 运行时采集与离线分析基底 |
| 代表工作 | AgentRx、Who&When、DoVer、GUIDE | AgentPex、Monitoring Monitorability、HarnessAudit | AgentTrace、OpenInference、OTel、Hermes |

三者不能互相替代。结构化日志是底座，过程合规是规范检查，失败诊断是根因解释。只做日志会停留在“可看见”；只做合规会知道违规但未必知道如何修；只做诊断而没有稳定 schema 则难以规模化。

### 5.2 学术论文与产品材料

| 维度 | 学术论文 | 产品/工程材料 |
|---|---|---|
| 关注对象 | 失败机制、归因任务、评测基准、形式化定义 | SDK 接入、dashboard、告警、成本、团队流程 |
| 证据形态 | 数据集、实验、消融、统计指标 | 文档、集成示例、架构图、客户案例 |
| 优势 | 问题定义清晰，能比较方法效果 | 贴近生产需求，暴露部署约束 |
| 盲区 | 部署成本和组织流程不足 | schema 细节和可复现实验不足 |
| 综述用法 | 概念和方法基准 | 工程需求和落地证据 |

这两类材料必须合读。只读论文会低估平台接入、权限和成本问题；只读产品材料会高估 dashboard 对失败诊断的帮助。

### 5.3 OpenTelemetry 与 Agent-specific Schema

| 维度 | OpenTelemetry | Agent-specific Schema |
|---|---|---|
| 擅长 | 跨服务 trace、span 传播、指标/日志生态、厂商集成 | 意图、计划、工具语义、记忆、推理步骤、规范和失败类别 |
| 不足 | 容易丢失 agent 任务语义 | 容易碎片化，生态互通弱 |
| 最佳组合 | OTel 作为传输和关联骨架 | agent-specific 字段作为诊断语义层 |

未来成熟方案大概率不是二选一，而是“OTel + agent semantic conventions + 可控隐私策略”。

### 5.4 单智能体失败与多智能体失败

| 维度 | 单智能体失败 | 多智能体失败 |
|---|---|---|
| 失败边界 | 单条轨迹内的步骤、工具和状态 | 多个角色之间的消息、依赖和共享状态 |
| 主要根因 | 工具参数错误、计划偏离、误读观察、输出不合规 | 通信丢失、角色职责混淆、依赖传播、冲突决策 |
| 归因难点 | 第一个不可恢复步骤不唯一 | 责任可能跨 agent 和时间扩散 |
| 所需 trace | 步骤级消息和工具调用 | agent 身份、交互边、依赖链、共享资源访问 |
| 代表材料 | AgentRx、AgentPex、AgentSight | Who&When、Why Do Multi-Agent LLM Systems Fail、EvoCF、MASPrism |

多智能体系统不是单智能体 trace 的简单拼接。它需要显式表示 agent 身份、handoff、依赖关系和共享状态，否则失败归因会被压扁成单条日志流。

### 5.5 运行时监控与离线分析

| 维度 | 运行时监控 | 离线分析 |
|---|---|---|
| 目标 | 及时发现异常、告警、限流或阻断 | 解释失败、比较模型、生成证据和改进系统 |
| 延迟要求 | 低延迟、低开销、可在线执行 | 可接受批处理和较高 judge 成本 |
| 数据粒度 | 核心 span、指标、错误和抽样日志 | 完整轨迹、原始上下文、标注和实验结果 |
| 常见方法 | OTel、eBPF、SDK 插桩、dashboard | AgentRx、AgentPex、AHE、benchmark 分析 |
| 取舍 | 实时性优先，解释可能较浅 | 解释性优先，成本和隐私压力更高 |

生产系统需要二者配合。运行时监控负责及时发现和止损，离线分析负责系统性修复和知识沉淀。

---

## 6. 方法谱系

### 6.1 轨迹记录与标准化

AgentTrace、OpenInference、Hermes trajectory format、AAT 草案、OpenTelemetry GenAI 语义约定和各平台 SDK 构成了轨迹记录与标准化谱系。该谱系的主要问题是如何在互操作性、隐私和诊断语义之间取得平衡。

AgentTrace 的价值在于强调 agent 行为不能只用普通 request span 表示。OpenInference 的价值在于把 LLM/agent 应用接入 OTel 生态。Hermes 的价值在于从训练数据角度强制轨迹格式一致。AAT 的价值在于把审计和合规需求提前纳入日志结构。它们分别服务不同下游，但最终会在同一个生产系统中相遇。

### 6.2 失败诊断与根因定位

AgentRx 是约束驱动诊断的核心代表；Who&When 形式化了多智能体失败主体和时间定位；DoVer 强调通过干预验证归因；HORIZON 把长程任务失败拆成可比较维度；AgentDiagnose 通过 toolkit 和可视化支持轨迹质量分析；MASPrism 和执行轨迹语义工作展示了轻量模型和结构化信号的可能性。

这一谱系的长期目标是把人工读日志变成半自动或自动诊断。但短期内更现实的定位是“放大工程师的注意力”：先筛出关键步骤、可疑 agent、违规工具调用和高价值失败样本，再由人确认修复。

### 6.3 过程评测与自动监督

AgentPex、AgentPro、HarnessAudit、Monitoring Monitorability、alignment auditing agents、Detecting Safety Violations Across Many Agent Traces 和相关安全评测材料构成过程评测谱系。它们共同反对只看最终结果。

过程评测的挑战是 judge 可靠性和规范抽取质量。提示和工具 schema 写得越清楚，过程规范越容易抽取；业务规则越隐含，judge 越可能不稳定。未来系统可能需要把“可评测性”作为 prompt/tool/harness 设计要求：规范如果不能被机器检查，就很难成为稳定治理机制。

### 6.4 Harness 演化与数据飞轮

Agentic Harness Engineering、Continual Harness、Lifting Traces to Logic、FLARE、Teaching Text Agents to Learn from Failure、AgentLoop、Coze Loop 和各类评估数据集材料共同构成“从 trace 到改进”的数据飞轮谱系。

这一谱系说明 trace 的最终价值不只是观察，而是改进。失败轨迹可以转化为训练数据、规则、技能、memory、prompt patch、tool schema patch 或 harness 组件变更。AHE 的“可证伪编辑契约”尤其重要：每次自动修改都应声明预期修复和潜在回退，下一轮用任务级结果验证。这比让 agent 自我解释“为什么改”更可靠。

### 6.5 安全、审计与合规

AgentVerify、OWASP ASI、Attack and Defense Landscape survey、Agent Audit Trail、AutoGen audit RFC、tamper-evident audit trail 和企业治理材料共同构成安全审计谱系。它们要求 trace 不只是可读，还要可信。

在这一谱系中，运行时监控、策略执行和审计记录必须联动。策略检查没有审计记录，无法证明执行过；审计记录没有防篡改，无法作为证据；防篡改记录没有语义字段，无法支持调查。智能体安全治理因此会推动 trace schema 变得更重、更严格。

### 6.6 产品平台与市场

Langfuse、Arize Phoenix、Braintrust、AgentOps、Helicone、LangSmith、Datadog、Splunk、Elastic、New Relic、AWS、Google、阿里云、百度、Coze 等材料构成产品平台谱系。它们之间的差异可以按四条轴看：开源与闭源、自托管与 SaaS、LLM/agent 专用与传统 APM 扩展、eval-first 与 monitoring-first。

产品层最重要的趋势是 eval 和 observability 的融合。传统 APM 关注延迟、错误和吞吐；LLM/agent 平台还必须关注输出质量、安全性、成本、提示版本、数据集和评测实验。只做 trace viewer 的工具会被平台化能力挤压。

---

## 7. 研究缺口

### 7.1 跨格式语义映射仍缺失

OpenTelemetry、OpenInference、AgentTrace、Hermes、ShareGPT、AAT、各产品自定义格式之间尚无稳定映射。没有这个映射，诊断器很难跨平台复用，benchmark 也难以比较。

### 7.2 失败分类法碎片化

AgentRx、Who&When、HORIZON、HarnessAudit、AgentDiagnose、AgentPex 和安全材料都有自己的类别体系。未来需要一套分层分类法：底层描述事件和工具错误，中层描述认知/计划/协作错误，高层描述业务和治理风险。

### 7.3 长轨迹与多智能体因果推断仍不可靠

长轨迹中错误传播路径长，后果和根因容易混淆。多智能体场景中，责任还可能跨 agent 边界传播。现有 LLM-as-judge 方法在这类场景中需要更多结构化辅助和干预验证。

### 7.4 过程评测依赖规范质量

AgentPex 类方法依赖系统提示和工具 schema 中可抽取的规范。真实业务常常把规则藏在文档、人工习惯和隐式流程中。如何把业务规范转成可检查规则，是过程评测落地的瓶颈。

### 7.5 隐私与诊断深度冲突

完整 trace 可能包含用户数据、企业机密、文件内容、内部推理和工具返回。masking、hash、采样和最小化记录会保护隐私，但也可能破坏诊断证据。当前材料对这一权衡讨论不足。

### 7.6 成本归因与质量归因尚未统一

成本平台能展示 token 和调用费用，评测平台能展示质量和失败，但二者经常分离。真正有用的指标应是“单位成功任务成本”“单位质量成本”“失败根因对应浪费成本”。这需要 trace、eval 和 billing 数据可 join。

### 7.7 自动修复缺少生产实证

AHE、Continual Harness、Lifting Traces to Logic 等工作显示 trace 可以驱动系统演化，但生产环境中自动修改 harness、prompt、tool 和 memory 的风险仍未充分评估。自动修复需要版本控制、预测声明、回滚机制和人类审批。

---

## 8. 面向系统设计的建议

1. 把 trace schema 作为产品/API 设计的一部分，而不是日志后处理格式。
2. 采用 OTel 作为传播骨架，同时保留 agent-specific 语义字段。
3. 每条工具调用至少记录工具名、参数摘要、返回摘要、错误、耗时、调用者 agent、父 span 和任务上下文。
4. 对多智能体系统显式记录 agent 身份、handoff、依赖边、共享状态访问和子 agent 侧链。
5. 将最终 reward、过程规范、失败类别、成本和安全事件写入同一 trace 关联域。
6. 对受监管场景区分调试日志和审计日志，审计日志要有身份、策略版本、时间戳和完整性保护。
7. 让失败样本进入数据飞轮：诊断、标注、评测集、prompt/tool/harness patch、回归测试。
8. 对自动修改建立可证伪变更契约：预期修复什么、可能破坏什么、如何回滚。
9. 产品选型时不要只看 dashboard，要检查原始轨迹导出、schema、隐私控制、eval 集成和成本 drill-down。
10. 对长轨迹和多智能体任务，不要只依赖单体 LLM judge；结合约束、干预、结构化信号和人工复核。

---

## 9. 结论

智能体可观测性正在形成一个新的基础设施层。它以轨迹为原始材料，但目标不是保存日志，而是生成可行动证据。这个证据层同时服务于五件事：运行时监控、失败诊断、过程评测、安全审计和成本归因。

117 篇本地笔记显示，学术界已经把 trace 分析从黑盒结果评估推进到步骤级归因、过程合规、长程失败机制和 harness 演化；产业界则把可观测性与 eval、dataset、prompt 管理、成本控制和合规集成到平台中。两条路线正在汇合。未来真正有价值的系统不是单点 trace viewer，而是能把 OpenTelemetry 生态、agent-specific schema、自动诊断、过程评测、审计证据和数据飞轮连接起来的综合平台。

因此，智能体可观测性的核心问题可以概括为一句话：如何把不可预测的智能体执行过程，转化为可复现、可解释、可验证、可审计、可改进的工程证据。这个问题将决定 2026 年以后 agent 系统能否从演示走向可靠生产。
