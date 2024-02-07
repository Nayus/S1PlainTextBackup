
*****

####  Machinery  
##### 1239#       发表于 2024-2-5 22:37

 本帖最后由 Machinery 于 2024-2-5 22:39 编辑 

TravelPlanner

测试语言代理者进行现实世界规划的基准

项目主页:https://osu-nlp-group.github.io/TravelPlanner/

github项目代码仓库:https://github.com/OSU-NLP-Group/TravelPlanner

hugface数据集下载:https://huggingface.co/datasets/osunlp/TravelPlanner

基准测试排行榜:https://huggingface.co/spaces/osunlp/TravelPlannerLeaderboard

自从人工智能的概念诞生以来，规划(planning)一直是其核心追求之一，但早期的AI代理者多数关注于受限环境设置下的测试，这主要是因为模型缺乏实现人类级别水平的规划所需的许多认知基础，最近，大型语言模型(LLMs)驱动的语言代理者们展现出了一些例如工具使用和推理之类的有趣能力，这些语言代理者们是否能在更复杂的环境中进行超越的先前AI代理者们的复杂规划吗？

为了推进这项研究，本文提出了TravelPlanner，这是一个新的规划基准，其中重点关注了旅行规划，一种常见的真实世界规划场景，它提供了一个丰富的沙箱环境，各种用于访问近400万条数据记录的工具，以及1225个精心策划的规划意图(planning intents)和参考计划(reference plans)

全面的评估表明，目前的语言代理者还不能处理如此复杂的规划任务，即使是GPT-4的成功率也只有0.6%。语言代理依然在保持任务连贯性、使用正确工具收集信息、遵从多个约束的规划方面都存在困难

然而，当前的语言代理者们仅仅能够应对如此复杂的问题本身就是不平凡的进步，TravelPlanner为未来的语言代理者们提供了一个具有挑战性富有意义的测试平台

<img src="https://img.saraba1st.com/forum/202402/05/223809b00b53kp053euc4q.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223250__01.jpg</strong> (630.86 KB, 下载次数: 0)

下载附件

2024-2-5 22:38 上传

TravelPlanner概览图，给定一个查询，语言代理者被要求使用各种搜索工具收集信息，根据收集到的信息，语言代理者需要提供一个计划，既满足查询中用户指定的需求，又符合常识约束

<img src="https://img.saraba1st.com/forum/202402/05/223829oftu3uuzv9hua196.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223307__01.jpg</strong> (577.94 KB, 下载次数: 0)

下载附件

2024-2-5 22:38 上传

约束描述，环境约束通过从环境接收的反馈来体现，用于评估语言代理者是否能够适当地调整其计划。常识约束和硬约束是根据语言代理者的计划与这些特定标准的一致性来评估的

<img src="https://img.saraba1st.com/forum/202402/05/223840tssltpl0tr9g4atv.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223315__01.jpg</strong> (70.26 KB, 下载次数: 0)

下载附件

2024-2-5 22:38 上传

数据库中的数据条目数量

<img src="https://img.saraba1st.com/forum/202402/05/223850nxnwr1cxv9xiwcco.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223341__01.jpg</strong> (473.22 KB, 下载次数: 0)

下载附件

2024-2-5 22:38 上传

不同的LLM与不同规划策略在TravelPlanner验证集和测试集上的主要结果

最佳结果用粗体标记，当收集的信息不足时，Gemini Pro倾向于直接拒绝提供计划，与标注者的访谈显示，手动标注一个计划平均需要约12分钟，然而，语言代理者们，如GPT-3.5-Turbo，只需1到2分钟就可以完成这个任务，这展现出了它们的效率

<img src="https://img.saraba1st.com/forum/202402/05/223857bc86mrycjtw2wfct.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223400__01.jpg</strong> (110.71 KB, 下载次数: 0)

下载附件

2024-2-5 22:38 上传

测试集上的工具使用错误分布，如果代理者连续三次失败尝试或重复操作，将触发提前停止，这代表语言代理者进入了死循环

<img src="https://img.saraba1st.com/forum/202402/05/223904u4acangtoiggk1ah.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223400__02.jpg</strong> (291.57 KB, 下载次数: 0)

下载附件

2024-2-5 22:39 上传

GPT-4-Turbo在测试集上的约束通过率，独立规划(sole-planning)模式的结果基于直接策略(Direct strategy)

<img src="https://img.saraba1st.com/forum/202402/05/223912x8b9za2cu7alppbo.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223408__01.jpg</strong> (94.88 KB, 下载次数: 0)

下载附件

2024-2-5 22:39 上传

对GPT-4-Turbo和参考之间的不同工具使用次数的对比，代理者的结果基于写入“Notebook”的条目数量

<img src="https://img.saraba1st.com/forum/202402/05/223918yqnw6fzhdmff6h22.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240205-223414__01.jpg</strong> (663.03 KB, 下载次数: 0)

下载附件

2024-2-5 22:39 上传

失败案例研究，代理由于重复错误(如日期错误)、信息细节混淆导致的幻觉性回答以及推理和行动之间的脱节而未能完成计划

所有案例均基于GPT-4-Turbo的代理，关于使用反思策略的GPT-4-Turbo的详细信息，请参见原论文

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  Machinery  
##### 1240#       发表于 2024-2-6 00:05

 本帖最后由 Machinery 于 2024-2-6 00:06 编辑 

MAGDi

对多代理者交互图(Multi-Agent Interaction Graphs)的结构化蒸馏(Structured Distillation)改进了小型语言模型的推理能力

github项目主页:https://github.com/dinobby/MAGDi

大型语言模型(LLM)代理者之间的交互推理方法，在不同的推理任务上都呈现出了改进，然而，这些方法涉及多个模型在多轮中进行长时间生成，导致计算成本高昂，此外，这些多代理者方法无法提供一个最终的、用于高效推理的单一模型

为了解决这个问题，本文引入了MAGDi，一种将多个LLM之间的推理交互进行结构化蒸馏进更小的语言模型的新方法，MAGDi通过将多代理者交互表征为图(graphs)，利用图编码器(graph encoder)增强基础学生模型，并使用三个目标函数进行知识蒸馏:下一个Token预测、正确和错误推理之间的对比损失，以及基于图形的目标函数以建模交互结构

在七个广泛使用的常识和数学推理基准测试中的实验证明，MAGDi提高了较小模型的推理能力，优于其他几种从单个教师和多个教师进行蒸馏的方法

此外，MAGDi还展现了比其教师更高的效率，进行的广泛分析显示MAGDi(1)增强了对OOD任务的泛化能力，(2)随着基础学生模型的规模和强度的增加而呈正相关缩放，(3)通过多教师训练，在应用自我一致性时(self-consistency)时，获得了更大的改进

<img src="https://img.saraba1st.com/forum/202402/06/000518qb83vr3rwwwycc32.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000100__01.jpg</strong> (323.81 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

本文蒸馏方法MAGDI的概览图，给定一个推理问题，多个教师LLMs进行多轮讨论，生成一个多代理交互图(MAG/multi-agent interaction graph)，然后本文的结构化蒸馏方法MAGDI将这些图中的推理知识蒸馏到基础学生模型中

<img src="https://img.saraba1st.com/forum/202402/06/000524sw8p54t6p6b5twk4.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000120__01.jpg</strong> (311.11 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

左边(a):使用GPT4、Bard和Claude2协同解决一个数学推理问题的多代理者交互图，经过三轮讨论生成

右边(b-e):MAGDI的四个不同级别，每个级别逐步从MAG的组成部分蒸馏知识

<img src="https://img.saraba1st.com/forum/202402/06/000529x9nwzk8ynn3op3aw.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000128__01.jpg</strong> (413.44 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

训练数据构建:给定一个推理问题，多个教师经过多轮讨论过程，生成多代理者交互图，MAGDI使用图神经网络(本文中为GCN)来增强基础学生模型，学习推理链的结构感知表征，然后使用涉及正向链、负向链和底层交互(positive chains, negative chains, and the underlying interactions)的三个目标进行微调

<img src="https://img.saraba1st.com/forum/202402/06/000549w3v33s9365i1gc3i.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000154__01.jpg</strong> (300.45 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

结构化蒸馏(MAGDI)与无教师、单教师和多教师蒸馏基线的对比

首先，MAGDI在所有五个推理基准测试中表现优于所有基线，平均而言，MAGDI比最强的SIT-GPT4基线提高了4.61%，比无教师基线提高了10.71%，其次，从MAG的每个组成部分进行知识蒸馏都能改善学生模型，从Level 1到Level 4，性能一直稳步提升

<img src="https://img.saraba1st.com/forum/202402/06/000554azldluhl3lip2tti.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000201__01.jpg</strong> (100.49 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

RECONCILE(一个多代理者交互框架)和MAGDI生成的Token计数的对比

<img src="https://img.saraba1st.com/forum/202402/06/000557obn4hh38ouq22njn.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000201__02.jpg</strong> (53.17 KB, 下载次数: 0)

下载附件

2024-2-6 00:05 上传

性能和效率之间的权衡，MAGDI超越了之前研究工作方法的帕累托边界，既在性能上超过了单教师模型，又在效率上超过了RECONCILE，效率定义为1/平均(Token数)

<img src="https://img.saraba1st.com/forum/202402/06/000601kbgf00mhqvszs0qq.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000213__01.jpg</strong> (38.02 KB, 下载次数: 0)

下载附件

2024-2-6 00:06 上传

单教师多任务(SIT-GPT4-MT)和MAGDI多任务(MAGDI-MT)模型在OOD数据集上的对比，即使在OOD数据集上(57.52 vs. 64.30)，MAGDI-MT的性能也比单教师基线提高了多达7%

<img src="https://img.saraba1st.com/forum/202402/06/000605bbbsmfsxph4tmxsi.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000213__02.jpg</strong> (78.62 KB, 下载次数: 0)

下载附件

2024-2-6 00:06 上传

使用不同的基础学生模型进行MAGDI蒸馏的缩放结果，随着基础模型的平均(零样本)性能的提高(Mistral-7B &gt; LLaMA-2-13B &gt; LLaMA-2-7B)，MAGDI蒸馏性能也相应增加

<img src="https://img.saraba1st.com/forum/202402/06/000609n3sak86ekiibjo1k.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-000221__01.jpg</strong> (50.63 KB, 下载次数: 0)

下载附件

2024-2-6 00:06 上传

MAGDI在GSM8K上的自我一致性相比基础学生模型和单教师蒸馏模型实现了最大的收益(高达15%)

