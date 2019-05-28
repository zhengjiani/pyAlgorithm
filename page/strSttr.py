# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 10:56
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import re
i = re.search('ll', 'helloll', flags=0)
#<re.Match object; span=(2, 4), match='ll'>
j = re.match('ll', 'helloll', flags=0)
#None
k = re.split('ll', 'helloll', maxsplit=1,flags=0)
print(k)