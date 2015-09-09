#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

class Car(object):
    country = u'中国'
    def __init__(self, length, width, height, owner=None):
        self.__owner = owner
        
        assert length>0,"length must larger than 0"
        self._length = length
        self._width = width
        self._height = height

    def getOwner(self):
        return self.__owner
    def setOwner(self, value):
        self.__owner = value

    def getLength(self):
        return self._length
        
    def setLength(self,value):
        assert value>0,"length must larger than 0"
        self._length = value

if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    print a.getOwner()

    #a.setLength(-1)
    #a.length
    #a.length=1