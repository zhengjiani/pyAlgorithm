# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:26
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
def main():
    str1 = 'hello,world!'
    #获得字符串首字母大写的拷贝
    print(str1.capitalize())
    #获得字符串变大写之后的拷贝
    print(str1.upper())
    #从字符串中查找子串所在的位置
    print(str1.find('or'))
    print(str1.find('shit'))#-1
    #检测字符串是否以指定字符串开头
    print(str1.startswith('hel'))
    #以指定字符串结尾
    print(str1.endswith('!'))
    list1 = [1, 3, 5, 7, 100]
    # 清空列表元素
    list1.clear()
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    #sorted函数返回列表排序后的拷贝不会修改传入的列表
    list2 = sorted(list1)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    list3 = sorted(list1,reverse=True)