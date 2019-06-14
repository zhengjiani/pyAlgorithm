# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 10:20
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
前序遍历过程的模拟
题目描述：
请实现两个函数，分别用来序列化和反序列化二叉树。
您需要确保二叉树可以序列化为字符串，并且可以将此字符串反序列化为原始树结构。
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 二叉树的前序遍历（递归）
class Solution(object):
    def preOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        lis = []
        lis.append(root.val)
        if root.left != None:
            lis += self.preOrderTraversal(root.left)

        if root.right != None:
            lis += self.preOrderTraversal(root.right)
        return lis
    # 非递归，采用栈的形式
    def preOrderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        lis = []
        while stack:
            node = stack.pop()
            lis.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    # 序列化二叉树，空节点用#表示
    def Serialize(self,root):
        vals = []
        def preOrder(root):
            if not root:
                vals.append('#')
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ','.join(vals)
    # 反序列化二叉树
    def Deserialize(self,s):
        vals = deque(val for val in s.split(' '))
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root
        return build()
if __name__ == '__main__':
    lis = [3, 9, 20, None, None, 15, 7]

    root = TreeNode(lis[0])
    root.left=TreeNode(lis[1])
    root.right=TreeNode(lis[2])
    # root.left.left=TreeNode(lis[3])
    # root.left.right=TreeNode(lis[4])
    root.right.left=TreeNode(lis[5])
    root.right.right=TreeNode(lis[6])
    solve = Solution()
    levels=solve.preOrderTraversal(root)
    s='3 9 # # 20 15 # # 7 # #'
    tree = solve.Deserialize(s)# <__main__.TreeNode object at 0x000002604D013048>
    # print(levels)
    print(tree)