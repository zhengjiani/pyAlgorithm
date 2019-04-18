# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 16:57
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
题目描述：
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

目前看到三种解法：正则解法，剑指解法以及有限自动机解法
"""
def is_number(s):
    """
    剑指解法
    :param s:
    :return:
    """
    n = len(s)
    if n<0:
        return False
    #正负号标志
    ab = False
    #e标志
    he = False
    #小数点标志
    po = False
    i = 0
    while i < n:
        if s[i] == '+' or s[i] == '-':
            #如果没有e字符串中至多出现一次正负号或者整个字符串只有一个正负号
            if(ab or (i>0 and (s[i-1] != 'e') and (s[i-1] != 'E')) or n==1):
                return False
            ab = True
        elif s[i] == '.':
            #小数点前后至少有一边是数字
            if(i==0 and (i+1 == n or (s[i+1].isdigit()==False))):
                return False
            if(he or po or (s[i-1].isdigit()==False and s[i+1].isdigit()==False)):
                return False
            po = True
        elif s[i] == 'e' or s[i] == 'E':
            if(i-1 < 0 or i+1 >= n or he):
                return False
            #e的左边一位可以是.或者数字
            if(s[i-1] == '.' or s[i-1].isdigit()):
                if s[i+1].isdigit():
                    he = True
                elif((s[i+1] == '+' or s[i+1] == '-') and i+2 <n and s[i+2].isdigit == True):
                    he = True
            if not he:
                return False
            ab = False
            po = True
        else:
            if s[i].isdigit() == False:
                return False
        i += 1
    return True
if __name__ == '__main__':
    s1 = "1a3.14"
    s2 = "5e2"
    print(is_number(s1))
    print(is_number(s2))
