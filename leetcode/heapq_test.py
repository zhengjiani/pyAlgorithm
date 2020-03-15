# -*- encoding: utf-8 -*-
"""
@File    : heapq_test.py
@Time    : 2020/1/14 4:02 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import heapq

li = [9,5,7,8,2,6,4,1,3]
# 建堆（小根堆）
heapq.heapify(li)
print(li)
heapq.heappush(li)