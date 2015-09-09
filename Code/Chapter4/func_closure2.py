#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

# 闭包closure
# 1. 嵌套函数
# 2. 内部函数使用外部变量(通常是外部函数的参数)
# 3. 外部函数返回内部函数


# 已经传进函数的变量list, 可以在程序中动态改变    
def largerx(x):
    def echo(value):
        return True if value>x[0] else False
    return echo


def pow_y(x):
    def echo(value):
        #x[0]=x[0]*2 
        #x=[2,2]
        return value**x[0],value**x[1]
    return echo 

if __name__ == '__main__':

    x=[1,1]
    lst2 = pow_y(x)
    #lst3 = pow_y([2,2])
    print "closure powy", lst2(2)
    x[0]=x[0]*2
    print "closure powy", lst2(3)
    print "closure powy", lst2(4)

    #print "closure powy", lst3(2)
    #print "closure powy", lst3(3)
    #print "closure powy", lst3(4)



    x=[10]
    larger10 = largerx(x)
    print x[0],larger10(2)
    x[0]=1
    print x[0],larger10(2)
    x = 100
    print x,larger10(2)
    
