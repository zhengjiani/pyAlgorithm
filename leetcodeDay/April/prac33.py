# -*- encoding: utf-8 -*-
"""
@File    : prac33.py
@Time    : 2020/4/27 8:20 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
通过比较端点数据查看子数组是否有序
"""
from typing import List


class Solution:
    """时间复杂度O(logN)"""
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r =0,len(nums)-1
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            # 端点比较验证子数组是否为有序数组
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 无序
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    # nums = [4,5,6,7,0,1,2]
    # target = 0
    nums = [3,1]
    target = 1
    s = Solution()
    print(s.search(nums,target))