# -*- encoding: utf-8 -*-
"""
@File    : Stack.py
@Time    : 2020/5/16 12:21 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Stack:

    def __init__(self):
        self.stack = []

    def add(self,dataval):
        """
        添加元素
        :param dataval:
        :return:
        """
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        """出栈"""
        if len(self.stack) <= 0:
            return ("栈空")
        else:
            return self.stack.pop()

    def peek(self):
        """
        栈顶
        :return:
        """
        return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())