# -*- encoding: utf-8 -*-
"""
@File    : prac108.py
@Time    : 2020/7/3 2:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left,right):
            if left > right:
                return None

            #总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1,right)
            return root
        return helper(0, len(nums) - 1)

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    sl = Solution()
    print(sl.sortedArrayToBST(nums))