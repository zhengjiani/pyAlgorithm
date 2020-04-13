# -*- encoding: utf-8 -*-
"""
@File    : prac887.py
@Time    : 2020/4/11 9:12 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """动态规划+二分搜索"""
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k,n):
            if (k,n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo,hi = 1,n
                    while lo+1 < hi:
                        x = (lo + hi)//2
                        t1 = dp(k-1,x-1)
                        t2 = dp(k,n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    ans = 1 + min(max(dp(k-1,x-1),dp(k,n-x)) for x in [lo,hi])
                memo[k,n] = ans
            return memo[k,n]
        return dp(K,N)
if __name__ == '__main__':
    s = Solution()
    print(s.superEggDrop(1,2))