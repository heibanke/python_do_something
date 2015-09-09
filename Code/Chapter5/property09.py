#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke        

class Car(object):
    country = u'中国'
    def __init__(self, length, width, height, owner=None):
        self._owner = owner
        self._length = length
        self._width = width
        self._height = height

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, value):
        self._owner = value
    @owner.deleter
    def owner(self):
        self._owner = None
    
    def __getattribute__(self, name):
        print "__getattribute__ ", self, name
        return object.__getattribute__( self, name )

        
        
if __name__=="__main__":    
    
    a = Car(1.2,1.4,1.5,u'黑板客')

    a._owner
