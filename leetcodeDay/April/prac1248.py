# -*- encoding: utf-8 -*-
"""
@File    : prac1248.py
@Time    : 2020/4/21 10:27 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """数学推导"""
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i]%2 == 1:
                # 存的是奇数下标
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1,len(odd)-k):
            ans += (odd[i]-odd[i-1])*(odd[i+k]-odd[i+k-1])
        return ans

class Solution1:
    """前缀和+差分"""
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = [0]*(len(nums)+1)
        cnt[0] = 1
        odd,ans = 0,0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd-k]
            cnt[odd] += 1
        return ans

if __name__ == '__main__':
    nums = [1,1,2,1,1]
    k = 3
    s = Solution()
    print(s.numberOfSubarrays(nums,k))