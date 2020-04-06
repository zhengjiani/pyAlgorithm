# -*- encoding: utf-8 -*-
"""
@File    : prac460.py
@Time    : 2020/4/5 8:56 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
bisect-数组二等分算法
参考：https://docs.python.org/3.7/library/bisect.html
"""
import bisect
import collections

class Node:
    def __init__(self,key,val,pre=None,nex=None,freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key
    # 插入节点
    # self->nex->self.nex
    def insert(self,nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex

# 创建双向链表，包含值为0的头和尾节点
def create_linked_list():
    head = Node(0,0)
    tail = Node(0,0)
    head.nex = tail
    tail.pre = head
    return (head,tail)

class LFUCache1:
    """双哈希表解法"""
    def __init__(self,capacity: int):
        self.capacity = capacity
        # 键值对总数
        self.size = 0
        # 记录最小的频率，当容量满了的时候就会删除这个频率的head.nex
        self.minFreq = 0
        # #key是频率，值是一条双向链表的head, tail，最近操作的节点插入tail前面，则head.nex是最小使用频率的节点，删除时删head.nex
        self.freqMap = collections.defaultdict(create_linked_list)
        # 存储键值对，值是node类型
        self.keyMap = {}

    # 双向链表中删除指定的节点
    def delete(self,node):
        if node.pre:
            # 前后连接起来
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            # #新的频率中已存在这个节点，且只有这个节点，那就直接把这个新频率删掉，方便后面插入最新数据
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key

    # 双向链表中加入节点
    def increase(self,node):
        # 当前节点频率为1
        node.freq += 1
        # 在旧频率中删除子节点
        self.delete(node)
        # 新频率中，tail节点前插入当前节点
        self.freqMap[node.freq][-1].pre.insert(node)
        # 记录频率为1的节点，容量满的时候从这里先删掉
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            # 这个频率里没有实际节点，只有head,tail
            if head.nex is tail:
                # 最小频率更新为当前频率
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:  # 有，更新value
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)  # 没有，新建一个node
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:  # 大于容量
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)  # 删除head.nex
                self.keyMap.pop(deleted)
            self.increase(node)

class LFUCache:
    """哈希表+平衡二叉树解法"""
    def __init__(self, capacity: int):
        self.cap, self.time = capacity, 0  # 容量和计时
        self.his = []  # 元素形式为：(freq, tick, key)
        self.dic = {}  # 键值对形式为：key:[val, freq, tick]

    def get(self, key: int) -> int:
        if key not in self.dic:  # key不存在
            return -1
        self.time += 1  # 计时
        val, freq, tick = self.dic[key]  # 取出值、频率和时间
        self.dic[key][1] += 1  # 将频率+1
        self.his.pop(bisect.bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
        bisect.insort(self.his, (freq+1, self.time, key))  # 将更新后的记录二分插入
        return val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.time += 1
        if key in self.dic:
            _, freq, tick = self.dic[key]  # 取出频率和时间
            self.dic[key][:] = value, freq+1, self.time  # 更新值、频率和计时
            self.his.pop(bisect.bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
            bisect.insort(self.his, (freq+1, self.time, key))  # 将更新后的记录二分插入
        else:  # 无该记录
            self.dic[key] = [value, 1, self.time]
            if len(self.his) == self.cap:  # history容量已满
                del self.dic[self.his.pop(0)[2]]  # 移除history首个元素即对应的键值对
            bisect.insort(self.his, (1, self.time, key))  # 将新记录插入history



if __name__ == '__main__':
    capacity = 2
    cache = LFUCache1(capacity)
    # # param_1 = obj.get(key)
    # # cache.put(key,value)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1))
    # ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
    print(cache.put(1,1))
    print(cache.put(2,2))
    print(cache.get(1))
    print(cache.put(3,3))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.put(4,4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


