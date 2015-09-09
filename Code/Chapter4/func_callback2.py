#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

def send_weixin(addr,message):
    print u"发微信("+message+u")给"+addr
def send_email(addr,message):
    print u"发邮件("+message+u")给"+addr
def send_qq(addr,message):
    print u"发QQ("+message+u")给"+addr
def send_duanxin(addr,message):
    print u"发短信("+message+u")给"+addr
    

send_method={
	'QQ':send_qq,
	'WeiXin':send_weixin,
	'DuanXin':send_duanxin,
	'Email':send_email
}



"""
def gupiao(f, message,custom_file,vip=False):
	# 处理message
	# 判断是否Vip
	# 解析文件，得到地址
	# f(message, addr)
	pass

gupiao(send_method['QQ'],message,file_qq)
gupiao(send_method['WeiXin'],message,file_weixin)
gupiao(send_method['DuanXin'],message,file_duanxin)
gupiao(send_method['Email'],message,file_email)

"""


def gupiao(message,custom_file,vip=False):
    
    send_s = []
    for s in message:
	    if vip==False:
	    	t = s.split(',')
	    	send_s.append(t[0])
	    else:
	    	send_s.append(s)

    send_message = ';'.join(send_s)

    #callback
    for line in open(custom_file,'r'):
        info = line.strip().split(',')
        send_method[info[0]](info[1],send_message)
    

if __name__=='__main__':

	gupiao([u"000001买,低于8.5买",u"000002卖,高于11.2卖"],'custom_info.txt')
	print "################### VIP ####################"
	gupiao([u"000001买,低于8.5买",u"000002卖,高于11.2卖"],'custom_info.txt',vip=True)
