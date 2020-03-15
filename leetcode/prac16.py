# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 19:02
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树
二叉树中每个节点的值都互不相同，输入的前序遍历和中序遍历一定合法
采用递归的方法，递归函数的形参依次为前序遍历的指针pre，中序遍历的指针in
前序遍历的起点pl，前序遍历的终点pr，中序遍历的起点il和中序遍历的中点ir,t=m[pre[pl]]
中序：左子树(il,t-1)，右子树(t+1,ir)，左子树大小是t-il
前序：左子树(pl+1,t-il+pl)，右子树是(t-il+pl+1,pr)
空节点：pr-pl+1
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self,preorder,inorder):
        """
        :param preorder: List[int]
        :param inorder: List[int]
        :return: TreeNode
        """

        def helper(in_left=0, in_right=len(inorder)):
            # 定义非局部变量pre_idx
            nonlocal pre_idx
            if in_left == in_right:
                return None
            # 前序遍历的元素作为根节点
            root_val = preorder[pre_idx]

            root = TreeNode(root_val)
            # 在中序遍历中找左右子树
            index = idx_map[root_val]

            # 递归
            pre_idx += 1
            # 创建左子树
            root.left = helper(in_left,index)
            # 创建右子树
            root.right = helper(index+1,in_right)
            return root
        # 从列表中的第一个元素开始遍历
        pre_idx = 0
        # 定义一个映射字典，即把前序遍历中的值映射到中序遍历中
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        # print(helper().val)
        return helper()


class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])
        return node
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    sol = Solution()
    print(sol.buildTree(preorder,inorder))