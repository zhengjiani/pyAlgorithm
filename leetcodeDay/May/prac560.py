# -*- encoding: utf-8 -*-
"""
@File    : prac560.py
@Time    : 2020/5/15 9:20 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        for idx,val in enumerate(nums):
            if idx == 0:
                prefix.append(val)
            else:
                prefix.append(val+prefix[-1])
        ans = 0
        import collections
        cnt = collections.defaultdict(int)
        cnt[0] += 1
        for idx,val in enumerate(prefix):
            if val - k in cnt:
                ans += cnt[val-k]
            cnt[val] += 1
        return ans


if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    s = Solution()
    print(s.subarraySum(nums,k))
