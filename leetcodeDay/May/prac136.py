# -*- encoding: utf-8 -*-
"""
@File    : prac136.py
@Time    : 2020/5/14 11:02 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from functools import reduce
from typing import List


class Solution:
    """异或
    满足交换律和结合律
    a^b^a = b^a^a = b^(a^a)=b^0=b
    """
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y,nums)

if __name__ == '__main__':
    nums = [2,2,1]
    s = Solution()
    print(s.singleNumber(nums))