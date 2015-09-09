#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

import random
import time

NUM_LEN = 10000

def bubbleSort(nums):
    for j in xrange(len(nums),-1,-1):
        for i in xrange(0,j-1,1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                #print nums
                
                
def partition(list,p,r):
        flag = list[r]
        i = p - 1
        for j in range(p,r):
            if list[j] <= flag:
                i += 1
                list[i],list[j] = list[j],list[i] 
                #print j,list
                
        list[i+1],list[r] = list[r],list[i+1]
        return i+1

def quick_sort_inner(list,p,r):    
    if p >= r:
        return
    #print p,r,list
    q = partition(list,p,r)
    #print "q = "+str(q)
    #print list
    
    quick_sort_inner(list,p,q-1)
    #print "1 is over:",list
    quick_sort_inner(list,q+1,r)
    #print "2 is over:",list

def quick_sort(list):
    quick_sort_inner(list,0,len(list)-1)
    
    
def test_time(f,run_loops):
    min_time = 1000
    avg_time = 0.0

    for num in range(run_loops):
        start_clock = time.clock()
        
        test_list=[random.randint(1,100) for i in range(NUM_LEN)]
        f(test_list)   
        #print test_list
        
        end_clock = time.clock()
        avg_time += end_clock-start_clock
        if (end_clock-start_clock)<min_time:
            min_time = end_clock-start_clock

    print run_loops,u"次的最好运行时间为",min_time,'s'
    print run_loops,u"次的平均运行时间为",avg_time/run_loops,'s'
    
    
if __name__=='__main__':
    run_loops = 1
    print "Quick sort time:"
    test_time(quick_sort,run_loops)
    
    print "\nBubble sort time:"
    test_time(bubbleSort,run_loops)


