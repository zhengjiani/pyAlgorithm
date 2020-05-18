# -*- encoding: utf-8 -*-
"""
@File    : 2D-Array.py
@Time    : 2020/5/16 11:45 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# 插入值
T.insert(2,[0,5,11,13,6])
# 删除值
del T[3]
for r in T:
    for c in r:
        print(c,end=" ")
    print()