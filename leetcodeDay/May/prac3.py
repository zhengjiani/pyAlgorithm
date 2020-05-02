# -*- encoding: utf-8 -*-
"""
@File    : prac3.py
@Time    : 2020/5/2 1:50 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution:
    """滑动窗口及优化，时间复杂度是O(n)，空间复杂度是O(m),m为字符空间
    测试：
    - 字符串为空的情况
    - 字符串均为重复字符的情况
    - 其他常规输入
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1,0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans,rk - i + 1)
        return ans
if __name__ == '__main__':
    string = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(string))