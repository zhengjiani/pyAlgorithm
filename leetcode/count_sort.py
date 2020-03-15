# -*- encoding: utf-8 -*-
"""
@File    : count_sort.py
@Time    : 2020/1/22 10:45 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 计数排序
import random

def count_sort(li,max_num=100):
    count = [0 for _ in range(max_num+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for i,v in enumerate(count): #表示i这个数出现了v次
        for _ in range(v):
            li.append(i)

li = [random.randint(0,100) for _ in range(100000)]
count_sort(li)