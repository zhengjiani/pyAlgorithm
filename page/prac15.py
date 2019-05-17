# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:22
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""修改全局作用域中的a"""

def main():
    def foo():
        global a
        a = 200
        print(a)

    a = 100
    foo()
    print(a)  # 200
if __name__ == '__main__':
    main()