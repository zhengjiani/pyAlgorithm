# -*- encoding: utf-8 -*-
"""
@File    : prac35.py
@Time    : 2019/11/24 10:56 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
"""
题目描述：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""
class Solution:
    def searchInsert(self,nums,target):
        """
        :param nums: List[int]
        :param target:int
        :return:int
        """
        for index,each in enumerate(nums):
            if target == each:
                return index
            else:
                nums.append(target)
                nums = sorted(nums)
                return nums.index(target)

if __name__ == "__main__":
    nums = [1,3,5,6]
    nums1 = [1,3,5,6]
    s = Solution()
    print(s.searchInsert(nums, 5))
    print(s.searchInsert(nums1, 7))

