# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 8:37
# @Author  : zhengjiani
# @Software: PyCharm
import unittest
from stack import Stack
class TestStack(unittest.TestCase):

    def test_init(self):
        s = Stack(6)
        self.assertEqual(s.size,6)

    def test_push(self):
        """测试元素入栈"""
        s = Stack(6)
        for i in range(6):
            s.push(i)
            self.assertEqual(s.get_top(),i)

    def test_stackfull(self):
        """测试栈满"""
        s = Stack(6)
        for i in range(6):
            s.push(i)
        self.assertTrue(s.is_full())
        s.clear()
        self.assertFalse(s.is_full())

    def test_stackempty(self):
        """测试栈空"""
        s = Stack(6)
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())
if __name__ == '__main__':
    unittest.main()