# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 17:01
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
def seq_search(items,key):
    """顺序查找"""
    for index,item in enumerate(items):
        if item == key:
            return index
    return -1
def bin_search(items,key):
    """折半查找"""
    start,end = 0,len(items)-1
    while start <= end:
        mid = (start + end)//2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid -1
        else:
            return mid