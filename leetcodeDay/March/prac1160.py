# -*- encoding: utf-8 -*-
"""
@File    : prac1160.py
@Time    : 2020/3/17 8:10 AM
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
拼写单词
"""
import collections


class Solution:
    def countCharacters(self,words,chars):
        # 哈希表计数，将word中单词每个字母的数量与chars中每个字母的数量进行对比
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans


if __name__ == '__main__':
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    s = Solution()
    print(s.countCharacters(words,chars))
