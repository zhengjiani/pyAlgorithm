# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 10:36
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
递归求解的方法
"""
def is_match(s,p):
    """

    :param s: 字符串
    :param p: 模式串
    :return: type(bool)
    """
    #s与p都为空，匹配，但是s为空也可以匹配p不为空，比如p为2*，*可以让前面字符出现次数变为0。
    # 当然，一旦模式串p为空，而s非空，那么肯定是不匹配的。
    if len(p)==0:
        return False
    return _match(s,p,0,0)
def _match(s,p,a,b):
    #在b刚刚越界时判断一下a是否也越界了
    if b==len(p):
        return a==len(s)
    #由于分类时首先考虑的是p[b+1]，所以还需要判断b是否是最后一个字符，如果是，只有在a也到达最后的字符且匹配整体才匹配。
    if b+1 == len(p):
        return a+1 == len(s) and (s[a] == p[b] or p[b] == '.')
    #直接比较s[a]和p[b]，匹配时指针均右移
    if p[b+1] != '*':
        if s[a]==p[b] or p[b]=='.':
            return _match(s,p,a+1,b+1)
        return False
    #p[b+1]='*'如果*不表示把p[b]出现次数置为0，那么就不匹配，所以此时我们考虑下一种状态
    if s[a] != p[b] and p[b] != '.':
        return _match(s,p,a,b+2)
    #s[a] == p[b]，此时就是不确定性有限状态机问题了，我们可以进一步转化为三种状态。
    # 即使当前字符匹配，我们还是让它出现的次数为0，说不定p后面的字符会和s当前字符匹配
    #*使得p[b]出现一次，也就是b直接右移两位进行比较即可match(s,p,a+1,b+2)
    #*使得p[b]出现不小于2次，那么可以递归的转化为子问题，b不变，a右移一位match(s,p,a+1,b)
    return _match(s,p,a,b+2) or _match(s,p,a+1,b+2) or _match(s,p,a+1,b)

if __name__ == '__main__':
    s="aaa"
    p="ab*a"
    print(is_match(s,p))