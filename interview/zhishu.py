# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 15:44
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
N以内素数
"""
# 常用方法
import math
import sys

def prime(n):
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
# 优化方法
def prime1(n):
    """
    除了2以外,其余的偶数不可能是素数
    除了3以外，其余能被3整除的都是合数
    除了5以外，其余能被5整除的都是合数
    :param n:
    :return:
    """
    if n%2 == 0:
        return n == 2
    if n%3 == 0:
        return n == 3
    if n%5 == 0:
        return n == 5
    for p in range(7,int(math.sqrt(n))+1,2):
        if n%p ==0:
            return 0
    return 1
# 埃氏筛法
# 构造一个大小为n的列表，初值都是1，每发现一个素数，
# 我们把所有它的倍数都置为0，直到发现下一个为1的数为素数。这就是书中提到的埃氏筛法。
def prime2(n):
    flag = [1]*(n+2)
    p = 2
    while (p<=n):
        print(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
if __name__ == "__main__":
    # sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径
    # n = int(sys.argv[1])
    n=14
    # for i in range(2,n+1):
    #     if prime(i):
    #         print(i)
    prime2(14)

