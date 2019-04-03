# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:28
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
例如，在数组[-3, -1, 1, 3, 5]中，数字3和它的下标相等。
输入：[-3, -1, 1, 3, 5]
输出：3
注意:如果不存在，则返回-1。
"""
def getNumberSameAsIndex(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        mid = (left+right)//2 #中位值向下取整
        if nums[mid]<mid:
            left = mid +1
        else:
            right = mid
        if right==nums[right]:
            return right
    return -1


if __name__ == '__main__':
    nums = [-3, -1, 1, 3, 5]
    print(getNumberSameAsIndex(nums))