---
tags:
  - trajectory-format
  - ShareGPT
  - JSONL
  - training-data
  - tool-normalization
  - Hermes-Agent
  - Nous-Research
  - reinforcement-learning
  - HuggingFace-datasets
  - agent-debugging
aliases:
  - "c-013"
  - "Hermes Agent 轨迹格式"
date: 2026-03-30
url: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/trajectory-format
---

# Trajectory Format | Hermes Agent

## 核心信息

- **标题**: Trajectory Format | Hermes Agent
- **作者**: Nous Research（Hermes Agent 开发团队）
- **发布日期**: 2026-03-30
- **来源类型**: 框架官方文档（Framework documentation）
- **URL**: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/trajectory-format
- **source_id**: c-013
- **PDF**: `[c-013]-hermes-agent-trajectory-format.pdf`
- **证据质量**: high

## 内容摘要

本文是 Nous Research 旗下 Hermes Agent 框架的官方开发者文档，详细规定了 agent 对话轨迹的保存格式、文件命名约定、JSONL 条目结构、内容归一化规则，以及轨迹数据的加载与训练对接方法。该文档的核心目标是为训练数据生成、调试产物归档和强化学习数据集构建提供一套标准化、可复现、与开源生态兼容的轨迹格式规范。

在文件命名方面，Hermes Agent 根据对话的完成状态将轨迹写入不同的文件：成功完成的对话保存至 trajectory_samples.jsonl，失败或被中断的对话保存至 failed_trajectories.jsonl。当使用批量运行器（batch_runner.py）时，轨迹会按批次写入自定义输出文件（如 batch_001_output.jsonl），并附带额外的元数据字段。用户也可以通过 save_trajectory() 函数的 filename 参数覆盖默认文件名。在 CLI 模式下，轨迹保存受 config.yaml 中 agent.save_trajectories 配置项或 --save-trajectories 命令行标志控制；而批量运行器则始终保存轨迹，因为其核心目的就是生成训练数据。批量运行器还会自动丢弃所有轮次中均不含推理内容的样本，以避免污染训练数据。这一设计体现了训练数据工程中的"质量优先"原则：与其保存大量低质量样本，不如严格筛选确保每一条数据都对模型训练有正面贡献。

JSONL 条目存在两种变体。CLI 与交互式格式（来自 _save_trajectory）包含 conversations 数组、timestamp 时间戳、model 模型标识和 completed 完成状态。批量运行器格式在此基础上扩展了 prompt_index、metadata（包含 prompt_source 和 difficulty 等字段）、partial 部分完成标记、api_calls API 调用次数、toolsets_used 使用的工具集列表、tool_stats（各工具的使用次数、成功次数和失败次数），以及 tool_error_counts（各工具的错误次数）。特别值得注意的是，tool_stats 和 tool_error_counts 字典会被归一化，包含所有可能的工具（来自 model_tools.TOOL_TO_TOOLSET_MAP）并以零作为默认值，从而确保所有条目具有一致的 schema，避免在加载 HuggingFace 数据集时出现 Arrow schema 不匹配错误。这种 schema 一致性的保障对于大规模训练数据流水线至关重要。

对话数组采用 ShareGPT 的角色约定，将 API 中的角色映射为 system、human、gpt、tool 四种 from 值。这一设计使得 Hermes Agent 的轨迹数据可以直接与 ShareGPT 生态中的训练流程对接，无需额外的角色转换层。ShareGPT 格式作为开源社区广泛接受的标准，其兼容性优势意味着 Hermes 的轨迹数据可以被直接用于多种主流训练框架，包括 Axolotl、LLaMA-Factory 和 transformers 库的数据加载器。

在内容归一化方面，文档规定了详尽的转换规则。对于推理内容，轨迹转换器将所有模型的推理输出统一归一化为 <think> 标签格式：原生思考令牌（如 Anthropic 和 OpenAI o-series 的 reasoning 字段）被包装为 <think>\n{reasoning}\n</think>\n 并前置到内容之前；当原生思考被禁用时，模型通过系统提示产生的 REASONING_SCRATCHPAD XML 标签会通过 convert_scratchpad_to_think() 函数转换为 <think> 格式；此外，每个 gpt 轮次都保证包含一个 <think> 块，即使未产生推理内容也会插入空的 <think>\n</think>\n，以确保训练数据格式的一致性。这种强制归一化消除了不同模型提供商在推理输出格式上的差异，使得训练数据可以在不同模型架构之间迁移使用。

对于工具调用，API 格式的 tool_call_id、函数名和 JSON 字符串参数被转换为 XML 包裹的 JSON 对象：<tool_call>{"name": "terminal", "arguments": {"command": "ls -la"}}</tool_call>。参数从 JSON 字符串解析回对象，避免双重编码；如果解析失败则使用空对象 {} 并记录警告；单次助手轮次中的多个工具调用会在同一条消息中生成多个 <tool_call> 块。对于工具响应，所有跟随在助手消息之后的工具结果被归并为单一的 tool 轮次，使用 <tool_response> XML 标签包裹 JSON 响应对象。如果工具内容看起来像 JSON（以 { 或 [ 开头），则会被解析为对象或数组而非字符串；多个工具结果会在同一消息中以换行符连接。

系统消息在保存时动态生成，而非直接取自对话历史。它遵循 Hermes 的函数调用提示模板，包含函数调用协议的前言说明、<tools> XML 块中的 JSON 工具定义、FunctionCall 对象的 schema 引用，以及 <tool_call> 示例。工具定义包含 name、description、parameters 和 required 字段（required 设为 null 以匹配规范格式）。动态生成系统消息的策略确保了训练样本中的工具定义始终与轨迹中实际调用的工具保持一致，即使工具集在对话过程中发生了变化。

在数据加载方面，文档提供了标准 Python 代码示例，展示如何通过 json 模块逐行读取 JSONL 文件，并筛选 completed 为 true 的成功条目。对于 HuggingFace 生态，文档展示了如何使用 load_dataset("json", data_files="...") 直接加载轨迹文件，并强调归一化的 tool_stats schema 对于避免 Arrow schema 不匹配的重要性。这种与 HuggingFace Datasets 库的无缝对接，显著降低了从轨迹数据到训练流水线的工程门槛。

## 关键要点

1. **双轨文件分流策略按完成状态隔离数据质量**
   - trajectory_samples.jsonl：成功完成的对话（completed=True）。
   - failed_trajectories.jsonl：失败或中断的对话（completed=False）。
   - batch_runner.py 输出：按批次命名的自定义文件（如 batch_001_output.jsonl），包含丰富的训练元数据。
   - 用户可通过 save_trajectory() 的 filename 参数自定义输出文件名。

2. **两种 JSONL 格式分别服务于交互调试和批量训练**
   - CLI/交互式格式：包含 conversations、timestamp、model、completed 四个核心字段。
   - 批量运行器格式：额外包含 prompt_index、metadata、partial、api_calls、toolsets_used、tool_stats、tool_error_counts。
   - 批量格式中的 metadata 可携带 prompt_source 和 difficulty 等自定义字段，支持按难度和来源进行数据分层采样。

3. **Schema 归一化是训练数据工程的关键基础设施**
   - tool_stats 和 tool_error_counts 字典强制包含所有可能的工具条目，未使用的工具以零值填充。
   - 归一化来源：model_tools.TOOL_TO_TOOLSET_MAP 定义的工具全集。
   - 目的：确保 HuggingFace Datasets 加载时不会出现 Arrow schema mismatch 错误。
   - 这一设计体现了"上游修正优于下游兼容"的数据工程原则。

4. **ShareGPT 角色约定确保开源生态兼容性**
   - system → "system"
   - user → "human"
   - assistant → "gpt"
   - tool → "tool"
   - 直接兼容 Axolotl、LLaMA-Factory 等主流训练框架的数据加载器。

5. **推理内容的三层归一化策略**
   - 原生 thinking tokens（msg["reasoning"]）：包装为 <think> 标签并前置到内容前。
   - REASONING_SCRATCHPAD XML（禁用原生思考时）：通过 convert_scratchpad_to_think() 转换。
   - 空推理保障：每个 gpt 轮次强制包含 <think> 块，无推理时插入空块 <think>\n</think>\n。
   - 效果：消除不同模型提供商的推理格式差异，实现训练数据的模型无关性。

6. **工具调用的 XML-wrapped JSON 表示**
   - 工具调用：转换为 <tool_call>{"name": ..., "arguments": ...}</tool_call> 格式。
   - 参数解析：从 JSON 字符串还原为对象，避免双重编码；解析失败时回退到空对象 {}。
   - 多工具调用：单次 assistant 消息中可包含多个 <tool_call> 块。
   - 工具响应：归并为单一 tool 轮次，使用 <tool_response> 标签包裹。
   - JSON 内容识别：以 { 或 [ 开头的工具内容会被解析为对象/数组而非纯字符串。

7. **系统消息动态生成确保工具定义一致性**
   - 保存时重新渲染 Hermes 函数调用模板，而非复用对话历史中的旧 system message。
   - 包含：协议前言、<tools> 块、FunctionCall schema、<tool_call> 示例。
   - 工具定义字段：name、description、parameters、required（设为 null 匹配规范）。
   - 优势：即使工具集随时间演进，历史轨迹中的工具定义仍与实际调用保持一致。

8. **数据加载与训练生态无缝对接**
   - 标准 Python json 模块逐行读取，筛选 completed=true 的成功样本。
   - HuggingFace datasets 库直接通过 load_dataset("json", data_files=...) 加载。
   - 支持从轨迹中提取 conversations 数组作为纯训练数据。
   - 批量运行器自动过滤零推理样本，防止非推理样本污染训练集。

9. **轨迹格式设计的核心哲学：训练优先、一致至上、生态兼容**
   - 所有归一化规则的首要目标都是消除数据异质性，确保训练数据的格式一致性。
   - ShareGPT 兼容性使得 Hermes 的轨迹可以直接接入已有的开源训练基础设施。
   - HuggingFace Datasets 的 Arrow schema 兼容性通过 tool_stats 归一化得到保障。
   - 这种设计体现了"数据格式即接口"的工程思想：格式规范定义了 agent 运行时与训练流水线之间的契约。

## 与综述的关联

本来源是综述中"agent 轨迹格式标准化"与"训练数据工程"章节的重要参考材料。与学术文献中侧重算法和评估指标的讨论不同，本文提供了一个完整的生产级轨迹格式规范，展示了如何将 agent 的运行时交互转化为可用于监督微调和强化学习的结构化数据。

在轨迹格式层面，Hermes Agent 的 ShareGPT-compatible JSONL 设计体现了与开源训练生态的兼容性优先策略。这与 AgentTrace [c-011] 提出的 JSONL + OpenTelemetry spans 双路径存储方案形成有趣的对比：Hermes 专注于训练数据格式的一致性和归一化，而 AgentTrace 侧重于运行时观测与事后分析的灵活性。综述可以在"轨迹存储格式"的比较框架中纳入这两种设计哲学——训练导向的严格归一化 vs. 观测导向的双模存储。这种对比有助于读者理解不同场景下轨迹格式的选型依据：如果主要目标是生成训练数据，Hermes 的严格归一化方案更为合适；如果主要目标是生产监控和故障排查，AgentTrace 的双模方案更具优势。

在工具调用表示方面，Hermes 的 XML-wrapped JSON 方案（<tool_call> 和 <tool_response>）是一种介于纯文本和结构化数据之间的折中设计。它保留了人类可读性（XML 标签明确标示语义角色），同时保持了机器可解析性（内部为合法 JSON）。这种表示方式与 OpenAI 的 Chat Completions API 工具格式、以及 Claude 的 function calling 格式均不相同，综述可以将其作为"agent 工具调用序列化格式多元化"的一个实例。特别是在多 agent 系统或跨框架迁移场景中，不同工具表示之间的转换开销是一个被低估的工程问题。Hermes 选择 XML 而非原生 JSON 结构的原因可能与其训练目标的设计有关：统一语言建模损失函数要求所有输出都以文本形式表达，而 XML 标签提供了一种在文本中嵌入结构化信息的轻量级机制。

在数据质量工程方面，批量运行器自动过滤零推理样本的机制，以及 tool_stats 的完整字典归一化策略，反映了从"记录数据"到"构建可训练数据集"之间的工程鸿沟。许多 agent 框架可以记录轨迹，但未必能直接产出可用于模型训练的高质量数据。Hermes 的设计提示我们：轨迹格式规范不仅要考虑"记录什么"，还要考虑"下游消费方需要什么"。这与综述中关于"agent 可观测性应服务于全生命周期（开发、调试、评估、训练）"的观点高度一致。此外，系统消息的动态生成策略（基于当前工具集重新渲染）揭示了 agent 轨迹的一个微妙但关键的问题：对话历史中的 system message 可能随时间发生变化（工具集增减、提示词版本更新），如果直接保存历史 system message，训练数据中的工具定义可能与实际可用的工具不一致。Hermes 选择在保存时重新生成 system message，确保训练样本中的工具定义始终与轨迹中的工具调用保持一致。这一细节对于构建可复现的训练数据集至关重要，但往往在学术讨论中被忽视。综述在讨论"agent 训练数据的可复现性"时，可以将这一策略作为最佳实践进行推荐，并指出忽略该问题可能导致训练数据与推理时环境之间的工具定义漂移（tool definition drift）。

## 我的笔记

Hermes Agent 的轨迹格式文档是我目前见过的最详尽的训练数据工程规范之一。它的价值不仅在于定义了一种格式，更在于展示了一个完整的"从运行时到训练集"的数据流水线设计。其中最令我印象深刻的是推理内容的归一化策略——通过强制每个 gpt 轮次包含 <think> 块，即使模型未产生显式推理，也保证了训练数据在格式上的绝对一致性。这种"宁缺勿滥"的严格性对于大规模预训练或微调至关重要，因为数据格式的不一致是导致训练失败或性能退化的常见原因。在分布式训练环境中，如果不同 worker 加载的数据具有不同的字段结构或内容格式，不仅会导致训练崩溃，还可能引入难以察觉的模型行为偏差。

工具调用的 XML-wrapped JSON 表示是一个值得深入分析的设计选择。与 OpenAI API 中工具调用作为独立消息对象的方案相比，Hermes 的方案将工具调用嵌入在 assistant 消息的文本内容中。这种设计的优势在于：它统一了"文本生成"和"工具调用"两种输出模式，模型始终生成文本，而工具调用只是文本中的特殊结构。这简化了训练目标的定义（统一的语言建模损失），但也可能增加了解析的复杂度——需要在文本中准确地提取 XML 块。在综述中讨论 agent 输出格式时，可以对比 Hermes 的 XML 方案、OpenAI 的 JSON schema 约束方案、以及纯 function calling API 方案各自的 trade-offs。特别是在评估不同格式的鲁棒性时，XML 方案对于解析错误的容忍度可能高于严格的 JSON schema 方案。

tool_stats 的完整字典归一化是一个看似微小但极具工程智慧的决策。Arrow schema 不匹配是 HuggingFace Datasets 用户经常遇到的痛点，当不同样本包含不同的列（例如某些样本使用了 terminal 工具而另一些没有）时，加载会失败。通过在保存时就确保所有工具都有条目（计数为零），Hermes 彻底消除了这一问题的根源。这体现了"上游修正优于下游兼容"的数据工程原则。在实际的大规模训练数据生产环境中，这种上游一致性保障可以节省大量的数据清洗和格式转换时间。对于需要处理数百万条轨迹的预训练项目而言，任何下游的数据修复操作都可能消耗巨大的计算资源和时间成本，因此 Hermes 的"保存时即正确"原则具有显著的规模化优势。

关于批量运行器自动丢弃零推理样本的机制，我认为这是一个非常务实的数据清洗策略。在 agent 的自我对弈或大规模批量运行中，模型有时会选择直接回答而不经过显式推理（尤其当问题非常简单时）。这些样本对于训练推理能力可能没有价值，甚至会产生负面作用。然而，我也注意到这一策略可能引入选择偏差：如果过滤条件过于严格，可能会丢失那些"直觉式正确回答"的有用样本。在实际应用中，可能需要根据训练目标动态调整过滤阈值。例如，如果训练目标是提升工具使用能力，那么保留无工具调用的简单回答样本可能是有益的；但如果训练目标是强化多步推理能力，则应严格过滤无推理样本。综述在讨论"训练数据质量控制"时，可以将 Hermes 的过滤机制作为一个基准方案，同时探讨更细粒度的质量评分模型（如基于 outcome 成功率、推理步数、工具使用多样性等维度的综合评分）。

文档中提到的"系统消息动态生成"策略对于综述的"可复现性"讨论具有重要意义。在 agent 系统的长期运行中，工具集和提示词模板往往会演进，如果训练数据保存的是当时的 system message 快照，那么当工具定义发生变化后，这些历史样本中的工具描述可能与最新代码不匹配。Hermes 的"保存时重新渲染"策略确保了数据的一致性，但也意味着保存操作需要访问当前的工具注册表，这在离线处理历史轨迹时可能是一个限制。例如，如果工程师希望在不启动完整 agent 环境的情况下批量转换历史日志，可能需要额外提供一个离线工具定义快照。

最后，我想指出该文档的一个潜在改进空间：虽然它详细描述了轨迹的保存格式和加载方法，但对于如何从这些轨迹中构建真正的训练数据（例如，如何构造 SFT 的 input-output 对，或如何为 RLHF 准备 reward model 的偏好对）几乎没有涉及。这部分内容可能需要参考 Hermes Agent 的其他文档或相关的训练脚本。对于综述而言，这提示我们：轨迹格式只是数据工程的第一步，从原始轨迹到可训练数据之间还有大量的后处理、过滤和格式转换工作需要标准化。这些后处理步骤包括对话截断、质量评分、去重、敏感信息过滤和分布平衡等，每一步都对最终模型性能有重要影响。未来研究可以探索将轨迹自动转换为不同训练范式（SFT、RLHF、DPO、KTO）所需格式的标准化工具链。

综述在引用本文时，应特别强调的是：Hermes 的轨迹格式规范代表了一种"以训练为中心"的观测数据设计理念。这与以调试为中心的 AgentTrace、以合规为中心的 IETF Audit Trail 形成了鲜明的功能定位差异。理解这三种设计目标（训练、调试、合规）之间的张力，对于综述构建一个全面的 agent 可观测性分类体系具有重要意义。

## 局限性

- 文档仅描述了轨迹的保存格式和加载方法，未涉及从轨迹到训练数据的后处理流程（如 SFT 样本构造、RLHF 偏好对生成）。
- 对于 XML-wrapped JSON 的解析失败处理较为简单（回退到空对象），在高容错要求的生产环境中可能需要更精细的错误恢复策略。
- 文档假设读者熟悉 ShareGPT 格式和 HuggingFace Datasets 库，对于新手而言可能需要额外的背景知识补充。
- 动态生成系统消息的设计虽然保证了数据一致性，但增加了保存操作对工具注册表的运行时依赖，离线处理历史轨迹时可能面临工具定义不可用的困境。
- 批量运行器过滤零推理样本的机制虽然提升了数据质量，但可能引入选择偏差，过滤阈值的设定缺乏量化指导。
- 对于多模态 agent（涉及图像、音频等非文本输出），本文的轨迹格式未做定义，扩展性存在疑问。
- 文档未提供轨迹数据的质量评估指标或自动校验脚本，用户难以在保存后快速验证数据的完整性和正确性。
- 对于超长对话（如数百轮以上的复杂任务执行），轨迹文件的体积和加载性能可能成为实际工程瓶颈，文档未提供相应的分片或压缩策略。
- 轨迹格式未包含环境信息（如操作系统、依赖版本、agent 框架版本），这些因素可能影响模型行为的复现性。


## 术语表

| 术语 | 英文 | 说明 |
|------|------|------|
| 轨迹 | trajectory | agent 执行过程中的完整交互记录，包含对话轮次、工具调用和推理内容 |
| ShareGPT | ShareGPT | 开源社区广泛采用的对话数据格式标准 |
| JSONL | JSON Lines | 每行一个独立 JSON 对象的文本格式，支持流式处理 |
| Arrow schema | Arrow schema | Apache Arrow 列式存储的 schema 定义，HuggingFace Datasets 的底层格式 |
| 归一化 | normalization | 将不同来源或格式的数据转换为统一标准格式的过程 |
