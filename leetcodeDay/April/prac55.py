# -*- encoding: utf-8 -*-
"""
@File    : prac55.py
@Time    : 2020/4/17 11:14 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n,rightmost = len(nums),0
        for i in range(n):
            if i<=rightmost:
                rightmost = max(i+nums[i],rightmost)
                if rightmost >= n - 1:
                    return True
        return False

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.canJump(nums))