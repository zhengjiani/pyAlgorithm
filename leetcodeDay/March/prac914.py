# -*- encoding: utf-8 -*-
"""
@File    : prac914.py
@Time    : 2020/3/27 10:47 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
prac914卡牌分组
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
"""
import random
from collections import Counter
from functools import reduce


class Solution:
    # 暴力解法，从小到大枚举
    # 卡牌总数的约束以及互为约束
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)
        N = len(deck)
        for X in range(2,N+1):
            if N % X == 0:
                if all(v % X ==0 for v in count.values()):
                    return True
        return False

class Solution1:
    # 最大公约数解法
    def hasGroupsSizeX(self, deck):
        from math import gcd
        vals = Counter(deck).values()
        return reduce(gcd,vals) >= 2

if __name__ == '__main__':
    deck = [0,0,0,0,0,1,1,2,3,4]
    s = Solution()
    s1 = Solution1()
    print(s1.hasGroupsSizeX(deck))

