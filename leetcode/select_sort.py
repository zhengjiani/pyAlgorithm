# -*- encoding: utf-8 -*-
"""
@File    : select_sort.py
@Time    : 2020/1/9 3:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import random
def get_min_pos(li):
    min_pos = 0
    for i in range(1,len(li)):
        if li[i] < li[min_pos]:
            min_pos = i
    return min_pos

def select_sort(li):
    for i in range(len(li)-1): #n或者n-1趟
        # 第i趟无序区范围i～最后
        min_pos = i # min_pos更新为无序区最小值位置
        for j in range(i+1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]

li = list(range(10000))
random.shuffle(li)
select_sort(li)