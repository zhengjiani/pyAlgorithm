# -*- encoding: utf-8 -*-
"""
@File    : recurision.py
@Time    : 2020/1/3 5:55 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from leetcode.cal_time import *

def fibnacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

@cal_time
def fib(n):
    return fibnacci(n)

@cal_time
def fib2(n):
    li = [1, 1]
    for i in range(2, n+1):
        li.append(li[-1]+li[-2])
    return li[n]

def fib3(n):
    a = 1
    b = 1
    c = 1
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
    return c

print(fib(21))