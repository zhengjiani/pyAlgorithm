# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 7:35
# @Author  : zhengjiani
# @Software: PyCharm
"""
用熟悉的语言实现一个完整的栈的功能，并且给出测试用例和数据
get_size()获取当前栈的大小
get_top()取栈顶元素
push()入栈
pop()出栈
is_empty()判断栈空
is_full()判断栈满
clear()清空栈
"""
class Stack(object):
    def __init__(self,size):
        self.size = size
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def get_top(self):
        return self.stack[-1]

    def push(self,item):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        top = self.get_top()
        self.stack.remove(top)
        return top

    def is_empty(self):
        if self.get_size() == 0:
            return True
        return False

    def is_full(self):
        if self.get_size() == self.size:
            return True
        return False

    def clear(self):
        del self.stack[:]

    def __str__(self):
        return str(self.stack)
if __name__ == '__main__':
    stack = Stack(6)
    print("----------元素入栈---------")
    for i in range(6):
        stack.push(i)
    print(stack)

    print(stack.get_top())
    print("----------元素出栈---------")
    for i in range(3):
        stack.pop()
    print(stack)
    print(stack.get_top())
    print("----------清空栈-----------")
    stack.clear()
    print(stack)
    print(stack.is_empty())
