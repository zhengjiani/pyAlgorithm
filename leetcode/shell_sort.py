# -*- encoding: utf-8 -*-
"""
@File    : shell_sort.py
@Time    : 2020/1/21 3:15 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
def insert_sort_gap(li,d):
    for i in range(d,len(li)):
        tmp = li[i]
        j = i-d
        while j >= 0 and li[j] > tmp:
            li[j+d] = li[j]
            j -= d
        li[j+d] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        insert_sort_gap(li,d)
        d = d // 2