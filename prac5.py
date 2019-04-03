# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:30
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
    寻找缺失元素的二分法
    一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n-1之内。
    在范围0到n-1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
    Input：[0,1,2,4]
    output：3
"""
def get_missing_number(nums):
    """
    二分法
    :param nums:
    :return: int
    """
    l = 0
    r = len(nums)-1
    if r < 0:
        return 0
    if r==nums[r]:
        return r + 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == mid:
            l = mid + 1
        else:
            r = mid
    return nums[r] - 1


if __name__ == "__main__":
    nums = [0,1,2,4]
    num = get_missing_number(nums)
    print(num)