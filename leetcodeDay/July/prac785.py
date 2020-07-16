# -*- encoding: utf-8 -*-
"""
@File    : prac785.py
@Time    : 2020/7/16 8:06 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# 二分图的概念
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCLORED, RED, GREEN = 0, 1, 2
        color = [UNCLORED] * n

        for i in range(n):
            if color[i] == UNCLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False
        return True

if __name__ == '__main__':
    graph = [[1,3], [0,2], [1,3], [0,2]]
    sl = Solution()
    print(sl.isBipartite(graph))