# -*- encoding: utf-8 -*-
"""
@File    : prac215.py
@Time    : 2020/6/29 8:14 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import heapq


class Solution1(object):
    """手写"""
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 替换nums[i]后维护最小堆
        def shift(i,k):
            flag = 0
            while (i*2+1)<k and flag == 0:
                t = i
                if nums[i] > nums[2*i+1]:
                    t = 2*i + 1
                if (i*2+2) < k and nums[t] > nums[2*i+2]:
                    t = 2*i + 2
                if t == i:
                    flag = 1
                else:
                    nums[i],nums[t] = nums[t],nums[i]
                    i = t
        # 建立大小为K的最小堆，k/2-1是最后一个非叶节点
        for i in range(k//2,-1,-1):
            shift(i,k)

        # 剩余元素依次比较替换
        for i in range(k,len(nums)):
            if nums[0]<nums[i]:
                nums[0] = nums[i]
                shift(0,k)
        return nums[0]

class Solution2(object):
    """库函数"""
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

class Solution3(object):
    """手写标准"""
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx],nums[max_loc] = nums[max_loc],nums[idx]
                adjust_heap(max_loc,max_len)

        # 建堆
        n = len(nums)
        for i in range(n//2 - 1,-1,-1):
            adjust_heap(i,n)
        res = None
        for i in range(1,k+1):
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0,n-i)
        return res

if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    # sl1 = Solution1()
    # print(sl1.findKthLargest(nums,k))
    # sl2 = Solution2()
    # print(sl2.findKthLargest(nums, k))
    sl3 = Solution3()
    print(sl3.findKthLargest(nums, k))