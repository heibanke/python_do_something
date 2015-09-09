#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

def sqrt_func_dg(x,small,low,high):
    guess = float(low+high)/2

    if abs(guess**2-x)<small:
        return guess
    elif guess**2<x:
        return sqrt_func_dg(x,small,guess,high)
    else:
        return sqrt_func_dg(x,small,low,guess)

    
if __name__=="__main__":
    import math
    small_value = 0.0001
    test_data = [10.0, 23, 25, 0, 2, 0.25, 0.5, 123456789,4]
    
    print u"二分法结果:"
    for x in test_data:
        y=sqrt_func_dg(x,small_value,0,max(x,1));loops=0

        assert abs(y**2-x)<small_value, u"二分法出错在"+str(x)
        print u"结果是 %f"%(y)
               
    print "Pass"