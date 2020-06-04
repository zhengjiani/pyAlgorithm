# -*- encoding: utf-8 -*-
"""
@File    : prac238.py
@Time    : 2020/6/4 10:02 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answser = [0]*length
        answser[0] = 1
        for i in range(1,length):
            answser[i] = nums[i-1] * answser[i-1]

        R = 1
        for i in reversed(range(length)):
            answser[i] = answser[i]*R
            R *= nums[i]
        return answser


if __name__ == '__main__':
    nums = [1,2,3,4]
    sl = Solution()
    print(sl.productExceptSelf(nums))