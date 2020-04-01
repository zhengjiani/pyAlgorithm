# -*- encoding: utf-8 -*-
"""
@File    : 面试题40.py
@Time    : 2020/3/20 8:31 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
最小的K个数：快速排序的思想，找其中k个最小的元素，而快速排序是每一个回合都根据基础数分成两个部分，左边的小于基础数，右边的大于基础数。
如果基础数的坐标i恰好等于k，就可以确定arr[:k]就是解
"""
import heapq
class Solution:
    def getLeastNumbers(self, arr, k):
        # 直接使用堆的API
        return heapq.nsmallest(k,arr)

class Solution1:
    def getLeastNumbers(self, arr, k):
        # 使用排序（快排），基于partition实现的selection,不同之处在于返回第k+1个元素还是第K个元素
        if k > len(arr) or k < 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr,start,end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr,start,end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr,start,end)
        return arr[:k]

    def quickSort(self,arr,start,end):
        low = start
        high = end
        temp = arr[low]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[high] < temp:
                low += 1
            arr[high] = arr[low]
            arr[low] = temp
        return low

class Solution2:
    def getLeastNumbers(self, arr, k):
        # 使用大根堆的方法
        # 1.将全部的数据进行大根堆排序，然后循环逐一取出前K个大的元素，不需要使用额外的辅助空间，时间复杂度为O(KlogN)
        # 2.将给定数组的前K个数据进行大根堆heap排序，然后从第i=k+1个元素开始跟大根堆的第一个元素，也就是当前K个元素里面的最大值进行比较
        # 当 arr[i] < heap[0] 时,我们将交换这两个元素,重新进行大根堆的排序,如此进行 n-k 次,我们的堆中就是我们最后要的结果.这个思路的时间复杂度为O(NlogK),空间复杂度为O(K).此方法在海量数据时应用比较好,因为我们的内存有限不能将全部数据读入.
        if k <= 0 or k > len(arr):
            return []
        heap = self.build_heap(arr[:k])
        for i in range(k,len(arr)):
            if arr[i] < heap[0]:
                # 交换
                heap[0] = arr[i]
                self.sink(heap,0)
        return heap

    # 排序
    def sink(self,array,k):
        n = len(array)
        left = 2*k + 1
        right = 2*k + 2
        if left >= n: return
        max_i = left
        if right < n and array[left] < array[right]:
            max_i = right
        if array[max_i] > array[k]:
            array[max_i],array[k] = array[k],array[max_i]
            self.sink(array,max_i)

    #建堆（堆化数组）
    def build_heap(self,list_):
        n = len(list_)
        for i in range(n//2,-1,-1):
            self.sink(list_,1)
        return list_

if __name__ == "__main__":
    arr = [3,2,1]
    k = 2
    # s = Solution()
    # print(s.getLeastNumbers(arr,k))
    s2 = Solution2()
    print(s2.getLeastNumbers(arr, k))