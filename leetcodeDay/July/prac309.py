# -*- encoding: utf-8 -*-
"""
@File    : prac309.py
@Time    : 2020/7/10 11:21 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """使用动态规划维护在股市中每一天结束后可以获得的累计最大收益"""
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # dp[i][0]手上持有股票的最大收益
        # dp[i][1]手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp[i][2]手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0]] + [[0]*3 for _ in range(n-1)]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])

        return max(dp[n-1][1], dp[n-1][2])


class Solution1:
    """空间优化"""
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        f0,f1,f2 = -prices[0],0,0
        for i in range(1,n):
            newf0 = max(f0,f2-prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1,f2)
            f0,f1,f2 = newf0,newf1,newf2
        return max(f1,f2)
if __name__ == '__main__':
    prices = [1,2,3,0,2]
    sl = Solution()
    print(sl.maxProfit(prices))