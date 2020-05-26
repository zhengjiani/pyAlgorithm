# -*- encoding: utf-8 -*-
"""
@File    : prac4.py
@Time    : 2020/5/24 7:47 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            :param k:
            :return:
            """
            index1,index2 = 0,0
            while True:
                #特殊情况
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums1[index1],nums2[index2])
                #正常情况
                newIndex1 = min(index1+k // 2 - 1,m-1)
                newIndex2 = min(index2+k // 2 - 1,n-1)
                pivot1,pivot2 = nums1[newIndex1],nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
        m,n = len(nums1),len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength+1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    sl = Solution()
    print(sl.findMedianSortedArrays(nums1,nums2))