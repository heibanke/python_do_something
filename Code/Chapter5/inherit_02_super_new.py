#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke  

class A(object):
    def test(self):
        print "A's test"

class B(A):
    def test(self):
        print "B's test"
        super(B,self).test()
    
class C(A):
    def test(self):
        print "C's test"
        super(C,self).test()
        
class D(B,C):
    def test(self):
        print "D's test"
        super(D,self).test()

    
if __name__=="__main__":
    a=D()
    a.test()