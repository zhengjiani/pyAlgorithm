# -*- encoding: utf-8 -*-
"""
@File    : prac50.py
@Time    : 2020/5/11 9:47 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """快速幂算法
    测试用例设计
    - x = 0,1的情况
    - n = 0,1的情况
    - 测试n为负数的情况
    - 是否需要考虑溢出（Double数越界的情况）INT_MIN
    - 其他正常测试
    """
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N//2)
            return y*y if N%2 == 0 else y*y*x
        return quickMul(n) if n >= 0 else 1/quickMul(-n)

class Solution1:
    """快速幂+迭代
    以x^77为例，每个额外乘的x都会被平方若干次，而这些指数1，4，8和64，恰好对应了77的二进制(1001101)2表示中的每个1
    """
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为x
            x_contribute = x
            # 在对N进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果N二进制表示的最低位为1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断的平方
                x_contribute *= x_contribute
                # 舍弃N二进制表示的最低位，这样我们每次只要判断最低位即可
                N // 2
            return ans
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
if __name__ == '__main__':
    x,n = 2.00000, 10
    s = Solution()
    print(s.myPow(x,n))