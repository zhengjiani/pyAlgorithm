# -*- encoding: utf-8 -*-
"""
@File    : prac409.py
@Time    : 2020/3/19 9:55 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
最长回文串
"""
import collections


class Solution:
    def longestPalindrome(self, s):
        num_dict = dict(collections.Counter(s))
        len = 0
        maximum = 0
        for k,v in num_dict.items():
            if (v % 2) == 0:
                # 是偶数就直接加上
                len += v
            else:
                # 是奇数就加上最大的偶数
                len += v - 1
                maximum = 1
        return len+maximum

if __name__ == "__main__":
    s1 = "abccccdd"
    s = Solution()
    print(s.longestPalindrome(s1))