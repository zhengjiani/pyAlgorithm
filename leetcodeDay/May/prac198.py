# -*- encoding: utf-8 -*-
"""
@File    : prac198.py
@Time    : 2020/5/29 9:56 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """动态规划+数组"""
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[size-1]


class Solution1:
    """滚动数组
    在每个时刻只需要存储前两间房屋的最高总金额
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first,second = nums[0],max(nums[0],nums[1])
        for i in range(2,size):
            first,second = second,max(first+nums[i],second)
        return second
if __name__ == '__main__':
    nums = [1,2,3,1]
    sl = Solution()
    print(sl.rob(nums))