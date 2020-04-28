# -*- encoding: utf-8 -*-
"""
@File    : 面试题56_1.py
@Time    : 2020/4/28 7:22 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import functools
from collections import Counter
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for k,v in Counter(nums).items():
            if v == 1:
                ans.append(k)
        return ans

class Solution1:
    """异或
        交换律、结合律(a^b)^c == a^(b^c)
        对于任何数都有x^x =0 x^0 = x
        自反性A XOR B XOR B = A XOR 0 = A
    """
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 先对所有数字进行一次异或，得到两个出现一次的数字异或值
        ret = functools.reduce(lambda x,y:x^y,nums)
        # 在异或结果中找到任意为1的位
        div = 1
        while (div&ret == 0):
            div <<= 1
        a,b = 0,0
        # 根据这一位对所有的数字进行分组
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a,b]

if __name__ == '__main__':
    nums = [4,1,4,6]
    s = Solution1()
    print(s.singleNumbers(nums))