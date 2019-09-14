# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:01
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from decimal import Decimal
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 计算共有多少个1
        count = 0
        tmp = n
        base = 1
        while tmp:
            last = tmp %10
            tmp = tmp / 10
            count +=tmp * base
            # 百位等于1，count（累加过last==0情况）受高位影响1200个，受低位影响113+1个
            if last == 1:
                count += n%base + 1
            elif last > 1:
                count += base
            base *= 10
        return count
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        mult, sumTimes = 1, 0
        while n // mult > 0:
            high, mod = divmod(n, mult * 10)
            curNum, low = divmod(mod, mult)
            if curNum > 1:
                sumTimes += high * mult + mult
            elif curNum == 1:
                sumTimes += high * mult + low + 1
            else:
                sumTimes += high * mult
            mult = mult * 10
        return sumTimes
if __name__ == "__main__":
    # s = Solution()
    # print(s.NumberOf1Between1AndN_Solution(1300))
    s1 = Solution1()
    print(s1.NumberOf1Between1AndN_Solution(1300))
    # 报错：OverflowError: int too large to convert to float
    # from decimal import Decimal