# -*- encoding: utf-8 -*-
"""
@File    : bin_search.py
@Time    : 2020/1/9 2:25 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from random import random


def bin_search(li,val):
    """
    二分查找,log_2(n)
    :param li:
    :param val:
    :return:
    """
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

li = list(range(0,200000,2))
# 打乱
random.shuffle(li)
bin_search(li, 2000001)