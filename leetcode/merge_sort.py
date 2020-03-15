# -*- encoding: utf-8 -*-
"""
@File    : merge_sort.py
@Time    : 2020/1/16 7:47 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""

def merge2list(li1,li2):
    li = []
    i = 0
    j = 0
    while i <len(li1) and j < len(li2):
        if li[i] <= li[j]:
            li.append(li[i])
            i += 1
        else:
            li.append(li[j])
            j += 1
    # 剩下的加进来
    while i < len(li1):
        li.append(li1[i])
        i += 1
    while j < len(li2):
        li.append(li2[j])
        j += 1

def merge(li, low, mid, high): #排序li的low到high的范围
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    # li_tmp[0:high-low+1] li[low:high+1],把排好序的li_tmp放回到li中
    # j = 0
    # for i in range(low,high+1):
    #     li[i] = li_tmp[j]
    #     j += 1
    for i in range(low,high+1):
        li[i] = li_tmp[i-low]
    # 切片可以进行赋值
    li[low:high+1] = li_tmp

def merge_sort(li,low,high):
    if low < high:
        mid = (low+high) // 2
        print(li[low:mid+1],li[mid+1:high+1])
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

li = [10,4,6,3,8,2,5,7]
merge_sort(li,0,len(li)-1)
print(li)