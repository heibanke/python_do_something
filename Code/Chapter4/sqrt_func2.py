#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
def sqrt_func_dg(x,small,low,high):
    guess = float(low+high)/2
    print guess,low,high
    if abs(guess**2-x)<small:
        return guess
    elif guess**2<x:
        return sqrt_func_dg(x,small,guess,high)
    else:
        return sqrt_func_dg(x,small,low,guess)


def sqrt_func(x, small):
    #check input
    assert x>=0
    assert small>0, str(small)
    
    #init value
    loops = 1
    low = 0.0
    high = max(x,1)
    while True and loops<=100:
        guess = float(low+high)/2
        #2fen
        if abs(guess**2-x)<small:
            break
        elif guess**2 < x:
            low = guess
        else:
            high = guess
                    
        #print low,high,guess
        loops+=1
        
    return guess,loops

def sqrt_nd(x,small):
    #check input
    assert x>=0
    assert small>0, str(small)
    
    #init value
    loops = 1
    low = 0.0
    high = max(x,1)
    guess = (low+high)/2
    while abs(guess**2-x)>small and loops<=100:
        guess = guess - (guess**2-x)/2/guess
        loops+=1
    return guess,loops
    
    
if __name__=="__main__":
    import math
    small_value = 0.0001
    test_data = [10.0, 23, 25, 0, 2, 0.25, 0.5, 123456789,4]
    
    print u"二分法结果:"
    for x in test_data:
        y=sqrt_func_dg(x,small_value,0,max(x,1));loops=0

        #y,loops=sqrt_func(x,small_value)
        assert abs(y**2-x)<small_value, u"二分法出错在"+str(x)
        print u"%d 次迭代的结果是 %f"%(loops,y)
        
        
    print u"\n牛顿法结果:"        
    for x in test_data:
        y,loops=sqrt_nd(x,small_value)
        assert abs(y**2-x)<small_value, "牛顿法出错在"+str(x)  
        print u"%d 次迭代的结果是 %f"%(loops,y)        
    print "Pass"