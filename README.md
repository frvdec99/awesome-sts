# awesome-sts
Something interesting about slay the spire

有关尖塔局数、胜率、连胜的讨论详情见https://tieba.baidu.com/p/8517271507, 原帖分为4个章节, 对应Chapter1-4目录的代码：
假设对局之间相互独立, 且每局满足参数为胜率y的伯努利分布

1. 已知胜率y和最高连胜x, 求局数z的期望E(z), 代码见chapter1/expect.py
2. 已知胜率y和局数z, 求最高连胜x的期望E(x), 也可以用来求解原贴中的概率P(x), 代码见chapter2/normal.py
3. 已知局数z和z局胜率u, 小样本下置信度为1-a的置信区间估计的代码见chapter3/little.py, 大样本下置信度为1-a的置信区间近似估计的代码见chapter3/big.py
4. 已知胜率y和局数z, 允许修改某一局的结果使得连胜最大化, 求最高连胜x的期望E(x), 代码见chapter4/slOnce.cpp
