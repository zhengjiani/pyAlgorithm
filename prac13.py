# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 12:12
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student."，则输出"student. a am I"。
思路
本题类似于将一个数组前k个数平移到末尾的问题，该问题分为两步：先将前k个元素和之后的元素分别翻转，再将数组整体翻转。
所以本题方法类似，先将每个单词逐一翻转，再将整个字符串也翻转下即可得到答案。
"""
def reverse_words(s):
    if s is None or len(s)==0:
        return s
    return " ".join(s.split(' ')[::-1])
if __name__ == '__main__':
    s="I am a student."
    print(reverse_words(s))