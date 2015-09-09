#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import random

# filter
s = "@431$%$314&6i7(431)^&^%2l#%^i6861642k765e&$%65%^$^#$p%^&*%66757y%*^&%th%*&^%&^$o$&*^n4637"
print filter(str.isalpha,s)

print "#######################"
# map
l = [random.randint(0,100) for i in range(10)]

def sub50(a):
    return a-50

print l
print map(sub50,l)

# reduce
# 1+2+3+...+99
# 1*2*3*...*99
# f(a,b)=(a+3)*b
# f(f(a,b),c) 
# f(f(f(f(a,b),c),d),e)

# sqrt(sqrt(sqrt(a*b)*c)*d)
print sum(range(1,100))

import math
def f_add(a,b):
    return a+b
def f_mul(a,b):
    return a*b
def f_sqrt(a,b):
    return math.sqrt(float(a*b))
print reduce(f_add,range(1,100))
print reduce(f_mul,range(1,100))
print reduce(f_sqrt,range(1,100))
