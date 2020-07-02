# -*- encoding: utf-8 -*-
"""
@File    : prac125.py
@Time    : 2020/7/2 8:58 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Solution1:
    """筛选+判断：使用字符串函数"""
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

class Solution2:
    """双指针"""
    def isPalindrome(self, s: str) -> bool:
        sl = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sl)
        left,right = 0, n-1
        while left < right:
            if sl[left] != sl[right]:
                return False
            left, right = left + 1, right - 1
        return True



if __name__ == '__main__':
    sl = Solution1()
    s = "A man, a plan, a canal: Panama"
    print(sl.isPalindrome(s))