# -*- encoding: utf-8 -*-
"""
@File    : prac23.py
@Time    : 2020/4/26 9:37 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for singly-linked list.
from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    暴力求解-时间复杂度O(NlogN),N是结点总数目
    遍历所有的值需话费O(N)的时间
    一个稳定的排序算法花费O(NlogN)时间
    遍历同时创建新的有序链表花费O(N)的时间
    空间复杂度：O(N)
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 声明用于排序的数组
        self.nodes = []
        # 声明头结点和构建链表结点
        head = point = ListNode(0)
        # 将输入的结点放入数组
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        # 将数组排序并放入链表
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

class Solution1:
    """优先队列优化逐一比较方法
        时间复杂度O(Nlogk)，k是链表数目
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 声明头结点和构建链表结点
        head = point = ListNode(0)
        q = PriorityQueue()
        # 将输入节点放入优先队列中
        for l in lists:
            if l:
                q.put((l.val,l))
        # 循环迭代队列
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val,node))
        return head.next

class Solution2:
    """逐一两两合并链表,分治
        将合并k个链表的问题转化为合并2个链表k-1次
        时间复杂度O(kN),空间复杂度O(1)
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        intervel = 1
        while intervel < amount:
            for i in range(0,amount-intervel,intervel*2):
                lists[i] = self.merge2Lists(lists[i],lists[i+intervel])
            intervel *=2
        return lists[0] if amount > 0 else None

    def merge2Lists(self,l1,l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next