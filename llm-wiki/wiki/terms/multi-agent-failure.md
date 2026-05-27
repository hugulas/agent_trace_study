# 多智能体失败

## 定义

多智能体失败来自角色分工、通信协议、依赖链、协调策略和共享状态中的错误传播，不能只用单智能体最终成功率解释。

## 使用边界

- 这个词条在本 wiki 中只按本地 notes 语料使用，不扩展到通用百科定义。
- 关注它能回答哪些工程和研究问题，而不是只给术语翻译。
- 与相邻词条重叠时，优先按“证据用途”区分：诊断、评测、审计、运行监控或成本归因。

## 关键问题

- 失败是单个智能体决策错误还是协作协议错误？
- 依赖链中哪个输出被后续错误放大？
- 是否需要群体级 trace schema？

## 证据入口

- [Why Do Multi-Agent LLM Systems Fail?](summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail.md) — 本文通过构建首个经验驱动的 MAS 失败分类法 MAST 与大规模标注数据集 MAST-Data，系统揭示了当前多智能体系统 41%–86.7% 高失败率的 14 种根因，并证明这些失败主要源于系统设计缺陷而非底层 LLM 局限，为未来 MAS 的可靠性改进提供了标准化语言与实证基础。
- [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](summaries/c-006-MASPrism-Lightweight-Failure-Attribution.md) — MASPrism 最吸引我的地方在于它从根本上重新定义了「诊断」与「推理」之间的关系。
- [Why Do Multi-Agent LLM Systems Fail?](summaries/p-021-Why-Do-Multi-Agent-LLM-Systems-Fail.md) — 本文通过构建经验驱动的失败分类体系 MAST 与大规模标注数据集 MAST-Data，系统揭示了当前多智能体系统的 14 种失败模式，并证明这些失败主要来自系统设计与协调缺陷而非底层模型局限。
- [How we built our multi-agent research system — Anthropic Engineering Blog](summaries/a-009-How-we-built-our-multi-agent-research-sy.md) — Anthropic 这篇文章堪称多智能体系统从原型到生产的最完整工程复盘之一，其价值不仅在于架构设计，更在于对"为什么有效"和"代价是什么"的坦诚剖析。90.2% 的性能提升令人印象深刻，但"token 消耗解释 80% 方差"这一发现更具理论意义——它暗示多智能体系统的性能提升在很大程度上是"推理容量扩展"的结果，而非某种神秘的涌现智能。这对综述的方法论有重要启示：在评估多智能体系统时，必须将 token 效率与结果质量同时纳入指标，否则可能产生误导性的结论。一个消耗 15 倍 token 却只提升 10% 准确率的系统，与一个消耗 2 倍 token
- [EAGER: Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation](summaries/p-018-EAGER-Efficient-Failure-Management-for-M.md) — EAGER 通过推理范围对比学习训练专用表示模型，将多智能体推理轨迹编码为统一潜在向量，从而以低成本实现逐步骤实时故障检测、诊断与反射式缓解，并通过持续积累历史故障知识提升系统可靠性。
- [EvoCF: Multi-Agent Collaboration via Agentic Memory-Driven Evolutionary Counterfactual Planning](summaries/p-023-EvoCF-Multi-Agent-Collaboration-via-Agen.md) — EvoCF 通过智能体记忆驱动的符号约束归纳、演化式反事实计划变异与经验锚定的计划评估，系统性提升多智能体具身协作规划的有效性与鲁棒性。
- [GitHub — openai/swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration](summaries/a-019-GitHub-openaiswarm.md) — Swarm 的最大价值在于其**极简主义设计哲学**。
- [Building Consistent Workflows with Codex CLI & Agents SDK](summaries/a-014-Building-Consistent-Workflows-with-Codex.md) — 这篇 Cookbook 的技术价值在于它提供了一个经过验证的、可立即复现的多智能体 Codex 工作流参考实现。
- [Multi-Agent Portfolio Collaboration with OpenAI Agents SDK](summaries/a-020-Multi-Agent-Portfolio-Collaboration-with.md) — 这是目前最为完整、可直接复现的工业级多智能体协作示例之一。其最大价值在于展示了"agents as a tool"不仅是一种设计模式，更是一种可观测性和可调试性的架构选择——当每个专家智能体都被封装为显式工具时，失败定位、性能归因和结果审计都变得更加直接和系统化。从可观测性研究的角度看，这是一个重要的架构级发现：observability 不应只是事后附加的监控层，而应该在架构设计阶段就被纳入考量。
- [OpsAgent: An Evolving Multi-agent System for Incident Management in Microservices](summaries/p-019-OpsAgent-An-Evolving-Multi-Agent-System.md) — OpsAgent 通过无需训练的数据处理器、多智能体协作诊断与双重自进化机制，将轻量级开源大模型转化为可泛化、可解释、可长期自我增强的事件管理系统，并在工业环境中验证了其有效性。

## 相关词条

- [智能体轨迹](terms/agent-trace.md)
