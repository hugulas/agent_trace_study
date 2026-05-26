---
tags:
  - agent-observability
  - codex-cli
  - reverse-engineering
  - trace-format
  - runtime-tooling
  - coding-agent
  - causal-tracing
  - openai
  - deepseek
aliases:
  - Codex CLI rollout traces 逆向工程
  - a-015
date: 2026-05-14
url: https://dev.to/milkoor/reverse-engineering-codex-cli-rollout-traces-3b9b
---

# Reverse engineering Codex CLI rollout traces - DEV Community

## 核心信息

- **标题**: Reverse engineering Codex CLI rollout traces
- **作者**: MilkoorY
- **来源**: DEV Community
- **URL**: https://dev.to/milkoor/reverse-engineering-codex-cli-rollout-traces-3b9b
- **日期**: 2026-05-14
- **PDF**: `[a-015]-reverse-engineering-codex-cli-rollout-traces.pdf`
- **证据质量**: high

## 内容摘要

本文是作者 MilkoorY 对 OpenAI Codex CLI 实际运行过程中生成的 trace 文件进行逆向工程的技术博客，属于其 "coding agent runtime observability" 系列文章的第二篇。作者的核心动机是希望为 coding agent 构建可观测性工具，因此必须先理解 Codex CLI 的 trace 格式。然而，Codex CLI 原生基于 OpenAI 的 Responses API，而作者希望使用 DeepSeek 作为后端以生成真实的 trace 数据，这要求他首先解决 API 兼容性问题。

作者编写了一个翻译代理（`tools/codex_deepseek_proxy.py`），将 Responses API 的调用转换为 DeepSeek 支持的 Chat Completions 格式。这个代理的核心工作包括：在 `/v1/responses` 端点接收 POST 请求，将 Responses API 格式的 `input` 字段翻译为 Chat Completions 的 `messages` 格式，将工具定义从 `{"name": "bash", "parameters": {...}}` 转换为 `{"type": "function", "function": {"name": "bash", "parameters": {...}}}`，然后将 DeepSeek 返回的 Chat Completions 响应再翻译回 Responses API 的事件格式。由于 DeepSeek 的流式输出与 Codex CLI 不兼容，代理以 JSON body 而非 SSE stream 返回响应。代理实现中有一个至关重要的细节：Codex CLI 期望 `function_call` 条目的状态为 `"in_progress"` 而非 `"completed"`，因为 `"in_progress"` 告诉 Codex 工具已被调用但尚未完成，正在等待 `function_call_output` 到达；若设为 `"completed"`，Codex 会误判工具已执行完毕且没有输出。

在成功运行并生成 trace 数据后，作者开始解析 Codex CLI 存储在 `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` 路径下的 session 文件。这些文件以 JSONL 格式存储，每行是一个带有 `type` 和 `payload` 字段的 JSON 对象。作者最初基于 Codex CLI 源码（特别是 `protocol.rs`）预期的 event 类型包括：`exec_command_begin` 和 `exec_command_end`（命令执行边界）、`mcp_tool_call_begin` 和 `mcp_tool_call_end`（MCP 工具调用边界）、以及 `agent_reasoning`（模型内部推理）。基于这些假设构建的第一个解析器每个 session 只能产出 1 个 event，显然与实际严重不符。

通过直接 dump 原始 rollout 文件并对照 Codex CLI v0.130.0 验证，作者揭示了真实的 trace 格式。核心事件类型包括：`response_item/function_call`，表示模型请求调用工具，包含 `name`（工具名）、`arguments`（JSON 字符串格式的参数）和 `call_id`（唯一调用标识）；`response_item/function_call_output`，表示工具执行结果，通过相同的 `call_id` 与对应的 `function_call` 配对；`event_msg/agent_message`，承载模型的 reasoning 文本和 thinking blocks；`response_item/message`（`role=assistant`），模型的文本回复；以及 `event_msg/token_count`，记录 token 使用统计。值得注意的是，实际格式中完全没有 `exec_command_begin/end` 或 `mcp_tool_call_begin/end` 事件，源码中描述的这些事件类型在序列化后的 rollout 文件中并不存在。

作者进一步总结了三个令人惊讶的发现。第一，call_id 配对而非嵌套结构：工具调用与结果在事件流中是扁平的，通过 `call_id` 关联。`function_call` 行出现后，可能在若干行之后才出现匹配的 `function_call_output`，期间可能穿插 token_count 事件、reasoning 消息或其他工具调用。这意味着解析器必须维护一个 pending call 缓冲区，按 `call_id` 匹配而非假设 begin/end 嵌套。第二，token_count 无处不在：`event_msg/token_count` 事件几乎出现在每个有意义的事件之间，且没有固定规律——有时在工具调用前，有时在后，有时在 reasoning blocks 之间。它们对因果追踪来说是噪声，但解析器必须妥善处理以避免破坏事件链。第三，缺乏显式因果性：rollout 格式没有 `parent_event_id` 或等效因果字段，因果关系完全依赖时间顺序推断——模型收到 `function_call_output` 后决定下一步动作，因此输出之后的下一个 `function_call` 或 `agent_message` 在因果上依赖于该输出。这与 Copilot 和 Continue.dev 的 log-based tailer 使用的时间启发式方法相同。

基于这些发现，作者实现了一个开源解析器（`causetrace/hooks/codex_parser.py`），其核心逻辑为：`response_item/function_call` 创建 pending call 并追踪 call_id；`response_item/function_call_output` 按 call_id 匹配并更新对应事件的 tool_output；`event_msg/agent_message` 创建带有因果父链接的 reasoning 事件；`response_item/message`（assistant）创建响应文本事件。该解析器将 465 行的 rollout 文件成功解析为 116 个具有因果关联的事件，解析准确率从基于源码假设的接近 0% 提升到 100%。

文章最后提炼了对构建 coding agent 运行时工具的几条关键教训：不要轻信源码注释，要相信实际的 wire data；`call_id` 配对是 industry-wide 的重复模式，解析器设计应围绕缓冲区匹配而非嵌套解析；基于日志的因果推断是可行的 fallback 方案，但存在模糊性（无法 always 判断哪个 `function_call_output` 触发了哪个后续的 `function_call`）；事件流是异构的，token 统计、元数据和控制事件与功能事件混合，健壮解析器必须能在不假设固定事件序列的前提下区分信号与噪声。

## 关键要点

- Codex CLI 的 rollout trace 格式（v0.130.0）与源码（`protocol.rs`）中注释描述的格式存在显著不一致，实际格式采用扁平化的事件流设计。
- 真实的 trace 采用 `call_id` 配对机制连接 `function_call` 与 `function_call_output`，而非源码中暗示的 begin/end 嵌套事件结构。
- `event_msg/token_count` 事件高频且不规律地穿插在 trace 中，解析器需要将其作为噪声过滤，同时确保不破坏事件链的连续性。
- 该格式缺少显式的因果字段（如 `parent_event_id`），因果关系完全依赖时间顺序进行启发式推断。
- 作者通过编写 DeepSeek 翻译代理成功绕过了 Responses API 限制，验证了第三方后端接入 Codex CLI 的可行性，并生成了可用于分析的真实 trace 数据。
- 开源解析器项目 causetrace 实现了对真实 rollout 格式的完整解析，将 465 行原始日志转化为 116 个因果关联事件，准确率从 ~0% 提升至 100%。
- 核心工程教训：构建 agent 可观测性工具时，应以实际 wire data 为准，而非源码注释、文档描述或开发者的口头说明。
- 代理实现中的关键细节：function_call 状态必须为 `"in_progress"`，这是 Codex CLI 正确等待 function_call_output 的前提条件。
- 同一响应中模型可能同时返回文本（assistant message）和工具调用（function_call items），代理必须处理这种混合响应。
- 事件流的异构性（metadata、token counts、control events 与 functional events 混合）要求解析器具备鲁棒的信号提取能力。
- 从 465 行原始日志到 116 个因果事件的压缩比说明：原始 agent 日志包含大量冗余信息，结构化解析是提取可观测性信号的必要步骤。
- 作者指出 `protocol.rs` 中的事件类型可能是内部数据结构而非序列化格式，提醒开发者注意“代码中的类型定义”与“磁盘上的数据格式”之间的区别。
- 代理将 DeepSeek 的 Chat Completions 响应翻译回 Responses API 事件格式时，必须返回 JSON body 而非 SSE stream，因为 DeepSeek 的流式输出与 Codex CLI 不兼容。
- 工具定义的格式转换是代理的核心工作之一：从 Responses API 的 `{"name": "bash", "parameters": {...}}` 转换为 Chat Completions 的 `{"type": "function", "function": {"name": "bash", "parameters": {...}}}`。
- 时间顺序推断因果的方法在 Copilot 和 Continue.dev 的 log-based tailer 中也有应用，说明这是 industry 的通用 fallback 策略。
- 解析器设计中，pending call buffer 是处理 flat call_id 配对模式的关键数据结构。
- 事件链中的噪声（token_count、session_meta、turn_context）虽然对因果追踪无直接价值，但必须被正确识别和跳过。
- 本文验证了通过第三方模型后端（非 OpenAI）生成 Codex CLI 兼容 trace 的技术可行性，为多模型 agent 可观测性研究打开了可能性。
- 开源实现地址：https://github.com/milkoor/causetrace，包含 codex_parser.py 和 codex_deepseek_proxy.py 两个核心组件。
- 该系列的前一篇文章为 "Coding agents produce causal DAGs, not logs"，与本篇形成了从理论到实践的完整闭环。
- 实际 rollout 文件中的 `turn_context` 事件包含当前使用的模型标识（如 `deepseek-chat`），这对多后端场景的追踪具有重要价值。
- `session_meta` 事件包含 `model_provider` 和 `cli_version`，为 trace 的版本控制和来源识别提供了元数据基础。
- 解析器输出的 116 个因果关联事件构成了一个有向无环图（DAG），而非线性日志序列，这与作者前一篇博文的核心论点一致。
- 本文的研究方法（proxy → trace generation → format reverse engineering → parser implementation）可作为分析其他 agent 工具的标准化流程模板。
- Codex CLI 的 rollout 文件按日期目录组织（`YYYY/MM/DD`），便于按时间范围检索，但不支持按项目或仓库的自动分组。
- 代理实现中 Responses API 与 Chat Completions 的互转逻辑，对理解 OpenAI 两代 API 的设计差异具有教学价值。
- 本文也为研究 coding agent 的 "reasoning trace" 提供了原始数据格式的第一手资料，有助于理解模型思考过程的外部化表示。
- 逆向工程过程中发现的问题（源码与实际不符）具有普遍性，建议所有 agent trace 解析项目都建立自动化回归测试。

## 与综述的关联

这篇笔记对 AI agent 可观测性、tracing 和 debugging 的综述具有直接且多层次的实证价值。

首先，它揭示了当前主流 coding agent（Codex CLI）的 trace schema 存在“文档与实现脱节”的典型问题。这是 agent 可观测性领域普遍面临的挑战——工具开发者往往更关注功能迭代和模型能力，而非 trace 格式的稳定性、文档准确性和向后兼容性。综述可以将此作为“schema drift”问题的典型案例，说明为什么 agent 可观测性工具不能依赖单一框架的自述文档，而必须建立基于实际数据验证的解析 pipeline。这种 drift 在快速迭代的 AI 工具中尤为常见，因为模型能力、API 格式和工具集都在同步演化。

其次，文章中提出的 `call_id` 配对模式与 OpenAI Responses API 的设计一致，说明 flat-ID-based 关联正在取代传统的嵌套 span 结构。这种设计转变的深层原因是异步和并行工具调用的普及——当模型同时调用多个工具时，嵌套结构难以表达并行关系，而 flat ID 配对更加灵活。这对设计下一代 agent trace 标准（如 OpenInference）和综述中关于“trace schema 演化”的章节具有重要参考意义。综述可以进一步探讨：如果 future agent 框架普遍采用 flat ID 模式，现有的嵌套 span 可视化工具（如 Jaeger、Zipkin）是否需要适配？

第三，作者对“时间顺序推断因果”的实践，与 GitHub Copilot、Continue.dev 等工具采用的 log-based tailer 方法属于同一技术路线。综述可以将其归为一类“启发式因果重建”（heuristic causal reconstruction）方案，并讨论其大约 80% 覆盖率的局限性——在某些边界情况下（如并行工具调用、回调嵌套、用户中断），纯粹基于时间顺序的推断会产生歧义，这正是显式因果字段（如 W3C Trace Context 的 parent_id）的价值所在。综述可以构建一个从“纯启发式”到“全显式”的因果建模光谱，并将 Codex CLI 放在启发式一端，Claude Code 的 OTel tracing 放在显式一端。

第四，通过第三方后端（DeepSeek）生成 trace 数据的思路，说明了 agent 可观测性工具需要具备模型无关（model-agnostic）的解析能力。随着多模型策略的普及，agent 框架可能在单次 session 中切换不同后端，tracing infrastructure 必须能适应不同模型的响应格式，这是构建通用 agent 可观测性平台的重要设计原则。综述可以将此作为“backend interoperability”的讨论起点。

最后，作者从“发现问题”到“构建 proxy”再到“实现解析器”的完整方法论，为综述中“如何研究闭源或半开源 agent 系统的可观测性”提供了可复用的研究范式。这种逆向工程方法对于分析其他缺乏完善文档的 agent 工具（如各类 IDE 插件、自定义 CLI 工具、内部企业 agent）同样适用。综述可以提炼出一套通用的研究流程：环境搭建 → 流量拦截/代理 → 原始数据 dump → 格式假设 → 假设验证 → 解析器实现 → 准确率评估。

## 我的笔记

这篇技术博客的最大价值在于它提供了一个“从假设到验证”的完整案例研究。作者没有停留在理论分析或文档阅读，而是通过构建 proxy、生成真实数据、对比源码预期与实际格式，最终产出可工作的开源解析器。这种“逆向工程”方法论对任何试图解析闭源或半开源 agent 工具的开发者都具有高度借鉴意义。

尤其值得注意的是，Codex CLI 作为 OpenAI 官方推出的 coding agent 工具，其 trace 格式竟然与源码注释存在如此显著的偏差。`protocol.rs` 中描述的事件类型（`exec_command_begin/end`、`mcp_tool_call_begin/end`）在实际 rollout 文件中完全不存在，这说明源码中的数据结构定义与序列化格式之间可能存在多层抽象，开发者若仅阅读源码极易产生误判。这一现象提醒我们：agent 生态仍处于快速迭代期，schema 稳定性不能被视为理所当然，甚至官方工具的文档和源码注释也可能滞后于实际实现。对于研究者和工具构建者而言，这意味着必须建立持续验证机制（regression testing against real data），而非一次性解析后永久适用。

此外，`call_id` 配对而非嵌套的设计选择，深刻反映了 modern LLM API 的演进趋势。传统的嵌套 span 模型源于同步 RPC 追踪（如 Google Dapper、Zipkin），而 LLM agent 的交互模式本质上是异步对话——模型发送工具调用请求后，可能需要等待外部执行、用户确认或网络延迟，期间事件流中会出现大量无关的元数据事件。flat ID 配对天然适合这种“发送-等待-响应”的异步模式，同时也更容易支持并行工具调用（多个 function_call 同时 pending）。Claude Code 的 OpenTelemetry tracing 同样采用扁平化的 span 层次结构（subagent span 嵌套在父 tool span 下，但同级事件之间是扁平的），可见这是 industry 的 converging pattern。

在综述写作中，可以将本文作为 Codex CLI 可观测性实现的 primary source，并与以下方面形成对比：（1）与 Claude Code 的 OTel 原生 tracing 对比——Codex CLI 是隐式、undocumented 的日志格式，而 Claude Code 是显式、标准化的 OTel 导出，两者代表了“事后日志”和“实时遥测”两种范式；（2）与 LangChain 等框架的 callback 系统对比——Codex CLI 的 trace 是运行时自动生成的日志，而非框架层面的结构化回调，缺乏 LangChain 那种在代码中显式插入 trace point 的能力；（3）与 OpenInference 规范对比——Codex CLI 的格式是 vendor-specific 的，缺乏跨框架的互操作性，而 OpenInference 试图建立统一标准。这些对比将帮助综述构建一个关于“agent trace 生态成熟度”的完整图景。

从技术实现角度，causetrace 项目中 codex_parser.py 的设计（pending call buffer、call_id matching、causal parent linking）可以作为解析类似扁平事件流的参考实现。如果未来需要解析其他 agent 工具的输出（如 Cursor、Windsurf、或各类自定义 agent），该解析器的架构模式很可能需要被复用。特别值得关注的是其“噪声过滤”策略——如何在不破坏事件链的前提下跳过 token_count 等元数据事件，这是一个在异构事件流解析中普遍存在的工程问题。

最后，本文也让我思考一个更深层的问题：为什么 OpenAI 没有在 Codex CLI 中内置更完善的可观测性导出？可能的解释包括：（1）Codex CLI 仍处于早期快速迭代阶段，团队优先保障核心功能；（2）OpenAI 可能认为开发者应该通过其 API 层面的 logging 获取可观测性，而非 CLI 层面的 trace；（3）rollout 文件可能主要用于 OpenAI 内部的调试和质量评估，而非面向终端用户的可观测性接口。无论原因如何，这种“可观测性缺口”正是社区工具（如 causetrace）的价值所在——填补官方工具与开发者需求之间的鸿沟。

## 局限性

- 本文的研究基于 Codex CLI v0.130.0，随着版本迭代，rollout 格式可能发生变化，解析器需要持续维护。
- 作者仅通过 DeepSeek 代理验证了 trace 生成，未测试其他第三方后端（如 Claude、Gemini、本地模型）的兼容性。
- 时间顺序推断因果的方法在并行工具调用或用户中断场景下存在固有歧义，无法达到 100% 的因果准确性。
- 解析器目前处理的是单 session 的 rollout 文件，未涉及跨 session 的追踪或长期状态关联。
- 文中未讨论 rollout 文件的保留策略、轮转机制和存储开销，这些对于生产环境的大规模部署至关重要。
- Codex CLI 的 rollout 格式是未公开的内部实现细节，OpenAI 可能在未来版本中随时更改，依赖此格式的工具存在 breaking change 风险。

## 术语表

| 术语 | 英文 | 说明 |
|------|------|------|
| 翻译代理 | translation proxy | 将一种 API 格式转换为另一种的中间层服务 |
| 事件流 | event stream | 按时间顺序排列的离散事件序列 |
| 扁平配对 | flat pairing | 通过唯一标识符（如 call_id）关联相关事件，而非嵌套结构 |
| 因果推断 | causal inference | 从观测数据中推断事件之间因果关系的过程 |
| 启发式推断 | heuristic inference | 基于经验规则而非确定性算法的推断方法 |
| 异构事件流 | heterogeneous event stream | 包含多种类型、不同语义的事件混合序列 |
| 噪声过滤 | noise filtering | 从原始数据中去除无关信息以提取有效信号 |
| Wire data | wire data | 实际在网络或进程间传输的原始数据 |
| Schema drift | schema drift | 数据格式或结构随时间发生的非预期变化 |
| Pending call buffer | pending call buffer | 用于暂存尚未收到响应的异步调用的数据结构 |
| JSONL | JSON Lines | 每行一个独立 JSON 对象的文本格式 |
| SSE | Server-Sent Events | 服务器向客户端推送实时事件的 HTTP 协议 |

## 引用

```bibtex
@misc{milkoor2026reverse,
  title={Reverse engineering Codex CLI rollout traces},
  author={MilkoorY},
  year={2026},
  howpublished={\url{https://dev.to/milkoor/reverse-engineering-codex-cli-rollout-traces-3b9b}},
  note={DEV Community blog post}
}
```

## 相关图片

![文章插图 1 — Codex CLI trace 结构示意](images/[a-015]/8j7kvp660rqzt99zui8e.png)

![文章插图 2 — 实际 rollout 格式示例](images/[a-015]/xjlyhbdqehj3akhz166w.png)

![文章插图 3 — 翻译代理流程图](images/[a-015]/v30ephnolfvnlwgwm0yz.png)
