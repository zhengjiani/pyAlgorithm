# -*- encoding: utf-8 -*-
"""
@File    : quick_sort.py
@Time    : 2020/1/14 11:01 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from random import random


def _quick_sort(li, left, right):
    if left < right:  # 待排序至少有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, 0, mid - 1)
        _quick_sort(li, mid + 1, len(li) - 1)


def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


def partition(li, left, right):
    # 取列表的第一个元素为枢轴
    tmp = li[0]
    while left < right:
        # 当右边元素大于枢轴的时候，不动
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        # 当左边元素小于枢轴的时候，不动
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    # left和right相等的位置就是mid
    li[left] = tmp
    return left


# 随机分区，防止倒序的情况
def random_partition(li, left, right):
    i = random.randint(left, right)
    print(i)
    li[i], li[left] = li[left], li[i]
    return partition(li, left, right)


# 切片的方法
def _quick_sort2(li):
    if len(li) < 2:
        return li
    tmp = li[0]
    left = [v for v in li[1:] if v <= tmp]
    right = [v for v in li[1:] if v > tmp]
    left = _quick_sort2(left)
    right = _quick_sort2(right)
    return left + [tmp] + right