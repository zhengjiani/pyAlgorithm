# -*- encoding: utf-8 -*-
"""
@File    : prac221.py
@Time    : 2020/5/8 8:13 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """动态规划"""
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n,m = len(matrix),len(matrix[0])
        ans = 0
        pre = []
        for val in matrix[0]:
            pre.append(int(val))
            if int(val) > ans:
                ans = int(val)
        for i in range(1,n):
            cur = [0]*m
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    cur[j] = 1
                else:
                    cur[j] =min(cur[j-1],pre[j-1],pre[j]) + 1
                if cur[j] > ans:
                    ans = cur[j]
            pre = cur
        return ans*ans

class Solution1:
    """暴力法"""
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        - 遍历矩阵中的每个元素，每次遇到1，就把它作为矩阵的左上角
        - 根据左上角所在的行和列，计算可能的最大正方形边长
        - 每次在下方新增一行或者在右方新增一列，判断所增的行和列是否满足所有元素都是1
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare




if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    s = Solution1()
    print(s.maximalSquare(matrix))