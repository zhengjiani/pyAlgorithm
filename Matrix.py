# -*- encoding: utf-8 -*-
"""
@File    : Matrix.py
@Time    : 2020/5/16 12:12 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

# 矩阵格式打印
m = reshape(a,(7,5))
print(m)

# 增加行
m_r = append(m,[['Avg',12,15,13,11]],0)
print(m_r)
# 增加列
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(m_c)
# 删除行
m = delete(m,[2],0)
print(m)