# GitHub — microsoft/AgentRx

## Source

- Raw note: `raw/notes/a-002_GitHub__microsoftAgentRx.md`
- 来源: Microsoft Research 官方开源仓库
- 证据质量: high（官方发布，可直接运行复现）

## Compiled Summary

AgentRx 的设计哲学值得在综述中重点展开：它将"诊断"视为一个独立于"执行"的工程环节，通过引入 Trajectory IR 和约束合成，把原本需要人工逐行阅读日志的调试工作自动化。这种分层思想——采集层（原始日志）→ 表示层（IR）→ 规则层（不变量）→ 证据层（检查器）→ 判断层（Judge）→ 应用层（报告）——为 agent 可观测性提供了一个完整的方法论闭环。

## Evidence Notes

- 从工程复现角度，该仓库的 CLI 设计非常友好。`python run.py trajectory.json --stage ir` 等分阶段命令降低了调试成本，而 `runs/` 目录的持久化设计使得批量评估与历史对比变得容易。对于希望在综述中补充实验验证的读者，可以直接使用仓库提供的 `trajectories/` 样本数据进行端到端复现。安装过程也很简洁，`pip install -e .` 或直接从 GitHub 安装均可快速搭建环境。

## Wiki Connections

- Concepts: [[concepts/agent-observability-landscape]], [[concepts/trace-schema-and-telemetry-standards]], [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/evaluation-and-benchmarking]], [[concepts/audit-trails-security-and-governance]], [[concepts/production-operations-and-cloud-platforms]], [[concepts/observability-products-and-market-map]], [[concepts/cost-token-and-resource-attribution]], [[concepts/agent-frameworks-and-coding-agents]]
- Entities: [[entities/OpenTelemetry|OpenTelemetry]], [[entities/LangSmith|LangSmith]]
