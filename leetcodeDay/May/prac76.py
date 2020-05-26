# -*- encoding: utf-8 -*-
"""
@File    : prac76.py
@Time    : 2020/5/23 9:59 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    def __init__(self):
        import collections
        self.ori = collections.defaultdict(int)
        self.cnt = collections.defaultdict(int)

    def cheak(self):
        for key, value in self.ori.items():
            if key not in self.cnt.keys() or self.cnt[key] < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        for ti in t:
            self.ori[ti] += 1
        l, r = 0, -1
        length, ansL, ansR = float('inf'), -1, -1
        sLen, tLen = len(s), len(t)
        while r < sLen:
            r += 1
            if r < sLen and s[r] in self.ori.keys():
                self.cnt[s[r]] += 1
            while self.cheak() and l <= r:
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l
                    ansR = l + length
                if s[l] in self.ori.keys():
                    self.cnt[s[l]] -= 1
                l += 1
        return "" if ansL == -1 else s[ansL:ansR]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    sl = Solution()
    print(sl.minWindow(s,t))