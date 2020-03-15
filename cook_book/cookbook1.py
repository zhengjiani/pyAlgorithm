# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 11:20
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
字典
OrderedDict OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候，
它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
"""
from collections import defaultdict
#字典中的键映射多个值
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
d1 = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d2 = defaultdict(set)
d2['a'].add(1)
d2['b'].add(2)
# 值得初始化
# d3 = defaultdict(list)
# for key,value in pairs:
#     d[key].append(value)

# 有序字典
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key,d[key])
import json
json.dumps(d)
# 字典中执行一些计算操作（求最小值、最大值、排序）
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 使用 zip() 函数先将键和值反转过来
min_price = min(zip(prices.values(),prices.keys()))
#  min_price is (10.75, 'FB')
# 根据字典值对字典排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
