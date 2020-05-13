# -*- encoding: utf-8 -*-
"""
@File    : prac102.py
@Time    : 2020/5/13 8:30 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None

    # 使用列表构建二叉树
    def construct_tree(self,values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        n = len(values)
        nums = 1
        while nums < n:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < n:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

class Solution:
    """BFS"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if level:
                res.append(level)
        return res

class Solution1:
    """DFS
    递归过程中同一层的节点放在同一个列表里
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root,0,res)
        return res

    def level(self,root,level,res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:self.level(root.left,level+1,res)
        if root.right:self.level(root.right,level+1,res)
if __name__ == '__main__':
    t = Tree()
    t.construct_tree([3,9,20,None,None,15,7])
    s = Solution()
    print(s.levelOrder(t.root))