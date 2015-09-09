#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

########################## shelve ################
import shelve
f = shelve.open('file_test.shelve')
f['baidu'] = 'www.baidu.com'
f['qq'] = 'www.qq.com'
f['163'] = 'www.163.com'

print f
f.close()
g = shelve.open('file_test.shelve')
print g


########################## pickle ################
print "--------------------------------------"
import cPickle
f=open('file_test.pkl','w')

obj1 = 2015,"heibanke",[1,2,3,4],{"python":1990,"java":1992}
obj2 = ['heibanke','junmin11','chutianshu1981','sjtujoe','ygkkv',
'liuyanping_0904','zhkmxx930']

cPickle.dump(obj1,f)
cPickle.dump(obj2,f)

f.close()

#read file
f=open('file_test.pkl','r')
obj1_r = cPickle.load(f)
print obj1_r

obj2_r = cPickle.load(f)
print obj2_r
f.close()
