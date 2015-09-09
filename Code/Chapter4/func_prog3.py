#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

"""
def compare_str(x,y):
    return 1 if (x.upper()>y.upper()) else -1

c = sorted(b,cmp=compare_str)
"""

a = "aAsmr3idd4bgs7Dlsf9eAF"  
# AaBbCcD...
b = list(filter(str.isalpha,a))
c = sorted(b,cmp=lambda x,y:1 if (x.upper()>y.upper()) else -1,reverse=False)

b.sort(lambda x,y:1 if (x.upper()>y.upper()) else -1)


print ''.join(c)
print ''.join(b)


        


