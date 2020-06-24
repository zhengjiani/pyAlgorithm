# -*- encoding: utf-8 -*-
"""
@File    : prac124.py
@Time    : 2020/6/21 3:38 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    def maxPathSum(self, root: TreeNode) -> float:
        def maxGain(node):
            if not node:
                return 0
            # 只有贡献值大于0时，才会选取贡献值
            leftGain = max(maxGain(node.left),0)
            rightGain = max(maxGain(node.right),0)

            priceNewPath = leftGain + rightGain + node.val
            self.maxSum = max(priceNewPath,self.maxSum)
            return node.val + max(leftGain,rightGain)
        maxGain(root)
        return self.maxSum




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sl = Solution()
    print(sl.maxPathSum(root))