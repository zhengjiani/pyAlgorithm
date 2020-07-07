# -*- encoding: utf-8 -*-
"""
@File    : prac112.py
@Time    : 2020/7/7 9:49 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""


import collections

# 二叉树的反序列化
def deserialize(data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    if data == '[]':
        return None
    vals, i = data[1:-1].split(','), 1
    print(vals)
    root = TreeNode(int(vals[0]))
    print(vals[1])
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if vals[i] != "null":
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if vals[i] != "null":
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    两个队列，一个队列存储要遍历的节点
    一个队列存储根节点到这些节点的路径和
    root可能为空
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = collections.deque([root])
        queue_value = collections.deque([root.val])
        while queue:
            node = queue.popleft()
            ans = queue_value.popleft()
            if not node.left and not node.right:
                if ans == sum:
                    return True
            if node.left:
                queue.append(node.left)
                queue_value.append(node.left.val+ans)
            if node.right:
                queue.append(node.right)
                queue_value.append(node.right.val+ans)
        return False

class Solution1:
    """
    递归-假设从根节点到当前节点的值之和是val，是否存在从当前节点的子节点到叶子节点的路径，满足其路径和sum-val
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
if __name__ == '__main__':
    #二叉树反序列化
    tree_list = "[5,4,8,11,null,13,4,7,2,null,null,null,1,null,null,null,null,null,null,null,1]"
    sl = Solution()
    root = deserialize(tree_list)
    print(sl.hasPathSum(root,22))
    sl1 = Solution1()
    print(sl1.hasPathSum(root,22))

