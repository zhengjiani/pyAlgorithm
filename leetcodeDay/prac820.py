# -*- encoding: utf-8 -*-
"""
@File    : prac820.py
@Time    : 2020/3/28 10:16 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
单词的压缩编码
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
1 <= words[i].length <= 7，数据范围一个单词最多含有7个后缀
"""
import collections
from functools import reduce


class Solution:
    def minimumLengthEncoding(self, words):
        # 目的是保留不是其他单词后缀的单词
        # 每一个单词后加#，就是目标单词长度加1的长度之和
        good = set(words)
        for word in words:
            for k in range(1,len(word)):
                good.discard(word[k:])
        return sum(len(word)+1 for word in good)

class Solution1:
    def minimumLengthEncoding(self, words):
        # 字典树 -> 寻找不同的单词是否有相同的后缀，将他们反序插入字典树中，统计叶子节点代表的单词长度+1
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        nodes = [reduce(dict.__getitem__,word[::-1],trie) for word in words]
        return sum(len(word)+1 for i,word in enumerate(words) if len(nodes[i]) == 0)



if __name__ == '__main__':
    words = ["time", "me", "bell"]
    s = Solution1()
    print(s.minimumLengthEncoding(words))