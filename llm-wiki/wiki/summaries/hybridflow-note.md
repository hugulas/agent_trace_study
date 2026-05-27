# HybridFlow: Resource-Adaptive Subtask Routing for Efficient Edge-Cloud LLM Inference

## Source

- Raw note: `raw/notes/hybridflow_note.md`
- Metadata: not available in note

## Compiled Summary

端云协同推理对基于大语言模型的边缘设备至关重要，因为端侧模型往往缺乏所需的推理能力，而纯云端推理在严格的延迟和令牌预算约束下可能成本高昂且速度缓慢。然而，现有的端云协作方法通常基于对输入任务难度的估计进行路由。这些静态的粗粒度启发式策略忽视了子任务之间的依赖关系，错失了并行执行和预算自适应路由的机会。为此，我们提出了 HybridFlow，一种资源自适应的端云推理框架，支持相互依赖的子任务并行执行。具体而言，我们为每个输入任务构建一个依赖感知的有向无环图，在其依赖关系满足后并发执行子任务，从而降低端到端延迟。此外，我们提出了一个动态的效益成本效用模型，实时优化准确率、令牌成本与延迟之间的权衡。这种动态路由在保持推理质量的同时，最小化

## Evidence Notes

- 大语言模型在多步推理和复杂决策任务上表现优异，但其云端部署面临高延迟、大内存占用和不可忽视的接口费用；纯端侧小模型又因容量受限而在深度推理任务上表现不佳。端云协作是一种自然的折中方案，但现有方法存在两个核心缺陷：
- **粗粒度路由错失并行机会**：现有工作通常在查询级别或固定推理步粒度上做路由，无法利用复杂查询内部自然存在的子任务并行性，导致执行基本按顺序进行。
- - **静态策略无法适应时变预算**：实际部署中网络延迟、接口预算和端侧负载均随时间波动，而现有方法多采用固定启发式或静态阈值，不能在线适应实时预算状态。
- HybridFlow 整体是一个两阶段的端云协同推理流水线：首先由端侧规划器将用户查询分解为带依赖的子任务图，然后由资源感知路由器根据实时预算状态将各子任务自适应分配给端侧小模型或云端大模型，并调度可并行的子任务同时执行。
- **模型部署配置**：
- 端侧：Llama3.2-3B，同时承担规划器角色和边缘执行器角色
- 云端：GPT-4.1，通过接口调用
- 子任务编码器：qwen3-embedding-0.6b
- 路由器：两层隐藏层的轻量级多层感知机，以 AdamW 优化器离线热启动，学习率 $1 \times 10^{-4}$
**核心建模**：
对于每个子任务 $t_i$，定义二元路由变量 $r_i \in \{0, 1\}$，其中 $r_i = 1$ 表示卸载到云端执行，$r_i = 0$ 表示在端侧执行。
- **准确率表现（Table 1）**：
- CoT（GPT-4.1）在所有非直接提示方法中取得最高平均准确率 58.99%
- HybridFlow 平均准确率为 55.34%，紧随其后，优于 SoT（52.90%）和 PASTA（45.56%）等单模型分解方法，以及协作基线 HybridLLM（38.70%）和 DoT（46.50%）
- 纯端侧 CoT（Llama3.2-3B）仅 19.59%，纯云端 Direct Prompt（GPT-4.1）为 53.33%
**效率表现（Table 2）**：
- HybridFlow 平均端到端延迟 $C_{time} = 17.48$ 秒，显著优于 HybridLLM（24.45 秒）
- 4: Performance–cost trends under different fixed offload thresholds τ0 on the GPQA benchmark
> 建议位置：关键结果
> 放置原因：展示固定阈值下准确率与成本的单调关系，反衬自适应阈值的必要性
> 当前状态：占位符

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [production-operations-and-cloud-platforms](concepts/production-operations-and-cloud-platforms.md)
- Entities: None identified
