# -*- encoding: utf-8 -*-
"""
@File    : prac25.py
@Time    : 2020/5/16 9:45 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
不涉及算法，主要考察面试者的设计能力
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        # head指向每组的头节点，指针每次向前移动K步，对于每个分组首先判断它的长度是否大于等于K,若是，则翻转这部分链表。
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分的长度是否大于等于K
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head,tail = self.reverse(head,tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next

    # 翻转一个子链表，并且返回新的头与尾,prev相当于头节点前的伪节点
    def reverse(self,head:ListNode,tail:ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail,head


if __name__ == '__main__':
    s = Solution()
    list1 = SLinkedList()
    list1.head = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(3)
    e4 = ListNode(4)
    e5 = ListNode(5)
    list1.head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    # list1.listprint()
    list2 = s.reverseKGroup(list1.head,2)
    print(list2.val,list2.next.val,list2.next.next.val,list2.next.next.next.val,list2.next.next.next.next.val)

