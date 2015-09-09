#!/usr/bin/env python
# coding: utf-8
#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html

class SimpleMeta1(type):
    def __init__(cls, name, bases, atts):
        super(SimpleMeta1, cls).__init__(name, bases, atts)
        cls.test = lambda self : "Yes! This is a test."
        cls.att=1

class A(object):
    __metaclass__=SimpleMeta1
    
if __name__ == "__main__":
    a=A()
    b=A()