# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 16:26
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
平衡二叉树：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
从下到上（从底到顶），分别判断某节点的左右子树是否为平衡二叉树，即根据该结点的左右子树高度差判断是否平衡
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def creatBTree(data,index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data,2*index+1)
        pNode.right = creatBTree(data,2*index+2)
    return pNode
class Solution:
    def isBalanced_Soulution(self,pRoot):
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced_Soulution(pRoot.left) and self.isBalanced_Soulution(pRoot.right)
    def TreeDepth(self,pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left,right) + 1
if __name__ == "__main__":
    data = [1, None, 2, 3]
    pNode = creatBTree(data, 0)
