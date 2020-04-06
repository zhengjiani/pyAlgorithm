# -*- encoding: utf-8 -*-
"""
@File    : prac72.py
@Time    : 2020/4/6 12:31 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
编辑距离
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n*m == 0:
            return n+m
        # 画DP矩阵
        DP = [[0]*(m+1) for _ in range(n+1)]
        # 边界状态初始化
        for i in range(n+1):
            DP[i][0] = i
        for j in range(m+1):
            DP[0][j] = j
        # 计算所有DP的值
        for i in range(1,n+1):
            for j in range(1,m+1):
                left = DP[i-1][j] + 1
                down = DP[i][j-1] + 1
                left_down = DP[i-1][j-1] #斜上角
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                DP[i][j] = min(left,down,left_down)
        return DP[n][m]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    s = Solution()
    print(s.minDistance(word1,word2))