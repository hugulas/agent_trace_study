# Subchapter Support Plan

Scope: expand chapters 3-6 of `report.md` using local notes, wiki pages, and existing figures. The target form is `判断 -> 机制 -> 数据/图 -> 含义`.

## Chapter 3: 五层架构

- Main judgment: agent observability is a layered evidence system; each layer has a different failure mode and figureable mechanism.
- Likely source ids: p-001 AgentRx, p-014 AgentTrace, p-025 AgentSight, p-021 multi-agent failure, s1-007 AWS AgentCore, s1-010 GenAIOps, a-014 Codex multi-agent workflow.
- Key numbers or signals: span/schema fields, multi-agent failure rates, cost decomposition, token/cost fields.
- Target figures:
  - `notes/p-014_AgentTrace_A_Structured_Logging_Framewor/images/fig1_system_flow.png`
  - `notes/p-001_AgentRx_Diagnosing_AI_Agent_Failures_from_Execution_Trajectories/images/fig1_agentrx.png`
  - `notes/images/[s1-007]/amazon_bedrock_agentcore_production_guide_cost_decomposition.png`
- Boundary: chapter 3 explains architecture; chapter 4 turns those architecture claims into opinions.

## Chapter 4: 七个核心观点

- Main judgment: each viewpoint should state a falsifiable position, show mechanism, attach evidence, and explain engineering implications.
- Likely source ids: p-001, p-006, p-011, p-014, p-017, p-021, s1-007, c-014, c-012, s3-011.
- Key numbers or signals: final reward vs process compliance, monitorability gap, harness edit loop, tamper evidence, token efficiency.
- Target figures:
  - `notes/p-006_Monitoring_Monitorability/images/fig1_aggregate_monitorability.png`
  - `notes/p-011_Agentic_Harness_Engineering_Observabilit/images/method.png`
  - `notes/p-017_Auditing_Agent_Harness_Safety/images/pipline.png`
  - `notes/images/[s1-007]/amazon_bedrock_agentcore_production_guide_cost_decomposition.png`
- Boundary: avoid repeating chapter 5 tables; chapter 4 should argue why these comparisons matter.

## Chapter 5: 关键对比

- Main judgment: comparisons should be operational decision tools, not descriptive lists.
- Likely source ids: AgentRx, AgentPex, AgentTrace, OpenInference, OTel, Why Do Multi-Agent LLM Systems Fail, AgentCore, token economics wiki pages.
- Key numbers or signals: single vs multi-agent failure boundary, runtime vs offline cost and latency, token cost vs quality fields.
- Target figures/tables:
  - existing markdown comparison tables
  - `notes/p-021_Why_Do_Multi_Agent_LLM_Systems_Fail/images/taxonomy_neurips_final_10_23_25.png`
  - `notes/p-022_Which_Agent_Causes_Task_Failures_and_Whe/images/fig1_overview.png`
- Boundary: keep tables concise; add prose after each table explaining when to use each axis.

## Chapter 6: 方法谱系

- Main judgment: the method landscape is not a list of papers; it is a pipeline from trace capture to diagnosis, governance, platformization, and token economics.
- Likely source ids: p-014, c-014, p-001, p-003, p-011, p-024, p-025, p-006, p-017, s1-007.
- Key numbers or signals: trajectory standardization, intervention-based diagnosis, harness evolution, cost-control levers.
- Target figures:
  - `notes/p-003_DoVer_Intervention-Driven_Auto_Debugging/images/fig2_pipeline.png`
  - `notes/p-024_Lifting_Traces_to_Logic_Programmatic_Ski/images/fig2_overview.png`
  - `notes/p-025_AgentSight_System-Level_Observability_fo/images/fig2_agentsight_system_architecture.png`
- Boundary: chapter 6 should map families and transitions; detailed research gaps remain in chapter 7.
