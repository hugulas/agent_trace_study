# bq-agent-app：基于 Google ADK 与 BigQuery 的多智能体数据分析系统

## Source

- Raw note: `raw/notes/s1-003_bq-agent-app_Observability_with_Agent_En.md`
- 证据质量: medium（开源代码仓库，README 与配置文档详尽，但未经同行评审）

## Compiled Summary

bq-agent-app 是目前在开源社区中看到的较为完整的多智能体数据分析系统之一，其价值不仅在于功能实现，更在于工程实践的透明度。与许多仅展示 Demo 视频或交互截图的项目不同，该仓库详细披露了技术栈版本、IAM 角色需求、环境变量配置、部署脚本、观测配置与隐私风险说明，这种文档化程度在开源智能体项目中并不常见。对于希望将智能体系统从原型推进到生产的研究者和工程师而言，这种级别的文档披露具有极高的参考价值。

## Evidence Notes

- 从架构角度看，五条路径的意图路由设计值得深入借鉴。根智能体不做"全能选手"，而是专注于"调度员"角色，将不同复杂度的分析请求交给最适合的下游智能体。PATH D 的 CA API 路径适用于大多数简单查询，响应快且资源消耗低，直接调用与 BigQuery Agents 和 Looker 共享的后端，确保了企业现有 BI 投资的兼容性；PATH C 的 DS 路径则借助 Code Interpreter 将分析能力扩展到统计检验和自定义可视化，预装的全套 Python 数据科学生态使得复杂分析无需额外配置；PATH B 的 BQML 路径填补了机器学习操作的需求缺口，并且通过 RAG 文档检索降低了模型在生成 BQML 语法时的幻觉概

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/Langfuse|Langfuse]], [[entities/Google-ADK-and-Vertex-AI|Google ADK and Vertex AI]]
