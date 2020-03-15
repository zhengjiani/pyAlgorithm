# -*- encoding: utf-8 -*-
"""
@File    : bubble_sort.py
@Time    : 2020/1/9 3:41 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from random import random


def bubble_sort(li):
    for i in range(len(li)-1):#i表示第n趟 一共n或者n-1趟
        exchange = False
        for j in range(len(li)-i-1):#第i趟 无序区[0,n-i-1] j表示箭头0~n-i-2
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            break
# 已经有序的情况
li = list(range(10000))
random.shuffle(li)
