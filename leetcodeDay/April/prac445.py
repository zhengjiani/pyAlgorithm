# -*- encoding: utf-8 -*-
"""
@File    : prac445.py
@Time    : 2020/4/14 10:19 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
链表中数位的顺序与我们做加法的顺序是相反的，为了逆序处理所有数位，可以使用栈；
把所有数字压入栈中，再一次取出相加，计算过程中注意进位。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        # 进位carry
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans

if __name__ == '__main__':
    s = Solution()

    # s.addTwoNumbers(l1,l2)