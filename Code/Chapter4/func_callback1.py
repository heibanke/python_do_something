#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

def test(callback):
    print 'test func begin'
    callback()
    
def test1(callback):
    print 'test1 func begin'
    for func in callback:
        func()
    
def cb1():
    print 'callback 1'

def cb2():
    print 'callback 2'



if __name__ == '__main__':
    #test(cb1)
    #test(cb2)
    test1([cb1,cb2])