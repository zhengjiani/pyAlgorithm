# -*- encoding: utf-8 -*-
"""
@File    : prac695.py
@Time    : 2020/3/15 9:17 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
第695题： 岛屿的最大面积
"""
class Solution:
    # 递归进行深度优先搜索
    def dfs(self,grid,cur_i,cur_j):
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di,dj in[[0,1],[0,-1],[1,0],[-1,0]]:
            next_i,next_j = cur_i + di,cur_j + dj
            ans += self.dfs(grid,next_i,next_j)
        return ans

    def maxAreaOfIsland(self, grid):
        ans = 0
        for i,l in enumerate(grid):
            for j,n in enumerate(l):
                ans = max(self.dfs(grid,i,j), ans)
        return ans

class Solution1:
    # 深度优先搜索 + 栈
    def maxAreaOfIsland(self, grid):
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                stack = [(i, j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        stack.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

if __name__ == '__main__':
    martix = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    s = Solution()
    s1 = Solution1()
    # print(s.maxAreaOfIsland(martix))
    print(s1.maxAreaOfIsland(martix))

