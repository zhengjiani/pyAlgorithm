# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:51
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""访问网络数据接口并从中获取照片下载链接"""
from time import time
from threading import Thread
import requests

#继承Thread类创建自定义的线程类
class DownloadHandler(Thread):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open('/Users/Hao'+filename,'wb') as f:
            f.write(resp.content)

def main():
    #通过requests模块的get函数获取网络资源
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    #将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newlist']:
        url = mm_dict['picUrl']
        #通过多线程的方式实现图片下载
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()