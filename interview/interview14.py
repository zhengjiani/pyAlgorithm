# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 14:51
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
最小的K个数——输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
"""
class Solution:
    # 蒂姆排序
    def GetLeastNumbers_Solution(self,tinput,k):
        return sorted(tinput)[:k]

# 快速排序
class Solution1:
    def GetLeastNumbers_Solution(self,tinput,k):
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x > pivot])
            return left + [pivot] + right
        if tinput == [] or k>len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]

# 归并排序
class Solution2:
    def GetLeastNumbers_Solution(self,tinput,k):
        # 分割
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            left = merge_sort(lst[:mid])
            right = merge_sort(lst[mid:])
            return merge(left,right)
        def merge(left,right):
            l,r,res = 0,0,[]
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res += left[l:]
            res += right[r:]
            return res
        if tinput == [] or k > len(tinput):
            return []
        tinput = merge_sort(tinput)
        return tinput[:k]

# 堆排序
class Solution3:
    def GetLeastNumbers_Solution(self,tinput,k):
        # 构建堆
        def siftup(lst,temp,begin,end):
            if lst == []:
                return []
            # i,j分别为根节点和叶子结点编号
            i,j = begin,begin*2 + 1
            while j < end:
                if j + 1 < end and lst[j+1] > lst[j]:
                    j += 1
                elif temp > lst[j]:
                    break
                else:
                    lst[i] = lst[j]
                    i,j = j,2*j + 1
            lst[i] = temp

        def heap_sort(lst):
            if lst == []:
                return []
            end = len(lst)
            # 从第一个非叶节点开始，第一个叶结点arr.length/2-1
            # 从左至右，从下至上进行调整
            for i in range((end//2)-1,-1,-1):
                siftup(lst,lst[i],i,end)
            for i in range(end-1,0,-1):
                temp = lst[i]
                # 堆顶与末尾元素交换
                lst[i] = lst[0]
                siftup(lst,temp,0,i)
            return lst

        if tinput == [] or k > len(tinput):
            return []
        tinput = heap_sort(tinput)
        return tinput[:k]

# 冒泡排序
class Solution4:
    def GetLeastNumbers_Solution(self,tinput,k):
        def bubble_sort(lst):
            if lst == []:
                return []
            for i in range(len(lst)):
                for j in range(1,len(lst)-i):
                    if lst[j-1] > lst[j]:
                        lst[j-1],lst[j] = lst[j],lst[j-1]
            return lst
        if tinput == [] or k > len(tinput):
            return []
        tinput = bubble_sort(tinput)
        return tinput[:k]

# 直接选择排序
class Solution5:
    def GetLeastNumbers_Solution(self,tinput,k):
        def select_sort(lst):
            if lst == []:
                return []
            for i in range(len(lst)-1):
                smallest = i
                for j in range(i,len(lst)):
                    if lst[j] < lst[smallest]:
                        smallest = j
                    lst[i],lst[smallest] = lst[smallest],lst[i]
                return lst

        if tinput == [] or k > len(tinput):
            return []
        tinput = select_sort(tinput)
        return tinput[:k]

# 插入排序
class Solution6:
    def GetLeastNumbers_Solution(self,tinput,k):
        def Insert_sort(lst):
            if lst == []:
                return []
            for i in range(1,len(lst)):
                temp = lst[i]
                j = i
                while j > 0 and temp < lst[j-1]:
                    lst[j] = lst[j-1]
                    j -= 1
                lst[j] = temp
            return lst
        if tinput == [] or k > len(tinput):
            return []
        tinput = Insert_sort(tinput)
        return tinput[:k]
if __name__ == "__main__":
    s = Solution()
    input_num = [4,5,1,6,2,7,3,8]
    k = 4
    print(s.GetLeastNumbers_Solution(input_num,k))