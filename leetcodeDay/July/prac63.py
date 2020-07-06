# -*- encoding: utf-8 -*-
"""
@File    : prac63.py
@Time    : 2020/7/6 8:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """动态规划"""
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0]*m
        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        else:
            dp[0] = 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if j-1 >= 0:
                    dp[j] += dp[j-1]
        return dp[m-1]


if __name__ == '__main__':
    obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                    ]
    sl = Solution()
    print(sl.uniquePathsWithObstacles(obstacleGrid))
