# -*- encoding: utf-8 -*-
"""
@File    : top_k.py
@Time    : 2020/1/15 12:38 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 找前5个最大的,使用小根堆
# 使用内置heapq
import heapq

from leetcode.cal_time import cal_time

@cal_time
def func_1():
    li = [9,5,7,8,2,6,4,1,3]
    return heapq.nlargest(5,li)

@cal_time
def func_2():
    # 排序后切片
    li = [9, 5, 7, 8, 2, 6, 4, 1, 3]
    li.sort()
    return li[:3:-1]


@cal_time
def func_3():
    li = [9, 5, 7, 8, 2, 6, 4, 1, 3]
    _bubble_sort(li, 5)
    return li[:3:-1]


# 冒泡排序，只冒前5位
def _bubble_sort(li, k):
    for i in range(k):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break

print(func_1())
print(func_2())
print(func_3())