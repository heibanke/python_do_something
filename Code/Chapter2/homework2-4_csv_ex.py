#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import csv
import re 

csvfile = open('beijing_jt.csv','r')

reader = csv.reader(csvfile)
# reader.next() only can use in py2
next(reader)

jt_info = next(reader)

print(jt_info[1].decode('utf-8'))
        
csvfile.close()

# convert stations info format
station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')
station_list = []

stations = re.findall(station_pattern,jt_info[-1].decode('utf-8')) 
for tmp in stations:
    print(tmp[0],tmp[1].strip())
    station_list.append(tmp[1].strip())
    
result={}
result[jt_info[1]]=station_list

print(result)