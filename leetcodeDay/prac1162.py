# -*- encoding: utf-8 -*-
"""
@File    : prac1162.py
@Time    : 2020/3/29 9:18 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
地图分析
"""
import collections


class Solution:
    def maxDistance(self, grid):
        N = len(grid)
        start = [] # 将起点存储在start数组
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    start.append((x,y,0))
        if len(start) == 0 or len(start) == N * N:
            return -1

        # 队列初始化
        queue = collections.deque(start)
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        while queue:
            x,y,dis = queue.popleft()
            for d in range(4):
                i = x + dr[d]
                j = y + dc[d]
                if i<0 or j<0 or i == N or j == N or grid[i][j] == 1:
                    continue
                queue.append((i,j,dis+1))
                grid[i][j] = 1
        return dis


if __name__ == '__main__':
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    # grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    s = Solution()
    print(s.maxDistance(grid))