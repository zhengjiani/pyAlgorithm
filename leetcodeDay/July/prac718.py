# -*- encoding: utf-8 -*-
"""
@File    : prac718.py
@Time    : 2020/7/1 10:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution1:
    """动态规划dp[i][j]由dp[i+1][j+1]转移而来"""
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m+1) for _ in range(n+1)]
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans

class Solution2:
    """滑动窗口对齐"""
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA:int,addB:int,length:int):
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret,maxLength(i,0,length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret,maxLength(0,i,length))
        return ret

if __name__ == '__main__':
    sl = Solution1()
    print(sl.findLength([1,2,3,2,1],[3,2,1,4,7]))
