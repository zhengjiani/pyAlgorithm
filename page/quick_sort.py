# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 17:07
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""快速排序 - 选择枢轴元素进行划分，左边都比枢轴小右边都比枢轴大，属分治法案例"""
def quick_sort(origin_items,comp=lambda x,y:x<=y):
    items = origin_items[:]
    _quick_sort(items,0,len(items)-1,comp)
    return items

def _quick_sort(items,start,end,comp):
    if start < end:
        pos = _partition(items,start,end,comp)
        # 对枢轴左区间重复排序步骤
        _quick_sort(items,start,pos-1,comp)
        # 对枢轴右区间重复排序步骤
        _quick_sort(items, pos+1,end, comp)
#分区过程
def _partition(items,start,end,comp):
    #基准数
    pivot = items[end]
    # 定位大于枢轴的数
    i = start - 1
    # 把大于枢轴的数a[i]与a[j]交换，大于枢轴的数依次与每个元素比较并向后移
    for j in range(start,end):
        if comp(items[j],pivot):
            i += 1
            items[i],items[j] = items[j],items[i]
    items[i+1],items[end] = items[end],items[i+1]
    return i+1

def main():
    list = [72,6,57,88,60,42,83,73,48,85]
    print(quick_sort(list))
if __name__ == '__main__':
    main()