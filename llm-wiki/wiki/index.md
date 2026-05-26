# Index — Agentic Trace Insight

> A compiled wiki for agent trace observability, auditability, failure diagnosis, production operations, and cost visibility.

## Navigation
- [[#Knowledge Layers]] · [[#Concepts]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]


## Knowledge Layers
- [[terms/agent-trace|词条：智能体轨迹]] · [[terms/failure-attribution|失败归因]] · [[terms/process-compliance|过程合规性]] · [[terms/trace-schema|轨迹 Schema]] · [[terms/harness|Harness]]
- [[viewpoints/observability-is-not-logging|观点：可观测性不是日志收集]] · [[viewpoints/final-reward-is-insufficient|最终奖励不足以评估智能体]] · [[viewpoints/schema-is-the-product-boundary|Schema 决定产品边界]]
- [[comparisons/diagnosis-vs-compliance-vs-logging|对比：诊断/合规/日志]] · [[comparisons/otel-vs-agent-specific-schema|OTel 与 Agent Schema]] · [[comparisons/observability-product-map|产品工具地图]]

## Concepts
### Engineering
- [[concepts/failure-diagnosis-and-attribution|Failure Diagnosis and Attribution]] — Collects work on localizing failures across agent steps, tools, dependencies, multi-agent coordination, and harnesses. (57 linked notes)
- [[concepts/runtime-instrumentation-and-otel|Runtime Instrumentation and OpenTelemetry]] — Covers implementation patterns for instrumenting agents, MCP servers, tool calls, model calls, and distributed workflows. (83 linked notes)

### Evaluation
- [[concepts/evaluation-and-benchmarking|Evaluation and Benchmarking]] — Organizes benchmark, white-box evaluation, monitorability, alignment auditing, and long-horizon task evaluation notes. (59 linked notes)

### Foundations
- [[concepts/agent-observability-landscape|Agent Observability Landscape]] — Frames agent observability as traces, evaluations, governance, and production operations rather than ordinary LLM logging. (92 linked notes)
- [[concepts/trace-schema-and-telemetry-standards|Trace Schema and Telemetry Standards]] — Compares structured agent trace schemas, OpenTelemetry alignment, OpenInference, Hermes-style trajectories, and audit-trail formats. (72 linked notes)

### Governance
- [[concepts/audit-trails-security-and-governance|Audit Trails, Security, and Governance]] — Synthesizes tamper-evident audit trails, guardrails, safety violations, agent vulnerabilities, and governance evidence. (42 linked notes)

### Operations
- [[concepts/cost-token-and-resource-attribution|Cost, Token, and Resource Attribution]] — Treats cost visibility as part of observability: token economics, invoice prediction, resource attribution, and optimization. (78 linked notes)
- [[concepts/observability-products-and-market-map|Observability Products and Market Map]] — Maps product-level agent observability tools such as LangSmith, Langfuse, Arize Phoenix, Braintrust, AgentOps, Datadog, Elastic, New Relic, Splunk, Helicone, and Opik. (66 linked notes)
- [[concepts/production-operations-and-cloud-platforms|Production Operations and Cloud Platforms]] — Tracks AWS, Google, Alibaba, Baidu, and enterprise deployment guidance for operating agentic systems. (58 linked notes)

### Systems
- [[concepts/agent-frameworks-and-coding-agents|Agent Frameworks and Coding Agents]] — Connects traces and observability to concrete agent frameworks, coding agents, Claude Code, Codex, Swarm, AgentRx, and workflow systems. (47 linked notes)

## Entities
- [[entities/AWS-AgentCore|AWS AgentCore]] — recurring entity in 19 source notes
- [[entities/AgentOps|AgentOps]] — recurring entity in 9 source notes
- [[entities/AgentTrace|AgentTrace]] — recurring entity in 18 source notes
- [[entities/Arize-Phoenix|Arize Phoenix]] — recurring entity in 24 source notes
- [[entities/Braintrust|Braintrust]] — recurring entity in 9 source notes
- [[entities/Claude-Code|Claude Code]] — recurring entity in 17 source notes
- [[entities/Codex-CLI|Codex CLI]] — recurring entity in 11 source notes
- [[entities/Google-ADK-and-Vertex-AI|Google ADK and Vertex AI]] — recurring entity in 14 source notes
- [[entities/Helicone|Helicone]] — recurring entity in 9 source notes
- [[entities/Hermes-Agent-Trajectory-Format|Hermes Agent Trajectory Format]] — recurring entity in 2 source notes
- [[entities/LangSmith|LangSmith]] — recurring entity in 23 source notes
- [[entities/Langfuse|Langfuse]] — recurring entity in 24 source notes
- [[entities/OpenInference|OpenInference]] — recurring entity in 17 source notes
- [[entities/OpenTelemetry|OpenTelemetry]] — recurring entity in 62 source notes

## Summaries
- [[summaries/AgentPex-Willful-Disobedience|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] — evidence quality: medium（bundle 中 method/mechanism 部分提取不完整）
- [[summaries/Dive-Into-Claude-Code|Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems]] — evidence quality: medium（bundle 中大量方法机制内容提取失败，此处结合 PDF 直接阅读补充）
- [[summaries/a-002-GitHub-microsoftAgentRx|GitHub — microsoft/AgentRx]] — evidence quality: high（官方发布，可直接运行复现）
- [[summaries/a-003-Systematic-debugging-for-AI-agents-Intro|Systematic debugging for AI agents: Introducing the AgentRx framework]] — evidence quality: unknown
- [[summaries/a-007-Monitoring-Claude-Code-Docs|Monitoring - Claude Code Docs]] — evidence quality: high
- [[summaries/a-009-How-we-built-our-multi-agent-research-sy|How we built our multi-agent research system — Anthropic Engineering Blog]] — evidence quality: high
- [[summaries/a-010-Announcing-the-Opik-Claude-Code-Plugin|Opik Claude Code Plugin: Auto-Configure Agent Observability]] — evidence quality: medium
- [[summaries/a-013-Advanced-Configuration-Codex-Observabil|Advanced Configuration — Codex (Observability and telemetry)]] — evidence quality: high（官方一手文档，直接描述产品能力）
- [[summaries/a-014-Building-Consistent-Workflows-with-Codex|Building Consistent Workflows with Codex CLI & Agents SDK]] — evidence quality: unknown
- [[summaries/a-015-Reverse-engineering-Codex-CLI-rollout-tr|Reverse engineering Codex CLI rollout traces - DEV Community]] — evidence quality: high
- [[summaries/a-019-GitHub-openaiswarm|GitHub — openai/swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration]] — evidence quality: medium
- [[summaries/a-020-Multi-Agent-Portfolio-Collaboration-with|Multi-Agent Portfolio Collaboration with OpenAI Agents SDK]] — evidence quality: high
- [[summaries/a-021-AI-agent-observability-tracing-debugging|AI agent observability: tracing, debugging, and monitoring multi-agent systems]] — evidence quality: unknown
- [[summaries/c-001-AI-Agent-Observability-Tracing-Debugging|AI Agent Observability: Tracing, Debugging, and the OpenTelemetry Standard]] — evidence quality: medium
- [[summaries/c-002-Observability-for-Agentic-Systems-What-t|Observability for Agentic Systems: What to Log, How to Redact, How to Debug]] — evidence quality: medium
- [[summaries/c-003-OpenTelemetry-AI-Agent-Observability-Sta|AI Agent Observability - Evolving Standards and Best Practices - OpenTelemetry]] — evidence quality: low
- [[summaries/c-004-OpenInference-OpenTelemetry-Instrumentat|GitHub - Arize-ai/openinference: OpenTelemetry Instrumentation for AI Observability]] — evidence quality: medium
- [[summaries/c-005-LangSmith-AI-Agent-LLM-Observability-Pl|LangSmith: AI Agent & LLM Observability Platform]] — evidence quality: medium
- [[summaries/c-006-MASPrism-Lightweight-Failure-Attribution|MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals]] — evidence quality: medium
- [[summaries/c-007-The-Reliability-Gap-Agent-Benchmarks-for|The Reliability Gap: Agent Benchmarks for Enterprise]] — evidence quality: unknown
- [[summaries/c-008-AI-NativeBench-An-Open-Source-White-Box|AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems]] — evidence quality: high
- [[summaries/c-009-Process-Centric-Analysis-of-Agentic-Soft|Process-Centric Analysis of Agentic Software Systems]] — evidence quality: medium
- [[summaries/c-010-GUIDE-Interpretable-GUI-Agent-Evaluation|GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis]] — evidence quality: medium
- [[summaries/c-011-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — evidence quality: medium
- [[summaries/c-012-Agent-Audit-Trail-A-Standard-Logging-For|Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems]] — evidence quality: unknown
- [[summaries/c-013-Hermes-Agent-Trajectory-Format|Trajectory Format - Hermes Agent]] — evidence quality: high
- [[summaries/c-014-OpenInference-Specification|OpenInference Specification - openinference]] — evidence quality: high（作为社区事实标准的技术规范文档）
- [[summaries/c-015-OpenInference-OpenTelemetry-for-LLM-Apps|What is OpenInference? OTel for LLM 2026]] — evidence quality: medium（作为生态概述和对比分析，时效性强，但带有 FutureAGI 自身产品视角）
- [[summaries/c-016-AgentVerify-Compositional-Formal-Verific|AgentVerify: Compositional Formal Verification of AI Agent Safety Properties via LTL Model Checking]] — evidence quality: medium
- [[summaries/c-017-Essential-Framework-for-AI-Agent-Guardra|Essential Framework for AI Agent Guardrails]] — evidence quality: unknown
- [[summaries/c-018-AI-Agents-in-Production-Monitoring-Guard|AI Agents in Production: Monitoring, Guardrails, and Safety Best Practices]] — evidence quality: unknown
- [[summaries/c-019-AI-Agent-Vulnerabilities-Understanding-S|AI Agent Vulnerabilities: Understanding and Mitigating Emerging Security Risks]] — evidence quality: unknown
- [[summaries/c-020-What-Is-AI-Agent-Monitoring-Key-Metrics|What Is AI Agent Monitoring? Key Metrics & Techniques]] — evidence quality: medium
- [[summaries/p-001-AgentRx-Diagnosing-AI-Agent-Failures-from-Execution-Trajectories|AgentRx: Diagnosing AI Agent Failures from Execution Trajectories]] — evidence quality: unknown
- [[summaries/p-002-AIOpsLab-A-Holistic-Framework-to-Evaluat|AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds]] — evidence quality: unknown
- [[summaries/p-003-DoVer-Intervention-Driven-Auto-Debugging|DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems]] — evidence quality: unknown
- [[summaries/p-004-Willful-Disobedience-Automatically-Detecting-Failures-in-Agentic-Traces|Willful Disobedience: Automatically Detecting Failures in Agentic Traces]] — evidence quality: unknown
- [[summaries/p-005-Debugging-the-Debuggers-Failure-Anchored|Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents]] — evidence quality: high
- [[summaries/p-006-Monitoring-Monitorability|Monitoring Monitorability]] — evidence quality: medium
- [[summaries/p-007-Evaluating-Chain-of-Thought-Monitorabili|评估思维链的可监控性]] — evidence quality: unknown
- [[summaries/p-008-Building-and-Evaluating-Alignment-Auditi|Building and evaluating alignment auditing agents]] — evidence quality: medium
- [[summaries/p-009-Beyond-the-Black-Box-Interpretability-of|Beyond the Black Box: Interpretability of Agentic AI Tool Use]] — evidence quality: high
- [[summaries/p-010-Online-Adaptation-for-Self-Improving-Fou|Continual Harness: Online Adaptation for Self-Improving Foundation Agents]] — evidence quality: high
- [[summaries/p-011-Agentic-Harness-Engineering-Observabilit|Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses]] — evidence quality: unknown
- [[summaries/p-012-A-Unified-Review-of-Memory-Skills-Protoc|Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering]] — evidence quality: unknown
- [[summaries/p-013-Detecting-Safety-Violations-Across-Many|Detecting Safety Violations Across Many Agent Traces]] — evidence quality: high
- [[summaries/p-014-AgentTrace-A-Structured-Logging-Framewor|AgentTrace: A Structured Logging Framework for Agent System Observability]] — evidence quality: unknown
- [[summaries/p-015-View-oriented-Conversation-Compiler-for|View-oriented Conversation Compiler for Agent Trace Analysis]] — evidence quality: high
- [[summaries/p-016-The-Long-Horizon-Task-Mirage-Diagnosing|The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break]] — evidence quality: medium
- [[summaries/p-017-Auditing-Agent-Harness-Safety|Auditing Agent Harness Safety]] — evidence quality: high
- [[summaries/p-018-EAGER-Efficient-Failure-Management-for-M|EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation]] — evidence quality: unknown
- [[summaries/p-019-OpsAgent-An-Evolving-Multi-Agent-System|OpsAgent: An Evolving Multi-agent System for Incident Management in Microservices]] — evidence quality: high
- [[summaries/p-020-Can-Dependencies-Induced-by-LLM-Agent-Wo|Can Dependencies Induced by LLM-Agent Workflows Be Trusted?]] — evidence quality: unknown
- [[summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail|Why Do Multi-Agent LLM Systems Fail?]] — evidence quality: high
- [[summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail-2|Why Do Multi-Agent LLM Systems Fail?]] — evidence quality: high
- [[summaries/p-022-Which-Agent-Causes-Task-Failures-and-Whe|Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems]] — evidence quality: high
- [[summaries/p-023-EvoCF-Multi-Agent-Collaboration-via-Agen|EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning]] — evidence quality: unknown
- [[summaries/p-024-Lifting-Traces-to-Logic-Programmatic-Ski|Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks]] — evidence quality: high
- [[summaries/p-025-AgentSight-System-Level-Observability-fo|AgentSight: System-Level Observability for AI Agents Using eBPF]] — evidence quality: unknown
- [[summaries/p-026-AgentPro-Enhancing-LLM-Agents-with-Autom|AgentPro: Enhancing LLM Agents with Automated Process Supervision]] — evidence quality: unknown
- [[summaries/p-027-Do-Code-Semantics-Help-A-Comprehensive-S|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] — evidence quality: unknown
- [[summaries/p-028-FLARE-Faithful-Logic-Aided-Reasoning-and|FLARE: Faithful Logic-Aided Reasoning and Exploration]] — evidence quality: unknown
- [[summaries/p-029-AgentDiagnose-An-Open-Toolkit-for-Diagno|AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories]] — evidence quality: unknown
- [[summaries/p-030-Teaching-Text-Agents-to-Learn-Sequential|Teaching Text Agents to Learn Sequential Decision Making from Failure]] — evidence quality: unknown
- [[summaries/s1-001-Google-Cloud-Trace-observability-for-ADK|Google Cloud Trace observability for ADK]] — evidence quality: unknown
- [[summaries/s1-002-Google-boosts-Vertex-AI-Agent-Builder-wi|Google boosts Vertex AI Agent Builder with new observability and deployment tools]] — evidence quality: unknown
- [[summaries/s1-003-bq-agent-app-Observability-with-Agent-En|bq-agent-app：基于 Google ADK 与 BigQuery 的多智能体数据分析系统]] — evidence quality: medium（开源代码仓库，README 与配置文档详尽，但未经同行评审）
- [[summaries/s1-004-Google-ADK-vs-AWS-AgentCore-Enterprise-F|Google ADK vs AWS AgentCore: Enterprise Framework Selection Guide]] — evidence quality: unknown
- [[summaries/s1-005-Getting-Started-with-AI-Agent-Observabil|Getting Started with AI Agent Observability using Vertex AI Agent Engine and Cloud Trace]] — evidence quality: high（官方学习平台发布的结构化实验，提供真实预配环境与逐步验证）
- [[summaries/s1-006-Amazon-CloudWatch-generative-AI-observab|Amazon CloudWatch Generative AI Observability Samples]] — evidence quality: high（官方发布，覆盖多种部署场景）
- [[summaries/s1-007-Amazon-Bedrock-AgentCore-Production-Oper|Amazon Bedrock AgentCore Production Operations Guide - Observability, Cost Optimization, and Disaster Recovery]] — evidence quality: low
- [[summaries/s1-008-Part-3-AgentCore-Runtime-Observability|Amazon Bedrock AgentCore Runtime - Part 3 AgentCore Runtime Observability]] — evidence quality: high（AWS Hero 撰写的官方生态实践指南，包含大量控制台截图与配置步骤）
- [[summaries/s1-009-Operating-agentic-AI-with-Amazon-Bedrock|Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA]] — evidence quality: unknown
- [[summaries/s1-010-GenAIOps-on-AWS-End-to-End-Observability|GenAIOps on AWS: 端到端可观测性栈]] — evidence quality: high
- [[summaries/s1-011-How-to-implement-observability-with-Pyth|使用 Python 与 Llama Stack 实现可观测性]] — evidence quality: medium（来自 Red Hat 官方开发者博客，作者为开源社区核心领袖，工程实践详实，但非经同行评审的学术论文）
- [[summaries/s1-012-How-to-implement-observability-with-Node|使用 Node.js 与 Llama Stack 实现可观测性]] — evidence quality: medium（来自 Red Hat 官方开发者博客，作者为 Node.js 社区核心领袖，工程实践详实，但非经同行评审的学术论文）
- [[summaries/s1-013-Accelerating-Enterprise-Gen-AI-applicati|Oracle OCI 企业级生成式 AI 应用加速方案（来源已失效）]] — evidence quality: very-low（内容不可读，仅存错误页面信息）
- [[summaries/s1-014-Observability-Add-Additional-Metrics-to|Llama Stack 遥测可观测性指标增强提案]] — evidence quality: medium
- [[summaries/s1-015-Llama-Stack-Tutorial|Llama Stack Tutorial]] — evidence quality: medium（官方教程，实践导向，内容覆盖较广但深度有限）
- [[summaries/s2-001-什么是AgentLoop-云监控CMS-阿里云文档|阿里云 AgentLoop — AI 应用全生命周期可观测与数据飞轮平台]] — evidence quality: unknown
- [[summaries/s2-002-应用观测-大模型服务平台百炼Model-Studio-阿里云文档|阿里云百炼应用观测 — 大模型应用端到端可观测实践]] — evidence quality: unknown
- [[summaries/s2-003-Appbuilder-Trace跟踪功能基本用法-百度千帆文档|千帆AppBuilder Trace跟踪功能基本用法]] — evidence quality: unknown
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] — evidence quality: unknown
- [[summaries/s2-005-目前主流的智能体可观测性和智能体评测相关的产品调研-Coze-Loop详细介绍|目前主流的智能体可观测性和智能体评测相关的产品调研]] — evidence quality: unknown
- [[summaries/s2-006-Monitor-troubleshoot-and-improve-AI-agen|使用 Datadog LLM Observability 监控、排查与优化 AI Agent]] — evidence quality: medium-high（基于官方产品文档，包含具体技术方案和可视化设计说明）
- [[summaries/s2-007-Datadog-LLM-Observability-Product-Page|Datadog LLM Observability 产品页面深度解读]] — evidence quality: 中（作为产品功能描述具有参考价值，但缺乏第三方独立验证或技术白皮书级别的细节披露）
- [[summaries/s2-008-Monitor-LLM-and-agent-performance-with-A|Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性]] — evidence quality: medium（基于官方产品发布声明，包含具体功能描述和技术架构信息）
- [[summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori|Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档]] — evidence quality: unknown
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] — evidence quality: unknown
- [[summaries/s2-011-Elastic-Brings-Observability-to-AI-Agent|Elastic Brings Observability to AI Agents with Amazon Bedrock AgentCore]] — evidence quality: low
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] — evidence quality: unknown
- [[summaries/s2-013-Introduction-to-AI-monitoring-New-Relic|Introduction to AI monitoring - New Relic Documentation]] — evidence quality: high
- [[summaries/s2-014-langfuselangfuse-GitHub|Langfuse: 开源 LLM 工程平台]] — evidence quality: high
- [[summaries/s2-015-AI-Agent-Observability-Platform-Langfuse|Langfuse 完成 5000 万美元 B 轮融资：AI Agent 可观测性迎来产业级拐点]] — evidence quality: unknown
- [[summaries/s2-016-Arize-aiphoenix-GitHub|Arize-ai/phoenix: AI Observability & Evaluation]] — evidence quality: medium
- [[summaries/s2-017-Arize-AI-Review-2026-AI-Observability-L|Arize AI Review 2026: AI Observability & LLM Evaluation]] — evidence quality: medium
- [[summaries/s2-018-What-Is-Braintrust-Is-It-the-Best-for-AI|What Is Braintrust? Is It the Best for AI Observability?]] — evidence quality: medium
- [[summaries/s2-019-Braintrust-Raises-80M-Series-B-for-AI-Ob|Braintrust 完成 8000 万美元 B 轮融资，加速 AI 可观测性平台建设]] — evidence quality: medium（基于官方融资公告及多个标杆客户证言）
- [[summaries/s2-020-AgentOps-AI-Agent-Monitoring-and-Obser|AgentOps - AI Agent Monitoring and Observability 评测深度解读]] — evidence quality: 中（第三方评测具有一定独立性，但内容深度受限于聚合平台的信息来源，缺乏原始用户访谈或量化基准测试）
- [[summaries/s2-021-AgentOps-AI-Infrastructure-Platform-Mark|AgentOps AI Infrastructure Platform Market Research Report 2034]] — evidence quality: unknown
- [[summaries/s2-022-Helicone-LLM-Observability-Platform-Lea|Helicone LLM 可观测性平台深度评测：一键集成与智能成本优化]] — evidence quality: unknown
- [[summaries/s2-023-Helicone-Open-source-LLM-observability-f|Helicone：开源 LLM 可观测性与 AI 网关一体化平台]] — evidence quality: unknown
- [[summaries/s3-001-Mind-the-Metrics-Patterns-for-Telemetry|Mind the Metrics: Patterns for Telemetry-Aware In-IDE AI Application Development using Model Context Protocol (MCP)]] — evidence quality: medium
- [[summaries/s3-002-Distributed-tracing-for-agentic-workflow|Distributed tracing for agentic workflows with OpenTelemetry]] — evidence quality: medium
- [[summaries/s3-003-Proposal-Adding-OpenTelemetry-Trace-Supp|(Proposal) Adding OpenTelemetry Trace Support to MCP]] — evidence quality: high
- [[summaries/s3-004-OpenTelemetry-for-AI-Agents-Implementing|OpenTelemetry for AI Agents: Implementing Observability in MCP Workflows]] — evidence quality: low
- [[summaries/s3-005-How-to-Instrument-MCP-Servers-with-OpenT|OneUptime：MCP 服务器 OpenTelemetry 仪器化指南（原文已失效）]] — evidence quality: low（原文为 404 页面，实质技术内容缺失）
- [[summaries/s3-006-The-Attack-and-Defense-Landscape-of-Agen|s3-006_The_Attack_and_Defense_Landscape_of_Agen]] — evidence quality: unknown
- [[summaries/s3-007-What-Are-AI-Agent-Audit-Trails-Why-They|What Are AI Agent Audit Trails? Why They Matter for Compliance]] — evidence quality: low（概念阐述为主，缺乏技术实现细节）
- [[summaries/s3-008-RFC-should-AutoGen-support-tamper-eviden|RFC: should AutoGen support tamper-evident audit trails for multi-agent conversations in regulated industries?]] — evidence quality: 中（基于社区实践反馈与跨框架趋势观察）
- [[summaries/s3-009-OWASP-Top-10-for-Agentic-Applications-Co|OWASP Top 10 for Agentic Applications: Compliance Guide]] — evidence quality: medium
- [[summaries/s3-010-Tamper-Evident-Audit-Trails-for-AI-Agent|防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南]] — evidence quality: medium（基于合规框架引用和具体技术要求，但带有厂商产品推广倾向）
- [[summaries/s3-011-Token-Economics-for-LLM-Agents-A-Dual-Vi|Token Economics for LLM Agents: A Dual-View Study from Computing and Economics]] — evidence quality: medium
- [[summaries/s3-012-AI-Cost-Visibility-Before-the-Invoice-Ho|AI Cost Visibility: How to Track and Optimize Token Spend Before the Invoice Arrives]] — evidence quality: low
- [[summaries/s3-013-A-Guide-to-AI-Agent-Cost-Optimization-Wi|A Guide to AI Agent Cost Optimization With Observability]] — evidence quality: unknown
- [[summaries/s3-014-LLM-Agent-Cost-Attribution-Complete-Prod|LLM Agent Cost Attribution: Complete Production 2026 Guide]] — evidence quality: medium
- [[summaries/s3-015-What-Is-AI-Agent-Observability-Why-Cost|What Is AI Agent Observability? Why Cost Is What You're Missing]] — evidence quality: unknown

## Open Questions
- Which agent trace events are essential across platforms, and which are product-specific?
- How should cognitive traces be captured without leaking sensitive reasoning or private data?
- Can failure attribution be standardized across single-agent, multi-agent, and coding-agent workflows?
- What minimum evidence should a production agent audit trail preserve for compliance and incident response?
