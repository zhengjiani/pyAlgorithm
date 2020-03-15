# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 10:55
# @Author  : zhengjiani
# @Software: PyCharm
import unittest
from leetcode.removenode import LinkedList,Node,remove_node

class TestDelete(unittest.TestCase):
    def test_delete(self):
        """测试是否删除所指节点"""
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        l = LinkedList()
        l.insert(a)
        l.insert(b)
        l.insert(c)
        l.insert(d)
        l.insert(e)
        item = l.get_data(2)
        self.assertTrue(item in l.get_all_data())
        remove_node(l,2)
        self.assertEqual(item,4)
        self.assertFalse(item in l.get_all_data())

    def test_valueerror(self):
        """测试尝试删除空链表是否报异常"""
        l = LinkedList()
        with self.assertRaises(ValueError):
            remove_node(l, 2)

if __name__ == '__main__':
    unittest.main()
