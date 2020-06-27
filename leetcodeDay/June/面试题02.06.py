# -*- encoding: utf-8 -*-
"""
@File    : 面试题02.06.py
@Time    : 2020/6/26 10:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = (head.val)
        pos = head
        # 枚举前驱节点
        while pos.next:
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head


if __name__ == '__main__':
    sl = Solution()

