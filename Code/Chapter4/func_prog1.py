#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

#f(a,b,c,d) = (a+b)*c-d
#f(a,b,c,d) = (a+b)*(c-d)

def f1(a,b,c,d):
    e = (a+b)
    f = e*c
    g = f-d
    return g

def f2(a,b,c,d):
    e = (a+b)
    f = c-d
    g = e*f
    return g
    
def f_add(a,b):
    return a+b
def f_mul(a,b):
    return a*b
def f_sub(a,b):
    return a-b
    
def g1(f,a,b):
    return f(a,b)
    
if __name__ == '__main__':
        
    a,b,c,d = 1,2,3,4
    print f1(a,b,c,d), f2(a,b,c,d)
    print g1(f_sub, g1(f_mul, g1(f_add,a,b), c), d),  g1(f_mul, g1(f_add,a,b), g1(f_sub,c, d))

# question, "支持，+,-,*,/,^,()"的任意表达式
