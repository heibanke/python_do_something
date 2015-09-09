#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke          

class Point(object):
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def __sub__(self, other):
        assert isinstance(other,Point)
        return Point(self.x-other.x,self.y-other.y)
    def __add__(self, other):
        assert isinstance(other,Point)
        return Point(self.x+other.x,self.y+other.y)
    def __mul__(self,factor):
        return Point(self.x*factor, self.y*factor)
    def __div__(self,factor):
        return Point(self.x/factor, self.y/factor)    
        
    @property    
    def xy(self):
        return (self.x,self.y)
    
    def __str__(self):
        return "x={0},y={1}".format(self.x,self.y)
    def __repr__(self):
        return str(self.xy)
        
if __name__ == '__main__':
       
    a = Point(50,60)
    b = Point(30,40)
    
    print a-b
    print a+b
    print a*2
    print a/2