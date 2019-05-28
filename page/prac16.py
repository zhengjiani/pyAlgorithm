# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 21:30
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
Python实现hash
"""
class HashTable:
    def __init__(self,size):
        #使用list数据结构保存hash表
        self.elem = [None for i in range(size)]
        #最大表长
        self.count = size
    #散列函数采用除留余数法
    def hash(self,key):
        return key % self.count

    def insert_hash(self,key):
        """插入关键字到hash表内"""
        print(key)
        address = self.hash(key)
        print(address)
        #有冲突的时候线性探测再散列
        while self.elem[address] != None:
            address = (address+1)%self.count
        print(address)
        #没有冲突则直接保存
        self.elem[address]=key
        print(self.elem)

    def search_hash(self,key):
        """查找关键字，返回布尔值"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address+1) % self.count
            if not self.elem[address] or address == star:
                return False
        return True
def main():
    a = [0, 12, 67, 56, 16, 16, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(len(a))
    for i in a:
        hash_table.insert_hash(i)

    for i in hash_table.elem:
        if i:
            # hash_table.elem.index(i)表示i所对应的hash值
            print((i, hash_table.elem.index(i)))
    print(hash_table.search_hash(16))
    print(hash_table.search_hash(33))
if __name__ == '__main__':
    main()