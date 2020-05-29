# -*- encoding: utf-8 -*-
"""
@File    : prac394.py
@Time    : 2020/5/28 1:18 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """辅助栈"""
    def decodeString(self, s: str) -> str:
        stack,res,multi = [],"",0
        for c in s:
            if c == '[':
                stack.append([multi,res])
                res,multi = "",0
            elif c == ']':
                cur_multi,last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res

class Solution1:
    """递归法"""
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)

if __name__ == '__main__':
    s = "3[a]2[bc]"
    sl = Solution()
    print(sl.decodeString(s))