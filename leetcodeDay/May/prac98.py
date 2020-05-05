# -*- encoding: utf-8 -*-
"""
@File    : prac98.py
@Time    : 2020/5/5 8:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.val,val,upper):
                return False
            if not helper(node.val,lower,val):
                return False
            return True
        return helper(root)