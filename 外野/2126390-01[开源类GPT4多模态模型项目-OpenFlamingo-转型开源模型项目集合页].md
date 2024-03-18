
*****

####  Machinery  
##### 1241#       发表于 2024-2-6 04:47

 本帖最后由 Machinery 于 2024-2-6 04:48 编辑 

Nomic Embed

可重现的长上下文文本嵌入器(Long Context Text Embedder)

技术报告:https://arxiv.org/abs/2402.01613

github项目主页:https://github.com/nomic-ai/contrastors

这份技术报告描述了nomic-embed-text-v1的训练过程，它是第一个可完全复现的、开源、开放权重、开放数据、上下文长度为8192的英文文本嵌入模型，在短文本和长文本任务上均优于OpenAI的Ada-002和OpenAI text-embedding-3-small

同时，以Apache 2许可证发布了训练代码和模型权重，与其他开源模型不同，还发布了一个训练数据加载器，其中包含了2.35亿个经过筛选的文本对，可以完全复制nomic-embed-text-v1的训练过程

<img src="https://img.saraba1st.com/forum/202402/06/044736z8h86fd6qthjtwas.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-044506.jpg</strong> (102.82 KB, 下载次数: 0)

下载附件

2024-2-6 04:47 上传

文本嵌入模型的基准测试结果，nomic-embed-text-v1、OpenAI text-embedding-ada、OpenAI text-embedding-3-small和jina-embedding-base-v2在短文本和长文本基准测试中的综合性能

Nomic Embed是唯一一个可以完全审计的长文本模型，它在短文本和长文本基准测试中都超过了OpenAI text-embedding-ada、OpenAI text-embedding-3-small和Jina的性能，X轴的单位因基准套件而异

<img src="https://img.saraba1st.com/forum/202402/06/044743r6wwdq3cczibyzwq.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-044529.jpg</strong> (109.71 KB, 下载次数: 0)

下载附件

2024-2-6 04:47 上传

将nomic-embed-text-v1与OpenAI模型和其他顶级长文本开源模型进行基准测试，Nomic-embed-text-v1是唯一一个具有1亿参数级别的开源模型，它在短文本和长文本任务上均优于OpenAI text-embedding-ada和text-embedding-3-small

Nomic-embed-text-v1-ablated是指第5.4节中描述的训练设置，其中省略了HotpotQA和FEVER数据，“Seq”表示模型的上下文长度，Jina LC是Jina长上下文基准测试中任务的平均值

<img src="https://img.saraba1st.com/forum/202402/06/044749xi3yxlao3j3a37fl.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-044541.jpg</strong> (99.13 KB, 下载次数: 0)

下载附件

2024-2-6 04:47 上传

GLUE Dev Set集结果，除了2048模型之外，以与nomic-bert-2048相同的方式进行评估

<img src="https://img.saraba1st.com/forum/202402/06/044755rc61vgd0ibz0x8wl.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-044559.jpg</strong> (298.74 KB, 下载次数: 0)

下载附件

2024-2-6 04:47 上传

MTEB基准测试结果，每个类别的数据均取平均值

<img src="https://img.saraba1st.com/forum/202402/06/044802mmrrvwustv7dm0p3.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-044621.jpg</strong> (200.35 KB, 下载次数: 0)

下载附件

2024-2-6 04:48 上传

Jina长上下文评估基准测试

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  Machinery  
##### 1242#       发表于 2024-2-6 05:35

 本帖最后由 Machinery 于 2024-2-6 05:38 编辑 

PokéLLMon

通过大型语言模型在宝可梦对战中实现人类水准的代理者

github项目主页:https://github.com/git-disl/PokeLLMon

PokéLLMon，它是第一个在战略战斗游戏中实现人类水平表现的LLM具身代理者，就像在宝可梦战斗中所展示的，PokéLLMon的设计包含三个关键策略:
(i)上下文强化学习，即时利用从战斗中产生的基于文本的反馈来迭代改进策略
(ii)知识增强生成，即检索外部知识以抵消幻觉，并使代理者能够及时正确地行动
(iii)一致的动作生成，以减轻代理者面对强大对手并想要躲避战斗时的“恐慌切换(panic switching)”现象

展示了与人类进行的在线战斗，证明了PokéLLMon的类人战斗策略和即时决策能力，其在排行比赛中胜率达到49％，在邀请战斗中胜率达到56％

<img src="https://img.saraba1st.com/forum/202402/06/053618l2hiqxgg2uub0l4h.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-052948.jpg</strong> (155.94 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

在每一轮中，玩家被要求决定采取哪个行动，例如，是让快龙出招还是切换到场外的另一个宝可梦

<img src="https://img.saraba1st.com/forum/202402/06/053624i9fa3atf4pb3b00z.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053004.jpg</strong> (198.93 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

两个代表性的宝可梦:喷火龙和妙蛙花，每个宝可梦都有(复数)类型、能力、属性和四个战斗招式

<img src="https://img.saraba1st.com/forum/202402/06/053630bcyadz39ssdffxec.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053018.jpg</strong> (184.48 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

类型相克关系，"+"表示超有效/2倍伤害；"-"表示无效/0.5倍伤害；"×"表示没有效果/0倍伤害，未标记的则为标准1倍伤害

<img src="https://img.saraba1st.com/forum/202402/06/053637gtsstrm9y5vx66z5.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053056.jpg</strong> (607.15 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

使LLMs能够与人类玩家进行战斗的框架:它解析从战斗服务器接收到的消息，并将状态日志转换为文本，LLMs将这些状态描述和历史回合日志作为输入，并为下一步生成一个行动，然后将该行动发送到战斗服务器，并与对手选择的行动一起执行

<img src="https://img.saraba1st.com/forum/202402/06/053644efduersj16zn8dtt.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053109.jpg</strong> (118.16 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

LLMs在与bot对战中的表现

<img src="https://img.saraba1st.com/forum/202402/06/053649i1xs1msxrswtbfvr.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053133.jpg</strong> (73.22 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

类型相克预测的混合矩阵

<img src="https://img.saraba1st.com/forum/202402/06/053654qbtttnslina3tlht.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053210.jpg</strong> (104.76 KB, 下载次数: 0)

下载附件

2024-2-6 05:36 上传

POKELLMON配备了三种策略:
(1)ICRL利用战斗中的即时反馈来迭代改进生成
(2)KAG检索外部知识来对抗幻觉，并及时正确地行动
(3)一致的行动生成以预防恐慌切换问题

<img src="https://img.saraba1st.com/forum/202402/06/053701p72b2bwdgd7gz01e.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053234.jpg</strong> (87.23 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

代理者重复使用相同的攻击招式，但由于其能力“干燥皮肤”，对对方宝可梦没有任何效果

<img src="https://img.saraba1st.com/forum/202402/06/053709idulizwh2i9c26rh.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053241.jpg</strong> (80.33 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

在第3回合中，代理者使用“精神冲击”，对对方宝可梦造成了零伤害，通过ICRL，代理者切换到另一个宝可梦

<img src="https://img.saraba1st.com/forum/202402/06/053716ezc7ec1dhctchd77.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053300.jpg</strong> (71.29 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

ICRL在与bot对战中的表现

<img src="https://img.saraba1st.com/forum/202402/06/053731rj2iag6j8j66a5ag.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053319.jpg</strong> (92.89 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

KAG在与bot对战中的表现

<img src="https://img.saraba1st.com/forum/202402/06/053737xm1mu78xydu7umu1.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053331.jpg</strong> (91.53 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

代理者理解了招式的效果并正确使用:钥圈儿对钻角犀兽的地面属性攻击很脆弱，代理者没有交换宝可梦，而是使用了“电磁飘浮”这个招式，可以保护自己免受地面属性攻击的影响，持续五回合，从而使对方的钻角犀兽的地面属性攻击“地震”无效

<img src="https://img.saraba1st.com/forum/202402/06/053750t4mf6umfhkikuynd.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053347.jpg</strong> (92.44 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

提示方法在与bot对战中的表现

<img src="https://img.saraba1st.com/forum/202402/06/053758bws5upsd23wc3s3d.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053406.jpg</strong> (146.14 KB, 下载次数: 0)

下载附件

2024-2-6 05:37 上传

当面对一个强大的宝可梦时，具有CoT的代理者连续三次换宝可梦来逃避战斗，这给了对手三个免费回合来四倍增加攻击属性，并迅速击败了代理者的整个队伍

<img src="https://img.saraba1st.com/forum/202402/06/053807pz77i8i0gngt7pob.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053417.jpg</strong> (96.33 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

恐慌切换宝可梦的统计分析

<img src="https://img.saraba1st.com/forum/202402/06/053811ngqajlugeeqelw25.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053428.jpg</strong> (168.49 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

POKELLMON每回合都选择了有效的招式，使对手的整个队伍都倒下了，只用了一个宝可梦

<img src="https://img.saraba1st.com/forum/202402/06/053816yntnqqjqrotncwco.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053434.jpg</strong> (57.78 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

POKELLMON对抗人类玩家的表现

<img src="https://img.saraba1st.com/forum/202402/06/053820po4pmmzzpmptmum5.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053455.jpg</strong> (155.56 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

POKELLMON受到了消耗战策略的困扰:对手玩家经常恢复高防御的宝可梦，要打破这个困境需要跨越多个回合的联合效果

<img src="https://img.saraba1st.com/forum/202402/06/053830ropwztzzthioxapt.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053514.jpg</strong> (55.15 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

战斗表现受到消耗战策略的影响

<img src="https://img.saraba1st.com/forum/202402/06/053837o78ohl79oz6lq1fl.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20240206-053527.jpg</strong> (174.49 KB, 下载次数: 0)

下载附件

2024-2-6 05:38 上传

一个经验丰富的人类玩家误导代理者使用龙属性攻击，首先派出一个龙属性宝可梦，然后立即换成另一个免疫龙属性攻击的宝可梦

*****

####  yesicant  
##### 1243#         楼主| 发表于 2024-2-8 07:01

先暂停更新，等泥潭把bug修好，大家新年快乐<img src="https://static.saraba1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  李少卿  
##### 1244#       发表于 2024-3-19 07:24

大佬不更新了吗？

—— 来自 OnePlus GM1910, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

