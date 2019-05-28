# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 8:40
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，
返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
#双指针
def removeElement(nums,val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
#当要移除的元素很少的时候，直接与最后一个元素进行交换
def removeElement1(nums,val):
    i = 0
    n = len(nums)
    while i<n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return n
#逆序循环
def removeElement2(nums,val):
    j = len(nums)
    for i in range(j-1,-1,-1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)
def main():
    nums = [4,1,2,3,5]
    nums1 =  [0,1,2,2,3,0,4,2]
    # length = removeElement(nums,2)
    length1 = removeElement1(nums,4)
    length2 = removeElement2(nums1,2)
    # for i in range(length):
    #     print(nums[i])
    for i in range(length2):
        print(nums1[i])

if __name__ == '__main__':
    main()