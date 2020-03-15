# -*- encoding: utf-8 -*-
"""
@File    : heap_sort.py
@Time    : 2020/1/14 2:22 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import random
# 堆排序
def sift(li,low,high):
    # li表示树，low表示树根，high表示树的最后一个节点的位置
    tmp = li[low]
    i = low
    j = 2 * i + 1 # 初始j指向空位的左孩子
    # i指向空位，j指向两个孩子
    while j <= high: # 循环退出的第二种情况：j>high,说明空位i是叶子节点
        if j+1 <= high and li[j] < li[j+1]: # 如果右孩子存在并且比左孩子大，指向右孩子
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else: # 循环退出的第一种情况：j位置的值都比tmp小，说明两个孩子都比tmp小
            break
    li[i] = tmp

def sift_small(li,low,high):
    # li表示树，low表示树根，high表示树的最后一个节点的位置
    tmp = li[low]
    i = low
    j = 2 * i + 1 # 初始j指向空位的左孩子
    # i指向空位，j指向两个孩子
    while j <= high: # 循环退出的第二种情况：j>high,说明空位i是叶子节点
        if j+1 <= high and li[j] > li[j+1]: # 如果右孩子存在并且比左孩子大，指向右孩子
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else: # 循环退出的第一种情况：j位置的值都比tmp大，说明两个孩子都比tmp小
            break
    li[i] = tmp
# 构造堆,要求是完全二叉树，整个堆最后一个元素的位置当作high
def heap_sort(li):
    n = len(li)
    # 1.构造堆
    for low in range(n//2-1, -1, -1):
        sift(li, low, n-1)
    # 2.挨个出数
    for high in range(n-1, -1, -1):
        li[0], li[high] = li[high], li[0] # 退休棋子
        sift(li, 0, high-1)

def heap_sort_small(li):
    n = len(li)
    # 1.构造堆
    for low in range(n//2-1, -1, -1):
        sift_small(li, low, n-1)
    # 2.挨个出数
    for high in range(n-1, -1, -1):
        li[0], li[high] = li[high], li[0] # 退休棋子
        sift_small(li, 0, high-1)
li = list(range(10))
random.shuffle(li)
print(li)
heap_sort(li)
print(li)
heap_sort_small(li)
print(li)

