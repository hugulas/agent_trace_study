# Operating agentic AI with Amazon Bedrock AgentCore and Datadog LLM Observability: Lessons from NTT DATA

## Source

- Raw note: `raw/notes/s1-009_Operating_agentic_AI_with_Amazon_Bedrock.md`
- 作者: Tohn Furutani（NTT DATA SRE 工程师）

## Compiled Summary

这篇案例的核心价值在于它并非产品宣传文档，而是来自 NTT DATA 这一大型系统集成商在真实客户场景中的验证经验。作者身份（SRE 工程师）决定了文章视角偏向运维可靠性与工程实践，而非算法创新或模型优化，这与综述关注"agentic AI 如何落地"的基调高度一致。系统集成商的视角尤为珍贵，因为他们需要同时理解平台技术能力、客户业务需求和运维现实约束，这种"三角视角"是单一厂商案例或学术研究难以提供的。在综述写作中，应当充分利用这种来自一线运维人员的声音，以平衡技术理想与工程现实之间的张力。

## Evidence Notes

- 最值得关注的洞察是文章对"从 PoC 到生产"鸿沟的刻画。文章明确指出，PoC 阶段可以靠容器化加 API 加独立 IAM 集成快速验证，但进入多工作流、多租户、多版本的企业场景后，执行平台的标准化（AgentCore 的 Runtime + Gateway + Memory + Identity + 版本管理）成为必要条件而非可选优化。这与软件工程中"先让代码工作，再让代码正确，最后让代码快速"的经典路径相似，但在智能体场景下，"正确"和"快速"的定义被扩展为"决策可解释"和"行为可复现"。这种扩展意味着智能体系统的成熟度模型需要全新的评估维度，不能简单套用传统软件的 DevOps 成熟度框架。

## Wiki Connections

- Concepts: [agent-observability-landscape](concepts/agent-observability-landscape.md), [trace-schema-and-telemetry-standards](concepts/trace-schema-and-telemetry-standards.md), [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [failure-diagnosis-and-attribution](concepts/failure-diagnosis-and-attribution.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md), [observability-products-and-market-map](concepts/observability-products-and-market-map.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: [OpenTelemetry](entities/OpenTelemetry.md), [AWS AgentCore](entities/AWS-AgentCore.md)
