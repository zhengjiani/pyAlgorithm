# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 10:51
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from functools import reduce
def mysum(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return n-1 + mysum(n-1)
if __name__ == "__main__":
    chars = 'abcdefghijklmnopqrstuvwxyz'
    word = 'cad'
    print(mysum(5))
    # res = []
    # for i in range(len(word)):
    #     res.append(mysum(chars.index(word[i])+1))
    # print(res)
    # r = reduce(lambda x,y:x*y,res)
    # print(r)


