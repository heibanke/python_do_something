#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

# 打印［10-0]之间的偶数
x = 10
while x:
    if x % 2 == 0: # Even? 
        print x
    x = x-1


# 判断是否素数(质数)：大于1的自然数，除1和它本身外没有整数能够整除
y=input()
x = y // 2 
while x > 1:
    if y % x == 0: 
        print y, 'has factor', x
        break
    x -= 1
else: # Normal exit
    print y, 'is prime number'

####################### for ###########################
sum = 0
for x in [1, 2, 3, 4]:
    sum += x

S = u"你在远方"
T = (u"我", u"在", u"故乡")
for x in S: print x, 
for x in T: print x,


file = open('test.txt','w')
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print >>file, key, '=>', D[key]

file.close()

#####################################################

items = [u"小方", u"小白", u"小三", u"小王"] # A set of objects
key = u"小李" # Keys to search for

for item in items: # For all items
    if item == key: # Check for match
        print key, "was found"
        break
else:
    print key, "not found!" 

#####################################################
file = open('test.txt')
while True:
    line = file.readline() # Read line by line
    if not line: break
    print line.strip() # Line already has a \n 

file.close()

for line in open('test.txt'):
    print line.strip()

