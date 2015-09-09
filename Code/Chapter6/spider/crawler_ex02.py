#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()
driver.get("http://www.heibanke/accounts/login")
time.sleep(3)
driver.find_element_by_id("id_username").send_keys("test")
driver.find_element_by_id("id_password").send_keys("test123")
driver.find_element_by_id("id_submit").click()
time.sleep(1)


number = 0


driver.get("http://www.heibanke/lesson/crawler_ex02/")
time.sleep(2)    
driver.find_element_by_name("username").send_keys("flysmoke")
driver.find_element_by_name("password").send_keys(str(number))
driver.find_element_by_id("id_submit").click()

#find_element_by_xpath
html = driver.page_source

bs_obj = BeautifulSoup(html,"html.parser")

if bs_obj.text.find(u"输入的密码错误")>0:
    print u"输入的密码",number,u"错误"
    number = number+1
else:
    print bs_obj.text


time.sleep(2)
driver.close()
