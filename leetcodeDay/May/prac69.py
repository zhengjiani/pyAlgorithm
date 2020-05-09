# -*- encoding: utf-8 -*-
"""
@File    : prac69.py
@Time    : 2020/5/9 10:45 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """二分查找"""
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x // 2
        while left < right:
            #取右中位数
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left

class Solution1:
    """牛顿法
    可以得到正实数的算术平方根，将牛顿法得到的浮点数转化为整数
    思想：在迭代过程中，以直线代替曲线，用一阶泰勒展开式（即当前点的切线）代替原曲线，求直线与x轴的交点，重复这个过程直到收敛
    """
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x/cur)/2
            if abs(cur-pre) < 1e-6:
                return int(cur)

if __name__ == '__main__':
    x = 8
    s = Solution1()
    print(s.mySqrt(x))