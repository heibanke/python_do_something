#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

class Car(object):
    country = u'中国'
    def __init__(self, length, width, height, owner=None):
        self.owner = owner
        self.length = length
        self.width = width
        self.height = height
        self.country = "china"

if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    b = Car(2.2,2.4,2.5,u'小张')
    print a.owner, b.owner
    print a.country, b.country

    b.country = u'美国'

    print a.country, b.country
    print Car.country

    print "--------------------------"
    del a.country
    print a.country
    #del a.country
    #del Car.country
    #print a.country
