# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:46
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
字符串的最小表示法的概念。我们需要求一个字符串的循环同构体中最小字典序的那个。
比如bcda的循环同构体有bcda，cdab，dabc，abcd，其中最小表示法是abcd。
"""

#字符串的最小表示法
def find_min(s):
    i = 0 #起始指针
    j = 1 #指向第一位
    k = 0 #匹配长度
    size = len(s)
    while i<size and j<size and k<size:
        a = (i+k) % size
        b = (j+k) % size
        if s[a] == s[b]:
            k += 1
        elif s[a]>s[b]:
            i += k+1
            k = 0 #已匹配长度置0
        else:
            j += k+1
            k = 0
        if i==j:
            j += 1
    return min(i,j)#返回最小表示的位置

def main():
    s = 'bcdabcebdd'
    print(find_min(s)+1)

if __name__ == '__main__':
    main()








