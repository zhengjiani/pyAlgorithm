# -*- encoding: utf-8 -*-
"""
@File    : prac300.py
@Time    : 2020/3/14 5:16 PM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
第300题：最长上升子序列
"""
class Solution:
    def lengthOfLIS(self,nums):
        # n^2的解法 - 动态规划解法
        # dp[i]表示：考虑前i个元素，以第i个数字结尾的最长上升子序列长度
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

class Solution2:
    def lengthOfLIS(self,nums):
        # nlog(n)的解法 - 贪心 + 二分查找
        # dp[i]表示： 长度为i的最长上升子序列的末尾元素的最小值
        d = []
        for n in nums:
            # 如果nums[i] > d[len],len = len + 1
            if not d or n > d[-1]:
                d.append(n)
            else:
                # else 在d数组中查找，找到第一个比nums[i]小的数d[k]，d[k+1] = nums[i]
                l,r = 0,len(d)-1
                loc = r
                while l<=r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)







if __name__ == '__main__':
    num_list = [4,10,4,3,8,9]
    s = Solution()
    s2 = Solution2()
    print(s.lengthOfLIS(num_list))
    print(s2.lengthOfLIS(num_list))


