#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

class Car(object):
    country = u'中国'
    __slots__=('length','width','height','owner','__dict__')
    
    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        
    def __getattr__(self,name):
        print "__getattr__",name
        return self.__dict__.get(name,None)
        
    def __setattr__(self,name,value):
        print "__setattr__",name
        if name!='owner':
            assert value>0, name+" must larger than 0"
        self.__dict__[name]=value
        
    def __delattr__(self,name):
        print "__delattr__",name
        if name=='owner':
            self.__dict__[name]=None

            
if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    """
    print a.owner
    del a.owner
    print a.owner
    a.length=1
    
    print a.country
    a.country = 'china'
    print a.country
    """
    a.name = u"一汽"