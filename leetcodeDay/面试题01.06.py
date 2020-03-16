# -*- encoding: utf-8 -*-
"""
@File    : 面试题01.06.py
@Time    : 2020/3/16 8:56 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
面试题01.06 字符串压缩，利用字符出现的次数，编写一种方法，实现基本的字符串压缩功能
"""
class Solution:
    def compressString(self, S):
        if not S:
            return ""
        ch = S[0]
        lis = ''
        num = 0
        for i in S:
            if i == ch:
                num += 1
            else:
                lis += ch + str(num)
                ch = i
                num = 1
        lis += ch + str(num)
        return lis if len(lis) < len(S) else S

class Solution1:
    # 双指针法取连续字符
    def compressString(self, S):
        N = len(S)
        i = 0
        lis = ''
        while i < N:
            j = i
            while j < N and S[j] == S[i]:
                j += 1
            lis += S[i] + str(j - i)
            i = j
        return lis if len(lis) < len(S) else S





if __name__ == '__main__':
    s = Solution()
    s1 = Solution1()
    S = "aabcccccaaa"
    print(s.compressString(S))
    print(s1.compressString(S))