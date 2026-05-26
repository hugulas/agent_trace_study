# Agent Audit Trail: A Standard Logging Format for Autonomous AI Systems

## Source

- Raw note: `raw/notes/c-012_Agent_Audit_Trail_A_Standard_Logging_For.md`
- 作者: Raza Sharif（CyberSecAI Ltd）

## Compiled Summary

这份 IETF 草案的出现在时机上极具战略意义：2026 年 3 月发布，恰好赶在欧盟 AI 法案 8 月生效之前，为高风险 AI 系统的日志合规提供了急需的标准化框架。作者 Raza Sharif 来自 CyberSecAI Ltd，这一背景也解释了为何文档对 SOC 2、PCI DSS 等企业合规框架有如此细致的映射。从标准演进角度看，AAT 目前仍处于 Individual 提交的 Internet-Draft 阶段，尚未被 IETF 正式背书，这意味着其在未来六个月内可能经历大幅修订，甚至被其他草案取代。在综述中引用时需注意其"work in progress"属性，避免过度断言其已具备标准效力。

## Evidence Notes

- AAT 的设计在安全性与实用性之间取得了值得称道的平衡。SHA-256 哈希链提供了基础防篡改能力，而可选的 ECDSA 签名则让实施者可以根据风险等级灵活选择安全强度。输入/输出哈希化与 tombstone 机制是隐私设计的亮点：前者避免了审计日志本身成为敏感数据泄露源，后者则在合规删除与链式完整性之间找到了技术折中。然而，文档对"原始数据独立存储"的具体实现（如密钥管理、访问控制、存储位置）着墨较少，这可能是后续版本需要加强的部分。在实际部署中，如果原始数据存储与审计日志之间的关联密钥泄露，整个隐私保护机制将形同虚设。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/cost-token-and-resource-attribution]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/OpenInference|OpenInference]], [[entities/AgentTrace|AgentTrace]]
