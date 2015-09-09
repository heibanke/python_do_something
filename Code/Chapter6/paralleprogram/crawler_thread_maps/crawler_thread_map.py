#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
 
import urllib
import os
import re
from threading import Thread
from multiprocessing import Process
import time

def downloadURL(urls,dirpath):
    """
    urls: 需要下载的url列表
    dirpath: 下载的本地路径
    """
    for url in urls:
        if len(url)>0:
            #print "current process id is ",os.getpid()
            content = urllib.urlopen(url).read()
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
            open(dirpath+r'/'+url[-26:],'w').write(content)
            
def parseTarget(url):
    """
    根据目标url获取文章列表的urls
    """
    urls=[]
    content=urllib.urlopen(url).read()
    pattern = r'<a title=(.*?) href="(.*?)">'
    hrefs = re.findall(pattern,content)
         
    for href in hrefs:
        urls.append(href[1])
 
    return urls   
    
def thread_process_job(n, Thread_or_Process, url_list, job):
    """
    n: 多线程或多进程数
    Thread_Process: Thread／Process类 
    job: countdown任务
    """
    local_time=time.time()
    threads_or_processes = [Thread_or_Process(target=job,args=(url_list[i],str(n)+Thread_or_Process.__name__)) for i in xrange(n)]
    for t in threads_or_processes:
        t.start()
    for t in threads_or_processes:
        t.join()
    
    print n,Thread_or_Process.__name__," run job need ",time.time()-local_time
    
if __name__=="__main__":

    t=time.time()

    urls=[]
    for i in xrange(7):
        urls.extend(parseTarget('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(i+1)+'.html'))
       
    url_len = len(urls)
    
    print "total urls number is ",url_len
    
    for n in [8,4,2,1]:
        #将urls分割到url_list
        url_list=[]
        url_split_len = url_len//n
        for i in xrange(n):
            if i==n-1:
                url_list.append(urls[i*url_split_len:url_len])
            else:
                url_list.append(urls[i*url_split_len:(i+1)*url_split_len])
        #分割任务后创建线程
        thread_process_job(n,Thread, url_list, downloadURL)
        thread_process_job(n,Process, url_list, downloadURL)

    print "All done in ",time.time()-t