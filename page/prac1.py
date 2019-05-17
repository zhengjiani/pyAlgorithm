# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 21:54
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""设计一个函数产生指定长度的验证码，由大小写字母和数字构成"""
import random
def generate_code(code_len=4):
    """
    生成指定长度验证码
    :param code_len:  验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code
