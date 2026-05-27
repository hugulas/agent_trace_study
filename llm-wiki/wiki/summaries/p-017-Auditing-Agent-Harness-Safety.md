# Auditing Agent Harness Safety

## Source

- Raw note: `raw/notes/p-017_Auditing_Agent_Harness_Safety.md`
- 作者: Chengzhi Liu, Yichen Guo, Yepeng Liu, Yuzhe Yang, Qianqi Yan, Xuandong Zhao, Wenyue Hua, Sheng Liu, Sharon Li, Yuheng Bu, Xin Eric Wang
- DOI: 10.48550/arXiv.2605.14271
- 证据质量: high
- PDF: [p-017]-harnessaudit-auditing-agent-harness-safety.pdf

## Compiled Summary

大语言模型智能体越来越依赖执行框架（execution harness）来完成任务调度、工具分发和资源路由。然而，一个框架可能在返回正确、无害的最终答案的同时，其执行轨迹中却访问了未授权资源，或将私有上下文泄露给了错误的智能体。仅基于输出层面的评估无法发现这类失败，而现有的大部分安全基准仅对最终输出或终止状态打分，尽管许多违规发生在轨迹中段而非终止时刻。核心问题在于：执行框架是否在整个执行过程中尊重用户意图、权限边界和信息流约束。

## Evidence Notes

- 为解决这一空白，本文提出 HarnessAudit，一个对完整执行轨迹进行审计的框架，从边界合规性、执行保真度和系统稳定性三个维度进行评估，并特别关注多智能体框架中风险最突出的场景。此外，本文还构建了 HarnessAudit-Bench 基准，涵盖八个真实世界领域的二百一十条任务，并在单智能体和多智能体两种配置下嵌入安全约束。作者评估了十种框架配置，覆盖前沿模型和三种多智能体框架，发现：任务完成度与安全执行之间存在错位，且违规数量随轨迹长度累积；安全风险因领域、任务类型和智能体角色而异；大多数违规集中在资源访问和智能体间信息传输；多智能体协作扩大了安全风险面，而框架设计决定了安全部署的上限。
- 现代大语言模型智能体通常运行在 OpenClaw、Claude Code、Codex 等执行框架内，由框架而非模型本身决定哪些动作可被暴露、谁有权调用工具以及何时终止执行。这种架构转移带来了一种输出级评估无法察觉的失败模式：框架可能在返回正确、无害答案的过程中，访问未授权资源、将私有上下文泄露给错误智能体，或触发预期范围之外的不可逆副作用。仅评估最终响应会将这些运行误分类为成功。
- 现有基准在三方面均存在不足：
- 大多数仅对最终输出或终止状态打分，导致一边访问禁限资源一边完成任务的运行与干净成功无法区分；
- 近期面向框架的基准虽增加了真实工具和约束，但仍以任务完成为中心，很少探测对抗条件下的稳定性；
- 几乎所有工作都针对单智能体，忽略了生产级多智能体框架引入的组件间通信通道。
- ### 框架形式化
HarnessAudit 将智能体执行框架定义为受策略约束的执行系统：
$$\mathcal{H} := (\mathcal{A}, \mathcal{T}, \mathcal{R}, \Pi, \Phi, \Sigma)$$
该形式化定义中，第一分量为执行组件集合，第二为可调工具，第三为环境资源，第四为权限策略，第五为信息流策略，第六为协调协议。执行产生可观察轨迹与最终输出。
- ### 三层安全评估体系
**L1 边界合规（Boundary Compliance）**：检查每个动作是否停留在 $\Pi$ 和 $\Phi$ 规定的边界内。违规渠道包括：
- 工具违规：调用未授权、与任务无关或超越角色的工具；
- 资源违规：访问受保护或超出范围的文件、记录、字段；
- 信息流违规：通过通信、转发或最终输出披露未获许可的信息。

## Wiki Connections

- Concepts: [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [audit-trails-security-and-governance](concepts/audit-trails-security-and-governance.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [agent-frameworks-and-coding-agents](concepts/agent-frameworks-and-coding-agents.md)
- Entities: [Claude Code](entities/Claude-Code.md), [Codex CLI](entities/Codex-CLI.md)
