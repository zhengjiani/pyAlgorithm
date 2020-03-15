# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 17:10
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
输入
每组输入数据为两行，第一行为有关约德尔人历史的字符串，第二行是黑默丁格观测星空得到的字符串。
(两个字符串的长度相等,字符串长度不小于1且不超过1000。)
输出
输出一行，在这一行输出相似率。用百分数表示。(相似率为相同字符的个数/总个数,精确到百分号小数点后两位。printf("%%");输出一个%。)
样例输入
@!%12dgsa
010111100
样例输出
66.67%
"""


def comparesimlar(s):
    old = list(s[0])
    std = list(s[1])
    total = len(old)
    count = 0
    for i in range(total):
        if old[i].isalnum() or old[i].isdigit():
            old[i] = '1'
        else:
            old[i] = '0'
    for i in range(total):
        if old[i] == std[i]:
            count += 1
        else:
            continue
    sim = count / total
    print('{:.2%}'.format(sim))


# if __name__ == '__main__':
s = []
while 1:
    lines = input()
    if lines != "":
        for x in lines.split():
            s.append(str(x))
    else:
        break
print(s)
