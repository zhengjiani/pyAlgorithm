# -*- encoding: utf-8 -*-
"""
@File    : prac983.py
@Time    : 2020/5/6 8:46 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from functools import lru_cache
from typing import List


class Solution:
    """记忆化搜索(日期变量型)
        需要遍历一年中所有天数
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1,7,30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i+d)+c for c,d in zip(costs,durations))
            else:
                return dp(i+1)
        return dp(1)

class Solution1:
    """记忆化搜索(窗口变量型)"""
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        durations = [1,7,30]

        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            ans = 10**9
            j = i
            for c,d in zip(costs,durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans,dp(j) + c)
            return ans
        return dp(0)

if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    s = Solution()
    print(s.mincostTickets(days,costs))


