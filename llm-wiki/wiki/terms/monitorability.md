# 可监控性

## 定义

可监控性描述从模型外部或过程信号中发现错误、违规或欺骗行为的能力。它不等同于可解释性，而是面向部署监控与安全评估的可检测性问题。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 哪些行为只能通过过程信号发现？
- 隐藏推理或压缩轨迹会损害哪些监控能力？
- 监控器自身如何被评估？

## 证据入口

- [[summaries/p-006-Monitoring-Monitorability|Monitoring Monitorability]] — 本文系统定义了思维链可监控性的评估框架与指标，通过大规模实验发现思维链长度与可监控性正相关，并揭示了模型能力、监控能力与可监控性之间的扩展权衡关系。
- [[summaries/p-007-Evaluating-Chain-of-Thought-Monitorabili|评估思维链的可监控性]] — 这篇文章的核心观点是：推理模型的思维链可以成为安全监控信号，但必须用系统评估持续测量其可监控性，而不能假设它会随模型规模自然保持。
- [[summaries/s2-008-Monitor-LLM-and-agent-performance-with-A|Splunk 推出 AI Agent Monitoring，为企业级 Agent 应用提供全栈可观测性]] — Splunk 推出 AI Agent Monitoring 是一个具有行业风向标意义的事件。作为传统可观测性领域的领军企业，Splunk 的进入意味着 Agent 监控已经从初创公司的创新探索阶段，进入了主流企业软件厂商的战略布局阶段。这对于整个赛道的成熟度和客户教育都是重大利好。回顾历史，当一个新兴市场出现足够多的独立初创公司后，传统巨头的进入往往是市场即将进入高速增长期的信号。Splunk 的决策可能基于其企业客户群中 AI 项目部署数量的显著增长，以及这些客户对统一监控平台的明确需求。
- [[summaries/c-020-What-Is-AI-Agent-Monitoring-Key-Metrics|What Is AI Agent Monitoring? Key Metrics & Techniques]] — 这篇文章虽然定位是入门指南，但其结构完整性出乎意料地高——从概念定义到指标体系、从技术方法到挑战分析、再到最佳实践，形成了一个闭环的知识框架。
- [[summaries/s2-009-Introduction-to-Splunk-AI-Agent-Monitori|Splunk AI Agent Monitoring：企业级 AI 代理可观测性官方文档]] — Splunk 官方文档对 AI Agent Monitoring 的介绍虽然篇幅精炼， 但透露出的战略信息却相当丰富。
- [[summaries/s2-012-Beyond-the-Black-Box-Next-Gen-AI-Agent-M|Beyond the Black Box: Next-Gen AI Agent Monitoring]] — 这篇博客是典型的厂商产品发布文章，其技术深度有限，但战略信号价值很高。David Fabritius 的写法非常清晰地遵循了 "痛点-方案-能力" 的叙事结构，对于理解产业界如何将 Agentic AI 可观测性产品化非常有帮助。作为一名读者，需要区分其中的产品愿景陈述与实际技术实现，尤其是文章中使用的 "game changing"、"strategic command center" 等营销用语需要批判性地看待。
- [[summaries/s2-010-LLM-and-agentic-AI-observability-Elasti|Elastic LLM与Agentic AI可观测性技术文档]] — Elastic的LLM可观测性文档虽然篇幅精炼，但战略意图清晰。
- [[summaries/s2-006-Monitor-troubleshoot-and-improve-AI-agen|使用 Datadog LLM Observability 监控、排查与优化 AI Agent]] — Datadog 这篇博客的技术价值在于它非常具体地描述了多 Agent 可观测性的痛点，并给出了清晰的产品化解决方案。与许多停留在概念层面的厂商文章不同，本文深入到了可视化设计的细节——为什么火焰图不行、为什么 Span 列表不行、以及基于图的视图如何解决这些问题。这种从第一性原理出发的分析方式，使文章具有很高的技术可信度，即使作为非学术来源也值得信赖。
- [[summaries/s1-005-Getting-Started-with-AI-Agent-Observabil|Getting Started with AI Agent Observability using Vertex AI Agent Engine and Cloud Trace]] — 该实验的价值不仅在于教授了 Vertex AI Agent Engine 的可观测性工具操作，更在于它展示了一种"教育即实践"的设计理念——学习者在真实环境中操作真实的 Agent，每一步都有即时反馈。从工程与综述写作角度，我认为以下几点值得深入展开： 第一，Google Cloud 三套工具（Logs Explorer、Cloud Trace、Cloud Monitoring）的原生集成度是其差异化优势。与 AWS 需要额外配置 ADOT SDK 才能将 trace 送入 CloudWatch 不同，Vertex AI Agent Engine 作为托
- [[summaries/s2-004-Agentic-AI基础设施实践经验系列七可观测性在Agent应用的挑战与实践|Agentic AI 基础设施实践经验系列（七）：可观测性在 Agent 应用的挑战与实践]] — 腾讯云这篇实践文章的价值在于其「从实践中来」的视角。

## 相关词条

- [[terms/agent-trace|智能体轨迹]]
