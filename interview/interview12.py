# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 9:33
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
输入字符串，找出全排列
"""
class Solution:
    def Permutation(self,ss):
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res)

if __name__ == "__main__":
    s = Solution()
    ss = "abc"
    print(s.Permutation(ss))

