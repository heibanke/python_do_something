#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke
class PositiveNum(object):
    def __init__(self):
        self.default = 1
        self.data = {}
 
    def __get__(self, instance, owner):
        # instance = x
        # owner = type(x)
        print "__get__",instance,owner
        return self.data.get(instance, self.default)
 
    def __set__(self, instance, value):
        # instance = x
        print "__set__",instance,value
        try:
            assert int(value)>0
            self.data[instance] = value
        except AssertionError:
            print "ERROR: "+str(value)+" is not positive number."
        except:
            print "ERROR: "+str(value)+" is not number value."
            
    def __delete__(self,instance):
        print "__delete__",instance
        del self.data[instance]
        
class Car(object):
    country = u'中国'
    length = PositiveNum()
    width = PositiveNum()
    height = PositiveNum()
    __slots__=('owner','length','width','height')
    
    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        

if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    b = Car(2.2,2.4,2.5,u'小明')
    """
    print a.owner
    print b.length
    a.length=1
    
    print a.country
    #a.country = 'china'    
    print a.country
    
    a.name = u"一汽"
    """
