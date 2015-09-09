#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

##########################################
import os

data1=[]
filename='a.txt'

if os.path.exists(filename):
    for line in open(filename,'r'):
        a=line.split(',')
        data1.append(a[0])
    print data1


import random
charactor='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
first_c='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

while True:
    # generate name
    print u"注册\n请输入用户名(首字符必须是字母, 最小长度为4, 大小写字母,数字,_,-,的组合):"
    name = raw_input()

    valid = True
    
    #检查用户名是否有效
    if len(name)<4:
        print u"你的输入%s不够4位, 请重新输入!"%(name)
        valid = False
    elif not name[0] in first_c:
        print u"你的输入%s首字符必须是字母, 请重新输入!"%(name)
        valid = False 
    else:
        for a in name:
            if not a in charactor:
                valid = False
                print u"你的输入%s有非法字符, 请重新输入!"%(name)
                break
        else:
            #检查是否已存在
            if name in data1:
                print u"这个用户名%s已经存在，请重新输入!"%(name)
                valid = False
    
    # 密码是否有效
    if valid:
        print u"该用户名可以使用，请输入密码(最小长度为6, 大小写字母,数字,_,-,的组合):"
        password = raw_input()
        
        #检查是否有效
        if len(password)<6:
            print u"你的输入密码%s不够6位, 请重新输入!"%(password)
        else:
            for a in password:
                if not a in charactor:
                    valid = False
                    print u"你的输入密码%s有非法字符, 请重新输入!"%(password)
                    break
            
    #write file
    if valid:
        file = open(filename, 'a')
        # md5 process
        import hashlib
        password_md5 = hashlib.md5(password).hexdigest()
        file.write(name+','+password_md5+'\n')
        file.close()
        print u"恭喜你，注册成功"
        break

