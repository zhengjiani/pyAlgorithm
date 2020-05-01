# -*- encoding: utf-8 -*-
"""
@File    : prac21.py
@Time    : 2020/5/1 3:18 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # 增加元素到链表，并使得新增加的元素成为链表中第一个节点
    def append(self,x):
        node = ListNode(x)
        # 链表为空时append一个节点
        if self.head is None:
            self.head = node
            self.tail = node
        # 链表不为空时append一个节点
        else:
            self.tail.next = node
            self.tail = node

    # 遍历链表
    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.val
        while cur.next:
            cur = cur.next
            yield cur.val

    # 指定位置插入节点
    def insert(self,idx,value):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = ListNode(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    # 移除指定位置的节点
    def remove(self,idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:
            raise Exception('The list is an empty list')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        # 删除第一个节点时
        if idx == 0:
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:
            # 当删除的节点是链表最后一个节点时
            self.tail = cur

    def size(self):
        cur = self.head
        count = 0
        if cur is None:
            return 'The list is an empty list'
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self,item):
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.val == item:
                found = True
            else:
                cur = cur.next
        return found

# 定义单链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """暴力解法，逐一比较
    模式识别：链表问题引入亚节点
    时间复杂度O(M+N)，空间复杂度O(1)
    """
    pass
class Solution1:
    """递归
    合并(L1,L2)等价于L1->next=合并(L1->next,L2)
    模式识别：子问题和原问题具有相同结构，考虑自上而下的递归
    时间复杂度O(M+N),空间复杂度O(M+N)
    - 有链表为空的情况
    - 正常情况
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

class Solution2:
    """
    迭代方法
    时间复杂度O(M+N),空间复杂度O(1)
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 当最多还有一个未合并完时
        prev.next = l1 if l1 is not None else l2
        return prehead.next

if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    # 1->2->4
    l1_list = [1, 2, 4]
    for i in l1_list:
        l1.append(i)
    # 1->3->4
    l2_list = [1, 3, 4]
    for i in l2_list:
        l2.append(i)
    for node in l1.iter():
        print(node)
    print(l1.size())