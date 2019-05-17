# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 20:41
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import math


def factorial(num):
    """
    求阶乘
    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for n in range(1,num+1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m)//factorial(n)//factorial(m-n))
print(math.factorial(m))

from random import randint

def roll_dice(n=2):
    """
    摇色子
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total
def add(a=0,b=0,c=0):
    return a+b+c
#如果没有指定参数那么使用默认值摇色子
print(roll_dice())
#摇3颗
print(roll_dice(3))
print(add())
print(add(1))
#传递参数时可以不按照设定的参数进行传递
print(add(c=50,a=100,b=200))

#在不确定参数个数的情况下采用可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add(1,2,3,4,5,6))
#实现计算求最大公约数和最小公倍数的函数
def gcd(x,y):
    (x,y) = (y,x) if x>y else (x,y)
    for factor in range(x,0,-1):
        if x % factor ==0 and y % factor == 0:
            return factor

def lcm(x,y):
    return x*y // gcd(x,y)

#实现判断一个数是不是回文数的函数
def is_palindrome(num):
    temp = num
    total = 0
    while temp>0:
        total = total*10 + temp%10
        temp //= 10
    return total == num

#实现判断一个数是不是素数的函数
def is_prime(num):
    for factor in range(2,num):
        if num % factor == 0:
            return False
    return True if num !=1 else False
#判断输入的正整数是不是回文素数
num = int(input('请输入正整数：'))
if is_palindrome(num) and is_prime(num):
    print('%d是回文素数'%num)
if __name__ == '__main__':
    is_palindrome(121)