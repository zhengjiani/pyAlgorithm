# -*- encoding: utf-8 -*-
"""
@File    : 面试题01.07.py
@Time    : 2020/4/7 12:04 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
规律-对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。
"""
import numpy as np
class Solution:
    """辅助数组"""
    def rotate(self, matrix):
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new

class Solution1:
    """原地转置矩阵"""
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


if __name__ == '__main__':
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    s = Solution()
    s.rotate(matrix)
    print(matrix)
    print(np.transpose(matrix))