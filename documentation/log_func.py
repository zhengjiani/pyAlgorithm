# -*- encoding: utf-8 -*-
"""
@File    : log_func.py
@Time    : 2020/3/27 7:26 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
日志记录
"""
# 将日志记录记录到文件
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('日志记录文件')
# logging.info('info information')
# logging.warning('And this,too')
# 记录可变数据
logging.warning('%s before you %s','Look','leap')
# WARNING:root:Look before you leap