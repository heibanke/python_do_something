#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke
import time

def is_in_words(words,answer):
    for word in words:
        if word in answer:
            return True
    else:
        return False
        
def machine():  
    have_talk=[]
    good_words=[u'好',u'棒',u'不错',u'good']
    bad_words=[u'不好',u'糟',u'坏',u'差',u'bad']
    s=''
    while True:  
        answer = (yield s)  
        if answer is not None:  
            if answer in have_talk:
                s= u"嘿，'%s'你忘了已经和我说过这句话了吗?"%answer
            elif answer.endswith('?'):  
                s= u"轻松一点，少问自己些问题"  
            elif is_in_words(good_words,answer):  
                s= u"啊哈，这样就好，继续努力吧！"  
            elif is_in_words(bad_words,answer):  
                s= u"不要那么消极嘛"  
            else:
                s= u"我不理解你说的'%s'是什么意思"%answer
            
            if answer not in have_talk:
                have_talk.append(answer)
                
                
if __name__=="__main__":
    free_talk = machine()  
    free_talk.next()  
    print u'我是黑板客的小伙伴，我叫板板'
    time.sleep(1)
    print u'今天天气不错，想和我聊些什么吗？'
    while True:
        message = raw_input()
        #answer=free_talk.send(message.decode('gbk'))
        answer=free_talk.send(message.decode('utf-8'))
        print u"板板说:'"+answer+"'"
        time.sleep(1.5)
        print u"板板说:'你还想聊些什么吗?'"