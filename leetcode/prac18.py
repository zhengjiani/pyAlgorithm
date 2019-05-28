# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 9:23
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
"""
#自定义算法实现匹配
import re


def strStr(haystack,needle):
    if needle not in haystack:
        return -1
    if needle == '':
        return 0
    n1 = len(haystack)
    n2 = len(needle)
    def helper(i):
        haystack_p = i
        needle_q = 0
        while needle_q < n2:
            if haystack[haystack_p] != needle[needle_q]:
                return False
            else:
                haystack_p += 1
                needle_q += 1
        return True
    for i in range(n1-n2+1):
        if helper(i):
            return i
    return -1
def strStr1(haystack,needle):
    if needle not in haystack:
        return -1
    if needle == '':
        return 0
    f =re.finditer(needle,haystack)
    for i in f:
        print(i.span()[0])


#KMP匹配算法
def strStr2(t,p):
    if not p:
        return 0
    #初始化字符串的部分匹配表
    _next = [0]*len(p)
    #获取字符串的部分匹配表
    def getNext(p,_next):
        _next[0] = -1
        i = 0
        j = -1
        while i<len(p)-1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]
    getNext(p, _next)
    i = 0
    j = 0
    while i < len(t) and j < len(p):
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = _next[j]
    if j == len(p):
        return i - j
    return -1


def main():
    haystack = "mississippi"
    needle = "issip"
    print(strStr2(haystack,needle))


if __name__ == '__main__':
    main()

