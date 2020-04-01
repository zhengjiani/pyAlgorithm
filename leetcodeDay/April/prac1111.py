# -*- encoding: utf-8 -*-
"""
@File    : prac1111.py
@Time    : 2020/4/1 9:35 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
划分出最大嵌套深度最小的分组
"""
class Solution:
    """用抽象栈进行括号匹配，奇偶分组"""
    def maxDepthAfterSplit(self, seq):
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d%2)
            if c == ')':
                ans.append(d%2)
                d -= 1
        return ans
class Solution1:
    """奇偶分组"""
    def maxDepthAfterSplit(self, seq):
        """
        左括号 ( 的下标编号与嵌套深度的奇偶性相反
        右括号 ) 的下标编号与嵌套深度的奇偶性相同
        :param seq:
        :return:
        """
        ans = list()
        for i,ch in enumerate(seq):
            if ch == '(':
                ans.append(i%2)
            else:
                ans.append(1-i%2)
        return ans
if __name__ == '__main__':
    seq = "()(())()"
    s = Solution1()
    print(s.maxDepthAfterSplit(seq))