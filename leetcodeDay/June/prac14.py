# -*- encoding: utf-8 -*-
"""
@File    : prac14.py
@Time    : 2020/6/15 9:40 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


class Solution:
    """水平扫描法"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    sl = Solution()
    print(sl.longestCommonPrefix(strs))