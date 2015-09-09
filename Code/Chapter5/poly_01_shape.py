#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke        
        
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
        
    @property    
    def xy(self):
        return (self.x,self.y)
    
    def __str__(self):
        return "x={0},y={1}".format(self.x,self.y)
    def __repr__(self):
        return str(self.xy)
        
class Shape(object):

    def __init__(self,points_list,**kwargs):
        for point in points_list:
            assert isinstance(point,Point),"input must be Point type"
        self._points=points_list[:]
        self._points.append(points_list[0])
        self._color=kwargs.get('color','#000000')   
    
    @property
    def area(self):
        return 0

        
class RectAngle(Shape):
    def __init__(self,startPoint,w,h,**kwargs):
        self._w = w
        self._h = h
        super(RectAngle,self).__init__([startPoint,startPoint+Point(w,0),startPoint+Point(w,h),startPoint+Point(0,h)],**kwargs)
        
    @property
    def area(self):
        return self._w*self._h

        
import math
class Circle(Shape):
    def __init__(self,center_p,radius,**kwargs):
        points_list = []
        self._radius = radius
        self._center_p=center_p
        N_circle=24
        for i in xrange(N_circle):
            points_list.append(center_p + Point(radius*math.cos(2.0*math.pi*i/N_circle),radius*math.sin(2.0*math.pi*i/N_circle)))
            
        super(Circle,self).__init__(points_list,**kwargs)
    
    @property    
    def area(self):
        return math.pi*self._radius**2

        
if __name__ == '__main__':
       
    prepare_draws=[]
    
    start_p = Point(50,60)
    a=RectAngle(start_p,100,80,color="#ff0000")
    prepare_draws.append(a)
    c=Circle(Point(200,200),100,color="#0000ff")
    prepare_draws.append(c) 
    
    
    for shape in prepare_draws:
        print shape.area
    
