# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 9:29
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
# 展开列表
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]

import numpy as np
b = np.array(a).flatten().tolist()
print(b)

# 将序列中并排的元素配对
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print(res)

a = "ab"
b = "xyz"
res = [i for i in zip(a,b)]
print(res)

# 从小到大排序,不用sort
list = [2,3,5,4,9,6]
new_list = []
def get_min(list):
    # 获取列表最小值
    a = min(list)
    # 删除最小值
    list.remove(a)
    # 将最小值加入新列表
    new_list.append(a)
    # 保证最后列里面有值，递归调用获取最小值
    # 直到所有值获取完，并加入新列表返回
    if len(list)>0:
        get_min(list)
    return new_list
new_list = get_min(list)
print(new_list)

# 单例模式：创建对象时__new__方法执行，并且必须return返回实例化出来的对象
# 判断cls.__instance是否存在，不存在的话就创建对象，存在的话就返回该对象，来保证只有一个实例对象存在
# 打印ID，值一样，说明对象是同一个
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 如果雷属性__instance的值为None,那么就创建一个对象，并且赋值为这个对象的引用，保证下次
        # 调用这个方法时，能够知道之前已经创建过对象了，这样就保证了只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18,"dongGe")#3085995507840
b = Singleton(8,"dongGe")#3085995507840

print(id(a))
print(id(b))

a.age = 19 #给a指向的对象添加一个属性
print(b.age) # 获取b指向的对象的age属性 19

# 升序列表
lis = [2,3,4,5,5,5,8,10]
# 有且仅有一个重复数,返回列表的重复数的第一个索引和重复次数
a = {}
for i in lis:
    a[i] = lis.count(i)
for k,v in a.items():
    if v > 1:
        print(lis.index(k),v)

from collections import Counter
print(Counter(lis))
for k,v in Counter(lis).items():
    if v>1:
        print(lis.index(k),v)

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):
    return sorted(list1,key=lambda x:x['age'],reverse=False)

print(sort_by_age(alist))

l1 = ['b','c','d','c','a','a']
# 返回第一个重复元素的索引值
print(l1.index('a'))
l2 = sorted(set(l1),key=l1.index)
print(l2)

import os

def get_files(dir,suffix):
    res = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root,filename))

    print(res)

get_files("./",'.pyc')
a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i>5:
        pass
    else:
        a.remove(i)
    print(a)
print('-----------')
print(id(a))

a=[1,2,3,4,5,6,7,8]
print(id(a))
for i in range(len(a)-1,-1,-1):
    print(a[i])

from collections import Counter

print("".join(map(lambda x: x[0] + str(x[1]), Counter("AAABBCCAC").most_common())))