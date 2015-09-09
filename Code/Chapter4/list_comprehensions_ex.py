#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

# 1. 两段程序哪个快些
##################################
import time

def list_comp():
    return [(x,y) for x in range(100) for y in range(100) if x*y > 25]
    
def for_loop():
    a=[]
    for x in range(0,100):
        for y in range(0,100):
            if x*y>25:
                a.append((x,y)) 
    return a
                
def test_time(f,run_loops):
    best_time = 1000
    avg_time = 0.0
    worse_time = 0.0

    for num in range(run_loops):
        start_clock = time.clock()
        a=f()   
        end_clock = time.clock()
        avg_time += end_clock-start_clock
        if (end_clock-start_clock)<best_time:
            best_time = end_clock-start_clock
        if (end_clock-start_clock)>worse_time:
            worse_time = end_clock-start_clock

    print "len of ",f.__name__,"results =",len(a)
    print run_loops,u"次的最好运行时间为",best_time,'s'
    print run_loops,u"次的平均运行时间为",avg_time/run_loops,'s'
    print run_loops,u"次的最坏运行时间为",worse_time,'s'

    
if __name__ == '__main__':

    test_time(list_comp,1000)
    print "\n"
    test_time(for_loop,1000)
