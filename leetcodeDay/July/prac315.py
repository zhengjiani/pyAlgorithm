# -*- encoding: utf-8 -*-
"""
@File    : prac315.py
@Time    : 2020/7/11 8:35 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List

class BinaryIndexedTree:
    '''
    树状数组
    '''
    def __init__(self,length):
        self.c = [0] * length

    def lowBit(self, x):
        return x & (-x)

    def update(self, pos, value=1):
        while pos < len(self.c):
            self.c[pos] += value
            pos += self.lowBit(pos)

    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans
class Solution:
    def discretization(self, nums):
        """
        离散化优化空间，对原数组进行去重后排序，原数组每个数映射到去重排序后这个数对应位置的下标，这个下标为这个数字对应id
        :param nums:
        :return:
        """
        a = sorted(set(nums))
        value2ID = {v : i+1 for i, v in enumerate(a)}
        return value2ID, len(a)

    def countSmaller(self, nums: List[int]) -> List[int]:
        value2ID, length = self.discretization(nums)
        BIT = BinaryIndexedTree(length + 1)
        ans = []

        for i in reversed(range(len(nums))):
            posID = value2ID[nums[i]]
            ans.append(BIT.query(posID - 1))
            BIT.update(posID)

        return ans[::-1]

if __name__ == '__main__':
    sl = Solution()
    print(sl.countSmaller([5,2,6,1]))