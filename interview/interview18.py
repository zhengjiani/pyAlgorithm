# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 20:54
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from collections import Counter
def func(s):
    if len(s) == 0 or len(s) == 1:
        return (s, len(s))
    result = [1] * len(s)
    for left in range(len(s) - 1):
        for right in range(left + 1, len(s)):
            if s[left] == s[right]:
                result[left] += 1
            else:
                break
    dic = {}
    dic[s[result.index(max(result))]]=max(result)
    s = s[result.index(max(result)):len(s)-1]
    return func(s)


if __name__ == "__main__":
    s = "aaabcccaddfffaa"
    func(s)
