# -*- encoding: utf-8 -*-
"""
@File    : prac32.py
@Time    : 2020/7/4 8:34 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution1:
    """暴力解法，偶数+从大到小遍历"""
    def longestValidParentheses(self, s: str) -> int:
        def isValid(x):
            stack = []
            for i in range(len(x)):
                if x[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

        if len(s) < 2:
            return 0
        n = len(s)
        for i in range(n if n%2==0 else n-1,0,-2):
            for j in range(n-i+1):
                if isValid(s[j:j+i]):
                    return i
        return 0

class Solution2:
    """动态规划 i-dp[i-1]-1是与当前）对称的位置"""
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0]*n
        for i in range(len(s)):
            if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1]=='(':
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)

class Solution3:
    """用栈来实现"""
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length,length)
        return max_length

class Solution4:
    """正向逆向相结合的方法
    当右括号个数 > 左括号个数的时候，直接将"左括号个数"、"右括号个数"重新初始化为0
    逆向遍历时，当右括号 < 左括号个数，直接将"左括号个数"、"右括号个数"重新初始化为0
    时间复杂度O(N)，空间复杂度O(1)
    """
    def longestValidParentheses(self, s: str) -> int:
        n, left, right, maxlength = len(s), 0, 0, 0
        # 正序遍历
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength,2*right)
            elif right > left:
                left = right = 0
        # 反序遍历
        left = right = 0
        for i in range(n-1,-1,-1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength,2*left)
            elif right < left:
                left = right = 0
        return maxlength


if __name__ == '__main__':
    sl = Solution1()
    print(sl.longestValidParentheses("()(())"))
    # sl = Solution2()
    # print(sl.longestValidParentheses("()(()))"))