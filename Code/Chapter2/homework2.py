#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

########################## 2-1 ################
import re
text='aaa@163.com chu-tian-shu_1981@heibanke2015.com abc-fff@xfd.org ccc_fd2@fff.edu'

print re.findall(r'(\w+[-\w]*)@([a-zA-Z0-9]+).(com|org|edu)',text)


########################## 2-2 ################
import random
charactor='abcdefghijklmnopqrstuvwxyz0123456789'

len_char = len(charactor)-1
# generate name
a=[0]*4
a[0]=charactor[random.randint(0,len_char)]
a[1]=charactor[random.randint(0,len_char)]
a[2]=charactor[random.randint(0,len_char)]
a[3]=charactor[random.randint(0,len_char)]

name=''.join(a)

# generate password
a=[0]*6
a[0]=charactor[random.randint(0,len_char)]
a[1]=charactor[random.randint(0,len_char)]
a[2]=charactor[random.randint(0,len_char)]
a[3]=charactor[random.randint(0,len_char)]
a[4]=charactor[random.randint(0,len_char)]
a[5]=charactor[random.randint(0,len_char)]

password=''.join(a)

#write file
f=open('a.txt','w')
f.write(name+','+password+'\n')
f.close()


########################## 2-3 ################
# read file
f=open('a.txt','r')
name_password = f.readline().strip().split(',')
f.close()

# md5 process
import hashlib
password_md5 = hashlib.md5(name_password[1]).hexdigest()

# write file
f=open('a_md5.txt','w')
f.write(name_password[0]+','+password_md5+'\n')

f.close()