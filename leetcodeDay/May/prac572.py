# -*- encoding: utf-8 -*-
"""
@File    : prac572.py
@Time    : 2020/5/7 3:03 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """DFS序列上做串匹配，先序遍历，加入null值"""
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = self.inorder(s)
        st = self.inorder(t)
        return st in ss
    #先序遍历
    def inorder(self,root):
        if not root:
            return '#'
        return '*'+str(root.val)+str(root.left)+str(root.right)

if __name__ == '__main__':
    print('''
       __   ___    _ _____ _______
     \ \ / / |  | |  __ \__   __|
      \ V /| |  | | |__) | | |
       > < | |  | |  ___/  | |
      / . \| |__| | |      | |
     /_/ \_\\____/|_|      |_|''')