#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

# 1. 两段程序哪个快些
##################################
import time

is_forloop =input("0 is list comprehension, 1 is for loop:")

min_time = 1000
avg_time = 0.0
run_loops = 1000
for num in range(run_loops):
    start_clock = time.clock()
    if is_forloop:
        a=[]
        for x in range(0,100):
            for y in range(0,100):
                if x*y>25:
                    a.append((x,y))
    else:
        a=[(x,y) for x in range(100) for y in range(100) if x*y > 25]
    
    end_clock = time.clock()
    avg_time += end_clock-start_clock
    if (end_clock-start_clock)<min_time:
        min_time = end_clock-start_clock
        
print "length of result is",len(a)
print run_loops,u"次的最好运行时间为",min_time,'s'
print run_loops,u"次的平均运行时间为",avg_time/run_loops,'s'


