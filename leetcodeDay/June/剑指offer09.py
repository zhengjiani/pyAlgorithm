# -*- encoding: utf-8 -*-
"""
@File    : 剑指offer09.py
@Time    : 2020/6/30 8:49 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class CQueue:

    def __init__(self):
        self.A, self.B = [], []


    def appendTail(self, value: int) -> None:
        self.A.append(value)


    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)
param_3 = obj.deleteHead()
print(param_3)