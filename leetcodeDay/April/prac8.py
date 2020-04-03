# -*- encoding: utf-8 -*-
"""
@File    : prac8.py
@Time    : 2020/4/3 9:43 上午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
字符串转换整数
"""
import re


class Solution:
    """采用正则表达式"""
    def myAtoi(self,str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # 去除左边空格
        str = str.lstrip()
        # 设置正则规则
        num_re = re.compile(r'^[\+\-]?\d+')
        # 查找匹配内容
        num = num_re.findall(str)
        # 由于返回的是列表，解包转换成整数
        num = int(*num)
        return max(min(num,INT_MAX),INT_MIN)

if __name__ == '__main__':
    str = "   -42"
    s = Solution()
    print(s.myAtoi(str))