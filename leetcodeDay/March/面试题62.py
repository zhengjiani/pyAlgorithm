# -*- encoding: utf-8 -*-
"""
@File    : 面试题62.py
@Time    : 2020/3/30 11:35 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
面试题62 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
约瑟夫环问题
"""
import sys
sys.setrecursionlimit(100000)
# 递归,空间复杂度O(n)
class Solution:
    def f(self,n,m):
        if n == 0:
            return 0
        x = self.f(n-1,m)
        return (m + x) % n
    def lastRemaining(self, n, m):
        return self.f(n,m)

# 迭代，空间复杂度O(1)
class Solution1:
    def lastRemaining(self, n, m):
        f = 0
        for i in range(2,n+1):
            f = (m + f) % i
        return f

if __name__ == '__main__':
    n,m = 5,3
    s = Solution1()
    print(s.lastRemaining(n,m))
