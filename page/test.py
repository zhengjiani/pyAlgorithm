# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:00
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
如果我们导入的模块除了定义函数之外还中有可以执行代码，
那么Python解释器在导入这个模块时就会执行这些代码
"""
import page.module1 as m1
import page.module2 as m2
#导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
import page.module3
m1.foo()
m2.foo()