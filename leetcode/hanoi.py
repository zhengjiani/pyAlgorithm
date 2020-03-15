# -*- encoding: utf-8 -*-
"""
@File    : hanoi.py
@Time    : 2020/1/9 1:32 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
def hanoi(n,A,B,C):
    hanoi(n-1,A,C,B)
    print('%s->%s' % (A,C))
    hanoi(n-1,B,A,C)
hanoi(3,'A','B','C')