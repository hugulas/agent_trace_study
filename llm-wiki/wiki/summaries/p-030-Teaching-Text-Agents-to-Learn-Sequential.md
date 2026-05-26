# Teaching Text Agents to Learn Sequential Decision Making from Failure

## Source

- Raw note: `raw/notes/p-030_Teaching_Text_Agents_to_Learn_Sequential.md`
- 作者: Canasai Kruengkrai, Koichiro Yoshino
- DOI: 10.18653/v1/2025.acl-long.1526

## Compiled Summary

基于文本的强化学习智能体通过与环境交互来收集更多训练数据，从而改进自身策略。然而，这些自收集的数据不可避免地包含中间失败动作，这些失败动作源于尝试物理上不可行的行为和幻觉。直接从这样的轨迹中学习策略会强化错误行为并降低任务成功率。本文提出了一种失败动作感知目标函数，它通过基于文本反馈赋予零回报来抑制训练过程中失败动作的负面影响。在此目标函数的基础上，我们引入了一种扰动方法，利用不成功的轨迹构建共享相同目标的新成功轨迹。这使得智能体无需进一步与环境交互就能从多样化的经验中获益。在 ALFWorld 和 ScienceWorld 上的实验表明，我们的方法显著优于强基线，并且能够跨环境泛化。

## Evidence Notes

- 文本智能体在在线交互过程中自收集的成功轨迹往往夹杂着中间失败动作，例如尝试物理上不可行的操作（如对抽屉执行关闭动作但实际上并未打开）或幻觉出场景中不存在的对象（如导航到不存在的家具）。直接将这类含噪轨迹用于策略更新会强化错误行为，降低任务成功率。因此，核心问题可以表述为：如何在不增加额外环境交互和外部标注成本的前提下，有效抑制中间失败动作对策略训练的负面影响，并充分利用不成功轨迹来扩充训练数据？
> [!figure] Fig.
- 1 ALFWorld 中的交互示例
> 建议位置：研究问题
> 放置原因：该图展示了智能体在 ALFWorld 中执行家务任务时的典型交互流程，并给出了操作导致失败消息的具体案例，直观说明了中间失败动作的产生场景。
- ### 问题形式化
作者将任务建模为离散、无折扣的部分可观察马尔可夫决策过程（POMDP）。状态空间、动作空间等关键要素定义如下：
$$\langle \mathcal{S}, \mathcal{A}, P, \Omega, O, R \rangle$$
其中状态空间、动作空间等要素定义如下：
$$\mathcal{S}, \mathcal{A}, P$$
分别对应环境状态集合、动作集合与状态转移函数。观察集合、观察函数与回报函数依次为：
$$\Omega, O, R$$
智能体无法直接访问上述函数，只能通过策略生成动作并与环境交互。
- 策略被参数化为基于大语言模型的随机策略。给定轨迹历史，动作由令牌级概率逐词生成：
$$p(a_t \mid \tau_{<t}; \theta) = \prod_{i=1}^{|a_t|} p(a_t^i \mid a_t^{<i}, \tau_{<t}; \theta)$$
其中每个令牌概率通过大语言模型的 softmax 输出计算，参数 $\theta$ 即模型自身的参数。
- ### ALFWorld 主实验
表 2 汇总了各方法在 ALFWorld 四个测试设置上的平均成功率（%）：
| 方法 | 已见（模板） | 未见（模板） | 已见（人工） | 未见（人工） |
|-----|-----------|-----------|-----------|-----------|
| Seq2Seq | 10 | 9 | — | — |
| BUTLER | 40 | 37 | — | — |
| ExpeL | — | 59 | — | — |
| ExpeL + Reflexion | — | 64 | — | — |
| SFT | 60 | 67 | — | — |
| ETO | 69 | 72
- 按任务类型的细分结果（参见论文表 3）显示，最具挑战性的任务是拾取两件物品并放置。IAM-FA + DA 在已见/未见集上将其从 IAM 的 43/32 提升至 70/53。

## Wiki Connections

- Concepts: [[concepts/runtime-instrumentation-and-otel]], [[concepts/failure-diagnosis-and-attribution]], [[concepts/cost-token-and-resource-attribution]]
- Entities: None identified
