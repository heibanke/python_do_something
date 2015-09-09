#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import requests

def post_data_django(s,url,data):

    s.get(url)
    
    params = {'csrfmiddlewaretoken':s.cookies.get('csrftoken')}
    params.update(data)

    r = s.post(url,data=params)

    return r,s
    
url_login = "http://www.heibanke.com/accounts/login/"
url_form = "http://www.heibanke.com/lesson/crawler_ex02/"

# login first
s = requests.Session()

r,s = post_data_django(s,url_login,{'username':'test','password':'test123'})
print 'login ',r.status_code

# find the password
for number in range(30):
    rr,s = post_data_django(s,url_form,{'username':'heibanke','password': str(number)})
    if rr.text.find(u"输入的密码错误")>0:
        print number,"not correct"
        number = number+1
    else:
        print rr.text
        break
