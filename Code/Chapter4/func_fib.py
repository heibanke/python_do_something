#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


fib1=lambda n:1 if n<=2 else fib1(n-1)+fib1(n-2)

print [fib(i) for i in xrange(1,35)]
#print [fib1(i) for i in xrange(1,35)]
