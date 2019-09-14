# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 10:58
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
# 从一个集合中获得最大或者最小的N个元素列表
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 最大3个元素
print(heapq.nlargest(3,nums))
# 最小3个元素
print(heapq.nsmallest(3,nums))
# 用于字典中，以price值进行比较
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3,portfolio,key = lambda s:s['price'])
# 实现一个优先级队列
# 仔细观察可以发现，第一个 pop() 操作返回优先级最高的元素。
# 另外注意到如果两个有着相同优先级的元素（ foo 和 grok ），pop 操作按照它们被插入到队列的顺序返回的
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)