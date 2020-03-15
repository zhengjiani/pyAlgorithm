# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 16:38
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。
请找出数组中任意一个重复的数，但不能修改输入的数组。
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。
返回 2 或 3。
"""
def duplicate(nums):
    l = 1
    r = len(nums)-1
    while l < r :
        mid = (l + r)//2
        count = 0
        for item in nums:
            if l <= item <=mid:
                count += 1
        if count > mid - l + 1:
            r = mid
        else:
            l = mid + 1
    return r
if __name__ == '__main__':
    nums = [2,1,5,4,3,2,6,7]
    print(duplicate(nums))