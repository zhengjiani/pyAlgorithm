# -*- encoding: utf-8 -*-
"""
@File    : prac155.py
@Time    : 2020/5/12 8:58 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import math


class MinStack:
    """
    使用辅助栈和元素栈同步插入和删除，用于存储与每个元素对应的最小值
    - 当一个元素要入栈时，取当前辅助栈的栈顶为最小值，与当前元素比较得出最小值，将这个最小值插入到辅助栈中
    - 当一个元素要出栈时，把辅助栈的栈顶元素也一并弹出
    - 在任意时刻，栈内元素的最小值就存储在辅助栈的栈顶中
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]


    def push(self, x: int) -> None:
        # 判断栈满
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
