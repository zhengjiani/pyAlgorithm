# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:29
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
统计一个数字在排序数组中出现的次数。
例如输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3，由于3在这个数组中出现了4次，因此输出4。
输入：[1, 2, 3, 3, 3, 3, 4, 5] ,  3
输出：4
"""
def find_min(nums,k):
    """
    :param nums: List
    :param k: int
    :return: type[int]
    """
    n = len(nums)
    if n < 0:
        return 0
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        #向右二分
        if nums[mid] > k :
            r = mid - 1
        else:
            l = mid + 1
    if nums[l-1] != k :
        return 0
    end = l
    l = 0
    r = end
    #找左边重复的
    while l < r :
        mid = (l + r)//2
        if nums[mid] < k:
            l = mid +1
        else:
            r = mid
    return end - l

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    print(find_min(nums,1))