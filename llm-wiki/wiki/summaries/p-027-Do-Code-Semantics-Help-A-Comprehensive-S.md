# Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models

## Source

- Raw note: `raw/notes/p-027_Do_Code_Semantics_Help_A_Comprehensive_S.md`
- 作者: Jian Wang, Xiaofei Xie, Qiang Hu, Shangqing Liu, Yi Li
- 年份: 2025
- 来源: Findings of the Association for Computational Linguistics: EMNLP 2025
- DOI: 10.18653/v1/2025.findings-emnlp.548
- arXiv: 2509.11686
- PDF: [p-027]-do-code-semantics-help-execution-trace-based-information-for.pdf

## Compiled Summary

代码大语言模型以其卓越的能力开启了编程的新纪元。然而，近期研究揭示了它们在推理程序运行时行为和理解程序实际功能方面存在严重局限，这对其后训练阶段和实际部署构成了重大挑战。具体而言，这类模型面临两个核心问题：（1）缺乏对程序执行行为进行推理的能力，难以解释程序在运行时的实际行为；（2）现有方法中语义信息（如执行轨迹）的表示方式不一致且碎片化，阻碍了模型的泛化和有效推理。为应对这些挑战，本文引入了一个通用框架，支持将语义信息整合到与代码任务相关的提示中，并据此开展了一项全面研究，以探索语义信息在增强代码大模型推理能力方面的作用。具体而言，研究重点是基于轨迹的语义信息在提升监督微调和测试时推理扩展方面的效用。实验结果与先前工作截然相反，表

## Evidence Notes

- 本文围绕以下两个核心子问题展开：
1.
- **基于语义信息的监督微调**：如何在程序修复任务的微调数据中最优地编码执行轨迹推理信号，使得代码大模型能够习得更好的代码生成能力？给定微调数据集，其中输入为缺陷代码片段与执行轨迹语义信息，输出为修复后的代码，核心问题是什么样的轨迹表示最有利于模型学习。
- ### 机制流程
本文框架的核心执行链可分为以下四个步骤：
1.
- **输入：执行行为数据构建**
- 从 APPs 数据集中通过 UniXcoder 嵌入相似度匹配（阈值 0.8）收集缺陷代码与修复代码对 $(B_X, P_Y)$。
- ### 全参数微调结果
来自 LaTeX 源码 `results.tex` 的 Table 2 展示了三种基座模型在全参数微调后的性能：
**Table 2 全参数微调性能对比（Pass@1，贪心解码）**
| 基座模型 | 训练语料 | 下游微调 | 轨迹 | MBPP-R | MBPP | BigCodeBench | LiveCodeBench | CRUXEval-I | CRUXEval-O |
|---------|---------|---------|------|--------|------|-------------|--------------|-----------|-----------|
| DeepS
- - **SemCoder 在程序修复上略优**：SemCoder 在 DeepSeek-Coder 的 MBPP-R 上取得 40.5，略高于无轨迹基线的 39.2，但提升幅度仅 1.3。

## Wiki Connections

- Concepts: [runtime-instrumentation-and-otel](concepts/runtime-instrumentation-and-otel.md), [evaluation-and-benchmarking](concepts/evaluation-and-benchmarking.md), [cost-token-and-resource-attribution](concepts/cost-token-and-resource-attribution.md)
- Entities: None identified
