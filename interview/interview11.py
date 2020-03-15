# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 8:39
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
递归版将二叉树转化为双向链表
1.将左子树构造成双链表，并返回链表头节点。
2.定位至左子树双链表的最后一个节点。
3.如果左子树链表不为空的话，将当前root追加到左子树链表。
4.将右子树构成双链表，并返回链表头节点。
5.如果右子树链表不为空的话，将该链表追加到root节点之后。
6.根据左子树链表是否为空确定返回的节点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self,root):
        if not root:
            return None
        if not root.left and root.right:
            return root

        # 将左子树构成双链表，返回链表头
        left = self.Convert(root.left)
        p = left

        # 定位到左子树最右边的一个节点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，追加root到左子树链表
        if left:
            p.right = root
            root.left = p

        # 将右子树构成双链表，返回链表头
        right = self.Convert(root.right)

        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = root
            root.right = right
        return left if left else root


    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end=" ")
            head = head.left
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None
        root = TreeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root


if __name__ == "__main__":
    solution = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    head = solution.Convert(treeRoot1)
    solution.printList(head)
