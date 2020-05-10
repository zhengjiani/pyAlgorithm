# -*- encoding: utf-8 -*-
"""
@File    : prac236.py
@Time    : 2020/5/10 9:29 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    # 使用列表构建二叉树
    def construct_tree(self,values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 <leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
class Solution:
    """
    最近公共祖先(flson&&frson)||((x==p ||x ==q)&&(flson||frson))
    递归,时间复杂度O(N),空间复杂度O(N)N是二叉树的节点数，递归调用的栈深度取决于二叉树的高度
    """
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :param root: TreeNode
        :param p: TreeNode
        :param q: TreeNode
        :return:
        """
        self.dfs(root,p,q)
        return self.ans
    def dfs(self,root,p,q):
        """
        :param root: TreeNode
        :param p: TreeNode
        :param q: TreeNode
        :return: boolean
        """
        if root is None:
            return False
        lson = self.dfs(root.left,p,q)
        rson = self.dfs(root.right,p,q)
        if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
            self.ans = root
        return lson or rson or (root.val == p.val or root.val == q.val)

class Solution1:
    """
    存储父节点使用哈希表
    - 从根节点开始遍历整棵二叉树，用哈希表记录每个节点的父节点指针
    - 从p节点开始不断往它的祖先移动，并用数据结构记录已经访问过的祖先节点
    - 同样，再从q节点开始不断往它的祖先移动，如果有祖先已经被访问过，意味着这是p和q深度最深的公共祖先，即LCA节点
    """
    def __init__(self):
        self.parent = {}
        self.visited = set()
    def lowestCommonAncestor(self, root, p, q):
        self.dfs(root)
        while p is not None:
            self.visited.add(p.val)
            p = self.parent.get(p.val)
        while q is not None:
            if q.val in self.visited:
                return q
            q = self.parent.get(q.val)
    def dfs(self,root):
        """
        :param root: TreeNode
        :return:
        """
        if root.left is not None:
            self.parent[root.left.val] = root
            self.dfs(root.left)
        if root.right is not None:
            self.parent[root.right.val] = root
            self.dfs(root.right)


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([3,5,1,6,2,0,8,None,None,7,4])
    p = TreeNode(5)
    q = TreeNode(1)
    s = Solution()
    print(s.lowestCommonAncestor(t.root,p,q).val)
