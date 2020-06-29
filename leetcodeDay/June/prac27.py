# -*- encoding: utf-8 -*-
"""
@File    : prac27.py
@Time    : 2020/6/29 9:03 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 转二进制
        x, y = int(a,2), int(b,2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

if __name__ == '__main__':
    a = "11"
    b = "1"
    sl = Solution()
    print(sl.addBinary(a,b))