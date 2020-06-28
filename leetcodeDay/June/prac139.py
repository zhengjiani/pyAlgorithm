# -*- encoding: utf-8 -*-
"""
@File    : prac139.py
@Time    : 2020/6/28 3:17 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        :param s: string
        :param wordDict: list
        :return: boolean
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]

if __name__ == '__main__':
    s = "leeatcode"
    wordDict = ["leet", "code"]
    sl = Solution()
    print(sl.wordBreak(s,wordDict))