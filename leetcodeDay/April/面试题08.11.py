# -*- encoding: utf-8 -*-
"""
@File    : 面试题08.11.py
@Time    : 2020/4/23 9:41 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25,10,5,1]
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i],n+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1] % 1000000007
class Solution1:
    """数列求和"""
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(n//25+1):
            rest = n-i*25
            a,b = rest//10,rest%10//5
            ans += (a+1)*(a+b+1)
        return ans % mod
if __name__ == '__main__':
    s = Solution()
    print(s.waysToChange(5))
