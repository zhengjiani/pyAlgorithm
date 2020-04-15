# -*- encoding: utf-8 -*-
"""
@File    : prac542.py
@Time    : 2020/4/15 8:27 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
01矩阵
广度优先搜索可以找到从起点到其他所有点的最短距离
"""
import collections
from typing import List


class Solution:
    """广度优先搜索
    时间复杂度O(rc)
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        dist = [[0]*n for _ in range(m)]
        zeroes_pos = [(i,j) for i in range(m) for j in range(n) if matrix[i][j] == 0]


        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i,j = q.popleft()
            for ni,nj in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni,nj))
                    seen.add((ni,nj))
        return dist

class Solution1:
    """动态规划
    需要遍历四次矩阵，时间复杂度O(4rc)=O(rc)
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        对于矩阵中的任意一个1和一个0，从1到达0距离最短的方法：
        - 只有水平向左移动和竖直向上移动
        - 只有水平向左移动和竖直向下移动
        - 只有水平向右移动和竖直向上移动
        - 只有水平向右移动和竖直向下移动
        :param matrix:
        :return:
        """
        m, n = len(matrix),len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果（i,j）的元素为0，那么距离为0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 默认向左向上为正，注意动态规划计算顺序
        # 只有 水平向左移动 和 竖直向上移动
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    dist[i][j] = min(dist[i][j],dist[i-1][j]+1)
                if j-1 >= 0:
                    dist[i][j] = min(dist[i][j],dist[i][j-1]+1)
        # 只有 水平向右移动 和 竖直向上移动
        for i in range(m):
            for j in range(n-1,-1,-1):
                if i-1 >= 0:
                    dist[i][j] = min(dist[i][j],dist[i-1][j]+1)
                if j+1 < n:
                    dist[i][j] = min(dist[i][j],dist[i][j+1]+1)
        # 只有 水平向右移动 和竖直向下移动
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1 < m:
                    dist[i][j] = min(dist[i][j],dist[i+1][j]+1)
                if j+1 < n:
                    dist[i][j] = min(dist[i][j],dist[i][j+1]+1)
        return dist

class Solution2:
    """动态规划的常数优化
    需要遍历两次矩阵O(2rc)=O(rc)
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        - 只有 水平向左移动 和 竖直向上移动
        - 只有 水平向右移动 和 竖直向下移动
        去掉一些重复计算的地方
        :param matrix:
        :return:
        """
        m,n = len(matrix),len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置一个很大的数
        dist = [[10 ** 9] * n for _ in range(m)]
        # 如果（i,j）的元素为0，那么距离为0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和竖直向下移动
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
if __name__ == '__main__':
    # 0 0 0
    # 0 1 0
    # 0 0 0
    matrix = [[0,0,0],
              [0,1,0],
              [0,0,0]]
    s = Solution()
    print(s.updateMatrix(matrix))
