# -*- encoding: utf-8 -*-
"""
@File    : Tree_traversal.py
@Time    : 2020/5/16 12:31 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        """
        insert node
        :param data:
        :return:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self,root):
        """
        Inorder traversal left-》root-》right
        :param root:
        :return:
        """
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self,root):
        """
        Preorder traversal root->left->right
        :param root:
        :return:
        """
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
#    27
#  14  35
#10 19 31 42
print(root.inorderTraversal(root))#[10, 14, 19, 27, 31, 35, 42]
print(root.preorderTraversal(root))#[27, 14, 10, 19, 35, 31, 42]
print(root.PostorderTraversal(root))# [10, 19, 14, 31, 42, 35, 27]


