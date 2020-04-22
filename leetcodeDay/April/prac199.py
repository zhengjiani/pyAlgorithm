# -*- encoding: utf-8 -*-
"""
@File    : prac199.py
@Time    : 2020/4/22 11:17 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """深度优先搜索
        先访问右子树，在这层见到的第一个结点一定是最右边的结点
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        right = dict()
        max_depth = -1
        stack = [(root,0)]
        while stack:
            node,depth = stack.pop()
            if node is not None:
                max_depth = max(max_depth,depth)
                right.setdefault(depth,node.val)
                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))

        return [right[depth] for depth in range(max_depth+1)]

class Solution1:
    """广度优先搜索
        对二叉树进行层次遍历，对于每层来说，最右边的结点一定是最后被遍历到的
    """
    def rightSideView(self, root: TreeNode) -> List[int]:
        right = dict()
        max_depth = -1
        queue = deque([(root,0)])
        while queue:
            node, depth = queue.popleft()
            if node is not None:
                max_depth = max(max_depth,depth)
                right[depth] = node.val
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return [right[depth] for depth in range(max_depth+1)]

