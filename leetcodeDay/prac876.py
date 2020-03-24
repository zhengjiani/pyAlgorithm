# -*- encoding: utf-8 -*-
"""
@File    : prac876.py
@Time    : 2020/3/23 8:55 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
链表的中间结点
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, p=0):
        self.val = x
        self.next = p

# 建立链表
class LinkList(object):
    def __init__(self):
        self.head = None

    # 类似于尾插法初始化链表
    def initList(self,data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        # 数组,空间和时间复杂度都是O(N)
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A)//2]

class Solution1:
    def middleNode(self, head:ListNode) -> ListNode:
        # 单指针法两次遍历,空间O(1),时间复杂度都是O(N)
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k, cur = 0, head
        while cur:
            k += 1
            cur = cur.next
        return cur

class Solution2:
    def middleNode(self, head:ListNode) -> ListNode:
        # 快慢指针
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    data = [1,2,3,4,5]
    l = LinkList()
    l.initList(data)
    s = Solution()
    print(s.middleNode(l.head))