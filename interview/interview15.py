# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 11:00
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
连续子数组的最大和
步骤：定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和，遍历数组中的每个元素，遍历到第i个数
如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值
如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值
判断累加值是否大于最大值，如果大于最大值，则最大和更新，否则，继续保留之前的最大和
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = array[0]
        pre_num = 0
        for i in array:
            if pre_num < 0:
                pre_num = i
            else:
                pre_num += i
            if pre_num > max_sum:
                max_sum = pre_num
        return max_sum