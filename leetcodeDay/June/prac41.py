# -*- encoding: utf-8 -*-
"""
@File    : prac41.py
@Time    : 2020/6/27 10:21 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution1:
    """哈希表"""
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num-1] = -abs(nums[num-1])

        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1

class Solution2:
    """置换"""
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

if __name__ == '__main__':
    nums = [1,2,0]
    # sl = Solution1()
    sl2 = Solution2()
    # print(sl.firstMissingPositive(nums))
    print(sl2.firstMissingPositive(nums))