# -*- encoding: utf-8 -*-
"""
@File    : 面试题17.13.py
@Time    : 2020/7/9 7:36 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from typing import List


# class Solution:
#
#     def respace(self, dictionary: List[str], sentence: str) -> int:
#         i, j = 0, 0
#         n = len(sentence)
#         for i in range(n):
#             if sentence[i:j] in dictionary:
#                 res = sentence.replace(sentence[i:j],'')
#             else:
#                 j += 1
#             i += 1
#         return len(res)

class Solution:
    """
    - 第i个字符无法与前面任何一个子串组成单词时，第i个字符算作一个未识别字符f[i]=f[i-1]+1
    - 第i个字符可以与前面某个子串组成单词时
        -  j的取之从0到i-1，j == 0时，新加入第i个字符恰好和前面所有字符组成一个单词；j == i-1时，字典里刚好有第i个字符形成的单字母单词
        - 本题主要求未识别的字符数，对应状态f[j]，所以这种情况下f[i]=f[j]
    """
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0]*(n+1)
        for i in range(1,n+1):
            f[i] = f[i-1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    f[i] = min(f[i],f[j])
        return f[-1]
if __name__ == '__main__':
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"
    sl = Solution()
    print(sl.respace(dictionary, sentence))
