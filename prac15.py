# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:48
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
有N片雪花，每片雪花由六个角组成，每个角都有长度。第i片雪花六个角的长度从某个角开始顺时针依次记为ai,1,ai,2,…,ai,6。
因为雪花的形状是封闭的环形，所以从任何一个角开始顺时针或逆时针往后记录长度，得到的六元组都代表形状相同的雪花。
例如ai,1,ai,2,…,ai,6和ai,2,ai,3,…,ai,6，ai,1就是形状相同的雪花。ai,1,ai,2,…,ai,6和ai,6,ai,5,…,ai,1也是形状相同的雪花。
我们称两片雪花形状相同，当且仅当它们各自从某一角开始顺时针或逆时针记录长度，能得到两个相同的六元组。求这N片雪花中是否存在两片形状相同的雪花。
"""


def cmp(a,b):
    for i in range(6):
        if a[i]<b[i]:
            return True
        elif a[i]>b[i]:
            return False
    return True

def issame(a,b):
    for i in range(6):
        if a[i] != b[i]:
            return False
    return True

#最小表示法
def get_min(a):
    i = 0
    j = 1
    k = 0
    while i<6 and j<6 and k<6:
        t1 = (i+k) % 6
        t2 = (j+k) % 6
        if a[t1] == a[t2]:
            k += 1
        elif a[t1] < a[t2]:
            j += k+1
            k = 0
        else:
            i += k+1
            k = 0
        if i==j:
            j +=1
    s = min(i,j)
    k = 0
    b = ''
    while k<6:
        s += 1
        b += a[s%6]
        k += 1
    #六个角的最小表示法相同
    for i in range(6):
        a[i] = b[i]
#对任意两片雪花的六个角求和并映射
def get_hash(a):
    sum = 0
    mod = 9999991
    for i in range(6):
        sum = (sum+a[i])%mod
    return sum

def get_unique(a,b):
    get_min(a)
    get_min(b)
    if cmp(a,b) == False:
        for i in range(6):
            a[i] = b[i]
def main():
    #列表生成式创建二维数组
    # a =[[0 for i in range(6)] for j in range(6)]
    # b =[[0 for i in range(6)] for j in range(6)]
    n = input()
    a = [[0 for i in range(int(n))] for j in range(6)]
    b = [[0 for i in range(int(n))] for 5-j in range(6)]
    for i in range(int(n)):
        get_unique(a[i],b[i])
    m = []
    for i in range(get_hash(a[i])):
        m.append(i)
    for x in m:
        siz = x
        #未完