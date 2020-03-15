# -*- encoding: utf-8 -*-
"""
@File    : cal_time.py
@Time    : 2020/1/3 5:51 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import time
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__,t2-t1))
        return result
    return wrapper