#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import urllib 
from bs4 import BeautifulSoup

url="http://www.heibanke.com"
html = urllib.urlopen(url)
bs_obj = BeautifulSoup(html,"html.parser")

imageLocation = bs_obj.find("img")["src"]
urllib.urlretrieve(url+imageLocation, "logo.jpg")