#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke


#a[1]         #NameError
#a=2; a[1]    #TypeError
#a=[2]; a[1]  #IndexError
#a={}; a[1]   #KeyError



try:
	a=[0]
	print a[1]
	#raise IndexError("error")
	#assert a[1]==0,"assert error"
except Exception,e:
	print "except excute"
	print e
#finally:
#	print "finally excute"


