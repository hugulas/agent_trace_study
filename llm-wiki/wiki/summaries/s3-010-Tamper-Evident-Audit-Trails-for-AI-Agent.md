# 防篡改 AI Agent 审计追踪：SIEM 集成的合规要求与实践指南

## Source

- Raw note: `raw/notes/s3-010_Tamper-Evident_Audit_Trails_for_AI_Agent.md`
- 证据质量: medium（基于合规框架引用和具体技术要求，但带有厂商产品推广倾向）

## Compiled Summary

这篇文章的价值在于它将一个通常被视为 "合规 checkbox" 的议题提升到了安全架构的核心位置。作者没有停留在 "你需要审计追踪来满足合规" 的表面陈述，而是深入论证了审计追踪为何是唯一能够验证其他安全控制是否生效的机制。这种 "元控制" 的视角非常深刻——如果身份认证、策略执行和加密保护都在运行，但没有审计记录来证明它们确实在运行，那么从监管和治理角度而言，这些控制的存在与否并无区别。这一逻辑对于构建可信 AI 系统具有重要的方法论意义。

## Evidence Notes

- 从技术实现角度，文章强调的 "防篡改是技术属性而非策略属性" 是一个关键洞察。许多组织错误地认为，只要限制对日志数据库的访问权限，就足以防止日志被篡改。但 Pillar Security 指出，无论谁有访问权限，存储在可写数据库中的日志都不具备防篡改性。真正的防篡改需要架构层面的机制——加密哈希链（如区块链技术中的链式结构）、WORM（Write Once Read Many）存储介质、或不可变日志服务（如 AWS CloudTrail 的不可变记录）。这些机制的共同特点是：篡改不仅被禁止，而且在技术上不可行或至少可被立即检测。综述在讨论 Agent 系统安全设计时，应当将这一区分作为基础认知来引入。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/LangSmith|LangSmith]]
