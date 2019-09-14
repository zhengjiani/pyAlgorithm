# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:05
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
二叉搜索树和双向链表
https://blog.csdn.net/u010005281/article/details/79657259
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        # 记录链表头节点，用于最后算法的返回
        self.listHead = None
        # 定位当前需要更改指向的节点
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self,pRoot):
        if pRoot == None:
            return
        self.Convert(pRoot.left)
        if self.listHead == None:
            self.listHead = pRoot
            self.listTail = pRoot
        else:
            self.listTail.right = pRoot
            pRoot.left = self.listTail
            self.listTail = pRoot
        self.Convert(pRoot.right)
        return self.listHead
    # 获得链表的正向序和反向序
    def printList(self,head):
        while head.right:
            print(head.val,end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val,end=" ")
            head = head.left
    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self,pre,tin):
        if len(pre) == 0 | len(tin) ==0:
            return None
        root = TreeNode(pre[0])
        for order,item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1],tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:],tin[order+1:])
                return root

if __name__ == "__main__":
    solution = Solution()
    preorder_seq = [4,2,1,3,6,5,7]
    middleorder_seq = [1,2,3,4,5,6,7]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq,middleorder_seq)
    head = solution.Convert(treeRoot1)
    solution.printList(head)
