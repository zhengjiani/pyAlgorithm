# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:15
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
请你写一个函数StrToInt，实现把字符串转换成整数这个功能。
当然，不能使用atoi或者其他类似的库函数。
函数应该满足的条件：
忽略所有行首空格，找到第一个非空格字符，
可以是 ‘+/−’ 表示是正数或者负数，紧随其后找到最长的一串连续数字，将其解析成一个整数；
整数后可能有任意非数字字符，请将其忽略
如果整数长度为0，则返回0；数字前面出现字母直接终止，返回0，数字后面出现其他字符，返回n
如果整数大于INT_MAX(2^31 − 1)，请返回INT_MAX；如果整数小于INT_MIN(−2^31) ，请返回INT_MIN；
"""
import re
def str_to_int(s):
    """
    :param s: str
    :return: int
    """
    #查找字符串中所有符合条件的数
    ret = re.findall(r"^[-+]?\d+",s.strip())
    if ret:
        #取字符串首位
        ret_str = ret[0]
        if ret_str[0] == "+" or ret_str[0] == "-":
            #ret_str2表示除首位符号以外的
            ret_str2 = ret_str[1:]
        else:
            ret_str2 = ret_str
        ret_int = int(ret_str2)
        if ret_str[0] == "-":
            return -ret_int if ret_int <= 2**31 else -2**31
        else:
            return ret_int if ret_int < 2**31 else 2**31-1
    else:
        return 0
if __name__ == '__main__':
    s = "-1B2345"
    print(str_to_int(s))