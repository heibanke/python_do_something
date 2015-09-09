#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

def reverse_s(s):
	if len(s)<=1:
		return s
	else:
		return reverse_s(s[1:])+s[0]

s="ilikepython"
print reverse_s(s)