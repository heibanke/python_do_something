#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import requests


headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.'}


def monkey_patch():
    prop = requests.models.Response.content
    def content(self):
        _content = prop.fget(self)
        if self.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(_content)
            if encodings:
                self.encoding = encodings[0]
            else:
                self.encoding = self.apparent_encoding
            _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
            self._content = _content
        return _content
    requests.models.Response.content = property(content)

monkey_patch()

url = "http://localhost:9000/accounts/login/"
url1 = "http://localhost:9000/lesson/crawler_ex02/"

s=requests.Session()
s.get(url)
headers.update({'X-CSRFToken':s.cookies.get('csrftoken')})

#s.headers.update(headers)
rr = s.post(url, params = {'username':'test','password': 'test123'},headers=headers,cookies=s.cookies)
#print unicode(rr.text)

"""
headers.update({'X-CSRFToken':s.cookies.get('csrftoken')})
s.headers.update(headers)
rr = s.post(url1, params = {'username':'test','password': 'test123'})

print rr.text
"""
