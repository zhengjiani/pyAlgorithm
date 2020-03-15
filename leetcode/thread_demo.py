# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 19:37
# @Author  : zhengjiani
# @Software: PyCharm
'''
三个不同的线程将会共用一个 Foo 实例。
线程 A 将会调用 one() 方法
线程 B 将会调用 two() 方法
线程 C 将会调用 three() 方法
请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行
输入: [1,2,3]
输出: "onetwothree"
'''
# 设全局成员变量
# 用一个全局变量flag，标示当前是什么状态，
# 状态1只能执行one()，状态2只能执行two()，状态3执行three()，
# 然后到每个函数下改变状态即可。（这种方法在leetcode平台下超出时间限制）
class Foo(object):
    def __init__(self):
        self.state = 1

    def first(self,printFirst):
        """
        :param printFirst: method
        :return: void
        """
        while self.state !=1:
            pass
        printFirst()
        self.state=2

    def second(self,printSecond):
        """
        :param printFirst: method
        :return: void
        """
        while self.state !=2:
            pass
        printSecond()
        self.state=3

    def third(self,printThird):
        """
        :param printFirst: method
        :return: void
        """
        while self.state !=3:
            pass
        printThird()
        self.state=0
