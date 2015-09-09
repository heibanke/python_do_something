#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke  

class A:
    def test(self):
        print "A's test"

class B(A):
    def test(self):
        print "B's test"
        A.test(self)
        #super(B,self).test()
    
class C(A):
    def test(self):
        print "C's test"
        A.test(self)
        
class D(B,C):
    def test(self):
        print "D's test"
        B.test(self) 
        C.test(self)
    
if __name__=="__main__":
    a=D()
    a.test()