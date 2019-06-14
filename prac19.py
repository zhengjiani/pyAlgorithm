# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 8:43
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
请实现一个函数按照之字形顺序从上向下打印二叉树。
即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 分行的层次遍历（递归）
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[[List]int]
        """
        levels = []
        if not root:
            return levels

        def helper(node,level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return levels

# 分行的层次遍历（迭代）
class Solution_1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[[List]int]
        """
        queue = deque([root,])
        level = 0
        levels = []
        if not root:
            return levels
        while queue:
            # 开始当前层
            levels.append([])
            # 当前层的元素个数
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels

class Solution_2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[[List]int]
        """
        queue = deque([root,])
        level = 0
        levels = []
        # 之字形打印的标志位
        flag = False
        if not root:
            return levels
        while queue:
            # 开始当前层
            levels.append([])
            # 当前层的元素个数
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                levels[level].append(node.val)
                if flag:
                    levels[level].reverse()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            level += 1
        return levels

if __name__ == '__main__':
    lis = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(lis[0])
    root.left=TreeNode(lis[1])
    root.right=TreeNode(lis[2])
    root.left.left=TreeNode(lis[3])
    root.left.right=TreeNode(lis[4])
    root.right.left=TreeNode(lis[5])
    root.right.right=TreeNode(lis[6])
    solve = Solution()
    levels=solve.levelOrder(root)
    print(levels)# [[3], [9, 20], [None, None, 15, 7]]
    solve1 = Solution_1()
    levels=solve1.levelOrder(root)
    print(levels)# [[3], [9, 20], [None, None, 15, 7]]
    solve2 = Solution_2()
    levels = solve2.levelOrder(root)
    print(levels)# [[3], [20, 9], [None, None, 15, 7]]