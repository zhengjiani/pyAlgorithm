# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:13
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""多线程实现下载文件"""
from random import randint
from threading import Thread
from time import time,sleep

def download(filename):
    print('开始下载%s...'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒'%(filename,time_to_download))

def main():
    start = time()
    t1 = Thread(target=download,args=('从刚入门.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒'%(end-start))

if __name__ == '__main__':
    main()