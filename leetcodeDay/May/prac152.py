# -*- encoding: utf-8 -*-
"""
@File    : prac152.py
@Time    : 2020/5/18 8:25 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float("-inf")
        for i in range(1,n+1):
            temp = a
            a = max(a*nums[i-1],b*nums[i-1],nums[i-1])
            b = min(b*nums[i-1],temp*nums[i-1],nums[i-1])
            ans = max(a,ans)
        return ans


if __name__ == '__main__':
    nums = [2,3,-2,4]
    s = Solution()
    print(s.maxProduct(nums))
