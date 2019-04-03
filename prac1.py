# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:25
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
样例
输入数组：
[
[1,2,8,9]，
[2,4,9,12]，
[4,7,10,13]，
[6,8,11,15]
]
如果输入查找数值为7，则返回true，
如果输入查找数值为5，则返回false。
"""
#与右上角的元素进行比较，大于则向下找，小于则向左找
def find_element(arr,target):
    if arr is None:
        return False
    i=0
    j=len(arr)-1
    while i<len(arr) and j>=0:
        if arr[i][j] == target:
            return True
        if arr[i][j] > target:
            j -= 1
        else :
            i += 1

    return False
if __name__ == '__main__':
    arr = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    print(find_element(arr,7))