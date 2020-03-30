# -*- encoding: utf-8 -*-
"""
@File    : files.py
@Time    : 2020/3/27 1:42 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
压缩文件
默认情况下提供的压缩格式zip,tar,gztar,bztar,xztar
"""

import shutil
from shutil import make_archive
import os
# 压缩
# os.path.expanduser把path中包含的"~"和"myarchive"转换成用户目录
# archive_name = os.path.expanduser(os.path.join('~','myarchive'))
# root_dir = os.path.expanduser(os.path.join('~','.ssh'))
# make_archive(archive_name,'gztar',root_dir)
# 解压缩
# filename = os.path.expanduser(os.path.join('~','myarchive.tar.gz'))
# root_dir = os.path.expanduser(os.path.join('~','myarchive'))
# shutil.unpack_archive(filename,root_dir,'gztar')
print(os.path.abspath('pyAlgorithm/prac20.py')) #返回绝对路径
print(os.path.basename('/Users/zhengjiani/PycharmProjects/pyAlgorithm/prac20.py')) #返回相对路径
# /Users/zhengjiani/PycharmProjects/pyAlgorithm/documentation/pyAlgorithm/prac20.py
# prac20.py
print(os.path.dirname('/Users/zhengjiani/PycharmProjects/pyAlgorithm/prac20.py'))
# /Users/zhengjiani/PycharmProjects/pyAlgorithm
print(os.path.isfile('/Users/zhengjiani/PycharmProjects/pyAlgorithm/prac20.py'))
# True
print(os.path.join('~','zjn','jjj'))
# ~/zjn/jjj
print(os.path.split('/Users/zhengjiani/PycharmProjects/pyAlgorithm/prac20.py'))
# ('/Users/zhengjiani/PycharmProjects/pyAlgorithm', 'prac20.py')拆分成dirname和basename
# 文件名模式匹配
import fnmatch
import os
names = []
for file in os.listdir('..'):
    if fnmatch.fnmatch(file,'*.py'):
        print(file)
        names.append(file)
print(names)
lis = [n for n in names if fnmatch.filter(n,'*')]
print(lis)