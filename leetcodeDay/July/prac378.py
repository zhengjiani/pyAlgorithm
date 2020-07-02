# -*- encoding: utf-8 -*-
"""
@File    : prac378.py
@Time    : 2020/7/2 8:38 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """利用矩阵性质进行二分查找"""
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0],matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
        ]
    sl = Solution()
    print(sl.kthSmallest(matrix,2))