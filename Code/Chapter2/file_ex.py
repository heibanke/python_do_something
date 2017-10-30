#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

########################## file ################
import codecs
f=codecs.open('file_ch.txt','w','utf-8')

f.write(u'用python做些事\n')
f.write(u'黑板客\n')
f.write(u'网易云课堂\n')
f.close()

#read file
f=codecs.open('file_ch.txt','r','utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
########################## os ################
import os
print(os.path.exists('file_ch.txt'))
os.rename('file_ch.txt', 'file_test.txt')
print(os.path.exists('file_ch.txt'))
