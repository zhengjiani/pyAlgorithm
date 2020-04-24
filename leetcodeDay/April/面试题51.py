# -*- encoding: utf-8 -*-
"""
@File    : 面试题51.py
@Time    : 2020/4/24 12:02 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
借用临时数组
"""
from typing import List


class Solution:
    """分治+归并"""
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 一边计算逆序对个数，一边排序。辅助数组用于归并两个有序数组
        tmp = [0] * n
        # [0,n-1]左闭右闭区间
        return self.mergeSort(nums,tmp,0,n-1)
    def mergeSort(self,nums,tmp,l,r):
        # 递归终止条件
        if l >= r:
            return 0

        # 二分查找中left+(right-left) // 2 整型溢出
        mid = (l + r)//2
        count = self.mergeSort(nums,tmp,l,mid)+self.mergeSort(nums,tmp,mid+1,r)
        i, j, pos = l,mid+1,l
        while i <= mid and j <= r:
            # 当nums[i]和nums[j]相等的时候，应该先把nums[i]归并回去
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                # 第一个数组中还没归并回去的元素数量
                count += (j-(mid+1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i,mid+1):
            tmp[pos] = nums[k]
            count += (j-(mid+1))
            pos += 1
        for k in range(j,r+1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return count
if __name__ == '__main__':
    nums = [7,5,6,4]
    s = Solution()
    print(s.reversePairs(nums))