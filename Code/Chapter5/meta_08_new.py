#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke        

class PositiveInt1(int):
    def __init__(self, value):
        super(PositiveInt1,self).__init__(self, abs(value))

        
class PositiveInt2(int):
    def __new__(cls, value):
        return super(PositiveInt2,cls).__new__(cls, abs(value))     
        
        
class Float_Units( float ):
    def __new__(cls, value, unit ):
        obj= super(Float_Units,cls).__new__( cls, value )
        obj.unit= unit
        return obj   
                
           
        
if __name__=="__main__":    
    
    i = PositiveInt1(-3)
    print i        
    i = PositiveInt2(-3)
    print i  
    
    speed= Float_Units( 6.5, "km/s" )        
    print speed, speed.unit
