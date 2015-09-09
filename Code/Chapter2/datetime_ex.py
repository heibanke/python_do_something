#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

# 1. 从现在开始1000天后和1000天前是哪一天
import datetime

a=datetime.date.today()
b=datetime.datetime.now()
d1=datetime.timedelta(days=1000)
d2=datetime.timedelta(hours=1000)

(a-d1).isoformat()
(a+d1).strftime('%m/%d/%Y')
b.isoformat()
(b-d2)

# 2. 离你的重要纪念日还有多少天
important_day=datetime.datetime.strptime('2008-06-18','%Y-%m-%d') 

important_day>b
d3=b-important_day
d3.days

t=datetime.time(12,11,30)

# 3. 两段程序哪个快些
############## time.time and time.clock ####################
import time

a=input("please input 0 or 1:")

start_time = time.time()
start_clock = time.clock()


if a:
    sum_i=0
    for i in range(100000):
        sum_i+=i
else:
    sum_i=sum(range(100000))

print sum_i

time.sleep(2)
end_time = time.time()
end_clock = time.clock()

print "time-delta:"
print start_time-end_time
print "clock-delta:"
print start_clock-end_clock