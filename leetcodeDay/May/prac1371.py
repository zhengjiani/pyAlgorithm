# -*- encoding: utf-8 -*-
"""
@File    : prac1371.py
@Time    : 2020/5/20 7:53 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
不重复遍历子串的前提下，快速求出区间字母出现的次数->前缀和
一个区间可以用两个前缀和的差值，得到某个字母的出现次数
[(00000)2,(11111)2]
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        state = [-1]*(1 << 5)
        cur, state[0] = 0, 0
        d = dict(zip('aeiou',range(5)))
        for idx,val in enumerate(s):
            tmp = -1
            if val in d:
                tmp = d[val]
            if tmp != -1:
                cur ^= 1 << tmp
            if state[cur] == -1:
                state[cur] = idx + 1
            else:
                res = max(res,idx+1-state[cur])
        return res


if __name__ == '__main__':
    s = "eleetminicoworoep"
    s1 = Solution()
    print(s1.findTheLongestSubstring(s))