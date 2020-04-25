# -*- encoding: utf-8 -*-
"""
@File    : prac46.py
@Time    : 2020/4/25 8:51 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """回溯"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res
if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    print(s.permute(nums))