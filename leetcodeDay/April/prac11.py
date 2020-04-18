# -*- encoding: utf-8 -*-
"""
@File    : prac11.py
@Time    : 2020/4/18 9:22 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
容纳的水量 = 两个指针指向的数字中较小值*指针之间的距离
"""
from typing import List


class Solution:
    """双指针解法"""
    def maxArea(self, height: List[int]) -> int:
        l, r = 0,len(height)-1
        ans = 0
        while l < r:
            area = min(height[l],height[r])*(r-l)
            ans = max(ans,area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
if __name__ == '__main__':
    lis = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print(s.maxArea(lis))