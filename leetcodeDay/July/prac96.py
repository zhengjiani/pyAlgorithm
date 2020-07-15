# -*- encoding: utf-8 -*-
"""
@File    : prac96.py
@Time    : 2020/7/15 9:18 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

if __name__ == '__main__':
    n = 3
    sl = Solution()
    print(sl.numTrees(n))