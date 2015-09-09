#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

X = 9 # Global scope name
def f1():
    #global X
    #print X
    X = 8  # Global or enclosing 
    def f2():
    	#print "in f2()", X
    	#X=7 # enclosing or local
        print "in f2()", X
    f2()
    print "in f1()",X


if __name__=="__main__":
	f1()
	print "out f1()",X
