# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 9:05
# @Author  : zhengjiani
# @Software: PyCharm
"""
给一个链表，去除掉倒数第n个节点。用熟悉的语言编写，并且针对设计的函数设计用例(需要给出具体场景的链表)
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
    def is_empty(self):
        return self.length == 0
    def insert(self,node):
        if isinstance(node,Node):
            pass
        else:
            node = Node(node)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def clear(self):
        self.head = None
        self.length = 0
    #以列表形式存储
    def get_all_data(self):
        if self.length == 0:
            return None
        else:
            cur = self.head
            list = [cur.data]
            while cur.next:
                cur = cur.next
                list.append(cur.data)
        return list
    def print_list(self):
        if self.length == 0:
            return None
        else:
            cur = self.head
            while cur.next:
                print(cur.data,'->',end='')
                cur = cur.next
            print(cur.data)
    #获取倒数第n个元素的值
    def get_data(self,n):
        if not 0 <= n <= self.length:
            return 'Error'
        if n == self.length:
            return self.head.data
        else:
            cur = self.head
            index = 0
            while index != self.length-n:
                cur = cur.next
                index += 1
            return cur.data
def remove_node(l,n):
    if l.is_empty():
        raise ValueError("链表没有元素")
    cur = l.head
    index = 0
    #链表中只含n个元素
    if l.length == n:
        return cur.next
    else:
        #寻找待删除元素的前一个元素
        while index != l.length-n-1:
            cur = cur.next
            index += 1
        cur.next = cur.next.next
        return l

if __name__ == '__main__':
    #创建链表
    a=Node(1)
    b=Node(2)
    c=Node(3)
    d=Node(4)
    e=Node(5)
    l = LinkedList()
    l.insert(a)
    l.insert(b)
    l.insert(c)
    l.insert(d)
    l.insert(e)
    print("-------删除倒数第n个元素前------")
    l.print_list()
    print(l.get_all_data())
    print("-------删除倒数第n个元素后------")
    print(l.get_data(2))#4
    remove_node(l,2)
    l.print_list()
    # 链表为空时异常
    # l = LinkedList()
    # remove_node(l,2)
    # l.print_list()