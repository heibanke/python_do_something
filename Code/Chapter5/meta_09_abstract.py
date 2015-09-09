#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke  

from abc import ABCMeta,abstractmethod

class MyAbstractClass1(object):
    def method1(self): raise NotImplementedError("Please Implement this method") 

    
class MyAbstractClass2(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def method1(self): pass   

    
class MyClass1(MyAbstractClass1): 
    pass

class MyClass2(MyAbstractClass2): 
    pass
    
class MyClass3(MyAbstractClass2): 
    def method1(self): pass    
    
    
a1=MyClass1()
#a1.method1()

#a2=MyClass2()


a3=MyClass3()
a3.method1()
