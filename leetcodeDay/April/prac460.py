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


class LFUCache:
    def __init__(self, capacity: int):
        self.cap, self.tick = capacity, 0  # 容量和计时
        self.his = []  # 元素形式为：(freq, tick, key)
        self.dic = {}  # 键值对形式为：key:[val, freq, tick]

    def get(self, key: int) -> int:
        if key not in self.dic:  # key不存在
            return -1
        self.tick += 1  # 计时
        val, freq, tick = self.dic[key]  # 取出值、频率和时间
        self.dic[key][1] += 1  # 将频率+1
        self.his.pop(bisect.bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
        bisect.insort(self.his, (freq+1, self.tick, key))  # 将更新后的记录二分插入
        return val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.tick += 1
        if key in self.dic:
            _, freq, tick = self.dic[key]  # 取出频率和时间
            self.dic[key][:] = value, freq+1, self.tick  # 更新值、频率和计时
            self.his.pop(bisect.bisect_left(self.his, (freq, tick, key)))  # 找到history里的记录并移除
            bisect.insort(self.his, (freq+1, self.tick, key))  # 将更新后的记录二分插入
        else:  # 无该记录
            self.dic[key] = [value, 1, self.tick]
            if len(self.his) == self.cap:  # history容量已满
                del self.dic[self.his.pop(0)[2]]  # 移除history首个元素即对应的键值对
            bisect.insort(self.his, (1, self.tick, key))  # 将新记录插入history



if __name__ == '__main__':
    capacity = 2
    cache = LFUCache(capacity)
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


