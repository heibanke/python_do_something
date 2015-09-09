#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://baike.baidu.com/view/284853.htm')
bs_obj = BeautifulSoup(html,"html.parser")

#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
#recursive=False表示只搜索直接儿子，否则搜索整个子树，默认为True。
#findAll(“a”）
#findAll(“a”, href=“”)
#findAll(“div”, class=“”)
#findAll(“button”, id=“”)

#a_list = bs_obj.findAll("a")
a_list = bs_obj.findAll("a",href=re.compile("baike\.baidu\.com\w?"))


for aa in a_list:
    if not aa.find("img"):
        if aa.attrs.get('href'):
            print aa.text, aa.attrs['href']
        