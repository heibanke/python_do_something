#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

class PositiveNum(object):
    def __init__(self,value):
        self.val = value
 
    def __get__(self, instance, owner):
        # instance = a,b
        # owner = Car
        print "__get__",instance,owner
        return self.val
 
    def __set__(self, instance, value):
        # instance = a,b
        print "__set__",instance,value
        try:
            assert int(value)>0
            self.val = value
        except AssertionError:
            print "ERROR: "+str(value)+" is not positive number."
        except:
            print "ERROR: "+str(value)+" is not number value."  
            
    def __delete__(self,instance):
        print "__delete__",instance
        self.val = None

    #def __getattribute__(self,name):
        #print self, name
        
class Car(object):
    country = u'中国'
    length = PositiveNum(0)
    width = PositiveNum(0)
    height = PositiveNum(0)
    #__slots__=('owner','length','width','height')
    
    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        


if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    b = Car(2.2,2.4,2.5,u'小明')
    

    
