# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 14:31
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
调整数组顺序使奇数位于偶数前面
"""
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1] %2 != 0 :
                odd.appendleft(array[x-i-1])
            if array[i]%2 == 0:
                odd.append(array[i])
        return list(odd)
if __name__ == '__main__':
    s = Solution()
    print(s.reOrderArray([1,2,3,4]))