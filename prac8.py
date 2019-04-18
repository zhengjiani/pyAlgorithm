# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:45
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
字符串的简单模拟
请实现一个函数，把字符串中的每个空格替换成"%20"。
你可以假定输入字符串的长度最大是1000。
注意输出字符串的长度可能大于1000。
"""
def replace_spaces(s,length):
    """
    :param s: 输入字符串
    :param length: 最大长度
    :return: 替换后的字符串
    """
    #判断输入是否合法
    if s == "" or len(s) > length:
        raise -1
    s = s.replace(' ', '%20')
    return s
if __name__ == '__main__':
    s = "We are happy."
    print(replace_spaces(s,1000))
