# -*- encoding: utf-8 -*-
"""
@File    : prac680.py
@Time    : 2020/5/19 2:02 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low,high):
            """
            检查字符串是否是回文串
            :param low:
            :param high:
            :return:
            """
            i,j = low,high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low,high = 0,len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low+1,high) or checkPalindrome(low,high-1)
        return True