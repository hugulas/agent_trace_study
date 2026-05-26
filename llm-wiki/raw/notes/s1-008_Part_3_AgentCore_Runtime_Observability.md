---
tags:
  - aws
  - bedrock
  - agentcore
  - observability
  - cloudwatch
  - opentelemetry
  - x-ray
  - dev-community
  - tutorial
aliases:
  - "Amazon Bedrock AgentCore Runtime Part 3 Observability"
  - "AgentCore Runtime Observability"
date: 2025-09-04
url: https://dev.to/aws-heroes/amazon-bedrock-agentcore-runtime-part-3-agentcore-observability-f08
---

# Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability

## 核心信息

- **标题**: Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability
- **作者**: Vadym Kazulkin（AWS Hero）
- **来源**: DEV Community 技术博客
- **类型**: 系列教程（第 3 部分，全系列共 8 篇）
- **日期**: 2025-09-04
- **URL**: https://dev.to/aws-heroes/amazon-bedrock-agentcore-runtime-part-3-agentcore-observability-f08
- **本地文件**: `[s1-008]-part-3-agentcore-runtime-observability.pdf`
- **证据质量**: high（AWS Hero 撰写的官方生态实践指南，包含大量控制台截图与配置步骤）
- **系列上下文**: 全系列共 8 篇，本文是第 3 篇，前置依赖为第 2 篇的 Agent 部署

## 内容摘要

本文是 Amazon Bedrock AgentCore Runtime 系列教程的第三部分，聚焦于 AgentCore 可观测性（Observability）能力的深入实践。在前两部分完成 Agent 的部署与基础配置之后，作者在本篇中系统介绍了如何利用 Amazon CloudWatch GenAI Observability、AWS Distro for OpenTelemetry（ADOT）以及 Amazon X-Ray 等工具，对运行在 AgentCore Runtime 上的 AI Agent 进行全链路监控、日志记录与分布式追踪。

AgentCore 可观测性的核心定位是帮助开发者在生产环境中追踪、调试与监控 Agent 性能。它提供了 Agent 工作流每一步的详细可视化，使运维人员能够审查执行路径、审计中间输出，并快速定位性能瓶颈与失败根因。在技术实现层面，AgentCore 默认以标准化的 OpenTelemetry（OTEL）兼容格式输出遥测数据，涵盖 Agent 会话、Gateway 资源与 Memory 资源三大层面的内置指标。这种标准化设计使得 AgentCore 能够无缝集成到企业现有的可观测性技术栈中，无需为 AI Agent 单独建设一套监控系统。

文章首先引导读者进入 Amazon CloudWatch 控制台的 GenAI Observability 面板，重点展示了 Model Invocations 指标视图。该视图提供了模型调用次数（Invocation count）、调用延迟（Invocation latency）、限流次数（Invocation throttles）、错误次数（Invocation error count）以及按模型维度拆分的 token 消耗统计（输入 token、输出 token 与总量）。所有指标均支持按模型粒度细分，这对于多模型混排场景下的成本归因与性能对比具有直接价值。

接下来，文章深入讲解了模型调用日志（Model Invocation Logging）的启用与配置流程。读者需要在 CloudWatch 控制台中手动开启日志记录功能，选择包含的数据类型（输入、输出、工具调用结果等），并指定日志目的地（CloudWatch Logs）。作者展示了如何在指定的 Log group 中查看每一次模型调用的完整输入、所用工具及其返回结果，以及模型最终输出的详细内容。这种细粒度的日志能力使得当 Agent 给出异常回答时，开发者可以逐层回溯到具体的工具调用失败或模型推理偏差。

在分布式追踪部分，文章重点介绍了 CloudWatch Transaction Search 与 X-Ray 的集成。读者需要在 CloudWatch GenAI Observability 控制台中启用 Transaction Search 功能，并配置 X-Ray Trace indexing。值得注意的是，X-Ray 默认仅对 1% 的 span 免费建立 trace summary 索引，超出部分需要额外配置。启用后，AgentCore 的每一次调用链都会在 X-Ray 中形成完整的追踪视图。

文章还详细说明了如何通过 AWS Distro for OpenTelemetry（ADOT）Python SDK 对 Agent 代码进行自动埋点。当使用 `agentcore configure` 命令配置 AgentCore Runtime Starter Toolkit 时，工具会自动生成包含 `aws-opentelemetry-distro>=0.10.1` 依赖的 Dockerfile，并通过 `opentelemetry-instrument` 包装启动命令，实现零侵入式的遥测数据采集。ADOT 作为 OpenTelemetry 的 AWS 官方发行版，支持将关联的指标与追踪数据同时发送至 CloudWatch 及其他合作伙伴监控平台。

在 Bedrock AgentCore 专属视图中，文章展示了 Agents View、Sessions View 与 Traces View 三个维度的监控界面。Agents View 提供会话数、追踪数、错误率与限流率的总览；Sessions View 展示所有 Agent 会话的列表；点击进入具体会话后，可查看关联的 trace。在 Trace 详情页中，开发者可以看到每次 Agent 调用的完整 span 链——从 /invocations 端点接收请求，到 Cognito 身份验证，再到 AgentCore Gateway Open API Target 的调用，以及 Strands Agents 事件循环中的模型决策与 MCP 工具调用。每个 span 都附带毫秒级延迟数据，并支持 Timeline 视图与 Trajectory 视图两种呈现方式。Trajectory 视图在排查错误时尤其有用，它会以红色高亮标出发生错误的具体 span，使开发者能够一眼定位问题所在。

在日志配置环节，作者特别强调了 IAM 角色的最小权限原则。创建用于授权 Bedrock 写入 CloudWatch Logs 的 IAM 角色时，应仅授予必要的日志写入与 Bedrock 调用权限，避免过度授权带来的安全风险。这种安全与可观测性并重的配置思路，在企业级生产环境中尤为重要。

最后，文章简要提及 Amazon CloudWatch GenAI Observability 同样支持对非 AgentCore Runtime 托管的开源 Agent 进行观测，为后续扩展阅读留下入口。这一开放性声明表明 AWS 的可观测性战略并不局限于自有运行时，而是试图通过 OpenTelemetry 标准覆盖更广泛的 Agent 生态。

## 关键要点

1. **OpenTelemetry 标准化遥测**
   AgentCore 默认以 OTEL 兼容格式输出遥测数据，内置指标覆盖 Agent 会话、Gateway 与 Memory 三个层面，支持与现有监控栈无缝集成。

2. **CloudWatch GenAI Observability 专属面板**
   提供 Model Invocations Dashboard 与 Bedrock AgentCore Agents Dashboard，开箱即用，支持模型调用次数、延迟、限流、错误与 token 消耗的细粒度监控。

3. **模型调用日志的完整审计能力**
   通过启用 Model Invocation Logging，开发者可在 CloudWatch Logs 中查看每次调用的输入、工具调用结果与模型输出，实现从请求到响应的全链路审计。

4. **X-Ray Transaction Search 的分布式追踪**
   支持跨服务边界的 trace 检索，默认 1% 的 span 免费索引为 trace summary。追踪链路覆盖 /invocations 端点、Cognito 认证、Gateway 调用、模型推理与 MCP 工具执行。

5. **ADOT Python SDK 自动埋点**
   通过 `aws-opentelemetry-distro` 与 `opentelemetry-instrument` 实现零侵入式埋点，`agentcore configure` 命令自动完成 Dockerfile 与启动命令的配置。

6. **多维度可视化视图**
   Agents View 提供总览指标，Sessions View 展示会话列表，Traces View 呈现完整 span 链；Timeline 视图展示时序延迟，Trajectory 视图以红色高亮错误位置。

7. **细粒度延迟洞察**
   每个 span 右侧标注毫秒级延迟，帮助开发者识别性能瓶颈——例如 Cognito 认证延迟、Gateway 调用延迟或模型推理延迟。

8. **跨模型指标拆分**
   所有 Model Invocations 指标均支持按模型维度拆分，便于在多模型混排场景下进行成本归因与性能基准对比。

9. **非 AgentCore Runtime Agent 的观测支持**
   CloudWatch GenAI Observability 通过 OpenTelemetry 集成，同样支持对未托管在 AgentCore Runtime 上的开源 Agent 进行观测。

10. **与 Strands Agents SDK 的深度集成**
    教程以 Strands Agents SDK 构建的 Agent 为例，展示了从事件循环到 MCP 工具调用的完整追踪链路，体现了 AWS 对第三方 Agent 框架的兼容态度。

11. **IAM 角色的最小权限实践**
    创建用于授权 Bedrock 写入 CloudWatch Logs 的 IAM 角色（如 bedrock-role）时，遵循最小权限原则，仅授予日志写入与 Bedrock 调用所需的精确权限。

12. **模型调用日志的隐私与合规考量**
    启用模型调用日志时，开发者可自主选择包含的数据类型（输入、输出、工具结果），这种可配置性有助于在满足审计需求的同时控制敏感数据的存储范围。

13. **日志存储成本与保留策略**
    模型调用日志会产生额外的 CloudWatch Logs 存储费用，生产环境建议配置合理的保留策略（如 7 天或 30 天），并结合 CloudWatch Logs Insights 进行聚合分析。

14. **系列文章的渐进式教学设计**
    全系列共 8 篇，第 3 篇建立在前两篇的概念介绍与部署实践之上，采用循序渐进的知识递进方式，降低了复杂技术的学习曲线。

## 与综述的关联

本篇文章是综述中"AWS 生态 Agent 可观测性工程实践"章节的核心参考来源之一 [s1-008]。具体而言：

- **云原生 Agent 可观测性的端到端范例**
  综述引用该文章作为 AWS 官方生态中唯一一篇从控制台操作到代码埋点、从指标监控到分布式追踪的完整手把手教程，论证了 Bedrock AgentCore 在可观测性层面的工程成熟度。

- **OpenTelemetry 语义约定的落地实践**
  综述在讨论 OpenTelemetry GenAI Semantic Conventions 时，以 AgentCore 的 OTEL 兼容遥测输出作为云厂商原生支持的典型案例，说明标准化语义约定如何降低多平台集成成本。

- **X-Ray Transaction Search 与采样策略**
  综述引用文中提到的"默认仅 1% span 免费索引"这一细节，作为企业级 Agent 可观测性成本模型讨论中的关键数据点，警示生产环境中高并发场景下的追踪采样策略设计。

- **CloudWatch GenAI Observability 的专用化能力**
  综述将 Model Invocations Dashboard、Trajectory View 与 Agent 专属监控面板，作为云厂商为 LLM Agent 构建专用可观测性产品的代表实现，与 Google Cloud Trace for ADK、Azure Monitor for Copilot 形成横向对比。

- **ADOT 自动埋点的工程价值**
  综述在分析 Agent 可观测性接入成本时，引用 `agentcore configure` 自动生成带 ADOT 的 Dockerfile 这一实践，说明云厂商工具链如何通过自动化降低开发者埋点负担。

- **错误定位的可视化方法论**
  综述引用 Trajectory View 以红色高亮错误 span 的设计，作为 Agent 执行链路可视化在故障排查场景中的最佳实践，与 LangSmith、Langfuse 等第三方平台的 trace 可视化形成方法论对照。

## 我的笔记

这篇教程的价值在于它提供了一个从"零配置"到"全链路可观测"的完整闭环实践。与大多数停留在概念层面的文档不同，作者每一步都配有控制台截图与具体配置参数，这使得该文章具有极高的复现价值。从工程实践角度，我认为以下几点值得在综述中深入展开：

第一，ADOT 自动埋点与 Starter Toolkit 的协同设计体现了 AWS 在开发者体验上的深度思考。传统上，为 Python Agent 应用添加 OpenTelemetry 埋点需要开发者手动修改依赖、配置 exporter、初始化 tracer provider，步骤繁琐且容易出错。而 AgentCore Runtime Starter Toolkit 通过 `agentcore configure` 命令一键生成包含 ADOT 的容器化配置，将埋点复杂度完全隐藏在基础设施层。这种"配置即埋点"的设计理念，对于推动 OpenTelemetry 在 Agent 领域的普及具有重要意义。

第二，CloudWatch GenAI Observability 的专属面板设计值得重点关注。与通用云监控产品不同，该面板针对 LLM Agent 的工作特性提供了 Model Invocations、Trajectory View、Session 级追踪等专属视图，这些功能并非通用监控平台的简单扩展，而是深入理解了 Agent 执行范式后的针对性设计。特别是 Trajectory View 将 span 链以决策流的方式呈现，使开发者能够直观理解 Agent 的"思考过程"——模型何时决定调用工具、工具返回后模型如何重新规划下一步行动。

第三，X-Ray Transaction Search 的 1% 免费采样策略是一个需要谨慎对待的生产约束。对于高并发的生产环境，1% 的采样率意味着绝大多数 trace 不会建立索引，这可能导致异常排查时"恰好错过"关键 trace。企业在规划 AgentCore 可观测性架构时，应当评估全量索引的成本与收益，或者结合 CloudWatch Logs 中的模型调用日志作为补充溯源手段。

第四，文章展示了 AgentCore 调用链路的完整架构细节——从 Runtime HTTP Server 的 /invocations 端点，到 Cognito 身份验证服务，再到 Gateway Open API Target，最后进入 Strands Agents 事件循环与 MCP 工具调用。这种透明化的架构 exposé 对于理解 AgentCore 的内部工作机制具有重要价值，也为自定义 Agent 实现时的性能优化提供了明确的方向。

需要进一步追踪的问题包括：

- CloudWatch GenAI Observability 中 Trajectory View 的延迟数据是否包含模型首 token 延迟（TTFT）与逐 token 生成延迟等细粒度指标
- ADOT Python SDK 在高并发异步 Agent 框架（如 LangGraph 异步图执行）中的兼容性与性能开销
- X-Ray Trace indexing 超出 1% 免费额度后的定价模型与成本优化策略
- AgentCore Memory 与 Identity 组件的追踪 span 具体包含哪些属性与事件
- 非 AgentCore Runtime 托管的开源 Agent 接入 CloudWatch GenAI Observability 的具体配置步骤与限制
- Strands Agents SDK 的异步事件循环在 X-Ray trace 中的 span 时序精确度与采样完整性
- 当 Agent 调用链涉及多个 MCP 服务时，跨服务 trace 上下文传播的具体机制与边缘案例
- AgentCore Gateway 的 Open API Target 在 trace 中的 span 命名规范与属性标准化程度

从复现角度，该教程的前置条件明确：需要完成系列第 2 部分的 Agent 部署，拥有有效的 AWS 账户、Bedrock 模型访问权限以及 AgentCore Runtime Starter Toolkit 环境。建议读者按照系列顺序依次完成，因为第 3 部分的可观测性配置直接依赖于第 2 部分生成的 Agent 运行时 ARN 与 IAM 角色。对于希望快速体验 AgentCore 可观测性能力的团队，可以从 Model Invocations Dashboard 入手——它无需额外代码修改即可在首次调用后自动展示指标，是最低门槛的入门路径。

对于已有 Kubernetes 或 ECS 基础设施的团队，也可以将该文章中介绍的 ADOT 自动埋点方案迁移至自托管容器环境，因为 ADOT Python SDK 的 `opentelemetry-instrument` 启动方式与底层容器编排平台无关，只需确保容器具有向 CloudWatch 提交遥测数据的 IAM 权限即可。在 EKS 环境中，通常通过 IRSA（IAM Roles for Service Accounts）或 Pod Identity 为工作负载授予精细化的 CloudWatch 与 X-Ray 写入权限；在 ECS Fargate 环境中，则通过任务角色的 IAM 策略实现相同效果。

第六，文章对模型调用日志的配置流程描述非常细致，包括选择数据类型、指定 Log group、创建 IAM 角色等步骤。这种细粒度的配置指导对于首次接触 Bedrock 日志功能的学习者非常友好。需要特别注意的是，模型调用日志会产生额外的 CloudWatch Logs 存储费用，对于高频调用的生产环境，建议配置合理的日志保留策略（如 7 天或 30 天），并考虑使用 CloudWatch Logs Insights 进行聚合分析，而非长期存储原始日志。

第七，作者在文末预告了系列后续内容将转向 Custom Agent 实现，取代 Starter Toolkit 的默认配置。这意味着更深入的可观测性自定义能力（如手动创建 span、注入自定义属性、配置多个 exporter）将在后续文章中展开。对于希望深度定制 AgentCore 可观测性的高级用户，建议持续关注该系列。

![模型调用指标示例](8j7kvp660rqzt99zui8e.png)

上图展示了 CloudWatch GenAI Observability 中 Model Invocations 面板的部分指标截图，可以看到按模型维度拆分的调用次数与 token 消耗分布。这种可视化对于快速识别高成本模型与异常调用模式非常有效。

综上所述，Amazon Bedrock AgentCore Runtime 系列第 3 部分不仅是一份操作手册，更是一份关于如何在 AWS 云原生环境中构建生产级 Agent 可观测性体系的实践指南。它所体现的标准化遥测、自动化埋点、专属化面板与可视化错误定位能力，为综述提供了丰富的第一手工程论据与可直接引用的实施路径。

