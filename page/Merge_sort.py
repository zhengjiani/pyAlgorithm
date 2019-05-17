# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 16:41
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""归并排序"""


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序（分治法）"""

    if len(items) < 2:
        return items[:]

    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items
def main():


    print(merge_sort([9,8,7,6]))


if __name__ == '__main__':
    main()