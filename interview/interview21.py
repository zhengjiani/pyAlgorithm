# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 15:13
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
丑数：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution(self,index):
        ugly_num = []
        i = 1
        count = 0
        while True:
            temp = i

