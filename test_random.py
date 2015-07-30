#!/usr/env/bin python
# coding=utf8
from __future__ import unicode_literals

__author__ = 'Dongjian'
import random
def random_distr(l):
    r = random.uniform(0, sum([x[1] for x in l]))
    s = 0
    for num,(item, prob) in enumerate(l):
        s += prob
        if s >= r:
            return num
    return l[-1]



l = [(4,0.4),(3,0.3),(2,0.2),(1,0.1)]

def generate_random(l):
    # 实现将一个列表全部随机出来，每次随机出来的数字pop。效率可以优化。
    for _ in xrange(len(l)):
        rrsn = random_distr(l)
        l[rrsn],l[-1] = l[-1],l[rrsn]
        yield l.pop()[0]

for i in generate_random(l):
    print i

