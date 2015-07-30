# sampling-according-to-probability-distribution

test_random

# 问题

基本问题是这样的：当我们扔一个骰子的时候是等概率的出现数字。那这个问题模拟。但我们能不能模拟不等概率的骰子呢。

#思路

## 最简单

给定一组序列 l = [(4,0.4),(3,0.3),(2,0.2),(1,0.1)]。

对应数字:出现概率

基于此最简单的思路 看代码。

    def random_distr(l):
        r = random.uniform(0, sum([x[1] for x in l]))
        s = 0
        for num,(item, prob) in enumerate(l):
            s += prob
            if s >= r:
                return num
        return l[-1]

思路很明确了。随机一个数n(假定0-1之间)，然后从0开始加l的概率指导大于n为止。


`弊端`

这个方法的复杂度是 空间复杂度是O(N)，时间复杂度是O(N)。显然不是最好解。

test_walk.
引用别人的代码。实现了walk 的alias method。


这里别人提出了个二维的维度来思考问题。

比如权重为 10,20,30,40. key 为ABCD.

则为

    10  AAAAAAAAAA
    20  BBBBBBBBBB BBBBBBBBBB
    30  CCCCCCCCCC CCCCCCCCCC CCCCCCCCCC
    40  DDDDDDDDDD DDDDDDDDDD DDDDDDDDDD DDDDDDDDDD

分割并重新安排后。

    AAAAAAAAAA DDDDDDDDDDDDDDD  -- 10 A + 15 D = 40% A + 60% D
    BBBBBBBBBBBBBBBBBBBB DDDDD  -- 20 B + 5 D  = 80% B + 20% D
    CCCCCCCCCCCCCCCCCCCCCCCCC   -- 25 C        = 100% C
    DDDDDDDDDDDDDDDDDDDD CCCCC  -- 20 D + 5 C  = 80% D + 20% C


那么随机的过程变为了，随机一个数字 n 比如1，随机一个0-1的概率x。那么如果x > 0.4 ,则为d，如果小于则为a。

这样空间负责为O(N),时间复杂度为O(1).

