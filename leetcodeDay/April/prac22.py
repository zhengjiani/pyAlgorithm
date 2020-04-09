# -*- encoding: utf-8 -*-
"""
@File    : prac22.py
@Time    : 2020/4/9 8:54 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from functools import lru_cache
from typing import List


class Solution:
    """按括号序列的长度进行递归"""
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n==0:
            return ['']
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left,right))
        return ans

class Solution2:
    """回溯解法
    模式识别：确保每一步都能产生有效序列，利用回溯搜索其他可能的解
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

class Solution1:
    """
    暴力解法
    1.生成所有序列
    2.检查是否有效
    3.模式识别：子问题与原问题有相同结构，考虑自上而下的递归
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                # 加入伪括号变成2*n的情况
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal<0:
                    return False
            return bal == 0
        ans = []
        generate([])
        return ans
if __name__ == '__main__':
    n = 3
    s = Solution()
    s1 = Solution1()
    s2 = Solution2()
    print(s.generateParenthesis(n))
    print(s1.generateParenthesis(n))
    print(s2.generateParenthesis(n))