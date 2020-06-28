# -*- encoding: utf-8 -*-
"""
@File    : prac209.py
@Time    : 2020/6/28 2:49 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """双指针解法"""
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        sums = 0
        while end < n:
            sums += nums[end]
            while sums >= s:
                ans = min(ans, end - start + 1)
                sums -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n+1 else ans


if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    sl = Solution()
    print(sl.minSubArrayLen(s, nums))