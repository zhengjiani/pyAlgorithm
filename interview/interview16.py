# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 11:13
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
查找二叉树的深度，求该树的深度
从根节点到叶节点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self,pRoot):
        if pRoot == None:
            return 0
        ldepth = Solution.TreeDepth(self,pRoot.left)
        rdepth = Solution.TreeDepth(self,pRoot.right)
        return max(ldepth,rdepth)+1
