# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:37
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a
def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()