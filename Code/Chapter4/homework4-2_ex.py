#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import csv
import re 
import pprint

def readData():

    csvfile = open('beijing_jt.csv','r')

    reader = csv.reader(csvfile)
    reader.next()

    result={}

    while True:
        try:
            jt_info = reader.next()
        except:
            break

        #print jt_info[1].decode('utf-8')
        # convert stations info format
        station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')
        station_list = []

        stations = re.findall(station_pattern,jt_info[-1].decode('utf-8')) 
        for tmp in stations:
            #print tmp[0],tmp[1].strip()
            station_list.append(tmp[1].strip())
    	
    	result[jt_info[1]]=station_list        


    csvfile.close()
    return result

def find_station(s,stations):
    line_list=[]
    for k,v in stations.iteritems():
        if unicode(s,'utf-8') in v:
            print k,s
            line_list.append((k,v))
    return line_list

def print_lines(lines):
    for l in lines:
        print unicode(l[0],'utf-8'),unicode(l[1],'utf-8'),u"中转站:",l[2]

if __name__=="__main__":

    stations=readData()
    print u"请输入你想查询的起始站名："
    start_station = raw_input()
    start_lines=find_station(start_station,stations)

    print u"请输入你想查询的终点站名："
    end_station = raw_input()
    end_lines=find_station(end_station,stations)

    #无需换乘
    your_selects=[]
    for i in start_lines:
        if i in end_lines:
            your_selects.append(i[0])

    print u"直达的公交："
    for l in your_selects:
        print unicode(l,'utf-8')

    
    #换乘一次
    huancheng_one=[]
    for i in start_lines:
        for j in end_lines:
            for mid_station in i[1]:
                if mid_station in j[1]:
                    huancheng_one.append((i[0],j[0],mid_station))
                    break


    print u"换乘一次的公交："
    print_lines(huancheng_one)
    
