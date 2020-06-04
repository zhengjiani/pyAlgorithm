# -*- encoding: utf-8 -*-
"""
@File    : prac101.py
@Time    : 2020/5/31 2:04 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
对称二叉树需要满足的条件：
它们的两个根结点具有相同的值
每个树的右子树都与另一个树的左子树镜像对称
通过「同步移动」两个指针的方法来遍历这棵树，pp 指针和 qq 指针一开始都指向这棵树的根，
随后 pp 右移时，qq 左移，pp 左移时，qq 右移。每次检查当前 pp 和 qq 节点的值是否相等

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTree(root.left,root.right)

    def isSymmetricTree(self,left,right):
        # 同时为空
        if left is None and right is None:
            return True
        # 一个为空
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricTree(left.left,right.right) and self.isSymmetricTree(left.right,right.left)