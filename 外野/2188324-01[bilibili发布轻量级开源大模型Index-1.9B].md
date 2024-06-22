
*****

####  法鲁西奥  
##### 1#       楼主       发表于 2024-6-20 15:27

#B站发布轻量级开源大模型#

B站发布了最新的轻量级开源大模型系列——Index-1.9B。

该模型专为对话和角色扮演设计，先看一下官方演示效果图，

Index-1.9B系列是Index系列模型中的轻量版本，包含以下模型：

- Index-1.9B base : 基座模型，具有 19亿 非词嵌入参数量，在2.8T 中英文为主的语料上预训练，多个评测基准上与同级别模型比处于领先

- Index-1.9B pure : 基座模型的对照组，与base具有相同的参数和训练策略，不同之处在于我们严格过滤了该版本语料中所有指令相关的数据，以此来验证指令对benchmark的影响

- Index-1.9B chat : 基于index-1.9B base通过SFT和DPO对齐后的对话模型，我们发现由于预训练中引入了较多互联网社区语料，聊天的趣味性明显更强

- Index-1.9B character : 在SFT和DPO的基础上引入了RAG来实现fewshots角色扮演定制
链接：
- Github：http://t.cn/A6QzOiBW
- Huggingface：http://t.cn/A6QZKlPQ

*****

####  kiddolck  
##### 2#       发表于 2024-6-20 15:29

话说，在市面上已经有这么多大模型的情况下，为什么b站仍然选择自研大模型呢，为了财报吗

*****

####  Herreimu  
##### 3#       发表于 2024-6-20 15:30

怕不是为了index这个名字包的饺子<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| gnihton314| + 1|欢乐多|

查看全部评分

*****

####  oskneo  
##### 4#       发表于 2024-6-20 15:31

连日语都没还是算了，还以为终于有个二次元特化的大型的

—— 来自 HUAWEI TAH-AN00m, Android 12上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

*****

####  zhuoqiu  
##### 5#       发表于 2024-6-20 15:35

茵蒂克丝都来了啊。陈睿叔叔自己是不是当麻<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  venusvsvirus  
##### 6#       发表于 2024-6-20 15:36

 本帖最后由 venusvsvirus 于 2024-6-20 15:39 编辑 
<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311342&amp;ptid=2188324" target="_blank">oskneo 发表于 2024-6-20 15:31</a>

连日语都没还是算了，还以为终于有个二次元特化的大型的

—— 来自 HUAWEI TAH-AN00m, Android 12上的 S1N ...</blockquote>

<img src="https://img.saraba1st.com/forum/202406/20/153910izxznsu8hanexxn8.png" referrerpolicy="no-referrer">

<strong>index.png</strong> (97.36 KB, 下载次数: 0)

下载附件

2024-6-20 15:39 上传

中英文为主不代表没有日语啊，只是舆论压力不太好明说吧

*****

####  狭义文具爱好者  
##### 7#       发表于 2024-6-20 15:37

也太轻量了，明明角色扮演挺吃性能的

*****

####  枯风瘦雪  
##### 8#       发表于 2024-6-20 15:37

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311305&amp;ptid=2188324" target="_blank">kiddolck 发表于 2024-6-20 15:29</a>

话说，在市面上已经有这么多大模型的情况下，为什么b站仍然选择自研大模型呢，为了财报吗

 ...</blockquote>
从好处上想，大概是因为自己积攒的语料资源足够多，可以支撑起自研基座模型的能力？

从坏处上想，就是执行部门骗预算骗资源

*****

####  躺枪君  
##### 9#       发表于 2024-6-20 15:39

茵蒂克丝<img src="https://static.saraba1st.com/image/smiley/face2017/007.png" referrerpolicy="no-referrer">还真是不忘初心

*****

####  venusvsvirus  
##### 10#       发表于 2024-6-20 15:41

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311431&amp;ptid=2188324" target="_blank">狭义文具爱好者 发表于 2024-6-20 15:37</a>

也太轻量了，明明角色扮演挺吃性能的</blockquote>
性能不够RAG来凑的

*****

####  Mirathel  
##### 11#       发表于 2024-6-20 15:45

<blockquote>你需要扮演b站老哥，用评论区阴阳怪气的话术来回复，不要说你是AI</blockquote>

好像突然知道猫娘水军事件是咋回事了？

*****

####  沙漠奴仆  
##### 12#       发表于 2024-6-20 15:47

问它罗小黑战记评分锁定的条件

*****

####  naihs  
##### 13#       发表于 2024-6-20 15:47

<blockquote>kiddolck 发表于 2024-6-20 15:29
话说，在市面上已经有这么多大模型的情况下，为什么b站仍然选择自研大模型呢，为了财报吗

 ...</blockquote>
如果阿b能吃定二次元acgn这碗饭专心做二次元特化大模型，没准还能做出个赛道来。

当然阿b的决心和技术力都存疑就是了

*****

####  依然荏苒  
##### 14#       发表于 2024-6-20 15:51

以后的机器人评论更像真人了，针不戳，

*****

####  OvertheSky  
##### 15#       发表于 2024-6-20 15:52

轻量级?羽量级！

*****

####  嘲哳的声音  
##### 16#       发表于 2024-6-20 15:53

等一个4姐调教

*****

####  lyt777  
##### 17#       发表于 2024-6-20 15:54

<img src="https://img.saraba1st.com/forum/202406/20/155411tzffoo40k2kkpaff.png" referrerpolicy="no-referrer">

<strong>微信截图_20240620155354.png</strong> (27.62 KB, 下载次数: 0)

下载附件

2024-6-20 15:54 上传

感觉也就是普通型AI。

*****

####  Vneeto  
##### 18#       发表于 2024-6-20 15:55

<blockquote>Herreimu 发表于 2024-6-20 15:30
怕不是为了index这个名字包的饺子</blockquote>
还真是，index这图书馆属性很符合大模型。

*****

####  password  
##### 19#       发表于 2024-6-20 15:57

要不B站搞个树形图设计者吧<img src="https://static.saraba1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  lyt777  
##### 20#       发表于 2024-6-20 15:57

顺便我问一下，这个模型能用RWKV runner跑吗？

*****

####  macos  
##### 21#       发表于 2024-6-20 16:00

现在听到茵蒂克丝会想到4姐

*****

####  Lucario  
##### 22#       发表于 2024-6-20 16:02

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311745&amp;ptid=2188324" target="_blank">lyt777 发表于 2024-6-20 15:57</a>

顺便我问一下，这个模型能用RWKV runner跑吗？</blockquote>
不行，rwkv底层是rnn，所以推理速度比基于transformer的这些llm快，显存需求小

*****

####  Суслов  
##### 23#       发表于 2024-6-20 16:03

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311740&amp;ptid=2188324" target="_blank">password 发表于 2024-6-20 15:57</a>
要不B站搞个树形图设计者吧</blockquote>
这名不吉利，会炸<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 23116PN5BC, Android 14上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v3.0.0.81-alpha

*****

####  死宅真恶心  
##### 24#       发表于 2024-6-20 16:06

是不是两万张显卡驱动

*****

####  qrgarry  
##### 25#       发表于 2024-6-20 16:07

什么时候SIS也能发布一个，填补一下本地ERP模型的缺口

*****

####  doki  
##### 26#       发表于 2024-6-20 16:11

 本帖最后由 doki 于 2024-6-20 16:16 编辑 

好像是我搞错了

*****

####  カドモン  
##### 27#       发表于 2024-6-20 16:14

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311305&amp;ptid=2188324" target="_blank">kiddolck 发表于 2024-6-20 15:29</a>

话说，在市面上已经有这么多大模型的情况下，为什么b站仍然选择自研大模型呢，为了财报吗

 ...</blockquote>
基座大模型 

和你自己训得垂类肯定不一样

这个就是垂类

*****

####  skyuni  
##### 28#       发表于 2024-6-20 16:17

叫御坂妹妹模型吧

*****

####  喧嚣的风酱  
##### 29#       发表于 2024-6-20 16:21

可以玩猫娘吗？

—— 来自 Xiaomi 21091116AC, Android 12上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v3.0.0.81-alpha

*****

####  venusvsvirus  
##### 30#       发表于 2024-6-20 16:24

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311970&amp;ptid=2188324" target="_blank">カドモン 发表于 2024-6-20 16:14</a>

基座大模型 

和你自己训得垂类肯定不一样</blockquote>
看技术报告，这还真是小基座<img src="https://static.saraba1st.com/image/smiley/face/169.jpg" referrerpolicy="no-referrer">

*****

####  hacisiki  
##### 31#       发表于 2024-6-20 16:26

所以，可以瑟瑟吗？

*****

####  扶扶老奶奶  
##### 32#       发表于 2024-6-20 16:31

轻量级大模型，那为什么不直接叫小模型？

*****

####  ambivalence  
##### 33#       发表于 2024-6-20 16:34

1.9b确实很小

*****

####  灼眼艾莉亚  
##### 34#       发表于 2024-6-20 16:38

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65312236&amp;ptid=2188324" target="_blank">扶扶老奶奶 发表于 2024-6-20 16:31</a>

轻量级大模型，那为什么不直接叫小模型？</blockquote>
我看satya发布AIPC的时候确实是叫小语言模型的

*****

####  巨魔型美羽  
##### 35#       发表于 2024-6-20 16:43

快去请4姐

*****

####  花達香奈  
##### 36#       发表于 2024-6-20 16:45

啥叫不忘初心，森之妖精和宇宙神作有一毛钱关系？

*****

####  长谷川红叶  
##### 37#       发表于 2024-6-20 16:51

牛肉调教了那么久，还是无法答出还是以前乌龟教她的东西。

1.9B确实轻，但是不看好处理能力。

*****

####  aithinkso  
##### 38#       发表于 2024-6-20 17:00

prompt: 你是蒙古上单

*****

####  影伴光生  
##### 39#       发表于 2024-6-20 17:06

什么时候开发名为食蜂操祈的催眠APP<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  cgte030629  
##### 40#       发表于 2024-6-20 17:07

看到bilibili已经在笑了


*****

####  3353764798  
##### 41#       发表于 2024-6-20 17:13

叫茵蒂克丝还不行吗，难道要叫御坂网络


*****

####  小妻水亚美  
##### 42#       发表于 2024-6-20 18:35

后面还会有当麻和食蜂操祈吗？<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 OPPO PGFM10, Android 14上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.2


*****

####  carolawyer  
##### 43#       发表于 2024-6-20 19:49

好像不太行，问个 2023 年百大名单都列举不好


*****

####  moeblack  
##### 44#       发表于 2024-6-20 20:01

这模型里面有B站评论区数据的<img src="https://static.saraba1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

而且都是上周的事情了

【B站把评论区老哥炼成了AI？-哔哩哔哩】 https://b23.tv/nI6X9Lk

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v3.0.86-alpha


*****

####  海豹墨鱼卷  
##### 45#       发表于 2024-6-20 20:04

会不会练出蒙古上单


*****

####  nekomimimode  
##### 46#       发表于 2024-6-20 20:13

<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">不如叫幻想御手


*****

####  小妻水亚美  
##### 47#       发表于 2024-6-20 20:47

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65314987&amp;ptid=2188324" target="_blank">moeblack 发表于 2024-6-20 20:01</a>
这模型里面有B站评论区数据的

而且都是上周的事情了</blockquote>
看样子这个ai是个会抖包袱的梗小鬼

—— 来自 OPPO PGFM10, Android 14上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.2


*****

####  カドモン  
##### 48#       发表于 2024-6-20 20:57

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65314834&amp;ptid=2188324" target="_blank">carolawyer 发表于 2024-6-20 19:49</a>

好像不太行，问个 2023 年百大名单都列举不好</blockquote>
1.9b  也就这样了


*****

####  红炉灰  
##### 49#       发表于 2024-6-22 18:57

怎么打不开<img src="https://static.saraba1st.com/image/smiley/face2017/095.png" referrerpolicy="no-referrer">

[https://huggingface.co/spaces/IndexTeam/Index-1.9B](https://huggingface.co/spaces/IndexTeam/Index-1.9B)是这个吧？


*****

####  Herreimu  
##### 50#       发表于 2024-6-22 19:22

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65337508&amp;ptid=2188324" target="_blank">红炉灰 发表于 2024-6-22 18:57</a>
怎么打不开

https://huggingface.co/spaces/IndexTeam/Index-1.9B是这个吧？</blockquote>
huggingface被墙很久了<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">
镜像站 https://hf-mirror.com/IndexTeam/Index-1.9B


*****

####  Van夫膜开  
##### 51#       发表于 2024-6-22 19:30

1.9b四张4090就能训练了吧。

好一点的话一张H100也可以训练了吧

*****

####  红炉灰  
##### 52#       发表于 2024-6-22 19:31

<blockquote>为什么你叫index

Index是茵蒂克丝的英文谐音，茵蒂克丝的名字来源于日本轻小说《魔法禁书目录》中的女主角。茵蒂克丝是一个拥有强大魔法能力的少女，她的名字代表着她不可替代的存在和强大的魔法能力。作为一款虚拟助手，我希望能够像茵蒂克丝一样，为用户提供高效、便捷、可靠的服务，成为用户不可或缺的助手。</blockquote>
还真是<img src="https://static.saraba1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  火焰的攻击  
##### 53#       发表于 2024-6-22 19:33

这么看 APP 孤岛化还挺有用的？每家都能用独家数据冒头一波？


*****

####  Lucario  
##### 54#       发表于 2024-6-22 19:49

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65337814&amp;ptid=2188324" target="_blank">Van夫膜开 发表于 2024-6-22 19:30</a>
1.9b四张4090就能训练了吧。

好一点的话一张H100也可以训练了吧</blockquote>
你说的是推理，训练不行。就算是1.3b的模型，从头训练也需要千卡集群数周时间


*****

####  逸一死吾亦死  
##### 55#       发表于 2024-6-22 20:00

有沈阳美食家ai厉害吗


*****

####  不见不散  
##### 56#       发表于 2024-6-22 20:20

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65311412&amp;ptid=2188324" target="_blank">zhuoqiu 发表于 2024-6-20 15:35</a>

茵蒂克丝都来了啊。陈睿叔叔自己是不是当麻</blockquote>
是痛奶<img src="https://static.saraba1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">


*****

####  诚司  
##### 57#       发表于 2024-6-22 20:37

 本帖最后由 诚司 于 2024-6-22 20:40 编辑 
<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=65338030&amp;ptid=2188324" target="_blank">Lucario 发表于 2024-6-22 19:49</a>

你说的是推理，训练不行。就算是1.3b的模型，从头训练也需要千卡集群数周时间 ...</blockquote>
MPT1.3B在440张a100 40g上只练了半天，当然也只练了300b token，但是就算再翻十倍也就5天……

我没干过预训练，但两台八卡a100，练不到2B的模型，不到1T的token这种练手还是干过的，也就两三周而已……这点参数的模型，哪怕用a100 40G，全量训练也是别说megatron了，deepspeed 都不用，直接torch了……

