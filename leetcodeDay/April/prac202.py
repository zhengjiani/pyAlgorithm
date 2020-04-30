# -*- encoding: utf-8 -*-
"""
@File    : prac202.py
@Time    : 2020/4/30 2:05 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """暴力解法，递归超出深度"""
    def isHappy(self, n: int) -> bool:
        res = 0
        if res == 1:
            return True
        nums = list(str(n))
        for num in nums:
            num = int(num)
            res += pow(num,2)
        self.isHappy(res)
class Solution1:
    """HashSet检测循环"""
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                # 数位拆分
                n,digit = divmod(n,10)
                total_sum += digit ** 2
            return total_sum
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


if __name__ == '__main__':
    s = Solution1()
    n = 19
    print(s.isHappy(n))
