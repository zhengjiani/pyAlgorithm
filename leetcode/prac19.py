# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 16:59
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
部分匹配表
获取“模式串”的部分匹配值
https://www.jianshu.com/p/320952d14632
"""
def pmt(s):
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(s)):
        prefix.add(s[:i])
        postfix = {s[j:i + 1] for j in range(1, i + 1)}
        ret.append(len(prefix & postfix))
    return ret
def kmp(t,p):
    """p是模式串"""
    m, n = len(t), len(p)
    cur = 0  # 起始指针cur
    table = pmt(p)
    while cur <= m - n:  # 最多做m-n趟匹配
        for i in range(n):  # 在每一趟比较中
            if t[i + cur] != p[i]:  # 匹配不成功时
                cur += max(i - table[i - 1], 1)  # 移动的位数 = 以匹配的字符数 - 匹配值
                break
        else:
            return True
    return False
if __name__ == '__main__':

    print(pmt("ABCDA"))
    print(kmp("BBC ABCDAB ABCDABCDABDE","ABCDABD"))
