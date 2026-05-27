# BEAVER: A Training-Free Hierarchical Prompt Compression Method via Structure-Aware Page Selection

## Source

- Raw note: `raw/notes/beaver_note.md`
- Metadata: not available in note

## Compiled Summary

大语言模型上下文窗口的指数级扩展虽然释放了长文档理解的能力，但也带来了推理延迟和信息利用方面的严重瓶颈。现有的压缩方法往往因激进的词元剪枝而面临高昂的训练成本或语义碎片化问题。本文提出 BEAVER，一种全新的无需训练框架，将压缩方式从线性词元移除转向结构感知的层次化选择。BEAVER 通过双路池化将变长上下文映射为密集的页级张量，从而最大化硬件并行度；并通过结合语义与词汇双分支选择以及句子平滑的混合规划器来保持语篇完整性。在四个长上下文基准上的广泛评估表明，BEAVER 取得了与 LongLLMLingua 等当前最优方法相媲美的性能。特别是在 RULER 基准上，BEAVER 在多针检索任务中保持了高保真度，而基线方法则出现明显

## Evidence Notes

- 大语言模型的上下文窗口已从早期的 32k 扩展到百万词元级别，但这一扩展带来了两个核心瓶颈。
- 第一，**计算墙**。自注意力的计算复杂度为 $O(L^2)$，导致预填充延迟随上下文长度激增，造成首词元时间与尾延迟过长。尽管量化与系统级优化可缓解内存压力，但注意力本身的二次复杂度仍是根本瓶颈。
- ### 总体架构
BEAVER 包含三个核心组件：Segmenter（分段器）、PageEncoder（页面编码器）与 QueryPlanner（查询规划器）。整体思路是先将变长提示映射为固定大小的二维页张量，再通过双路池化获得层次化页面向量，最后结合查询相关性与结构先验选择保留页面，并经句子平滑恢复为连贯文本。
- ### 机制流程
1.
- ### 主基准性能
在 LongBench 与 ZeroSCROLLS 基准上，BEAVER 在 2,000 与 3,000 词元预算约束下整体优于 LLMLingua-2 与 LongLLMLingua。
- 以 LongBench 单文档问答为例，BEAVER 在多项子任务上取得最优或次优成绩，平均压缩后词元数约为 1,900–2,100，压缩比约 $1/\tau \approx 4\times$。

## Wiki Connections

- Concepts: [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
