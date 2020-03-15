# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 14:42
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
输出该链表倒数第k个结点
遍历一次链表获取链表长度，再次遍历链表，至n-k+1输出
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p = head
        n = 1
        while p.next != None:
            p = p.next
            n = n+1
        if k > n:
            return None
        for i in range(n-k):
            head = head.next
        return head

# 设置两个指针，第一个指针走k步之后，第二个指针从头走当指针1走到链表尾部时候，第二个指针正好
# 在倒数第k个结点
    def FindKthToTail2(self, head, k):
        if head == None or k<=0:
            return None
        p1 = head
        p2 = head
        # 先走k步
        for i in range(k-1):
            if p1.next == None:
                return None
            p1 = p1.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2
if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    s = Solution()
    print(s.FindKthToTail(l,1))