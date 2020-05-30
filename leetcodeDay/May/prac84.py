# -*- encoding: utf-8 -*-
"""
@File    : prac84.py
@Time    : 2020/5/30 10:53 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List

class Solution:
    """
    单调栈
    下标为3的面积后看到但是先于下标2计算出来，符合LIFO规律
    栈作为辅助数据结构「空间换时间」
    出栈的时候表示栈顶位置可以勾勒出来的最大矩形的面积
    元素出栈的前提：看到的元素高度严格小于当前栈顶元素高度的时候
    栈顶元素出栈，进而能确定栈顶元素能够勾勒出来的最大矩形的面积
    入栈元素是矩形的下标，高度直接通过数组下标访问可以获得,最一般的情况width=i-stack.peekLast()-1
    - 特殊情况1：遍历完成以后，栈内元素出栈，栈顶元素一定可以扩散到数组末尾
    - 特殊情况2：出栈以后栈内元素为空，当前位置一定可以扩散到数组的最左边
    - 特殊情况3：栈中存在高度相等的元素，遇到新栈顶和当前栈顶的高度一样的时候，弹出当前栈顶
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = [0]*n,[0]*n
        mono_stack = []
        for i in range(n):
            # 当前元素下标小于栈顶元素下标
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        # 将当前栈内元素全部弹出
        mono_stack = []
        for i in range(n-1,-1,-1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n>0 else 0
        return ans

class Solution1:
    """单调栈+常数优化的方法
    哨兵1 高度为0，保证栈中一定非空
    哨兵2 高度为0，保证遍历完成以后所有原始输入数据可以完成计算，而不必重复写相关逻辑
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = [0]*n,[n]*n

        mono_stack = []
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        ans = max((right[i]-left[i]-1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    sl = Solution()
    print(sl.largestRectangleArea(heights))