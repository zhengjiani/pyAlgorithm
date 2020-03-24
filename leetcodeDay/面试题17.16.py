# -*- encoding: utf-8 -*-
"""
@File    : 面试题17.16.py
@Time    : 2020/3/24 9:14 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
按摩师
"""
class Solution:
    # 动态规划方法
    def massage(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp0,dp1 = 0,nums[0]
        for i in range(1,n):
            # dp0和dp1表示dp[i-1][0]以及dp[i-1][1]
            # tdp0和tdp[1]表示dp[i][0]以及dp[i][1]
            tdp0 = max(dp0,dp1)
            tdp1 = dp0 + nums[i]
            dp0,dp1=tdp0,tdp1
        return max(dp0,dp1)

if __name__ == '__main__':
    nums = [1,1]
    s = Solution()
    print(s.massage(nums))