# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 8:33
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import copy
will = ["Will",28,["Python","c#","JavaScript"]]
# 直接赋值
#创建一个will变量，这个变量指向一个list对象
#wilber变量将指向will变量对应的对象（内存地址），对象的赋值都是进行对象引用（内存地址）传递
#由于will和wilber指向同一个对象，所以对will的任何修改都会体现在wilber上，而str是不可变类型，修改时会替换旧的对象，产生一个新地址
wilber = copy.deepcopy(will)
print(id(will))
print(will)
print([id(ele) for ele in will])
print(wilber)
print(id(wilber))
print([id(ele) for ele in wilber])
#修改
will[0] = "Wilber"
will[2].append("CSS")
print(id(will))
print(will)
print([id(ele) for ele in will])
print(id(wilber))
print(wilber)
print([id(ele) for ele in wilber])