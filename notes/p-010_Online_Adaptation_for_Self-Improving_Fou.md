---
tags:
  - paper
  - agentic-ai
  - continual-learning
  - self-improvement
  - embodied-agents
  - pokemon
aliases:
  - Continual Harness
  - p-010
  - Online Adaptation for Self-Improving Foundation Agents
date: 2026-05-11
doi: 10.48550/arXiv.2605.09998
---

# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

## 核心信息

- **标题**: Continual Harness: Online Adaptation for Self-Improving Foundation Agents
- **作者**: Seth Karten, Joel Zhang, Tersoo Upaa, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli
- **机构**: Princeton University, ARISE Foundation, Google DeepMind
- **发表时间**: 2026 年 5 月
- **会议 / 期刊**: arXiv preprint
- **DOI**: 10.48550/arXiv.2605.09998
- **arXiv ID**: 2605.09998
- **论文类型**: 方法型论文（agentic harness + 在线协同学习）
- **证据质量**: high

## 原文摘要翻译

业界已有成熟的编程 harness。
代表产品包括 CC 与 OH。
但具身领域尚无对等方案。
本文首先报告 GPP 项目。
该项目完成了 Blue。
也完成了 Yellow Legacy 的困难模式。
以及 Crystal 的全程无败绩通关。
在最困难的阶段，智能体通过长上下文记忆自主迭代策略，涌现出早期形式的 continual-harness 行为。

本文提出的方法将人类完全移出该闭环。
这是一个无需环境重置、面向具身智能体的自改进 harness。
它将我们在 GPP 中观察到的现象形式化并自动化。
智能体仅从一个最简环境接口出发，在行动与精修自身提示词、子智能体、技能库和记忆之间交替进行，利用同一次运行中的全部轨迹数据。
传统的提示词优化方法需要逐轮 episode 重置。
本文提出的方法则在单次运行中在线适应。
在某两款作品上，该方法从零开始显著降低了相对最简基线的按键开销，并恢复了与人工专家 harness 之间的大部分差距，且增益随模型能力变化。
随后，本文将闭环收束到模型自身。
一个在线过程奖励协同学习循环让开源智能体在持续精修的 harness 中运行。
由 frontier teacher 重新标注低奖励窗口并用于更新模型。
在不重置环境的情况下驱动游戏上的持续里程碑进展。

## 创新点

1. **首个通关多款 RPG 的 AI 系统**：
GPP 项目完成了 Blue。
也完成了 Yellow Legacy 的困难模式。
以及 Crystal 的全程无败绩通关。
这证明 harness 迭代对具身任务具有决定性作用。
2. **无重置的自改进 harness**：
将 GPP 中的人工精修自动化为在线上下文学习。
每次运行内部即可更新系统提示、子智能体、技能与记忆，无需 episode 重置。
3. **模型与 harness 协同学习**：
提出在线协同训练循环。
该循环将 frontier model 作为教师、开源模型作为学生。
通过过程奖励模型评分、教师重标注与软更新，实现 harness 状态与模型权重的联合进化。
4. **能力依赖的 harness 增益**：
实验显示 harness 收益并非均匀分布，而是随模型能力呈现 Pareto 前沿式的分层。
Pro 上严格占优，Flash 上高方差，Lite 上低于能力地板。

## 一句话总结

本文提出 Continual Harness，一个无需环境重置、通过在线上下文学习持续精修自身脚手架的具身智能体框架，并进一步将 frontier model 的 harness 精修能力蒸馏给开源模型，实现模型权重与 harness 状态的协同进化。

## 研究问题

具身智能体领域长期缺乏像编程 agent 那样成熟的 harness 基础设施。
PokeAgent Challenge 的报告指出，若没有领域特定的 scaffolding，前沿视觉语言模型在 RPG 游戏中几乎无法取得进展。
问题的核心在于：

- **环境的长时程与部分可观测性**：RPG 中的对话链、多步解谜和后期战斗需要跨数千步的上下文推理。
- **空间推理受限**：当前 VLM 对屏幕像素的纯视觉理解不足以支撑可靠导航。
- **harness 的工程瓶颈**：人工设计专家级 harness 成本极高，且难以迁移到新游戏或新领域。

GPP 项目首先验证了解题路径——通过人工读取轨迹并改写 harness，模型确实能完成复杂 RPG。
但这引出了更深层的科学问题：
**能否将人工 harness 精修完全自动化？**
**能否让 harness 与模型权重在同一个在线循环中共同进化？**

## 数据与任务定义

### 环境与评估指标

实验在某两款作品上进行，两者同属 RPG 类型，但地图布局、机制与难度不同。
它们分别是 Red 与 Emerald。
评估采用 PokeAgent Challenge 的标准化里程碑体系，主指标为**到达每个里程碑的累积按键次数**。
按键次数越少，说明 agent 的决策效率越高。

### 观察空间

每一步 $t$，智能体接收：
- 帧观测 $o_t$：当前环境状态的渲染图像；
- 文本地图 $m_t$：以 ASCII 描述可见区域与可行走位置的局部地图，补偿 VLM 的空间推理短板；
- 动作空间：固定按键集合。

文本地图完全来自人类玩家可从屏幕读取的游戏状态，**不含攻略、目标列表或寻路信息**，确保评估的公平性。

### Harness 条件

- 最简 harness：仅提供帧、文本地图、按键接口与通用系统提示，无子智能体、记忆或技能。
- 专家 harness：PokeAgent 手工设计的 harness，包含预建子智能体、寻路、属性克制表、伤害计算器与精选目标。
- Continual Harness：从最简 harness 出发，在游戏过程中在线精修，分三种变体：从零开始、加载冻结（加载成功运行后关闭精修）、加载继续（加载后持续精修）。

## 方法主线

### Harness 的四元组表示

Harness 状态被形式化为四元组：

$$
\mathcal{H} = (p, \mathcal{G}, \mathcal{K}, \mathcal{M})
$$

其中：
- $p$：系统提示词，包含指令与战略指导；
- $\mathcal{G}$：子智能体集合，可被编排器调用以处理特定任务；
- $\mathcal{K}$：技能库，既包含文本级启发式，也包含可执行代码；
- $\mathcal{M}$：持久记忆，累积事实、策略与观测。

此外，harness 暴露一组元工具，允许智能体与精修器就地编辑上述四组件。

### 双循环架构

Continual Harness 包含嵌套的两个循环：

**内循环（智能体执行）**：模型在当前 harness 的包裹下，根据当前观测与已收集轨迹生成动作。

**外循环（harness 精修）**：每运行 $F$ 步（在 $W$ 步预热之后），精修器读取最近轨迹窗口：

$$
\tau_{t-F:t}
$$

识别失败信号（导航循环、工具调用失败、目标停滞、遗漏探索机会），然后输出四组件编辑：

$$
\Delta = (\Delta p, \Delta \mathcal{G}, \Delta \mathcal{K}, \Delta \mathcal{M})
$$

更新后的 harness 在下一步立即生效：

$$
\mathcal{H}_{t+1} = \mathcal{H}_t \oplus \Delta
$$

不重置环境。
其中 $p$ 被直接替换，其余三组件接受增删改查操作。
智能体与精修器共享同一个底层模型，区别仅在于调用时机与轨迹上下文。

Fig. 2 方法总览：单次运行内的 harness 精修与跨迭代的协同学习循环
![fig2](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig2_methodology.png)

### 机制流程

单次运行可拆解为以下步骤：

1. **输入观测与上下文**。
智能体读取当前帧、文本地图以及当前 harness 状态，送入模型生成动作。
2. **环境交互与轨迹累积**。
动作作用于环境，产生下一观测；轨迹持续累积，供后续精修器使用。
3. **失败签名检测与四路精修**。
每 $F$ 步后，精修器扫描近期轨迹，识别失败模式，随后分四路并行编辑：重写提示词、增删改子智能体、固化成功序列并修复异常代码于技能库、以及更新记忆。
4. **更新 harness 并继续执行**。
编辑通过元工具接口应用到 harness 状态；智能体在下一时间步直接使用更新后的 harness，无需重置环境。

### 持续模型-Harness 协同学习循环

在推理循环之上，本文进一步将 Continual Harness 实例化为开源模型的训练循环。
每次在线迭代让策略在实时精修的 harness 中执行 $K = 256$ 步。
一对过程奖励模型对滑动窗口内的每个转移打分：

$$
R(s_t, a_t, \tau) \in [0, 1]
$$

低奖励窗口由 Gemini-3.1-pro 作为教师重新标注，随后对重标注分片执行软 SFT 更新，得到新参数。
该训练循环同样是无重置的：迭代结束时的模拟器状态直接加载为下一次迭代的起始状态，因此模型的游戏位置随训练持续累积。
轨迹分布通过 harness 与模型耦合：模型动作产生轨迹，精修器读取轨迹更新 harness，而 harness 又塑造下一时刻的观测分布。

## 关键结果

### GPP 项目：首款通关多款 Pokémon RPG 的 AI

GPP 项目在 2025 年 5 月至 11 月间，先后通关了 Blue。
也完成了 Yellow Legacy 的困难模式。
以及 Crystal 的全程无败绩通关。
在最困难的后期阶段，模型通过长上下文记忆自主迭代策略，涌现出早期形式的 continual-harness 行为。
四天王战斗中，智能体经历了多次失败与 harness 重写，最终在第四次尝试中战胜冠军。

Fig. 1 三个演进阶段：人工介入、自动精修、模型协同学习
![fig1](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig1_hero_progression.png)

### Continual Harness 显著缩小与专家 harness 的差距

从零开始的 Continual Harness 相对最简基线显著降低了到达各里程碑的按键开销。
并恢复了最简基线到专家 harness 之间的大部分效率差距。
残差主要集中在对话密集的房间与多回合战斗策略。

Fig. 5 两个游戏上的里程碑达成率
![fig5](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig5_progression.png)

在某款游戏上，加载继续变体在每个里程碑上都比从零开始更高效，说明精修信号在运行内部具有复利效应。

### 能力分层的 Pareto 前沿

Fig. 6 成本-完成度 Pareto 平面
![fig6](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig6_pareto.png)

上图显示 harness 增益与模型能力强相关：
- **Pro 变体严格占优**。
Continual Harness 从零开始达到 100% 里程碑，中位成本仅 130 美元。
而最简基线为 98% 完成度、215 美元，成本降低约 40% 且无完成度损失。
两个加载变体达到 96–100% 里程碑，成本 110–140 美元。
- **Flash 变体收益高方差**。
加载继续达到 80% 里程碑、42 美元。
仅略高于最简基线的 77%/30 美元。
- **Flash-Lite 变体位于能力地板以下**。
最简基线本身仅达 20%/11 美元。
而所有 Continual Harness 变体跌至 3–13%，成本反而更高。

### 开源模型的协同学习进展

在线协同学习循环让开源 Gemma-4 模型在某款游戏上取得持续的游戏里程碑进展。
训练迭代中，模型既可以从游戏起点出发，也可以从中期检查点出发，两种曲线形状一致，说明训练信号不限于早期分布。
负面对照中，未经监督预热的 Qwen3.5（27B、35B）虽能生成可解析的工具调用，但无法离开起始区域，排除了 rollout 协议伪迹。

Fig. 8 无重置训练驱动持续里程碑进展
![fig8](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig8_colearn_pipeline.png)

### 技能可度量地自改进趋近 oracle

以 Dijkstra 最优路径为 oracle，评估导航技能的路径开销缺陷。
在 warp-to-warp 障碍导航任务上，从零开始的运行将路径开销缺陷从接近 50% 的惩罚迅速压低至个位数，并在后续保持。
这一改进完全发生在循环内部且无重置：早期调用的失败被精修器诊断并修复，后续调用即可使用更新后的技能。

Fig. 7 导航技能的路径开销缺陷与累计调用次数
![fig7](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig7_pathfinding.png)

### 主要实验表格

来自 LaTeX 源码 `analysis/tables/h6_training_progression.tex` 的 Table 2 展示了各预热阶段的渐进提升：

**Table 2** 某作品上各 warm-up 阶段的评估结果（20 条 held-out transitions）

| Stage | Model | tool_fmt | act'ble | act_rel | reason | ground |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| Base | Gemma-4 26B | 0.05 | 0.25 | 0.33 | 0.25 | 0.23 |
| SFT | Gemma-4 31B | 0.50 | 0.50 | **0.75** | **0.65** | 0.44 |
| Offline GRPO (heuristic) | Gemma-4 26B | 0.50 | 0.50 | 0.65 | 0.50 | 0.44 |
| Offline GRPO (Gemini oracle) | Gemma-4 26B | 0.50 | 0.50 | 0.55 | 0.30 | 0.40 |
| Base | Qwen3.5 35B | parseable | parseable | 0 | game progress | stuck |

SFT 将格式遵从率从接近零提升到 0.50。
与此同时，动作相关性与推理相似度显著改善。
离线 GRPO 在保持格式的同时继续优化动作质量，而在线协同学习阶段才产生实际的游戏里程碑进展。

来自 `analysis/tables/c5_inheritance.tex` 的 Table 3 报告了 bootstrap 继承率：

**Table 3** 第二阶段调用中起源于第一阶段 bootstrap 的目标比例（均值 ± 标准差，n=3）

| Game | Store | Frozen | Continued |
|:---|:---|:---:|:---:|
| Emerald | skills | 100.0% ± 0.0 | 99.6% ± 0.6 |
| | subagents | 100.0% ± 0.0 | 100.0% ± 0.0 |
| | memories | 98.2% ± 1.9 | 100.0% ± 0.0 |
| Red | skills | 100.0% ± 0.0 | 96.5% ± 3.8 |
| | subagents | 100.0% ± 0.0 | 6.4% ± 5.7 |
| | memories | 100.0% ± 0.0 | 100.0% ± 0.0 |

Frozen 条件几乎完全继承，而 Continued 条件下 Red 的 subagent 继承率仅 6.4% ± 5.7%，说明持续精修会大幅重写子智能体结构。

> [!figure] Table 1 某作品四天王终身尝试次数统计
> 建议位置：关键结果
> 放置原因：该表记录 GPP 通关四天王阶段各训练家的尝试次数与最终胜利，体现 harness 精修在困难战斗中的迭代价值。
> 当前状态：保留占位；数据来自附录，后续可从 `appendices/gpp_extras.tex` 补充完整 Markdown 表格。

## 深度分析

### Harness 精修的集中性与循环性

对 Yellow Legacy 全程运行的分析表明，harness 更新并非均匀分布，而是集中于少数导航与战斗组件。
在 2000 步的每个区间内，技能与子智能体的增删改操作持续发生，说明 harness 并未收敛到固定脚手架。

Fig. 3 精修的集中与循环特征
![fig3](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig3_gpp_yellow.png)

五个最常被更新的组件占据了绝大多数更新次数。
这种“少组件高频迭代”的模式与软件工程中热点模块的持续重构高度相似。

### 提示词复杂度的振荡演化

对 Yellow Legacy 四天王阶段 battle_strategist_agent 提示词的 14 个结构检查点分析显示，总节点数、决策门、图深度与最大扇出呈现增长-简化交替的振荡模式。
在一次结构性重写中，逐决策逻辑被吸收进一个主战斗智能体，后者分派给具名子检查。
提示词并非单调膨胀，而是在功能增长与结构精简之间周期性摆动。

Fig. 4 四天王阶段战斗策略提示词的复杂度演化
![fig4](p-010_Online_Adaptation_for_Self-Improving_Fou/images/fig4_battle_complexity.png)

### 无重置 vs 重置方法的范式差异

传统提示词优化方法要求完成整个 episode 后重置环境再更新提示词。
Continual Harness 的核心优势在于：
- **失败信号的单向累积**：早期观测到的失败签名持续保留在轨迹中，供后续所有精修轮次使用，形成复利效应；
- **深度运行可达性**：后期才会出现的失败模式可被持续诊断与修复，而重置方法按构造无法触及这些状态；
- **实际部署匹配度**：对长时程编程 agent、具身 agent 与运维任务而言，免费环境重置往往不可得。

### Co-learning 的耦合动力学

模型参数与 harness 状态的更新发生在不同时间尺度。
参数跨迭代更新（通过重标注轨迹上的 SFT）。
harness 在每次迭代内部更新（通过精修器）。
这种双时间尺度耦合让轨迹分布与策略共同演化：
harness 精修塑造模型所见的数据分布，而模型行为又暴露新的失败模式供 harness 下一轮修复。
作者将这种闭环称为 continual model-harness co-learning。

### 负面结果的价值

Flash-Lite 的实验并非无效：它明确标定了 harness 自改进的**能力地板**。
当模型本身无法正确调用或利用 harness 组件时，再多的精修也无法弥补底层推理能力的不足。
这一发现对 agentic 系统的资源分配具有指导意义——在能力地板以下的模型上投入 harness 工程可能不如直接升级模型。

## 局限

1. **能力地板限制**：
Flash-Lite 在某作品上低于 20% 完成度。
所有 Continual Harness 变体均不及最简基线。
存在明确的模型能力阈值，低于该阈值时精修循环无法自举。

2. **开源模型的双重角色尚未实现**：
当前协同学习实验使用 frontier model 作为教师、开源模型作为学生。
理论上同一模型可兼任两职，但评估的 Gemma-4（最大 31B dense）尚不具备同时承担教师与学生角色的能力。

3. **训练循环未达饱和**：
实验报告了训练区间内的持续里程碑进展，但未确定收敛点，无法判断长期训练后的最终性能。

4. **无重置与有重置的对比尚未完成**：
本文专注于无重置训练（迭代结束时的模拟器状态直接作为下一次迭代的起始状态），虽然同一循环也适用于传统带重置的批次累积，但两种机制在同任务上的直接对比仍属开放问题。

5. **残差差距集中在特定组件**：
对话密集型房间与多回合战斗策略的残差差距提示，当前精修器在生成长程对话策略与复杂战斗编排方面仍有提升空间。

## 我的笔记

**复现思路**：
Continual Harness 的核心复现难点不在于算法复杂度，而在于工程基础设施——需要同时维护一个可版本化的 harness 状态、一个支持增删改查的元工具接口、以及一个能在运行中热更新的上下文管理系统。
对于希望复现的研究者，建议先从最简 harness 加单一组件（如技能库）的在线精修开始，验证失败签名检测与增删改查编辑的可靠性，再逐步扩展至多组件与协同学习循环。

**与相关工作的联系**：
- 与 GEPA 及 OPRO 相比，本文方法的突破性在于优化对象更完整。
从单一提示词扩展到完整 harness 状态，且无需重置。
- 与 DAgger 等模仿学习方法相比，协同学习循环的区别在于教师仅对低奖励窗口做稀疏重标注，而非全程示范，且 harness 本身作为数据分布的塑造者参与训练。
- 与经典的无重置强化学习相比，本文的贡献不在于提出新的 RL 算法，而是将无重置思想扩展到 harness 状态的在线自适应，实现了脚手架与策略的协同演化。

**值得关注的技术细节**：
- 过程奖励模型的组件权重在附录中给出，不同分量（格式遵从、动作可执行性、推理相似度等）的加权方式直接影响低奖励窗口的筛选阈值；
- 继承率的巨大差异暗示子智能体可能是最不稳定的组件。
某作品上的 subagent 继承率仅 6.4% ± 5.7%。
这说明持续精修会大幅重写子智能体结构。
- 导航技能的 Dijkstra oracle 评估方法提供了一个将端到端任务性能拆解为可解释技能指标的范例，值得在其他具身任务中借鉴。

**个人判断**：
这篇论文的价值不仅在于某游戏上的具体数字，而在于它提出了一种新的 agentic 系统进化范式——脚手架不再是静态的先验工程产物，而是与模型策略共同在线演化的动态实体。
随着基础模型能力持续提升，harness 精修的收益曲线可能会进一步上移。
模型与 harness 的协同学习可能成为未来通用具身智能体的标准训练范式。

## 引用

```bibtex
@article{karten2026continual, title={Continual Harness: Online Adaptation for Self-Improving Foundation Agents}, author={Karten, Seth and Zhang, Joel and Upaa, Tersoo and Feng, Ruirong and Li, Wenzhe and Shi, Chengshuai and Jin, Chi and Vodrahalli, Kiran}, journal={arXiv preprint arXiv:2605.09998}, year={2026}, doi={10.48550/arXiv.2605.09998}}
```
