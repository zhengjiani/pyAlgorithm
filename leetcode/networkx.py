# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 14:15
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import lxml
import time
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://zhengjiani.cn:8080/#/login?redirect=%2Fdashboard')
driver.find_element_by_xpath("//*[@id='app']/div/form/div[2]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/button").click()
time.sleep(2)
cookie_list = driver.get_cookies()
for item in cookie_list: driver.add_cookie(
    {
        'domain': 'localhost',
        'httpOnly': False,
        'name': 'X-Litemall-Admin-Token',
        'path': '/',
        'secure': False,
        'value': '1fpzctbhesj4eqfg5e2k6gkg77m2u220'
    }
)
time.sleep(5)
html1 = driver.page_source
page=etree.HTML(html1)
result=page.xpath('//@href')
print('链接数量{}'.format(len(result)))
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/ul/div[2]/li").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]/li").click()
time.sleep(5)
html2 = driver.page_source
page=etree.HTML(html2)
result2=page.xpath('//button')
print(result2)
print('用户管理按钮{}'.format(len(result2)))
driver.close()
