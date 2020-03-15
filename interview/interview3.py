# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 8:43
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
两数求和
给定1，3，5；再给定4，9，看看之前给定的值里有没有两个值的和是4或者9的
"""
def twoSum(nums,target):
    l = len(nums)
    array = nums.copy()
    array.sort()
    i,j = 0,l-1
    max_num = max(target)
    min_num = min(target)
    while i<j:
        s = array[i] + array[j]
        if s < min_num:
            i += 1
        elif s >min_num and s < max_num:
            if array[i+1] < min_num:
                j -= 1
            elif array[i+1] > min_num:
                i += 1
            else:
                i = i+1
        elif s > max_num:
            j -= 1
        elif s == min_num or s == max_num :
            return array[i], array[j]
    return "没有这样的值"

if __name__ == '__main__':
    a = [0,3,4]
    b = [4,9]
    print(twoSum(a,b))
