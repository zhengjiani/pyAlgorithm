# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 8:29
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
第一个元素降序，第二个元素升序
"""
a = [[2,3],[4,1],[2,8],[2,1],[3,4]]
b = sorted(a,key=lambda x:(x[-1],x[0]))
print(b)