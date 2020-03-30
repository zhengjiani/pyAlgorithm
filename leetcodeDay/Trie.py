# -*- encoding: utf-8 -*-
"""
@File    : Trie.py
@Time    : 2020/3/28 11:20 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
class Trie:
    def __init__(self):
       self._end = '_end_'

    def make_trie(self,*words):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter,{})
            current_dict[self._end] = self._end
        return root

    def in_trie(self,trie,word):
        current_dict = trie
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return self._end in current_dict

if __name__ == '__main__':
    trie = Trie()
    print(trie.make_trie('foo', 'bar', 'baz', 'barz'))
    print(trie.in_trie(trie.make_trie('foo', 'bar', 'baz', 'barz'),'bar'))