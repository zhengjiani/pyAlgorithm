# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 15:03
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
合并两个递增链表
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead2.next, pHead1)
            return pHead2
    def getNewChart(self,list):
        if list:
            node = ListNode(list.pop(0))
            node.next = self.getNewChart(list)
            return node
if __name__ == '__main__':
    list1 = [1,3,5]
    list2 = [0,1,4]
    testList1 = Solution().getNewChart(list1)
    testList2 = Solution().getNewChart(list2)
    final = Solution().Merge(testList1,testList2)
    while final:
        print(final.val,end=" ")
        final = final.next

