# -*- coding: utf-8 -*-
# CopyRight by heibanke

import urllib
from bs4 import BeautifulSoup

url='http://www.heibanke.com/lesson/crawler_ex00/'
content = urllib.urlopen(url)

bs_obj = BeautifulSoup(content,"html.parser")
number = bs_obj.find("strong")

print number.get_text()