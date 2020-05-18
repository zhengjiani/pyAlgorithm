# -*- encoding: utf-8 -*-
"""
@File    : LinkedList.py
@Time    : 2020/5/16 10:24 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
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

    def AtBegining(self,newdata):
        """
        头插法
        :param newdata:
        :return:
        """
        Newnode = ListNode(newdata)
        # 将新节点的下一个值更新为现有节点Newnode->head
        Newnode.next = self.head
        self.head = Newnode

    def AtEnd(self,newdata):
        """
        尾插法
        :param newdata:
        :return:
        """
        NewNode = ListNode(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = NewNode

    def Inbetween(self,middle_node,newdata):
        """
        两个节点中插入新的节点
        :param middle_node:
        :param newdata:
        :return:
        """
        if middle_node is None:
            print("提到的节点不存在")
            return

        Newnode = ListNode(newdata)
        Newnode.next = middle_node.next
        middle_node.next = Newnode

    def RemoveNode(self,Removekey):
        """
        移除链表中的节点
        :param Removekey:
        :return:
        """
        Head = self.head
        if(Head is not None):
            if(Head.val == Removekey):
                self.head = Head.next
                Head = None
                return

            while (Head is not None):
                if(Head.val == Removekey):
                    break
                prev = Head
                Head = Head.next

            if (Head == None):
                return

            prev.next = Head.next
            Head = None
if __name__ == '__main__':
    list = SLinkedList()
    list.head = ListNode("Mon")
    e2 = ListNode("Tue")
    e3 = ListNode("Wed")

    list.head.next = e2
    e2.next = e3
    list.AtBegining("Sun")
    list.AtEnd("Thu")
    list.Inbetween(list.head.next, "Fri")
    list.RemoveNode("Tue")
    list.listprint()