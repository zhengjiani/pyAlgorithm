# -*- encoding: utf-8 -*-
"""
@File    : prac365.py
@Time    : 2020/3/21 8:52 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
水壶问题：有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
你允许：
装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
"""
import math


class Solution:
    def canMeasureWater(self, x, y, z):
        # 深度优先搜索
        stack = [(0,0)]
        self.seen = set()
        # remain_x表示x中现有的水量
        while stack:
            remain_x,remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x,remain_y) in self.seen:
                continue
            self.seen.add((remain_x,remain_y))
            # 把x灌满
            stack.append((x,remain_y))
            # 把y灌满
            stack.append((remain_x,y))
            # 倒空x
            stack.append((0,remain_y))
            # 倒空y
            stack.append((remain_x,0))
            # 把x的水灌进y壶，直至灌满或倒空
            stack.append((remain_x - min(remain_x,y-remain_y), remain_y + min(remain_x,y-remain_y)))
            # 把y的水灌进x壶，直至灌满或倒空
            stack.append((remain_x + min(x-remain_x,remain_y), remain_y-min(x-remain_x,remain_y)))
        return False

class Solution1:
    def canMeasureWater(self, x, y, z):
        # 裴蜀定理（或贝祖定理）说明了对任何整数a、b和它们的最大公约数d，
        # 关于未知数x和y的线性不定方程（称为裴蜀等式）：若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，
        # 特别地，一定存在整数x,y，使ax+by=d成立。
        # 它的一个重要推论是：a,b互质的充要条件是存在整数x,y使ax+by=1.
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x,y) == 0
if __name__ == '__main__':
    x,y,z = 3,5,4
    s = Solution()
    print(s.canMeasureWater(x,y,z))