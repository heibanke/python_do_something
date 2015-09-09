#!/usr/bin/python
# -*- coding: utf-8 -*-
class A:
    #classic class
    """this is class A"""
    pass
    __slots__=('x','y')
    def test(self):
        # classic class test
        """this is A.test()"""
        print "A class"
class B(object):
    #new class
    """this is class B"""
    __slots__=('x','y')
    pass
    def test(self):
        # new class test
        """this is B.test()"""
        print "B class"

        
if __name__ == '__main__':
    a=A()
    b=B()
    print dir(a)
    print dir(b)

    #a.x=1
    #b.x=1

    #help(a)
    #help(b)