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

mem_cache={}

def fib(n):
	if n not in mem_cache.keys():

		if n<=2:
			mem_cache[n] = 1
		else:
			mem_cache[n] = fib(n-1)+fib(n-2)
	
	return mem_cache[n]

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
import random
start = time.clock()

num_list = [random.randint(1,30) for i in xrange(N)]
opt_result= [fib_opt(i) for i in num_list]
end = time.clock()
print end-start

print "--------------after opt-------------"
start = time.clock()
opt_result= [fib(i) for i in num_list]
end = time.clock()
print end-start