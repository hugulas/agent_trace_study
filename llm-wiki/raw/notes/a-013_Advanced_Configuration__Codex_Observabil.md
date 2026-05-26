---
tags:
  - codex
  - openai
  - agent-configuration
  - cli
  - observability
  - telemetry
aliases:
  - "Codex Advanced Configuration"
  - "OpenAI Codex Observability"
date: 2025-04-01
url: https://developers.openai.com/codex/config-advanced
---

# Advanced Configuration — Codex (Observability and telemetry)

## 核心信息

- **标题**: Advanced Configuration — Codex (Observability and telemetry)
- **来源**: OpenAI 官方开发者文档
- **类型**: 产品官方文档
- **日期**: 2025-04-01
- **URL**: https://developers.openai.com/codex/config-advanced
- **本地文件**: `[a-013]-advanced-configuration--codex-observability-and-telemetry.pdf`
- **证据质量**: high（官方一手文档，直接描述产品能力）

## 内容摘要

OpenAI Codex CLI 的高级配置文档详细说明了如何通过 `~/.codex/config.toml` 对 Codex 命令行工具进行精细化控制，涵盖配置轮廓（profiles）、命令行一次性覆盖、可观测性与遥测（observability and telemetry）等关键主题。该文档的定位是为需要超越快速入门、希望对模型提供者、审批策略和集成进行深度定制的开发者提供权威参考。

配置系统的核心载体是 `~/.codex/config.toml` 文件。文档首先介绍了配置轮廓（profiles）机制，允许用户保存命名的配置值集合，并通过 CLI 的 `--profile <name>` 参数快速切换。需要注意的是，profiles 目前处于实验阶段，未来可能发生变化或移除，且暂不支持 Codex IDE 扩展。轮廓的定义方式是在 `config.toml` 中使用 `[profiles.<name>]` 节。

文档给出的典型轮廓示例如下：

- `deep-review` 轮廓：
  - `approval_policy = "on-request"`
  - `model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"`
  - `model_reasoning_effort = "gpt-5-pro"`

- `lightweight` 轮廓：
  - `approval_policy = "untrusted"`

当顶层配置和选中的轮廓同时设置了 `model_catalog_json` 时，Codex 优先采用轮廓中的值。若希望某个轮廓作为默认配置，只需在 `config.toml` 顶层添加 `profile = "deep-review"`，除非命令行显式覆盖，否则 Codex 将始终加载该轮廓。

除编辑配置文件外，文档还介绍了通过 CLI 进行一次性配置覆盖的方法。开发者应优先使用专用标志（dedicated flags），当需要覆盖任意配置键时，可使用通用的 key/value 覆盖语法。例如：

- `--model '"gpt-5.4"'` 覆盖模型选择
- `--sandbox_workspace_write.network_access='shell_environment_policy.include_only=["PATH","HOME"]'` 设置嵌套值

需要特别注意的是，这些值被解析为 TOML 格式而非 JSON，因此当值包含空格时，应当使用引号包裹，以防止 shell 将其拆分。如果值无法被解析为 TOML，Codex 会将其视为字符串处理。

在可观测性与遥测方面，Codex CLI 体现了一种"轻量、可选"的观测哲学。OpenTelemetry 日志导出并非默认开启，而是 opt-in 功能，开发者需要手动在 `~/.codex/config.toml` 的 `[otel]` 节中启用。一旦开启，Codex CLI 会导出多种类型的事件，包括：

- 会话启动事件
- API 请求事件
- SSE 事件
- 工具决策事件
- 工具结果事件

与此同时，系统还会发出 OTel 指标（metrics），包括计数器（counters）和直方图（histograms），覆盖 API 活动、流事件、工具活动等维度。具体的指标名称包括：

- `codex.api_request`
- `codex.sse_event`
- `codex.tool.call`
- `codex.tool.call.duration_ms`
- `turn.e2e_duration_ms`
- `turn.ttft.duration_ms`
- `turn.token_usage`

这些指标为开发者提供了从请求发出到首个 token 返回（TTFT）、端到端延迟、工具调用耗时以及 token 消耗等多维度的量化数据，有助于识别性能瓶颈和异常模式。

此外，文档还提及了匿名健康指标（anonymous health metrics）的默认行为：Codex CLI 会默认向 OpenAI 发送匿名健康数据，但开发者可以通过在配置中添加 `[analytics] enabled = false` 来完全禁用这一行为。这种透明且可控的数据收集策略，既帮助 OpenAI 改进产品，也尊重了用户对隐私的控制权。

从更广泛的文档结构来看，Advanced Configuration 位于 Codex 文档体系中"运行与扩展"（Run and scale）章节之下，与对话状态（Conversation state）、后台模式（Background mode）、WebSocket 模式、文件输入、上下文管理、token 计数、提示缓存等主题并列。这表明 OpenAI 将可观测性视为 Codex CLI 生产化部署的核心支柱之一，而非事后的附加功能。

在配置参考层面，文档还链接了 Configuration Reference 和 Sample Config，为开发者提供了完整的配置键列表与示例模板。这对于需要自动化部署或 CI/CD 集成的团队尤为重要，因为可以通过版本控制 `config.toml` 来确保环境间的一致性。

## 关键要点

1. **配置轮廓（Profiles）机制**
   支持在 `config.toml` 中定义多个 `[profiles.<name>]` 节，通过 `codex --profile <name>` 切换。可覆盖 `approval_policy`、`model_catalog_json`、`model_reasoning_effort` 等关键参数。实验性功能，IDE 扩展暂不支持。

2. **CLI 一次性覆盖**
   除编辑配置文件外，支持通过 `--key=value` 语法进行单次运行的配置覆盖。值按 TOML 解析，支持点号表示法设置嵌套值。专用标志优先级高于通用覆盖。

3. **Opt-in 的 OpenTelemetry 日志导出**
   需在 `[otel]` 节中手动启用。导出事件涵盖会话启动、API 请求、SSE 事件、工具决策与工具结果，形成完整的执行时间线。

4. **内置 OTel 指标体系**
   提供计数器与直方图两类指标，覆盖 API 请求、SSE 事件、工具调用、端到端延迟、TTFT、token 用量等关键维度，便于量化分析 agent 性能。

5. **可控的匿名健康数据收集**
   默认向 OpenAI 发送匿名健康指标，但可通过 `[analytics] enabled = false` 完全关闭，体现了隐私可控的设计理念。

6. **与 Codex 生态的深度集成**
   该文档与 Agents SDK、MCP 连接器、安全沙箱、代码解释器等主题共同构成 Codex 的生产级部署指南，说明 OpenAI 将可观测性内建于 CLI 架构之中。

7. **TOML 优先的配置语法**
   所有配置值均按 TOML 解析而非 JSON，这一设计简化了嵌套结构与数组的表示，但要求开发者注意 shell 转义与引号使用。

8. **生产级配置管理**
   通过 `config.toml` 的版本控制，团队可以确保不同环境（开发、测试、生产）使用一致的 agent 行为策略，支持配置即代码（Configuration as Code）的实践。

## 与综述的关联

本文档是综述中"平台级观测方案"章节的重要一手证据来源，直接证明了主流 AI 编码工具厂商正在将可观测性作为一等公民（first-class citizen）内置于 CLI 产品之中 [a-013]。具体关联如下：

- **轻量可选的观测哲学**
  综述将 Codex CLI 的 opt-in OTel 导出策略作为"轻量、可选"观测范式的典型代表，与 Claude Code 的详细 beta tracing [a-007] 形成对比，展示了不同厂商在观测深度与性能开销之间的权衡选择。

- **OTel 作为事实标准**
  文档明确使用 OpenTelemetry 作为日志与指标的导出协议，为综述中"OTel 正在统一 instrumentation 层"的论断提供了直接的产品级证据 [a-013][c-003]。同时，Codex CLI 的具体指标命名（如 `codex.tool.call.duration_ms`、`turn.token_usage`）可作为 agent 语义约定设计的行业参考。

- **开发者可控的隐私模型**
  `[analytics] enabled = false` 的设计为综述讨论"agent 观测中的隐私与合规"提供了正面案例，说明即使是默认收集匿名数据的云厂商产品，也可以提供细粒度的退出机制。

- **与 MCP 和 Agents SDK 的协同**
  结合 [a-014] 的 cookbook 内容可知，Codex CLI 内置的 Traces 仪表板能够可视化 prompts、tool calls、handoffs、MCP 服务器调用、执行时长、文件写入、错误与警告。这意味着 Advanced Configuration 中启用的 OTel 导出，实际上为 multi-agent 工作流提供了跨组件的分布式追踪能力。

- **配置即代码（Configuration as Code）**
  `config.toml` 的轮廓机制与 CLI 覆盖能力，为综述中"agent 系统的可重复部署与审计"话题提供了实践参考。通过版本控制配置文件，团队可以确保不同成员、不同环境使用一致的 agent 行为策略。

- **指标维度的行业参考**
  Codex CLI 定义的 `turn.e2e_duration_ms`、`turn.ttft.duration_ms`、`turn.token_usage` 等指标，为综述讨论"agent 性能基准"提供了具体的测量维度建议，可直接用于构建跨工具的性能对比实验。

## 我的笔记

Codex CLI 的高级配置文档虽然篇幅不长，但信息密度很高。它揭示了一个重要趋势：AI 编码工具的可观测性正在从"平台侧"（如 LangSmith、Langfuse 等第三方服务）向"客户端侧"（CLI 本身）下沉。这意味着开发者无需额外的 SDK 集成或代码插桩，只需修改配置文件即可获取生产级的 trace 与 metrics 数据。

从架构设计角度看，opt-in 策略是一个精明的权衡。一方面，默认关闭 OTel 导出避免了不必要的性能开销和网络流量，尤其对在资源受限环境或敏感网络中使用的开发者更为友好；另一方面，一旦启用，`[otel]` 节提供的丰富事件类型和指标维度，足以支撑大多数调试与监控场景。这种"按需启用、深度可用"的设计，值得其他 agent 框架借鉴。

profiles 机制对于多角色、多项目的团队尤其有价值。例如：

- 安全审计团队可以使用 `approval_policy = "on-request"` 的保守轮廓
- 内部自动化脚本可以使用 `"untrusted"` 的轻量轮廓
- 代码审查场景可以使用 `deep-review` 轮廓配合专用模型目录

通过 `profile = "deep-review"` 设置默认值，再配合 `--profile` 进行临时切换，可以实现灵活且安全的配置管理。

TOML 语法的选择也值得注意。相比于 JSON，TOML 在处理嵌套配置和数组时更为简洁直观，例如 `shell_environment_policy.include_only=["PATH","HOME"]` 这种表达式在 TOML 中非常自然。但这也对不熟悉 TOML 的开发者提出了学习成本，特别是在处理引号与 shell 转义时容易出错。

需要进一步验证的问题包括：

- OTel 导出对 Codex CLI 运行时性能的具体影响（延迟增加百分比、内存占用变化）
- `codex.tool.call.duration_ms` 等指标是否包含网络往返时间，还是仅计算本地处理时间
- `[otel]` 节是否支持自定义标签（labels/tags），以便在多项目环境中进行成本分摊与归属
- 匿名健康指标的具体字段与采样率，以及禁用后是否完全停止所有出站遥测请求
- profiles 机制与 Codex IDE 扩展的集成路线图，以及实验性标签何时会被移除
- OTel exporter 支持的协议版本（OTLP/gRPC、OTLP/HTTP）以及对应的端点认证方式

此外，结合 [a-015] 对 Codex CLI rollout trace 的逆向工程分析，可以发现 Codex 内部还存在一套与 OTel 并行的扁平事件流格式。这两套系统之间的关系——是互补、迁移中还是服务于不同用途——是一个值得深挖的技术细节。对于希望在综述中对比不同 agent 工具观测架构的写作者，建议同时阅读 [a-013]（官方文档）与 [a-015]（逆向工程），以获得更完整的图景。

从更宏观的视角来看，Codex CLI 的配置体系体现了 OpenAI 对产品成熟度的追求：不再是简单的 demo 工具，而是面向企业级部署的完整解决方案。可观测性、配置管理、隐私控制这三大能力的组合，使 Codex CLI 具备了进入大型组织开发工作流的资格。综述在讨论"agent 工具从实验到生产"的演进路径时，可以将 Codex CLI 作为典型案例进行剖析。
