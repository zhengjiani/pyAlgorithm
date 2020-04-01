# -*- encoding: utf-8 -*-
"""
@File    : prac912.py
@Time    : 2020/3/31 9:37 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
排序数组：给定一个整数数组 nums，将该数组升序排列。
"""
import random


class Solution:
    """算法导论中的快排"""
    def quick_sort(self,array,l,r):
        if l<r:
            q = self.partition(array,l,r)
            self.quick_sort(array,l,q-1)
            self.quick_sort(array,q+1,r)
    def partition(self,array,l,r):
        x = array[r]
        i = l - 1
        for j in range(l,r):
            if array[j] <= x:
                i += 1
                array[i],array[j] = array[j],array[i]
        array[i+1],array[r] = array[r],array[i+1]
        return i+1
    def sortArray(self, nums):
        self.quick_sort(nums,0,len(nums)-1)
        return nums

class Solution1:
    """常规的快排实现方法"""
    def quick_sort(self,array,left,right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array,low,left-1)
        self.quick_sort(array,left+1,high)

    def sortArray(self, nums):
        self.quick_sort(nums,0,len(nums)-1)
        return nums

# class Solution2:
#     """一行代码实现的pythonic版本"""
#     quick_sort = lambda array: array if len(array) <= 1 else \
#             quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + \
#             quick_sort([item for item in array[1:] if item > array[0]])


if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    s = Solution1()
    print(s.sortArray(nums))