# -*- encoding: utf-8 -*-
"""
@File    : prac287.py
@Time    : 2020/5/26 9:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
- 不能更改原数组（假设数组是只读的）。
- 只能使用额外的 O(1) 的空间。
- 时间复杂度小于 O(n2) 。
- 数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
from typing import List


class Solution:
    """
    二分查找
    - cnt[i]表示nums[]中小于等于i的数数量，假设重复的数为target
    target出现两次的情况：
    - [1,target-1]  cnt[i]<=i
    - [target,n]  cnt[i]>i
    target出现三次及以上
    如果替换的数i<target，[i,target]的cnt值-1
    如果替换的数j>=target,[target,j-1]的cnt值+1
    """
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l,r,ans = 1,n-1,-1
        while l <= r:
            mid = (l+r) // 2
            cnt = 0
            for i in range(0,n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    sl = Solution()
    print(sl.findDuplicate(nums))
