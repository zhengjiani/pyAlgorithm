# -*- encoding: utf-8 -*-
"""
@File    : console_input.py
@Time    : 2020/7/8 9:32 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 机考中Python读取多行键盘输入的处理方式

# 多元输入-一行键盘输入
# 输入1 2 3
# 输出1 2 3
# n,k,m = map(int,input().split())
# print(n,k,m)

# 将输入转化为列表，以空格为分隔符
# 输入1 2 3
# 输出['1', '2', '3']
# line = list(map(str,input().split()))
# print(line)

# 将每行读取成矩阵的形式
# 输入1 2 3
# 输出[1, 2, 3]
# arr = input("")
# num = [int(n) for n in arr.split()]
# print(num)

# 多行（矩阵）键盘输入
# 读入二维矩阵适用于n*n矩阵
# 输入2
# 1 2
# 3 4
# 输出
# [['1', '2'], ['3', '4']]
# n = int(input())
# m = [[0]*n]*n
# for i in range(n):
#     m[i] = input().split(" ")
# print(m)

# 读入二维矩阵适用于n*任意列矩阵
# 输入2
# 1 2 3
# 4 5 6
# 输出
# [[1, 2, 3], [4, 5, 6]]
# n = int(input())
# m = []
# for i in range(n):
#     m.append(list(map(int,input().split(" "))))
# print(m)

# 读取多行输入，不知道行数，但是以换行符结束
# 输入 1 2 3
#     1 2 3
#
# 输出 ['1 2 3', '1 2 3']
# s = []
# for line in iter(input,''):
#     s.append(line.replace(',',''))
# print(s)

# 输入多行数据，返回二维list
# 1 2 3
# 1 2 3
#
# [['1', '2', '3'], ['1', '2', '3']]
try:
    mx = []
    while True:
        m = input().strip()
        if m == '':
            break
        m = list(m.split())
        mx.append(m)
    print(mx)
except:
    pass

# 不指定行数，但是每输入一行就处理一行，持续等待输入
# 1 2 3
# 1 2 3
#
# [['1', '2', '3'], ['1', '2', '3']]

try:
    ssn = []
    while True:
        sn = input().strip()
        if sn == '':
            break
        sn = list(sn.split())
        ssn.append(sn)
    print(ssn)
except:
    pass