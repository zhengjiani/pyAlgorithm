# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 13:08
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
层序遍历序列使用BFS,不分行从上往下打印二叉树
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 分行的层次遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        if not root:
            return []
        q = []
        q.append(root)
        while q:
            node = q.pop(0)
            lis.append(node.val)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        return lis

