# -*- encoding: utf-8 -*-
"""
@File    : prac350.py
@Time    : 2020/7/13 12:41 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)

        # 遍历较短数组记录每个数字出现次数
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        # 遍历较长数组得到交集
        intersection = list()
        for num in nums2:
            count = m.get(num, 0)
            if count > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sl = Solution()
    print(sl.intersect(nums1,nums2))