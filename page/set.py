# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:45
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
def main():
    set1 = {1,2,3,3,3,2}
    set2 = set(range(1,10))
    set1.add(4)
    set1.add(5)
    set2.update([11,12])
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
    #集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    print(set1.intersection(set2))
    print(set1 | set2)
    print(set1.union(set2))
    print(set1-set2)
    print(set1.difference(set2))
    print(set1^set2)
    print(set1.symmetric_difference(set2))
    #判断子集和超集
    print(set2 <= set1)
    print(set2.issubset(set1))
    print(set3 <= set1)
    print(set3.issubset(set1))
    print(set1 >= set2)
    print(set1.issuperset(set3))
    #字典
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 删除字典中的元素
    print(scores.popitem())
    # 清空字典
    scores.clear()
    print(scores)
if __name__ == '__main__':
    main()