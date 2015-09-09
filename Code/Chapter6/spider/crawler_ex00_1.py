# -*- coding: utf-8 -*-
# CopyRight by heibanke

import urllib
from bs4 import BeautifulSoup

url='http://www.heibanke.com/lesson/crawler_ex00/'
number=''
loops = 0

while True:
    content = urllib.urlopen(url+number)

    bs_obj = BeautifulSoup(content,"html.parser")
    tag_number = bs_obj.find("strong")
    
    if not tag_number or loops>100:
        break
    else:
        number = tag_number.get_text()
        print number

    loops+=1


print bs_obj.text