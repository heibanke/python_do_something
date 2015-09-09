#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

a=[1,2,3,4,5]
print "----------- index and slice ----------"

print a[0]
print a[-1]
print a[0:4]
print a[0:5:2]

print "------------ ref and copy -----------"

a_ref=a

a[2]=100

print "a="+str(a)
print "a_ref="+str(a_ref)

a_copy = a[:]
print "a_copy="+str(a_copy)
print "------------ list methods ----------"
a.append(300)
print "After append: a="+str(a)

a.insert(1,50)
print "After insert: a="+str(a)

a.pop()
print "After pop: a="+str(a)

a.sort()
print "After sort: a="+str(a)

a.reverse()
print "After reverse: a="+str(a)

del a[0]
print "After del: a="+str(a)

print "------------ ref and copy ------------"
print "a="+str(a)
print "a_ref="+str(a_ref)
print "a_copy="+str(a_copy)


b=[a,a_ref,a_copy]
c=[1,[1,2,3],'abc']
