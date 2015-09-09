#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
import time

def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print f.__name__,"run cost time is ",end-start
        return a
    return _f

   
def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

#@time_cost
def fib_opt(n):
	a,b,i=0,1,0
	
	while i<n:
		a,b=b,a+b
		i+=1
	else:
		return b

def fib_iter():
	a,b = 0,1
	while True:
		yield b
		a,b = b,a+b



N=10000
#print time_cost(fib)(N)
#print fib_opt(N)
import time
start = time.clock()
opt_result= [fib_opt(i) for i in xrange(N)]
end = time.clock()
print end-start

print "------------------------------"
A=fib_iter()
start = time.clock()
iter_result= [A.next() for i in xrange(N)]
end = time.clock()
print end-start