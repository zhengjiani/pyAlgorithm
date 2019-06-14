# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:56
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
N叉树的层次遍历
利用深度搜索实现

"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        lis = []
        self.traverse(root,0,lis)
        return lis

    def traverse(self,root,depth,lis):
        if root == None:
            return
        if len(lis) == depth:
            lis.append([])
        # 同一层加进去
        lis[depth].append(root.val)
        for x in root.children:
            self.traverse(x,depth+1,lis)