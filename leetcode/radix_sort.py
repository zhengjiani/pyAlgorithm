# -*- encoding: utf-8 -*-
"""
@File    : radix_sort.py
@Time    : 2020/1/22 11:14 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 基数排序
def get_digit(num,i):
    # i=0 个位1 十位 2 百位
    return num // (10 ** i) % 10

# num = 12345
def int2list(num):
    li = []
    while num > 0:
        li.append(num % 10)
        num = num // 10
    li.reverse()

def reverse_list(li):
    n = len(li)
    for i in range(len(li)//2):
        li[i],li[n-i-1] = li[n-i-1],li[i]
    return li

def reverse_int(num):
    is_neg = False
    if num < 0:
        is_neg = True
        num = -1 * num
    res = 0
    while num > 0:
        res = res * 10
        res += num % 10
        num = num // 10
    if is_neg:
        res = res * -1
    return res

print(reverse_int(123001))
def radix_sort(li):
    max_num = max(li)
    i = 0
    while (10 ** i <= max_num):
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = val // (10 ** i) % 10
            buckets[digit].append(val)
        li.clear()
        for bucket in buckets:
            for val in bucket:
                li.append(val)
        i += 1