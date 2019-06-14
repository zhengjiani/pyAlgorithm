# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:09
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。
如果给定的节点是中序遍历序列的最后一个，则返回空节点;
二叉树一定不为空，且给定的节点一定不是空节点；
某结点有右孩子，则该结点在其中序遍历序列下的后继为其右子树最左下的那个结点
若某结点没有右孩子，且它是其父结点的左孩子，则其父结点为其后继
若它是其父结点的右孩子，则一直往上遍历，\
直到找到某结点是其父结点的左孩子或者其父结点为空（访问到了根结点）为止，该结点的父结点便是所求的后继
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def inorderSuccessor(self,p_val):
        p = TreeNode(p_val)
        # 该节点有右孩子，则后继为其右子树最左下的那个节点，沿着右孩子一直遍历
        if p is None:
            return
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        else:
            # 返回父节点
            if p.next is None:
                return
            # 该节点是其父节点的左孩子
            elif p.next.left == p:
                return p.next
            else:
                # 该节点是其父节点的右孩子
                if p.next.next.left == p.next:
                    return p.next.next
                else:
                    return
if __name__ == '__main__':
    solve = Solution()
    inorder = [2, 1, 3, None, None, None, None]
    print(solve.inorderSuccessor(2))
