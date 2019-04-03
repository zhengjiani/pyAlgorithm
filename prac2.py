# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:27
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
注意：如果某些数字不在 0∼n−1的范围内，或数组中不包含重复数字，则返回 -1；
"""
def duplicateInArray(nums):
    for index,value in enumerate(nums):
        if index !=value:
            nums[index],nums[value] = nums[value],nums[index]
        if index !=value and value == nums[value]:
            return nums[index]

if __name__ == '__main__':
    nums = [0,1,2,3,4,6,4]
    print(duplicateInArray(nums))#4