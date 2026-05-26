# Amazon CloudWatch Generative AI Observability Samples

## Source

- Raw note: `raw/notes/s1-006_Amazon_CloudWatch_generative_AI_observab.md`
- 来源: AWS 官方示例仓库（aws-samples）
- 证据质量: high（官方发布，覆盖多种部署场景）

## Compiled Summary

该仓库的价值不仅在于提供了四种可直接运行的部署示例，更在于它构建了一个完整的"可观测性即代码"参考框架。从工程实践角度，我认为以下几点值得在综述中深入展开：
第一，多平台一致性体验的设计思路。同一套 Python 应用代码配合不同的基础设施即代码模板（CloudFormation、Helm），即可在四种计算环境中获得一致的可观测性体验，这种"一次埋点，多处运行"的设计理念对于企业级 Agent 落地至关重要。实际生产环境中，团队往往需要在开发阶段使用 EC2 进行调试，在测试阶段使用 ECS Fargate 进行快速验证，在生产阶段使用 EKS 进行大规模编排，同时部分场景可能直接采用 Bedrock AgentCore 免除运维负

## Evidence Notes

- 第二，自动埋点对开发者体验的改善。传统的可观测性接入往往需要开发者在每个 LLM 调用点、每次工具执行处手动插入追踪代码，这不仅增加了代码复杂度，也容易因遗漏而导致观测盲区。ADOT Python SDK 的自动埋点机制通过运行时字节码注入或框架钩子（hook）实现无侵入式采集，这种设计哲学值得在综述的"观测性接入成本"分析中重点讨论。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/AWS-AgentCore|AWS AgentCore]]
